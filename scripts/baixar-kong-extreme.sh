#!/usr/bin/env bash
# Baixa as fotos principais do Kong Extreme no Mercado Livre, converte para WebP
# e grava em public/imagens-produtos/kong-extreme/.
set -euo pipefail

URL="https://www.mercadolivre.com.br/brinquedo-kong-extreme-grande-para-caes-mordedores-fortes-preto/p/MLB27036635"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="${ROOT}/public/imagens-produtos/kong-extreme"
TMP="$(mktemp -d "${TMPDIR:-/tmp}/kong-extreme.XXXXXX")"
PROFILE="$(mktemp -d "${TMPDIR:-/tmp}/chrome-kong-extreme.XXXXXX")"
PORT="${CHROME_DEBUG_PORT:-9341}"
CHROME_PID=""
LISTA="${TMP}/urls.txt"

cleanup() {
  local status=$?
  if [[ -n "${CHROME_PID}" ]]; then
    kill "${CHROME_PID}" 2>/dev/null || true
    pkill -P "${CHROME_PID}" 2>/dev/null || true
    sleep 0.4
    kill -9 "${CHROME_PID}" 2>/dev/null || true
    wait "${CHROME_PID}" 2>/dev/null || true
  fi
  rm -rf "${TMP}" "${PROFILE}" 2>/dev/null || true
  if [[ "${status}" -ne 0 ]]; then
    exit "${status}"
  fi
}
trap cleanup EXIT

export DISPLAY="${DISPLAY:-:0}"

google-chrome \
  --disable-gpu \
  --no-first-run \
  --no-default-browser-check \
  --disable-blink-features=AutomationControlled \
  --user-data-dir="${PROFILE}" \
  --remote-debugging-port="${PORT}" \
  --window-size=1280,900 \
  "${URL}" \
  >/tmp/baixar-kong-extreme-chrome.log 2>&1 &
CHROME_PID=$!

echo "Aguardando a galeria do produto..."
python3 - "${PORT}" "${LISTA}" <<'PY'
import json, os, socket, struct, sys, time, urllib.request

port, lista = sys.argv[1], sys.argv[2]
deadline = time.time() + 45

def page_target():
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/json/list", timeout=2) as resp:
            tabs = json.load(resp)
    except Exception:
        return None
    for tab in tabs:
        url = tab.get("url", "")
        if tab.get("type") == "page" and "MLB27036635" in url and "account-verification" not in url:
            return tab
    return None

tab = None
while time.time() < deadline:
    tab = page_target()
    if tab:
        break
    time.sleep(0.4)
else:
    raise SystemExit("A página do produto não abriu. O Mercado Livre pode ter pedido login.")

ws = tab["webSocketDebuggerUrl"]
rest = ws[len("ws://"):]
hostport, path = rest.split("/", 1)
host, port_s = hostport.split(":")
path = "/" + path
expr = r'''
(() => [...document.querySelectorAll("figure.ui-pdp-gallery__figure")]
  .map(f => (f.getAttribute("data-zoom") || f.querySelector("img")?.currentSrc || "").split("?")[0])
  .filter(u => u.includes("mlstatic.com")))()
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

def recv_text(sock):
    b0, b1 = recvn(sock, 2)
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

def gallery_urls():
    key = __import__("base64").b64encode(os.urandom(16)).decode()
    req = (
        f"GET {path} HTTP/1.1\r\nHost: {hostport}\r\nUpgrade: websocket\r\n"
        f"Connection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n"
    )
    sock = socket.create_connection((host, int(port_s)), timeout=10)
    sock.sendall(req.encode())
    buf = b""
    while b"\r\n\r\n" not in buf:
        buf += sock.recv(4096)
    if b" 101 " not in buf.split(b"\r\n", 1)[0]:
        sock.close()
        raise SystemExit("Falha ao ligar ao Chrome.")
    send(sock, {"id": 1, "method": "Runtime.evaluate", "params": {"expression": expr, "returnByValue": True}})
    urls = []
    while True:
        msg = json.loads(recv_text(sock))
        if msg.get("id") == 1:
            urls = msg["result"]["result"].get("value") or []
            break
    sock.close()
    return urls

urls = []
while time.time() < deadline:
    urls = gallery_urls()
    if urls:
        break
    time.sleep(0.5)

if not urls:
    raise SystemExit("Nenhuma imagem da galeria principal foi encontrada.")

with open(lista, "w", encoding="utf-8") as fh:
    for url in urls:
        fh.write(url + "\n")
print(f"Encontradas {len(urls)} imagens.")
PY

mapfile -t IMAGES < "${LISTA}"
if [[ "${#IMAGES[@]}" -eq 0 ]]; then
  echo "Nenhuma imagem principal encontrada." >&2
  exit 1
fi

echo "A descarregar e a converter com cwebp -q 85..."
i=1
for url in "${IMAGES[@]}"; do
  src="${TMP}/origem-${i}"
  curl -fsSL --retry 3 --retry-delay 1 \
    -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" \
    -e "${URL}" \
    -o "${src}" \
    "${url}"
  out="${TMP}/kong-extreme-brinquedo-mordedor-${i}.webp"
  cwebp -quiet -q 85 "${src}" -o "${out}"
  if command -v identify >/dev/null 2>&1; then
    dim="$(identify -format '%wx%h' "${out}")"
  else
    dim="$(wc -c < "${out}") bytes"
  fi
  echo "  ${i}: ${dim}"
  i=$((i + 1))
done

mkdir -p "${DEST}"
rm -f "${DEST}"/kong-extreme-brinquedo-mordedor-*.webp
mv "${TMP}"/kong-extreme-brinquedo-mordedor-*.webp "${DEST}/"

echo "Gravadas em ${DEST}:"
ls -1 "${DEST}"/kong-extreme-brinquedo-mordedor-*.webp
