#!/usr/bin/env python3
"""Baixa as galerias do Mercado Livre, converte com cwebp -q 85 e grava em public/imagens-produtos/."""
import json
import os
import socket
import struct
import subprocess
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST_ROOT = ROOT / "public" / "imagens-produtos"
PORT = int(os.environ.get("CHROME_DEBUG_PORT", "9347"))
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

PRODUCTS = [
    {
        "slug": "clicker-adestramento",
        "prefix": "clicker-adestramento-caes",
        "url": "https://www.mercadolivre.com.br/adestrador-manual-de-caes-clicker-home-pet-azul-com-alca/p/MLB25725143",
    },
    {
        "slug": "kit-mordedores-borracha-macica",
        "prefix": "kit-mordedores-borracha-macica",
        "url": "https://www.mercadolivre.com.br/kit-brinquedos-mordedores-cachorro-grande-resistente-05-und/up/MLBU2957594443?pdp_filters=item_id%3AMLB3952122379",
    },
    {
        "slug": "pipi-pode-educa-cao",
        "prefix": "pipi-pode-educa-cao",
        "url": "https://www.mercadolivre.com.br/educador-sanitario-cachorro-gato-pipi-dog-aqui-nao-xixi-sim/up/MLBU797217416?pdp_filters=item_id%3AMLB2606085704",
    },
    {
        "slug": "comedouro-lento",
        "prefix": "comedouro-lento-labirinto",
        "url": "https://www.mercadolivre.com.br/comedouro-labirinto-pet-games-antiengasgo-e-antiderrapante-dobravel-de-silicone-laranja-200-ml/p/MLB20874199",
    },
    {
        "slug": "guia-peitoral-filhote",
        "prefix": "guia-peitoral-filhote",
        "url": "https://www.mercadolivre.com.br/peitoral-coleira-pra-cachorro-grande-e-medio-reforcado-guia/up/MLBU3841919301?pdp_filters=item_id%3AMLB6470309714",
    },
    {
        "slug": "casinha-plastico-furacao-pet",
        "prefix": "casinha-plastico-furacao-pet",
        "url": "https://produto.mercadolivre.com.br/MLB-3808898369-casinha-pet-iglu-para-cachorros-pequenos-n6-furaco-pet-_JM",
    },
    {
        "slug": "racao-golden-filhotes",
        "prefix": "racao-golden-filhotes",
        "url": "https://www.mercadolivre.com.br/racao-premier-golden-formula-caes-filhotes-15kg-frangoarro/up/MLBU3794327275?pdp_filters=item_id%3AMLB4478808233",
    },
    {
        "slug": "herbalvet-ta",
        "prefix": "herbalvet-ta",
        "url": "https://www.mercadolivre.com.br/herbalvet-ta-1-litro-ourofino-desinfetante-bactericida-pet/up/MLBU2738396717?pdp_filters=item_id%3AMLB5173284112",
    },
    {
        "slug": "melhores-acessorios-adestramento",
        "prefix": "guia-unificada-adestramento",
        "url": "https://www.mercadolivre.com.br/social/pf20260421093326?matt_word=pf20260421093326&matt_tool=33826420&forceInApp=true&ref=BDB37if1M54bIEL6JsvbXvKEJjfx%2Bokk1WEIF1R9WMTCPwVWennnZBSXKxZSJtbzxybqbeFEm9j2Y0aCbJgNkMZcyciakR%2F%2B9oxtigyY48GPXJMBEh9tOIWQIzVR%2B3jaGDaxkQVwLaJ041YhFmeYnIjRkDDShnS7bTi6a7HaUhTFg2lnBxNwuUTrh6ioIqd%2Bdy8adjCEFM%2F0S9bcxBR5oVerobILyISy3VafDUDkvwAL53mkp3%2F03QyCC460dDo6OFv%2B",
    },
    {
        "slug": "nylabone-puppy",
        "prefix": "nylabone-puppy",
        "url": "https://www.mercadolivre.com.br/nylabone-puppy-chew-teething-bone-dog-chew-toy-chicken/up/MLBU5756680626?pdp_filters=item_id%3AMLB5488595891",
    },
    {
        "slug": "portao-pet-pressao",
        "prefix": "portao-pet-pressao",
        "url": "https://www.mercadolivre.com.br/portao-pet-criancas-reforcadas-80-a-90-cm-grade-de-protecao/up/MLBU3734342628?pdp_filters=item_id%3AMLB4420333129",
    },
]

EXPR = r'''
(() => {
  const figs = [...document.querySelectorAll("figure.ui-pdp-gallery__figure")];
  const urls = [];
  const seen = new Set();
  for (const f of figs) {
    const raw = f.getAttribute("data-zoom") || f.querySelector("img")?.currentSrc || "";
    const url = raw.split("?")[0];
    if (!url.includes("mlstatic.com") || seen.has(url)) continue;
    seen.add(url);
    urls.push({ url, alt: (f.querySelector("img")?.alt || "").trim() });
  }
  return {
    title: document.title,
    href: location.href,
    blocked: location.href.includes("account-verification"),
    urls
  };
})()
'''


def send(sock, obj):
    data = json.dumps(obj).encode()
    mask = os.urandom(4)
    n = len(data)
    header = bytearray([0x81])
    if n < 126:
        header.append(0x80 | n)
    elif n < 65536:
        header.append(0x80 | 126)
        header += struct.pack(">H", n)
    else:
        header.append(0x80 | 127)
        header += struct.pack(">Q", n)
    header += mask
    sock.sendall(header + bytes(b ^ mask[i % 4] for i, b in enumerate(data)))


