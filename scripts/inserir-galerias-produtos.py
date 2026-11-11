#!/usr/bin/env python3
"""Insere galeria, Open Graph e JSON-LD de produto nos artigos."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "scripts" / "galerias-produtos.json").read_text(encoding="utf-8"))
SITE = "https://www.guiadoadestrador.com.br"

SKIP = {"comedouro-lento-labirinto-2.webp"}

PAGES = {
    "clicker-adestramento": {
        "html": "public/reviews/clicker-para-adestramento-vale-a-pena.html",
        "product": "Clicker para cachorro (clicker adestramento com pulseira)",
        "caption": "Clicker com botão e pulseira espiral: cores, uso no pulso e o click na frente do cão.",
    },
    "kit-mordedores-borracha-macica": {
        "html": "public/reviews/kit-mordedores-borracha-macica-5-pecas.html",
        "product": "Kit de 5 Brinquedos Mordedores de Borracha Maciça",
        "caption": "Kit de cinco mordedores de borracha maciça: peças, medidas e textura.",
    },
    "pipi-pode-educa-cao": {
        "html": "public/reviews/pipi-pode-educa-cao.html",
        "product": "Atrativo sanitário Pipi Pode / Educa Cão",
        "caption": "Kit Procão Não Pode e Pode, frascos de 200 ml para marcar o lugar do xixi.",
    },
    "comedouro-lento": {
        "html": "public/reviews/comedouro-lento.html",
        "product": "Comedouro lento / bola recheável (Stark, Pet Games, Buddy Colmeia)",
        "caption": "Comedouro labirinto Pet Games de silicone laranja, com sulcos, medidas e ventosas.",
    },
    "guia-peitoral-filhote": {
        "html": "public/reviews/guia-e-peitoral-filhote.html",
        "product": "Peitoral modelo H reforçado 25–30 mm + guia com mosquetão de aço",
        "caption": "Peitoral com guia: cores, mola anti-impacto e tabela de tamanhos.",
    },
    "casinha-plastico-furacao-pet": {
        "html": "public/reviews/casinha-plastico-furacao-pet.html",
        "product": "Casinha plástica 2 em 1 nº 5 (Furacão Pet / Tánatela)",
        "caption": "Casinha iglu Furacão Pet: formato, medidas internas e bandeja.",
    },
    "racao-golden-filhotes": {
        "html": "public/reviews/racao-filhotes-porte-grande.html",
        "product": "Ração filhotes raças grandes (NutriSano / Golden / Premier)",
        "caption": "Ração Golden Formula para cães filhotes, pacote de 15 kg, frango e arroz.",
    },
    "herbalvet-ta": {
        "html": "public/reviews/herbalvet-eliminador-enzimatico.html",
        "product": "Desinfetante Herbalvet T.A. Ourofino (500ml / 1000ml)",
        "caption": "Herbalvet T.A. Ourofino, galão de 1 litro na embalagem nova.",
    },
    "nylabone-puppy": {
        "html": "public/reviews/nylabone-puppy-chew-toy.html",
        "product": "Nylabone Puppy Chew Toy — Mordedor de Nylon para Filhote",
        "caption": "Nylabone Puppy Chew sabor frango: embalagem, tamanho de filhote e o osso.",
    },
    "portao-pet-pressao": {
        "html": "public/reviews/portao-pet-de-pressao.html",
        "product": "Portão de segurança pet de pressão (ferro)",
        "caption": "Portão pet de pressão, branco, com extensão de 69 a 93 cm.",
    },
}

ALTS = {
    "clicker-adestramento-caes-1.webp": ("Clicker preto com botão amarelo e pulseira espiral amarela", "Miniatura do clicker preto com pulseira amarela"),
    "clicker-adestramento-caes-2.webp": ("Clicker azul com botão amarelo e pulseira espiral", "Miniatura do clicker azul"),
    "clicker-adestramento-caes-3.webp": ("Quatro clickers nas cores azul, preto, laranja e vermelho, cada um com pulseira amarela", "Miniatura dos clickers coloridos"),
    "clicker-adestramento-caes-4.webp": ("Clicker azul visto de cima, com a pulseira espiral amarela", "Miniatura do clicker azul visto de cima"),
    "clicker-adestramento-caes-5.webp": ("Clicker vermelho com botão amarelo e pulseira espiral", "Miniatura do clicker vermelho"),
    "clicker-adestramento-caes-6.webp": ("Clicker vermelho de frente, com o botão amarelo em destaque", "Miniatura do botão amarelo do clicker vermelho"),
    "clicker-adestramento-caes-7.webp": ("Clicker vermelho de lado, mostrando o botão e o corpo oval", "Miniatura do clicker vermelho de lado"),
    "clicker-adestramento-caes-8.webp": ("Pulseira espiral amarela do clicker, com o anel de metal", "Miniatura da pulseira espiral amarela"),
    "clicker-adestramento-caes-9.webp": ("Pulseira amarela do clicker no pulso, com o clicker vermelho pendurado", "Miniatura do clicker no pulso"),
    "clicker-adestramento-caes-10.webp": ("Mão apertando o clicker vermelho na frente de um border collie sentado", "Miniatura do click na frente do cão"),
    "kit-mordedores-borracha-macica-1.webp": ("Kit de cinco mordedores pretos de borracha maciça: osso, anel, pneu, bola e disco", "Miniatura do kit de cinco mordedores pretos"),
    "kit-mordedores-borracha-macica-2.webp": ("As cinco peças do kit de mordedores pretos sobre uma mesa", "Miniatura das peças do kit sobre a mesa"),
    "kit-mordedores-borracha-macica-3.webp": ("Kit de mordedores pretos com corda, ao lado de um pastor alemão", "Miniatura do kit com corda e do pastor alemão"),
    "kit-mordedores-borracha-macica-4.webp": ("Osso de borracha maciça com corda e detalhe da textura que ajuda a tirar o tártaro", "Miniatura do osso de borracha com corda"),
    "kit-mordedores-borracha-macica-5.webp": ("Pneu de borracha maciça resistente, indicado para a limpeza dos dentes", "Miniatura do pneu de borracha maciça"),
    "kit-mordedores-borracha-macica-6.webp": ("Bola cravada de borracha maciça com 7,5 cm", "Miniatura da bola cravada de 7,5 cm"),
    "kit-mordedores-borracha-macica-7.webp": ("Argola de borracha maciça com corda", "Miniatura da argola de borracha com corda"),
    "kit-mordedores-borracha-macica-8.webp": ("Pneu de borracha maciça com 12 cm de diâmetro", "Miniatura do pneu de 12 cm"),
    "kit-mordedores-borracha-macica-9.webp": ("Osso de borracha maciça com corda, medindo 15,5 cm", "Miniatura do osso de 15,5 cm"),
    "kit-mordedores-borracha-macica-10.webp": ("Argola dentada de borracha maciça com 19 cm", "Miniatura da argola dentada de 19 cm"),
    "kit-mordedores-borracha-macica-11.webp": ("Bola de borracha maciça com 7,5 cm", "Miniatura da bola de borracha de 7,5 cm"),
    "kit-mordedores-borracha-macica-12.webp": ("Quadro das peças da linha black: material atóxico e uso para saúde bucal", "Miniatura do quadro da linha black"),
    "pipi-pode-educa-cao-1.webp": ("Kit Procão com os frascos Não Pode e Pode, de 200 ml", "Miniatura dos frascos Procão Não Pode e Pode"),
    "pipi-pode-educa-cao-2.webp": ("Infográfico do kit Procão: o Não Pode afasta e o Pode atrai para o lugar certo", "Miniatura do infográfico do kit Procão"),
    "pipi-pode-educa-cao-3.webp": ("Frascos Procão Não Pode e Pode, com a indicação de 200 ml cada", "Miniatura do kit com 200 ml em cada frasco"),
    "pipi-pode-educa-cao-4.webp": ("Golden retriever ao lado do frasco Procão Pode e de um tapete higiênico", "Miniatura do golden com o frasco Procão Pode"),
    "pipi-pode-educa-cao-5.webp": ("Aplicação do spray Procão Não Pode no sofá, com um gato por perto", "Miniatura do spray Procão no sofá"),
    "pipi-pode-educa-cao-6.webp": ("Cartaz do kit completo Procão, com os dois frascos de 200 ml", "Miniatura do cartaz do kit Procão"),
    "comedouro-lento-labirinto-1.webp": ("Comedouro labirinto Pet Games de silicone laranja, com detalhes do uso", "Miniatura do comedouro labirinto laranja"),
    "comedouro-lento-labirinto-3.webp": ("Comedouro labirinto laranja visto de cima, com o desenho em espiral", "Miniatura do labirinto visto de cima"),
    "comedouro-lento-labirinto-4.webp": ("Embalagem do comedouro Labirinto Pet Games, de silicone laranja", "Miniatura da embalagem do Labirinto Pet Games"),
    "comedouro-lento-labirinto-5.webp": ("Medidas do comedouro labirinto: 20 cm por 20 cm", "Miniatura das medidas de 20 cm"),
    "comedouro-lento-labirinto-6.webp": ("Comedouro labirinto laranja com ração espalhada nos sulcos", "Miniatura do labirinto com ração"),
    "comedouro-lento-labirinto-7.webp": ("Base do comedouro labirinto com ventosas antiderrapantes", "Miniatura das ventosas do comedouro"),
    "guia-peitoral-filhote-1.webp": ("Golden retriever com peitoral rosa e guia, em pé de perfil", "Miniatura do golden com peitoral rosa"),
    "guia-peitoral-filhote-2.webp": ("Tutor segurando o peitoral rosa com a guia", "Miniatura do peitoral rosa na mão"),
    "guia-peitoral-filhote-3.webp": ("Infográfico do peitoral azul: fita, fivela e peito acolchoado", "Miniatura do infográfico do peitoral azul"),
    "guia-peitoral-filhote-4.webp": ("Guia azul com mola anti-impacto e mosquetão", "Miniatura da guia com mola anti-impacto"),
    "guia-peitoral-filhote-5.webp": ("Golden com peitoral azul e o quadro de tamanhos do P ao GG", "Miniatura do peitoral azul e dos tamanhos"),
    "guia-peitoral-filhote-6.webp": ("Peitorais nas cores vermelho, preto, bege, azul e rosa", "Miniatura dos peitorais coloridos"),
    "guia-peitoral-filhote-7.webp": ("Golden retriever de perfil com peitoral e guia azuis", "Miniatura do golden com guia azul"),
    "guia-peitoral-filhote-8.webp": ("Selo da loja sobre o envio do peitoral e da guia", "Miniatura do selo de envio do peitoral"),
    "casinha-plastico-furacao-pet-1.webp": ("Casinha iglu Furacão Pet rosa e preta, com um filhote na frente", "Miniatura da casinha iglu rosa"),
    "casinha-plastico-furacao-pet-2.webp": ("Casinha iglu azul vista de frente, com a abertura", "Miniatura da casinha iglu azul"),
    "casinha-plastico-furacao-pet-3.webp": ("Casinha iglu rosa no jardim, com um filhote na entrada", "Miniatura da casinha no jardim"),
    "casinha-plastico-furacao-pet-4.webp": ("Texto com as medidas internas da casinha iglu N6: 55 cm, 78 cm e 75 cm", "Miniatura das medidas internas da casinha N6"),
    "casinha-plastico-furacao-pet-5.webp": ("Desenho da casinha iglu N6 com largura 55 cm, altura 78 cm e comprimento 75 cm", "Miniatura do desenho com as medidas da casinha"),
    "casinha-plastico-furacao-pet-6.webp": ("Esquema das medidas da entrada, do teto e da base da casinha N6", "Miniatura do esquema da casinha N6"),
    "casinha-plastico-furacao-pet-7.webp": ("Bandeja preta da casinha, com 55 cm por 73 cm", "Miniatura da bandeja da casinha"),
    "casinha-plastico-furacao-pet-8.webp": ("Quadro de raças da Furacão Pet ao lado do iglu azul", "Miniatura do quadro de raças da casinha"),
    "racao-golden-filhotes-1.webp": ("Pacote de ração Golden Formula para cães filhotes, sabor frango e arroz, 15 kg", "Miniatura do pacote Golden Formula filhotes"),
    "racao-golden-filhotes-2.webp": ("Frente do pacote Golden Formula filhotes, com o filhote e a indicação de 15 kg", "Miniatura da frente do pacote Golden"),
    "herbalvet-ta-1.webp": ("Galão de 1 litro do Herbalvet T.A. Ourofino, na embalagem nova", "Miniatura do galão Herbalvet T.A."),
    "herbalvet-ta-2.webp": ("Mão segurando o galão de 1 litro do Herbalvet T.A.", "Miniatura do galão Herbalvet na mão"),
    "herbalvet-ta-3.webp": ("Embalagem antiga e a nova do Herbalvet T.A., lado a lado", "Miniatura da embalagem antiga e da nova"),
    "herbalvet-ta-4.webp": ("Verso e frente do galão Herbalvet T.A. Ourofino", "Miniatura do verso e da frente do galão"),
    "herbalvet-ta-5.webp": ("Comparação da embalagem antiga com a nova do Herbalvet, que tem dosador", "Miniatura da embalagem com dosador"),
    "herbalvet-ta-6.webp": ("Rótulo do Herbalvet T.A. com a indicação de bactericida, fungicida e viricida", "Miniatura do rótulo do Herbalvet T.A."),
    "herbalvet-ta-7.webp": ("Verso do rótulo do Herbalvet T.A. Ourofino", "Miniatura do verso do rótulo"),
    "nylabone-puppy-1.webp": ("Embalagem do Nylabone Puppy Chew sabor frango, no formato de osso", "Miniatura da embalagem do Nylabone Puppy"),
    "nylabone-puppy-2.webp": ("Filhote deitado mordendo o osso Nylabone Puppy", "Miniatura do filhote mordendo o Nylabone"),
    "nylabone-puppy-3.webp": ("Comparação da embalagem antiga e da nova do Nylabone Puppy", "Miniatura da embalagem nova do Nylabone"),
    "nylabone-puppy-4.webp": ("Osso Nylabone Puppy para gengiva sensível, com a dica de congelar", "Miniatura do osso para gengiva"),
    "nylabone-puppy-5.webp": ("Quadro de resistência do Nylabone: Puppy Chew é o material mais macio", "Miniatura do quadro de resistência Puppy Chew"),
    "nylabone-puppy-6.webp": ("Tabela de tamanho do Nylabone Puppy, do XX-Small ao X-Small", "Miniatura da tabela de tamanho"),
    "nylabone-puppy-7.webp": ("Usos do Nylabone: dentição, tédio, treino e ansiedade", "Miniatura dos usos do Nylabone"),
    "nylabone-puppy-8.webp": ("Osso Nylabone Puppy sabor frango, fora da embalagem", "Miniatura do osso Nylabone fora da embalagem"),
    "nylabone-puppy-9.webp": ("Cartaz da doação de mordedores Nylabone para abrigos", "Miniatura do cartaz de doação da Nylabone"),
    "nylabone-puppy-10.webp": ("Cão na grama com bandana Nylabone", "Miniatura do cão com bandana Nylabone"),
    "nylabone-puppy-11.webp": ("Verso da embalagem do Nylabone Puppy", "Miniatura do verso da embalagem"),
    "nylabone-puppy-12.webp": ("Três cães na toalha com o texto Nylabone feito em Nova Jersey", "Miniatura dos cães com o Nylabone"),
    "portao-pet-pressao-1.webp": ("Portão pet branco com extensão, de 69 a 93 cm de largura e 80 cm de altura", "Miniatura do portão de 69 a 93 cm"),
    "portao-pet-pressao-2.webp": ("Portão pet instalado num vão, com uma pessoa e um cão", "Miniatura do portão instalado no vão"),
    "portao-pet-pressao-3.webp": ("Portão pet em varanda, quintal, porta e escada", "Miniatura do portão em vários vãos"),
    "portao-pet-pressao-4.webp": ("Detalhe do parafuso de pressão do portão pet", "Miniatura do parafuso de pressão"),
    "portao-pet-pressao-5.webp": ("Portão branco separando a sala, com cão e criança", "Miniatura do portão na sala"),
    "portao-pet-pressao-6.webp": ("Portão branco com os extensores que acompanham o kit", "Miniatura do portão com extensores"),
    "portao-pet-pressao-7.webp": ("Sala antes e depois do portão pet delimitando o espaço", "Miniatura da sala com e sem o portão"),
    "portao-pet-pressao-8.webp": ("Portão pet branco instalado no vão da sala", "Miniatura do portão no vão da sala"),
}

SWIPER_CSS = """  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" media="print" onload="this.media='all'">
  <style>
    .swiper-main { width: 100%; height: auto; background: #fafaf9; }
    .swiper-main .swiper-slide { display: flex; align-items: center; justify-content: center; height: auto; background: #fafaf9; }
    .swiper-main .swiper-slide img { image-orientation: from-image; display: block; width: auto; max-width: 100%; height: auto; max-height: 500px; margin-inline: auto; object-fit: contain; }
    .swiper-thumbs { height: 80px; box-sizing: border-box; padding: 10px 0; }
    .swiper-thumbs .swiper-slide { display: flex; align-items: center; justify-content: center; width: 20%; height: 100%; opacity: 0.4; cursor: pointer; }
    .swiper-thumbs .swiper-slide-thumb-active { opacity: 1; border: 2px solid #d97706; border-radius: 6px; }
    .swiper-thumbs .swiper-slide img { image-orientation: from-image; width: 100%; height: 100%; max-height: none; object-fit: contain; }
    .swiper-button-next, .swiper-button-prev { color: #d97706; }
    @media (max-width: 640px) { .swiper-main .swiper-slide img { max-height: 320px; } }
  </style>
"""

SWIPER_JS = """  <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
  <script>
    var swiperThumbs = new Swiper(".swiper-thumbs", {
      spaceBetween: 8,
      slidesPerView: 5,
      freeMode: true,
      watchSlidesProgress: true,
    });
    var swiperMain = new Swiper(".swiper-main", {
      spaceBetween: 10,
      autoHeight: true,
      navigation: { nextEl: ".swiper-button-next", prevEl: ".swiper-button-prev" },
      thumbs: { swiper: swiperThumbs },
    });
    swiperMain.on("slideChange", function () {
      swiperThumbs.slideTo(swiperMain.activeIndex);
    });
  </script>
"""


def gallery_html(slug, files, caption, indent):
    pad = " " * indent
    mains, thumbs = [], []
    for item in files:
        alt, thumb = ALTS[item["file"]]
        src = f"/imagens-produtos/{slug}/{item['file']}"
        mains.append(
            f'{pad}    <div class="swiper-slide"><img src="{src}" loading="lazy" width="{item["width"]}" height="{item["height"]}" class="mx-auto h-auto w-auto max-h-[500px] max-w-full object-contain rounded-xl shadow-md" alt="{alt}"></div>'
        )
        thumbs.append(
            f'{pad}    <div class="swiper-slide"><img src="{src}" loading="lazy" width="{item["width"]}" height="{item["height"]}" class="mx-auto h-full w-full object-contain" alt="{thumb}"></div>'
        )
    return "\n".join([
        f'{pad}<figure class="mb-10 overflow-hidden rounded-xl border border-stone-200 bg-white p-2 shadow-sm">',
        f'{pad}  <div class="swiper swiper-main">',
        f'{pad}    <div class="swiper-wrapper">',
        *mains,
        f'{pad}    </div>',
        f'{pad}    <div class="swiper-button-next"></div>',
        f'{pad}    <div class="swiper-button-prev"></div>',
        f'{pad}  </div>',
        f'{pad}  <div class="swiper swiper-thumbs mt-2">',
        f'{pad}    <div class="swiper-wrapper">',
        *thumbs,
        f'{pad}    </div>',
        f'{pad}  </div>',
        f'{pad}  <figcaption class="px-2 pb-1 pt-2 text-sm text-stone-500">{caption}</figcaption>',
        f'{pad}</figure>',
        "",
    ])


def image_json(slug, files, indent):
    urls = [f"{SITE}/imagens-produtos/{slug}/{item['file']}" for item in files]
    lines = [" " * indent + '"image": [']
    for i, url in enumerate(urls):
        comma = "," if i < len(urls) - 1 else ""
        lines.append(" " * (indent + 2) + json.dumps(url, ensure_ascii=False) + comma)
    lines.append(" " * indent + "],")
    return "\n".join(lines)


def update(slug, entry):
    page = PAGES[slug]
    path = ROOT / page["html"]
    text = path.read_text(encoding="utf-8")
    files = [item for item in entry["files"] if item["file"] not in SKIP]
    if not files:
        raise SystemExit(f"Sem fotos para {slug}")
    for item in files:
        if item["file"] not in ALTS:
            raise SystemExit(f"Alt ausente: {item['file']}")

    if "swiper-bundle.min.css" not in text:
        text = text.replace(
            '  <link rel="stylesheet" href="../output.css">\n',
            '  <link rel="stylesheet" href="../output.css">\n' + SWIPER_CSS,
            1,
        )
    if 'property="og:image"' not in text:
        first = files[0]
        image = f"{SITE}/imagens-produtos/{slug}/{first['file']}"
        text = text.replace(
            '  <meta name="twitter:card" content="summary">\n',
            '  <meta name="twitter:card" content="summary_large_image">\n',
            1,
        )
        og = f'  <meta property="og:image" content="{image}">\n'
        tw = f'  <meta name="twitter:image" content="{image}">\n'
        text = text.replace(
            f'  <meta property="og:url" content="{SITE}/reviews/{path.stem}">\n',
            f'  <meta property="og:url" content="{SITE}/reviews/{path.stem}">\n{og}',
            1,
        )
        marker = '  <meta name="twitter:description"'
        pos = text.find(marker)
        end = text.find("\n", pos)
        text = text[: end + 1] + tw + text[end + 1 :]

    if "primaryImageOfPage" not in text:
        first = files[0]
        block = (
            '      "primaryImageOfPage": {\n'
            '        "@type": "ImageObject",\n'
            f'        "url": "{SITE}/imagens-produtos/{slug}/{first["file"]}",\n'
            f'        "width": {first["width"]},\n'
            f'        "height": {first["height"]}\n'
            "      },\n"
        )
        text = text.replace('      "isPartOf": {\n', block + '      "isPartOf": {\n', 1)

    name_line = f'      "name": "{page["product"]}",\n'
    if text.count(name_line) != 1:
        raise SystemExit(f"Nome do produto não único em {path.name}: {text.count(name_line)}")
    after_name = text[text.find(name_line): text.find(name_line) + 400]
    if '"image":' not in after_name:
        text = text.replace(name_line, name_line + image_json(slug, files, 6) + "\n", 1)

    if 'class="swiper swiper-main"' not in text:
        lines = text.splitlines(keepends=True)
        idx = next(i for i, line in enumerate(lines) if "Ficha técnica" in line)
        start = idx
        while start > 0 and "overflow-hidden" not in lines[start]:
            start -= 1
        indent = len(lines[start]) - len(lines[start].lstrip(" "))
        figure = gallery_html(slug, files, page["caption"], indent)
        lines.insert(start, figure)
        text = "".join(lines)

    if "swiper-bundle.min.js" not in text:
        text = text.replace(
            '  <script src="../scripts/scroll-to-top.js" defer></script>\n',
            SWIPER_JS + '  <script src="../scripts/scroll-to-top.js" defer></script>\n',
            1,
        )

    block = re.search(r'<script type="application/ld\+json">(.*?)</script>', text, re.S)
    json.loads(block.group(1))
    path.write_text(text, encoding="utf-8")
    print(f"{path.name}: {len(files)} fotos")


def main():
    by_slug = {item["slug"]: item for item in MANIFEST}
    for slug in PAGES:
        update(slug, by_slug[slug])


if __name__ == "__main__":
    main()