def recvn(sock, n):
    buf = b""
    while len(buf) < n:
        chunk = sock.recv(n - len(buf))
        if not chunk:
            raise SystemExit("Conexão com o Chrome fechou.")
        buf += chunk
    return buf


def recv_payload(sock):
    _, b1 = recvn(sock, 2)
    length = b1 & 0x7F
    if length == 126:
        length = struct.unpack(">H", recvn(sock, 2))[0]
    elif length == 127:
        length = struct.unpack(">Q", recvn(sock, 8))[0]
    mask = recvn(sock, 4) if (b1 & 0x80) else None
    payload = recvn(sock, length)
    if mask:
        payload = bytes(b ^ mask[i % 4] for i, b in enumerate(payload))
    return payload


class Cdp:
    def __init__(self, ws_url):
        rest = ws_url[len("ws://"):]
        hostport, path = rest.split("/", 1)
        host, port_s = hostport.split(":")
        key = __import__("base64").b64encode(os.urandom(16)).decode()
        req = (
            f"GET /{path} HTTP/1.1\r\nHost: {hostport}\r\nUpgrade: websocket\r\n"
            f"Connection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n"
        )
        self.sock = socket.create_connection((host, int(port_s)), timeout=20)
        self.sock.sendall(req.encode())
        buf = b""
        while b"\r\n\r\n" not in buf:
            buf += self.sock.recv(4096)
        if b" 101 " not in buf.split(b"\r\n", 1)[0]:
            raise SystemExit("Falha ao ligar ao Chrome.")
        self.msg_id = 0

    def call(self, method, params=None, timeout=25):
        self.msg_id += 1
        mid = self.msg_id
        send(self.sock, {"id": mid, "method": method, "params": params or {}})
        self.sock.settimeout(timeout)
        while True:
            msg = json.loads(recv_payload(self.sock))
            if msg.get("id") == mid:
                return msg

    def close(self):
        self.sock.close()


def page_target():
    with urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json/list", timeout=3) as resp:
        tabs = json.load(resp)
    for tab in tabs:
        if tab.get("type") == "page" and tab.get("webSocketDebuggerUrl"):
            return tab
    raise SystemExit("Aba do Chrome não encontrada.")


def start_chrome():
    profile = f"/tmp/chrome-galerias-{os.getpid()}"
    os.makedirs(profile, exist_ok=True)
    env = os.environ.copy()
    env["DISPLAY"] = env.get("DISPLAY") or ":0"
    proc = subprocess.Popen(
        [
            "google-chrome",
            "--disable-gpu",
            "--no-first-run",
            "--no-default-browser-check",
            "--disable-blink-features=AutomationControlled",
            f"--user-data-dir={profile}",
            f"--remote-debugging-port={PORT}",
            "--window-size=1280,900",
            "about:blank",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        env=env,
    )
    deadline = time.time() + 20
    while time.time() < deadline:
        try:
            page_target()
            return proc, profile
        except Exception:
            time.sleep(0.3)
    raise SystemExit("O Chrome não abriu a porta de depuração.")


def gallery(cdp):
    msg = cdp.call("Runtime.evaluate", {"expression": EXPR, "returnByValue": True})
    return msg["result"]["result"].get("value") or {}


def download(url, referer, dest):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Referer": referer})
    with urllib.request.urlopen(req, timeout=40) as resp:
        dest.write_bytes(resp.read())


def main():
    proc, profile = start_chrome()
    manifest = []
    try:
        tab = page_target()
        cdp = Cdp(tab["webSocketDebuggerUrl"])
        for product in PRODUCTS:
            print(f"\n== {product['slug']} ==")
            cdp.call("Page.navigate", {"url": product["url"]}, timeout=30)
            found = {}
            deadline = time.time() + 25
            while time.time() < deadline:
                time.sleep(0.8)
                found = gallery(cdp)
                if found.get("blocked"):
                    break
                if found.get("urls"):
                    break
            urls = found.get("urls") or []
            print(f"  título: {found.get('title')}")
            print(f"  url: {found.get('href')}")
            print(f"  fotos: {len(urls)}")
            entry = {
                "slug": product["slug"],
                "prefix": product["prefix"],
                "page": found.get("href"),
                "title": found.get("title"),
                "blocked": bool(found.get("blocked")),
                "files": [],
            }
            if not urls:
                manifest.append(entry)
                continue
            folder = DEST_ROOT / product["slug"]
            folder.mkdir(parents=True, exist_ok=True)
            for old in folder.glob(f"{product['prefix']}-*.webp"):
                old.unlink()
            tmp = Path(f"/tmp/{product['slug']}-src")
            tmp.mkdir(parents=True, exist_ok=True)
            for i, item in enumerate(urls, start=1):
                src = tmp / f"{i}.bin"
                out = folder / f"{product['prefix']}-{i}.webp"
                download(item["url"], found.get("href") or product["url"], src)
                subprocess.run(["cwebp", "-quiet", "-q", "85", str(src), "-o", str(out)], check=True)
                dim = subprocess.check_output(["identify", "-format", "%w %h", str(out)], text=True).split()
                entry["files"].append({
                    "file": out.name,
                    "width": int(dim[0]),
                    "height": int(dim[1]),
                    "source_alt": item.get("alt") or "",
                })
                print(f"  {i}: {dim[0]}x{dim[1]}")
            manifest.append(entry)
        cdp.close()
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=3)
        except subprocess.TimeoutExpired:
            proc.kill()
        subprocess.run(["rm", "-rf", profile], check=False)
    out = ROOT / "scripts" / "galerias-produtos.json"
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nManifesto: {out}")


if __name__ == "__main__":
    main()
