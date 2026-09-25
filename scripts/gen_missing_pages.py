#!/usr/bin/env python3
"""Gera as páginas faltantes do Guia do Adestramento a partir do briefing."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
BASE = "https://www.guiadoadestramento.com.br"
YMYL_ASIDE = """        <aside class="mt-6 max-w-2xl rounded-xl border border-amber-300 bg-amber-50 px-4 py-3 text-sm leading-relaxed text-amber-950" role="note">
          <p><strong>Nota editorial:</strong> Este conteúdo reflete a experiência prática de campo no treino do filhote. As orientações de saúde, vacinação e alimentação não substituem a consulta individualizada com um médico-veterinário.</p>
        </aside>
"""
CURSO_LINK = '<a class="font-semibold underline" href="./guia-completo-adestramento-canino">Guia Completo de Adestramento</a>'
SAME_AS = [
    "https://www.linkedin.com/in/philipef-dev/",
    "https://x.com/radarofertas_ph",
    "https://www.reddit.com/user/RadarOfertas_Philipe/",
    "https://br.pinterest.com/philipefdev/",
]


def dump(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=2)


def org() -> dict:
    return {
        "@type": "Organization",
        "@id": f"{BASE}/#organization",
        "name": "Guia do Adestramento",
        "url": f"{BASE}/",
        "sameAs": SAME_AS,
    }


def website() -> dict:
    return {
        "@type": "WebSite",
        "@id": f"{BASE}/#website",
        "url": f"{BASE}/",
        "name": "Guia do Adestramento",
        "publisher": {"@id": f"{BASE}/#organization"},
    }


def person() -> dict:
    return {
        "@type": "Person",
        "@id": f"{BASE}/#philipe",
        "name": "Philipe",
        "jobTitle": "Tutor e editor do Guia do Adestramento",
        "email": "philipefdev@gmail.com",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Volta Redonda",
            "addressRegion": "RJ",
            "addressCountry": "BR",
        },
        "sameAs": ["https://www.linkedin.com/in/philipef-dev/"],
        "worksFor": {"@id": f"{BASE}/#organization"},
        "url": f"{BASE}/quem-somos",
    }


def breadcrumbs(slug: str, name: str) -> dict:
    return {
        "@type": "BreadcrumbList",
        "@id": f"{BASE}/reviews/{slug}#breadcrumb",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Início", "item": f"{BASE}/"},
            {"@type": "ListItem", "position": 2, "name": "Reviews", "item": f"{BASE}/reviews"},
            {"@type": "ListItem", "position": 3, "name": name, "item": f"{BASE}/reviews/{slug}"},
        ],
    }


FOOTER_LINKS = """
      <div class="flex flex-wrap justify-center gap-4">
        <a href="/quem-somos" class="hover:text-stone-800">Sobre Mim</a>
        <a href="/metodologia" class="hover:text-stone-800">Metodologia</a>
        <a href="/politica-de-privacidade" class="hover:text-stone-800">Política de Privacidade</a>
        <a href="/termos-e-condicoes" class="hover:text-stone-800">Termos de Uso</a>
        <a href="/contato" class="hover:text-stone-800">Contato</a>
      </div>"""

SOCIAL = """
        <div class="flex items-center gap-4">
          <a href="https://x.com/radarofertas_ph" target="_blank" rel="noopener noreferrer" class="text-stone-400 hover:text-stone-900" aria-label="Twitter">X</a>
          <a href="https://www.reddit.com/user/RadarOfertas_Philipe/" target="_blank" rel="noopener noreferrer" class="text-stone-400 hover:text-stone-900" aria-label="Reddit">Reddit</a>
          <a href="https://br.pinterest.com/philipefdev/" target="_blank" rel="noopener noreferrer" class="text-stone-400 hover:text-stone-900" aria-label="Pinterest">Pinterest</a>
        </div>"""


def nav(prefix: str, active: str) -> str:
    def cls(key: str) -> str:
        if key == active:
            return "text-amber-800 font-medium"
        return "hover:text-stone-900"

    def mcls(key: str) -> str:
        if key == active:
            return "block px-4 py-2.5 font-medium text-amber-800 bg-amber-50"
        return "block px-4 py-2.5 text-stone-700 hover:bg-stone-50 hover:text-stone-900"

    return f"""  <header class="sticky top-0 z-50 border-b border-stone-200 bg-white/80 backdrop-blur">
    <div class="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8 flex items-center justify-between h-16">
      <a href="/" class="font-semibold tracking-tight text-stone-900">
        <span class="inline-flex items-center gap-2">
          <span class="inline-flex h-8 w-8 items-center justify-center rounded-full bg-amber-400 text-amber-950 text-sm">🐾</span>
          <span>Guia do Adestramento</span>
        </span>
      </a>
      <div class="flex items-center gap-2">
        <details class="relative sm:hidden">
          <summary class="flex h-10 w-10 cursor-pointer list-none items-center justify-center rounded-md border border-stone-200 text-stone-700 hover:bg-stone-100 [&::-webkit-details-marker]:hidden" aria-label="Abrir menu">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" /></svg>
          </summary>
          <nav class="absolute right-0 top-full z-60 mt-2 w-56 rounded-xl border border-stone-200 bg-white py-1 text-sm shadow-lg" aria-label="Menu principal">
            <a href="/" class="{mcls("home")}">Início</a>
            <a href="/quem-somos" class="{mcls("about")}">Sobre Mim</a>
            <a href="/reviews" class="{mcls("reviews")}">Reviews</a>
            <a href="/contato" class="{mcls("contato")}">Contato</a>
          </nav>
        </details>
        <nav class="hidden sm:flex gap-6 text-sm text-stone-600">
          <a href="/" class="{cls("home")}">Início</a>
          <a href="/quem-somos" class="{cls("about")}">Sobre Mim</a>
          <a href="/reviews" class="{cls("reviews")}">Reviews</a>
          <a href="/contato" class="{cls("contato")}">Contato</a>
        </nav>
      </div>
    </div>
  </header>"""


def footer(prefix: str) -> str:
    return f"""  <div id="scroll-up" title="Voltar ao topo" class="scrollup fixed bottom-12 right-6 bg-amber-600 p-2 rounded-full shadow-lg cursor-pointer transition-all duration-300 hover:bg-amber-700 opacity-0 pointer-events-none" aria-label="Voltar ao topo" role="button" tabindex="0">
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-4 h-4 text-white" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M5 15l7-7 7 7" /></svg>
  </div>
  <footer class="border-t border-stone-200 bg-stone-50">
    <div class="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8 py-6 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-stone-500">
      <div class="flex flex-col items-center gap-3 sm:items-start">
        <p>© 2026 Guia do Adestramento. Todos os direitos reservados.</p>
        {SOCIAL}
      </div>
      {FOOTER_LINKS}
    </div>
  </footer>
  <script src="/scripts/scroll-to-top.js" defer></script>"""


def shell(title: str, desc: str, canonical: str, graph: list, body: str, prefix: str, active: str) -> str:
    css = "/output.css"
    ld = dump({"@context": "https://schema.org", "@graph": graph})
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="preload" href="{css}" as="style">
  <link rel="stylesheet" href="{css}">
  <title>{title}</title>
  <link rel="canonical" href="{canonical}" />
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Guia do Adestramento">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="description" content="{desc}">
  <script type="application/ld+json">
{ld}
  </script>
</head>
<body class="antialiased bg-stone-50 text-stone-900">
{nav(prefix, active)}
{body}
{footer(prefix)}
</body>
</html>
"""


def faq_html(faqs: list[tuple[str, str]]) -> str:
    blocks = []
    for q, a in faqs:
        blocks.append(
            f"""        <details class="group rounded-2xl border border-stone-200 bg-white p-6 shadow-sm open:border-amber-200">
          <summary class="cursor-pointer list-none font-semibold text-stone-900 [&::-webkit-details-marker]:hidden">{q}</summary>
          <p class="mt-3 text-stone-600 leading-relaxed">{a}</p>
        </details>"""
        )
    return "\n".join(blocks)


def faq_schema(slug: str, faqs: list[tuple[str, str]]) -> dict:
    return {
        "@type": "FAQPage",
        "@id": f"{BASE}/reviews/{slug}#faq",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in faqs
        ],
    }


def sections_html(h2s: list[tuple[str, list[str]]]) -> str:
    out = []
    for title, paras in h2s:
        chunks = [f'        <h2 class="text-2xl font-bold text-stone-900">{title}</h2>']
        for p in paras:
            chunks.append(f'        <p class="mt-4 text-stone-700 leading-relaxed">{p}</p>')
        out.append("\n".join(chunks))
    return "\n".join(out)


def article_howto_body(kicker: str, h1: str, lead: str, h2s, faqs, related: str, ymyl: bool = False) -> str:
    ymyl_html = YMYL_ASIDE if ymyl else ""
    return f"""  <main>
    <section class="bg-linear-to-b from-amber-50 to-stone-50 border-b border-amber-100">
      <div class="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 py-10 lg:py-14">
        <p class="text-xs font-semibold tracking-[0.2em] text-amber-800 uppercase mb-3">{kicker}</p>
        <h1 class="text-3xl sm:text-4xl font-semibold tracking-tight text-stone-900 mb-3">{h1}</h1>
        <p class="text-base sm:text-lg text-stone-600 max-w-2xl">{lead}</p>
{ymyl_html}        <p class="mt-4 text-xs text-stone-500">Por <a href="/quem-somos" class="font-semibold text-stone-700 hover:underline">Philipe</a> · Atualizado em setembro de 2026 · Diário da Maraca, quitinete em Volta Redonda</p>
      </div>
    </section>
    <article class="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 py-12 space-y-10">
{sections_html(h2s)}
      <section>
        <h2 class="text-2xl font-bold text-stone-900 mb-6">Perguntas frequentes (FAQ)</h2>
        <div class="space-y-4">
{faq_html(faqs)}
        </div>
      </section>
      <div class="rounded-2xl border border-amber-200 bg-amber-50 p-6">
        <p class="text-sm sm:text-base text-amber-950">{related}</p>
      </div>
    </article>
  </main>"""


def product_body(p: dict) -> str:
    specs = "".join(
        f'<div class="flex border-b border-stone-100 p-4"><span class="font-bold w-1/2 text-stone-900">{k}</span><span class="text-stone-600 w-1/2">{v}</span></div>'
        for k, v in p["specs"]
    )
    return f"""  <main>
    <section class="bg-linear-to-b from-amber-50 to-stone-50 border-b border-amber-100">
      <div class="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 py-10 lg:py-14">
        <p class="text-xs font-semibold tracking-[0.2em] text-amber-800 uppercase mb-3">{p["kicker"]}</p>
        <h1 class="text-3xl sm:text-4xl font-semibold tracking-tight text-stone-900 mb-3">{p["h1"]}</h1>
        <p class="text-base sm:text-lg text-stone-600 max-w-2xl mb-8">{p["lead"]}</p>
{YMYL_ASIDE if p.get("ymyl") else ""}        <div class="mb-8 overflow-hidden rounded-2xl border-2 border-amber-200 bg-white shadow-lg">
          <div class="grid grid-cols-1 gap-5 p-5 sm:p-6 md:grid-cols-[1.4fr_1fr]">
            <div>
              <div class="flex items-center gap-2 mb-4">
                <div class="text-amber-400 text-lg leading-none" aria-hidden="true">★★★★★</div>
                <span class="text-sm font-extrabold text-stone-900">{p["rating"]}/5</span>
                <span class="text-xs text-stone-500">(análise editorial)</span>
              </div>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-sm">
                <div>
                  <p class="font-bold text-emerald-700 mb-1.5">✓ Pontos Fortes</p>
                  <ul class="space-y-1 text-stone-700">{"".join(f"<li>{x}</li>" for x in p["pros"])}</ul>
                </div>
                <div>
                  <p class="font-bold text-red-600 mb-1.5">✕ Pontos Fracos</p>
                  <ul class="space-y-1 text-stone-700">{"".join(f"<li>{x}</li>" for x in p["cons"])}</ul>
                </div>
              </div>
            </div>
            <div class="flex flex-col justify-center gap-3 border-t border-stone-100 pt-5 md:border-t-0 md:border-l md:pl-6 md:pt-0">
              <p class="text-xs font-semibold uppercase tracking-wider text-stone-500">Onde comprar agora</p>
              <a href="{p["ml"]}" rel="nofollow noopener sponsored" target="_blank" class="flex items-center justify-center rounded-xl bg-blue-600 px-6 py-4 text-base font-bold text-white hover:bg-blue-700">Ver no Mercado Livre</a>
              <a href="{p["amz"]}" rel="sponsored noopener noreferrer" target="_blank" class="flex items-center justify-center rounded-xl bg-amber-500 px-6 py-4 text-base font-bold text-stone-900 hover:bg-amber-400">Ver na Amazon</a>
            </div>
          </div>
          <div class="border-t border-stone-100 bg-stone-50/60 px-5 py-3 text-xs text-stone-500">Por <a href="/quem-somos" class="font-semibold text-stone-700 hover:underline">Philipe</a> • Atualizado em setembro de 2026</div>
        </div>
      </div>
    </section>
    <section class="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 py-12">
      <div class="mb-10 overflow-hidden border border-stone-200 rounded-lg bg-white">
        <div class="bg-stone-100 px-4 py-3 border-b border-stone-200"><h2 class="font-bold text-stone-800 italic">Ficha técnica</h2></div>
        <div class="grid grid-cols-1 md:grid-cols-2 text-sm">{specs}</div>
      </div>
      <div class="mb-12 rounded-lg border border-emerald-100 bg-emerald-50/50 p-6">
        <h2 class="text-xl font-bold text-stone-900 mb-3">{p["verdict_h2"]}</h2>
        <p class="text-stone-800 leading-relaxed">{p["verdict"]}</p>
      </div>
      <article class="space-y-10">
{sections_html(p["h2s"])}
        <section>
          <h2 class="text-2xl font-bold text-stone-900 mb-6">Perguntas frequentes (FAQ)</h2>
          <div class="space-y-4">{faq_html(p["faqs"])}</div>
        </section>
        <p class="text-[11px] text-stone-500">Participo de programas de afiliados. Se você comprar pelos links, posso receber comissão sem custo extra para você.</p>
      </article>
    </section>
  </main>"""


def relativize(html: str, in_reviews: bool) -> str:
    """Caminhos relativos + .html para o Live Server (e Vercel com cleanUrls)."""
    p = "../" if in_reviews else ""

    def review_href(match: re.Match[str]) -> str:
        slug = match.group(1)
        return f'href="./{slug}.html"' if in_reviews else f'href="reviews/{slug}.html"'

    html = re.sub(r'href="/reviews/([a-z0-9-]+)"', review_href, html)
    html = re.sub(r'href="\./([a-z0-9-]+)"', r'href="./\1.html"', html)
    html = html.replace('href="/output.css"', f'href="{p}output.css"')
    html = html.replace('src="/scripts/scroll-to-top.js"', f'src="{p}scripts/scroll-to-top.js"')
    for slug in (
        "quem-somos",
        "metodologia",
        "politica-de-privacidade",
        "termos-e-condicoes",
        "contato-obrigado",
        "contato",
        "reviews",
    ):
        html = html.replace(f'href="/{slug}"', f'href="{p}{slug}.html"')
        html = html.replace(f'href="{slug}"', f'href="{slug}.html"')
    html = html.replace('href="/"', f'href="{p}index.html"')
    return html


def write(path: Path, html: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    html = relativize(html, path.parent.name == "reviews")
    path.write_text(html, encoding="utf-8")
    print("wrote", path.relative_to(ROOT))


# --- conteúdo das fichas ---

def article_page(slug, crumb, kicker, h1, title, desc, lead, h2s, faqs, related, howto=False, ymyl=False):
    url = f"{BASE}/reviews/{slug}"
    webpage = {
        "@type": "WebPage",
        "@id": f"{url}#webpage",
        "url": url,
        "name": h1,
        "description": desc,
        "isPartOf": {"@id": f"{BASE}/#website"},
        "publisher": {"@id": f"{BASE}/#organization"},
    }
    if howto:
        entity = {
            "@type": "HowTo",
            "@id": f"{url}#howto",
            "name": h1,
            "description": desc,
            "step": [
                {"@type": "HowToStep", "position": i + 1, "name": t}
                for i, (t, _) in enumerate(h2s)
            ],
        }
    else:
        entity = {
            "@type": "Article",
            "@id": f"{url}#article",
            "headline": h1,
            "author": {
                "@type": "Person",
                "name": "Philipe Ferreira",
                "url": "https://www.linkedin.com/in/philipef-dev/",
            },
            "publisher": {"@id": f"{BASE}/#organization"},
            "mainEntityOfPage": {"@id": f"{url}#webpage"},
        }
    graph = [org(), website(), webpage, breadcrumbs(slug, crumb), entity, faq_schema(slug, faqs)]
    body = article_howto_body(kicker, h1, lead, h2s, faqs, related, ymyl=ymyl)
    html = shell(title, desc, url, graph, body, "../", "reviews")
    write(PUBLIC / "reviews" / f"{slug}.html", html)


def product_page(p: dict):
    slug = p["slug"]
    url = f"{BASE}/reviews/{slug}"
    webpage = {
        "@type": "WebPage",
        "@id": f"{url}#webpage",
        "url": url,
        "name": p["h1"],
        "description": p["desc"],
        "isPartOf": {"@id": f"{BASE}/#website"},
        "publisher": {"@id": f"{BASE}/#organization"},
    }
    product = {
        "@type": "Product",
        "@id": f"{url}#product",
        "name": p["product_name"],
        "brand": {"@type": "Brand", "name": p["brand"]},
        "description": p["desc"],
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": p["rating"],
            "reviewCount": "1",
            "bestRating": "5",
            "worstRating": "1",
        },
        "review": {
            "@type": "Review",
            "author": {
                "@type": "Person",
                "name": "Philipe Ferreira",
                "url": "https://www.linkedin.com/in/philipef-dev/",
            },
            "reviewRating": {"@type": "Rating", "ratingValue": p["rating"], "bestRating": "5"},
            "reviewBody": p["review_body"],
        },
        "offers": [
            {
                "@type": "Offer",
                "priceCurrency": "BRL",
                "url": p["amz"],
                "itemCondition": "https://schema.org/NewCondition",
                "availability": "https://schema.org/InStock",
                "seller": {"@type": "Organization", "name": "Amazon"},
                "price": p.get("price_amz", "99.90"),
                "priceValidUntil": "2026-12-31",
            },
            {
                "@type": "Offer",
                "priceCurrency": "BRL",
                "url": p["ml"],
                "itemCondition": "https://schema.org/NewCondition",
                "availability": "https://schema.org/InStock",
                "seller": {"@type": "Organization", "name": "Mercado Livre"},
                "price": p.get("price_ml", "89.90"),
                "priceValidUntil": "2026-12-31",
            },
        ],
    }
    graph = [org(), website(), webpage, breadcrumbs(slug, p["crumb"]), product, faq_schema(slug, p["faqs"])]
    html = shell(p["title"], p["desc"], url, graph, product_body(p), "../", "reviews")
    write(PUBLIC / "reviews" / f"{slug}.html", html)


def build_articles():
    article_page(
        "pitbull-filhote-2-meses",
        "Pitbull 2 meses",
        "Características · Raça · Filhote",
        "Características de um Pitbull filhote de 2 meses",
        "Características de um Pitbull filhote de 2 meses | Guia do Adestramento",
        "Peso, patas grandes, cabeça, orelhas em rosa, pelagem Red Nose e a janela de socialização de 8 a 12 semanas — o que o corpo de um Pitbull filhote já antecipa.",
        "Com cerca de 8 semanas a Maraca já mostrava o recado da raça: 3 a 6 kg, patas grossas, cabeça começando a quadrar e uma janela de socialização que não espera o “quando ela crescer”.",
        [
            ("Peso, porte e patas grandes: o que o corpo já antecipa", [
                "Aos 2 meses um Pitbull filhote pesa em média entre 3 kg e 6 kg, conforme sexo e linhagem (APBT, American Bully, Red Nose, Blue Nose). A Maraca chegou perto dos 2,9 kg na primeira pesagem comigo e ganhou cerca de 3 kg no mês seguinte — fermento puro.",
                "Patas visivelmente grandes em proporção ao corpo não são defeito: são antecipação de porte. O peito ainda é compacto, mas já largo o bastante para você entender que o adulto não cabe debaixo do sofá da quitinete.",
            ]),
            ("Cabeça, orelhas em rosa e pelagem (Red Nose, blaze, brindle)", [
                "A cabeça tem formato levemente quadrado, bochechas começando a marcar. Orelhas caídas ou semi-eretas (“em rosa”) são o padrão do filhote — não precisa cortar nada.",
                "Pelagem curta, lisa, brilhante. Na Maraca o recado visual é Red Nose: trufa rosada/amarronzada, pelagem chocolate e uma faixa branca (blaze) subindo do peito à cabeça. Brindle e sólido também existem na raça.",
            ]),
            ("APBT, American Bully e Blue Nose: o que muda no filhote", [
                "O mercado mistura nome. APBT tende a estrutura atlétic; Bully, mais massa. Blue Nose é pigmentação, não outro manual de adestramento. O que muda no dia a dia da quitinete é energia e mandíbula — não a cor do nariz.",
                "Trato a Maraca como Pitbull de porte médio/grande em crescimento: ração de filhote de raça grande, brinquedo que a boca não engole, portão que o adulto de 20 kg não vira.",
            ]),
            ("Janela de 8 a 12 semanas: por que essa fase não espera", [
                "Entre 8 e 12 semanas o cérebro está no pico de receptividade: barulho, piso, gente, o cheiro da Nina do outro lado do muro. É agora que reforço positivo cola. Depois, o mesmo susto vira medo cristalizado.",
                "Passeio na rua espera a V10. Socializar em casa — sons, superfícies, visita no corredor com distância — não espera. Essa janela fecha quer você treine ou não.",
            ]),
        ],
        [
            ("Quanto pesa um Pitbull filhote de 2 meses?", "Em geral 3 a 6 kg. A Maraca estava com 2,9 kg na primeira consulta e cresceu cerca de 3 kg em um mês. Use a tabela da ração de porte grande e o cocô firme como medidor, não a “mãozada” no olho."),
            ("Orelha caída de Pitbull filhote vai ficar em pé?", "Muitas ficam semi-eretas ou caídas. “Orelha em rosa” é comum. Não é sinal de doença isolado. Corte de orelha não entra neste guia."),
            ("Red Nose é outra raça?", "É pigmentação (trufa mais clara) dentro do tipo Pitbull/APBT. O manejo — dentição, energia, limites na quitinete — é o mesmo."),
            ("Posso apresentar outros cães aos 2 meses?", "Só se o outro cão estiver com V8/V10 e raiva em dia, e o contato for controlado. A Maraca e a Nina (Poodle) começaram por cheiro e muro. Rua espera o esquema vacinal."),
        ],
        'O corpo antecipa o adulto. O manejo está em <a class="font-semibold underline" href="./temperamento-pitbull-filhote">temperamento</a> e em <a class="font-semibold underline" href="./limites-cao-em-quitinete">limites na quitinete</a>.',
    )

    article_page(
        "temperamento-pitbull-filhote",
        "Temperamento",
        "Características · Comportamento",
        "Temperamento do Pitbull filhote: energia, boca e latido",
        "Temperamento do Pitbull filhote: energia, mouthing e latido | Guia do Adestramento",
        "Alta energia, fase da mordedura, raça pouco latidora e rosnar no pote: o que é temperamento de Pitbull filhote e o que é falta de manejo na quitinete.",
        "A Maraca não late o dia todo. Ela morde, pula, explora e capota. Quem espera um alarme de corredor se surpreende. Quem espera um filhote quieto se frustra.",
        [
            ("Alta energia e curiosidade: picos de brincadeira e sono profundo", [
                "O padrão é sprint curto + sono pesado. Depois de papelão ou pano congelado ela apaga de barriga para cima. Isso não é “já cansou para sempre”: a bateria recarrega.",
                "Na quitinete, o erro é deixar oito brinquedos no chão o tempo todo. Overdose de estímulo vira agitação. Rodízio de um ou dois itens gasta a cabeça de verdade.",
            ]),
            ("Fase da mordedura (mouthing): dente de leite, não maldade", [
                "Dos 2 aos 5 meses a gengiva coça. Pé, mão, chinelo, cueca, cortina, rodo, parede. Não é pirraça. É boca explorando e dente rasgando tecido.",
                "O protocolo que funcionou: ignorar o pulo, redirecionar para borracha ou papelão, nunca transformar a mão em cabo de guerra. Bronca falada vira brincadeira.",
            ]),
            ("Pitbull late pouco? O que isso muda no prédio", [
                "APBT/Bully em geral não são raça de alarme como Pinscher, York ou Poodle. A Maraca passou semanas quase muda. Motivo de comemorar no corredor — e de não achar que “não precisa socializar”.",
                "Quando late, costuma ser gatilho pontual (Nina do outro lado). Petisco na hora do latido da vizinha, sem festa de perseguição, foi o que dessensibilizou.",
            ]),
            ("Rosnar no pote: proteção de recurso em filhote", [
                "Ela rosnou quando a mão chegou no prato no meio da refeição. Filhote + fome + “vão tirar minha comida”. Não ignore e não grite. Troque a lógica: mão chega com pedaço melhor (frango cozido sem sal), não para roubar.",
                "Ração só na tigela, petisco de treino fora. Comando Deixa nasce daí. Adulto de 20 kg rosnando no pote é o filhote que aprendeu que a mão compete.",
            ]),
        ],
        [
            ("É normal Pitbull filhote não latir?", "Sim. Muitos são mais de corpo e boca do que de alarme. A Maraca quase não latia. Preocupe-se se surgir medo intenso ou agressão, não com o silêncio."),
            ("Filhote que morde pé vai ser agressivo?", "Mouthing de dentição não é agressão. Redirecione. Se a mordida vier com trava, olho fixo e recusa de soltar em contexto de recurso, aí é outro assunto — e aula particular."),
            ("O que fazer quando o filhote rosna na comida?", "Não encare, não tire o prato na marra. Aproxime a mão com um prêmio melhor jogado no pote. A mão passa a significar ganho."),
            ("Como gastar energia sem caminhada na rua?", "Rua espera vacina. Em casa: Kong/pano congelado, papelão supervisionado, comedouro lento. Estímulo mental cansa mais que circular na sala."),
        ],
        'Boca no lugar certo: <a class="font-semibold underline" href="./filhote-mordendo-tudo">filhote mordendo tudo</a> e <a class="font-semibold underline" href="./kong-puppy">Kong Puppy</a>.',
        howto=False,
    )

    article_page(
        "crescimento-peso-e-castracao",
        "Crescimento",
        "Características · Saúde",
        "Crescimento do Pitbull: peso, porte adulto e quando castrar",
        "Crescimento do Pitbull: peso, escore corporal e castração | Guia do Adestramento",
        "Do filhote de ~3 kg à fêmea APBT de 14 a 23 kg, escore corporal em casa, quando castrar e o que muda no cio — com a Maraca como régua.",
        "Em um mês a Maraca pareceu outra cadela. Quem adia limite “porque ainda é bebê” acorda com 20 kg no sofá.",
        [
            ("Do filhote de ~3 kg à fêmea de 14 a 23 kg", [
                "Fêmea APBT adulta saudável costuma ficar entre 14 e 23 kg. Bully pode passar disso. O peito alarga, a mandíbula fecha, o pulo que era fofo vira trator.",
                "Ganhar ~3 kg em 30 dias na fase de filhote pode ser normal. O medidor é costela visível demais vs. gordura na cintura — não a balança da vizinhança.",
            ]),
            ("Como checar escore corporal em casa", [
                "Vista de cima: cintura atrás das costelas. De lado: abdômen recolhido, não barril. Costela sente com a palma sem cavar. Barriga de verme (inchada + cocô mole) não é “fartura”.",
                "Ajuste ração pela tabela de porte grande e pelo cocô. 10 colheres três vezes ao dia ficou pouco quando ela passou dos 3 kg; subi com o veterinário na conversa, não no achismo eterno.",
            ]),
            ("Quando castrar e o que muda no cio", [
                "Com 2–3 meses dá tempo de planejar. A janela conversa com o veterinário: muitas fêmeas entre o primeiro cio e por volta de 12–18 meses, conforme protocolo local. Depois de castrada, cio some.",
                "Castrar de graça existe em campanha de prefeitura (RG, CPF, comprovante). Fila. Enquanto isso, o manejo de limite na quitinete não espera a cirurgia.",
            ]),
            ("Programa público de castração (documentos, fila)", [
                "Em Volta Redonda, campanhas abrem e fecham. Separe documento do tutor e da cadela (carteirinha de vacina ajuda). Não é walk-in no mesmo dia na maior parte dos casos.",
                "Cirurgia não substitui treino. Cadela castrada ainda destrói cortina se a gengiva pedir e o chão estiver vazio.",
            ]),
        ],
        [
            ("Quanto pesa uma Pitbull fêmea adulta?", "APBT tradicional: em geral 14 a 23 kg. A Maraca ainda é filhote; o plano de casa assume o teto, não o peso atual."),
            ("É normal ganhar 3 kg em um mês?", "Na fase de crescimento de porte grande, sim, se o escore corporal estiver limpo e o cocô firme. Dispare o vet se houver apatia, vômito ou barriga de verme."),
            ("Castrada entra no cio?", "Não. Depois da cirurgia o cio não volta. Antes da data, converse o protocolo com o veterinário que aplicou a V10."),
            ("Castrar cedo deixa o Pitbull “calmo”?", "Reduz comportamento de cio. Não apaga energia de raça nem mouthing. Isso é manejo e enriquecimento."),
        ],
        'Quantidade no pote: <a class="font-semibold underline" href="./alimentacao-filhote-porte-grande">alimentação</a> e <a class="font-semibold underline" href="./racao-filhotes-porte-grande">ração</a>.',
        ymyl=True,
    )

    article_page(
        "pitbull-e-outros-caes",
        "Outros cães",
        "Características · Socialização",
        "Pitbull filhote e outros cães: como apresentar sem atropelo",
        "Pitbull filhote e outros cães: Nina, Poodle e visitas | Guia do Adestramento",
        "Pitbull vs Poodle, cão medroso do outro lado do muro, com quantos meses apresentar e como receber visita sem o filhote virar um míssil.",
        "A vizinha da Maraca é a Nina, Poodle média medrosa. Muro de 1,70 m. O problema nunca foi “Pitbull é bravo”. Foi ritmo de corpo contra cão que já chega tenso.",
        [
            ("Pitbull vs Poodle: corpo pesado contra brincadeira leve", [
                "Maraca brinca com peitada, patada e morde-morde. Poodle responde a petisco e espaço. Daqui a poucos meses o peso inverte: a filhote passa a Nina. Se o primeiro encontro for solto no corredor, alguém se assusta.",
                "Deixe o cão menor dar o tom. Distância de metros, coleira frouxa, sessão de 3 a 5 minutos. Festa só quando os dois estiverem soltos no corpo, não só o Pitbull.",
            ]),
            ("Cão medroso do outro lado do muro: cheiro, distância e petisco", [
                "Elas já se conheciam pelo cheiro antes de se verem. Troque um pano. Depois visão a 2–3 metros. Nina latiu? Petisco na Maraca na hora — o latido vira previsão de comida, não de briga.",
                "Não force focinho no focinho. Medo da Nina não se resolve “para ela se acostumar” no colo da Pitbull.",
            ]),
            ("Com quantos meses apresentar (e o papel da vacina)", [
                "Imunidade do filhote é frágil até o meio do esquema V10. Contato direto só com cão vacinado (V8/V10 + raiva), sem pulga. Rua e cão desconhecido esperam o vet liberar — muitas vezes só após a 3ª dose, lá para o fim de outubro no calendário da Maraca.",
                "Apresentação visual no corredor do prédio, com donos presentes, pode começar antes da rua se o outro cão estiver em dia. Não é parque.",
            ]),
            ("Visitas em casa: porta, petisco e cantinho do sossego", [
                "Pote de ração perto da porta. Visita entra, grão no chão, quatro patas. Pulo some de recompensa. Caixa/toca da área é o “cantinho do sossego” se a agitação disparar.",
                "Filhote de 3 kg no colo da visita é treino invertido para o adulto de 20 kg. Ensaia agora o cumprimento no chão.",
            ]),
        ],
        [
            ("Com quantos meses o Pitbull pode encontrar outro cão?", "Depende da vacina do outro cão e do seu esquema V10. Cheiro e visão com barreira podem começar cedo. Parque e rua esperam o veterinário."),
            ("Pitbull e Poodle se dão bem?", "Podem. O risco é o estilo de brincadeira, não o rótulo. Controle o corpo do filhote grande. A Poodle medrosa decide a distância."),
            ("O outro cão late. Meu filhote fica com medo. E agora?", "Como a Maraca com a Nina: petisco no latido, você junto no quintal no começo, sem perseguir o som. Associação positiva, sessão curta."),
            ("Como receber visita sem o filhote pular?", "Ignore o pulo, recompense o chão, petisco na porta. Detalhe em filhote pulando nas pessoas."),
        ],
        'Passo a passo: <a class="font-semibold underline" href="./socializacao-filhote-com-outros-caes">socialização</a> e <a class="font-semibold underline" href="./filhote-pulando-nas-pessoas">pulo nas pessoas</a>.',
    )


def build_howtos():
    common_related = (
        'Produto que apaga o cheiro: <a class="font-semibold underline" href="./herbalvet-eliminador-enzimatico">Herbalvet</a>. '
        'Atrativo sanitário: <a class="font-semibold underline" href="./pipi-pode-educa-cao">Pipi Pode</a>. '
        f"Método: {CURSO_LINK}."
    )
    article_page(
        "xixi-e-coco-no-lugar-certo",
        "Xixi e cocô",
        "Cuidados · Banheiro",
        "Como ensinar o filhote a fazer xixi e cocô no lugar certo",
        "Como ensinar filhote a fazer xixi e cocô no lugar certo | Guia do Adestramento",
        "Quintal é banheiro, área é descanso. Pós-sono, pós-ração e pós-brincadeira. Por que Veja não apaga ureia e o que o Pipi Pode realmente faz.",
        "A Maraca urinava na área porque dormia lá. O alvo era o quintal de cimento. Sem briga. Com relógio.",
        [
            ("Quintal é banheiro, área é descanso: separe os espaços", [
                "Água, ração e toca de um lado. Banheiro do outro. Cão não faz onde come se o mapa estiver claro. Misturar os dois vira “qualquer piso serve”.",
                "Na sala, o xixi que passou vira ímã se o cheiro ficar. Enzimático na marca, não perfume de Veja por cima.",
            ]),
            ("Os três horários que não podem falhar (acordar, comer, brincar)", [
                "Acordou: quintal, 2–3 minutos parado, sem brincadeira. Comeu: 10 a 20 minutos depois, de novo. Brincou agitado: de novo. Fez lá? Festa curta e petisco.",
                "Aos 2 meses acidente é regra. Entre 4 e 6 meses, com essa rotina, ela pede o quintal. A Maraca zerou cocô na sala antes do xixi — xixi raro veio depois.",
            ]),
            ("Por que Veja e cloro não apagam o cheiro para o cão", [
                "O olfato dela é ordens de grandeza acima do seu. Veja tira o cheiro para você e deixa ureia para ela. O canto continua banheiro.",
                "Herbalvet T.A. diluído na PET de 2 L quebrou a molécula debaixo do sofá. Quintal de cimento: não “apague” o cheiro do banheiro certo; apague o da sala.",
            ]),
            ("Pipi Pode ajuda — e o que ele não faz sozinho", [
                "Atrativo sanitário (Educa Cão / Pipi Pode) aponta o nariz. Não substitui levar no horário nem limpar a sala. Sem rotina, o frasco vira gasto.",
                "Tapete higiênico é apoio, não banheiro eterno se o alvo é o quintal. Senão você treina tapete para sempre.",
            ]),
        ],
        [
            ("Quanto tempo até o filhote fazer só no quintal?", "Com treino diário, muitos avançam entre 4 e 6 meses. Aos 2 meses o acidente faz parte. Relógio pesa mais que bronca."),
            ("Posso brigar quando faz na sala?", "Não. Atraso de segundos e o cão não liga o xixi na bronca. Limpe, leve ao lugar certo no próximo ciclo, comemore o acerto."),
            ("Veja serve para xixi de cachorro?", "Para o seu nariz, às vezes. Para o dela, não. Use enzimático (Herbalvet) na marca errada."),
            ("Pipi Pode funciona sozinho?", "Não. Ajuda o olfato se você já leva no horário. Priorize enzimático e rotina; o kit sanitário é extra."),
        ],
        common_related,
        howto=True,
    )

    article_page(
        "filhote-mordendo-tudo",
        "Mordedura",
        "Cuidados · Dentição",
        "Como fazer o filhote parar de morder móveis, pés e sofá",
        "Filhote mordendo tudo: móveis, pés e sofá | Guia do Adestramento",
        "Não é pirraça: é gengiva de Pitbull. Substituição direcionada, pano congelado, papelão e quando o Kong entra — o que tirei da boca da Maraca na quitinete.",
        "Sofá, tapete, chinelo, cortina, rodo, parede, cueca. A lista da Maraca. A solução não foi grito. Foi objeto melhor na hora certa.",
        [
            ("Não é pirraça: é gengiva e mandíbula de Pitbull", [
                "Dente de leite afiado + coceira + força que já aparece no filhote. Móvel é textura. Pé é quente e se mexe — vira brinquedo se você reage.",
                "Ignore a mão como cabo de guerra. Congelou o corpo, o pé virou estátua chata, ela voltou para a caixa de papelão. Isso é aprendizado, não milagre.",
            ]),
            ("Substituição direcionada: do chinelo para o objeto certo", [
                "Antes de ela chegar no chinelo, o mordedor já está na mão. Boca no brinquedo = festa. Boca no móvel = “não” firme sem teatro, e borracha na boca na hora.",
                "Cueca usada tem seu cheiro: tesouro. Cesto fechado. Não transforme roupa suja em treino de cabo de guerra.",
            ]),
            ("Pano congelado e caixa de papelão: o que testei de graça", [
                "Pano com nó, molhado, freezer. Gengiva anestesia. Com ração seca no nó, o tempo de lambida dispara. Sem ração molhada em bloco — isso amoleceu o cocô no Kong caseiro.",
                "Papelão: destruição permitida, instinto de picar “presa”, custo zero. Só com você em casa. Recolhe pedaço grande. Não é todo dia que chega caixa enorme: rolo de papel, caixinha de mercado, PET sem tampa no rodízio.",
            ]),
            ("Quando o Kong (e o que não deixar sozinho)", [
                "Oito horas fora: Kong Puppy Medium congelado com ração seca, ou galho de borracha maciça. Pano e papelão rasgam e engolem. PET só supervisionada.",
                "Kong Puppy não é Senior roxo. Small engasga Pitbull. Detalhe na ficha do Kong.",
            ]),
        ],
        [
            ("Por que o filhote morde o sofá?", "Textura + tédio + dentição. Ocupe a boca com item permitido e recorte o acesso quando você não está. Não deixe o sofá como único “osso” da sala."),
            ("Pano congelado substitui o Kong?", "Enquanto você está em casa, sim, barato e eficaz. Sozinha, pano vira fiapo. Kong ou borracha maciça na ausência."),
            ("Posso deixar caixa de papelão o dia todo?", "Melhor como prêmio quando você chega. Sozinha, risco de engolir pedaço. A Maraca ganha a caixa no fim do expediente."),
            ("Ignorar a mordida no pé não é deixar barato?", "Reagir vira brincadeira. Ignorar + redirecionar ensina que pé não paga atenção. Funcionou com a Maraca voltando sozinha para o papelão."),
        ],
        'Review do mordedor: <a class="font-semibold underline" href="./kong-puppy">Kong Puppy</a> e <a class="font-semibold underline" href="./kong-classic-vs-puppy">Kong Classic vs Puppy</a>. '
        f"Método: {CURSO_LINK}.",
        howto=True,
    )

    article_page(
        "filhote-pulando-nas-pessoas",
        "Pular",
        "Cuidados · Convívio",
        "Como ensinar o filhote a não pular nas pessoas",
        "Como ensinar filhote a não pular nas pessoas | Guia do Adestramento",
        "Ignore o pulo, recompense as quatro patas, cuidado com a cabeça no chão e o que é fofo aos 3 kg vira problema aos 20 kg.",
        "A Maraca subia em mim porque era o caminho mais curto até o rosto. Lindinho agora. Impossível no adulto.",
        [
            ("Ignore o pulo, recompense as 4 patas no chão", [
                "Braços cruzados, costas, silêncio. Sem “não” cantado. No segundo em que as quatro patas no chão (ou o sentar), você desce, carinho, voz baixa.",
                "Empurrar vira brincadeira. O reforço é a atenção. Tire a atenção do pulo, devolva no chão.",
            ]),
            ("Cabeça na altura do rosto: o que o filhote entende como convite", [
                "Deitar no chão ou abaixar a cabeça dispara o “trator”. Ela pula mais. Se quiser deitar, entregue o mordedor antes ou levante. Não ensine que rosto no tapete = convite de luta.",
            ]),
            ("Visitas na porta: petisco no chão, não no colo", [
                "Grãos na entrada. Visita não pega no colo. Quatro patas = acesso ao cumprimento. Pulo = visita vira estátua igual a você.",
            ]),
            ("O que é fofo aos 3 kg vira problema aos 20 kg", [
                "Treine o peso futuro. Cada colo agora é ensaio do pulo no peito depois. A quitinete não tem espaço para um Pitbull adulto em modo canguru.",
            ]),
        ],
        [
            ("Por que o filhote pula em mim?", "Cumprimento de cão: chegar na cara. Energia + falta de regra. Não é dominância de filme. É caminho que pagou atenção até hoje."),
            ("Posso joelho no peito?", "Não. Dói, assusta, não ensina o que fazer. Ignore e recompense o chão."),
            ("Visita insiste em pegar no colo. E agora?", "Peça para a visita seguir a regra ou o treino zera na porta. Explique em uma frase: “Ela só ganha carinho com as quatro no chão.”"),
            ("Ela pula mais quando eu chego do trabalho?", "Chegada neutra. Água no quintal, 30 segundos sem festa, depois cumprimento no chão. Igual ansiedade de separação invertida."),
        ],
        'Guia e peitoral: <a class="font-semibold underline" href="./guia-e-peitoral-filhote">guia e peitoral</a>. '
        f"Método: {CURSO_LINK}.",
        howto=True,
    )

    article_page(
        "limites-cao-em-quitinete",
        "Quitinete",
        "Cuidados · Espaço",
        "Como criar um Pitbull em quitinete sem ele invadir quarto e cozinha",
        "Pitbull em quitinete: limites, portão e 8 horas fora | Guia do Adestramento",
        "Sala sim, cozinha e quarto não. Portão de pressão, o que deixar no chão em 8 h fora, choro na porta e chegada neutra — o que consolidou com a Maraca.",
        "Oito horas na sala sem invadir cozinha nem quarto. Isso não veio de milagre. Veio de mapa fixo e de não ceder “só hoje”.",
        [
            ("Restrição de ambiente: sala sim, resto não", [
                "Filhote solto na kitnet inteira caça xixi e cabo de panela. Um cômodo sob vista, depois amplia. Cozinha sem porta vira terra de ninguém — precisa de barreira.",
                "Quando eu saía, a geografia já estava na cabeça dela: quarto e cozinha não existem como circulação. Não é castigo. É planta baixa.",
            ]),
            ("Portão de pressão: altura, força e o que segura à noite", [
                "Sem porta entre sala e cozinha, o portão pet de pressão é o que segura. Ferro bem calibrado o filhote não derruba só encostando. Cheque travas antes de dormir.",
                "Muro de 1,70 m no quintal está ok agora. Adulto entediado procura apoio de pata. Altura sozinha não basta: sem estímulo ela testa o limite.",
            ]),
            ("Oito horas fora: o que deixar no chão (e o que recolher)", [
                "Água firme, um item de roer seguro (Kong ou borracha maciça), caminha. Recolha papelão, PET, bola recheável, vasilha de ração vazia. Overdose vira ansiedade.",
                "A Maraca ficou 8 h na sala, voltou para a caixa quando cheguei, sem forçar quarto. Neutralidade na saída e na chegada pesou mais que câmera.",
            ]),
            ("Choro na porta e chegada neutra", [
                "Ela chorou para entrar. Esperei segundos de silêncio e abri. Choro não abre. Silêncio abre. Saída sem despedida de novela.",
                "Isso não é frieza. É o contrário de ansiedade de separação ensaiada na porta.",
            ]),
        ],
        [
            ("Pitbull vive em apartamento pequeno?", "Sim, se o mapa de cômodos for claro, o banheiro for o quintal/área certa e a boca tiver trabalho. Sem isso, o adulto explode o espaço."),
            ("Ela chora quando fecho o quarto. Abro?", "Não no auge do choro. Espere o silêncio. Senão o choro vira interruptor."),
            ("O que deixar quando trabalho 8 horas?", "Água, caminha, um roedor seguro. Papelão e PET só com você. Detalhe no enriquecimento ambiental."),
            ("Portão de papelão serve?", "Improviso curto. Filhote de Pitbull testa força. Portão de pressão de ferro é o que eu usaria para dormir em paz."),
        ],
        'Barreira: <a class="font-semibold underline" href="./portao-pet-de-pressao">portão pet</a>. Toca: <a class="font-semibold underline" href="./casinha-plastico-furacao-pet">casinha plástica</a>. '
        f"Método: {CURSO_LINK}.",
        howto=True,
    )

    article_page(
        "alimentacao-filhote-porte-grande",
        "Alimentação",
        "Cuidados · Ração",
        "Quanto de ração dar para filhote de Pitbull (e quando o cocô mole denuncia erro)",
        "Quanto de ração dar para filhote de Pitbull | Guia do Adestramento",
        "Colheres, 3 refeições, jejum perigoso, granel vs saco, troca gradual e por que ração molhada no brinquedo amolece o cocô.",
        "Duas “mãos” de ração três vezes ao dia era demais no começo. Depois 5 colheres ficou pouco. O cocô foi o painel. Jejum de 12 h não.",
        [
            ("Colheres, refeições e por que jejum de 12 h é perigoso", [
                "Filhote de porte grande: 3 a 4 refeições. A Maraca fechou em 3 (manhã, tarde, noite). Colher de sopa cheia como copo medidor quando o saco não tem dosador.",
                "Esperar do jantar até o meio-dia seguinte: risco de hipoglicemia e vômito de espuma amarela. Café da manhã no horário. Ajuste quantidade, não apague refeição.",
            ]),
            ("Granel vs saco fechado: Dog Chow Minis não é ração de porte grande", [
                "A granel oxida, perde crocante, e o balcão empurra o que tem. Dog Chow Filhotes Minis e Pequenos não é fórmula de Pitbull em crescimento. NutriSano filhotes / Golden filhotes porte grande, sim.",
                "Voltei da NutriSano a granel para saco. Mistura gradual quando a loja só tinha Dog Chow: 75/25 e invertendo, para o intestino não cair junto.",
            ]),
            ("Como trocar de marca sem derrubar o intestino", [
                "Dois a cinco dias de mistura. Cocô mole demais: pause a troca, hidratação, vet se virar água, sangue ou apatia. Vermes também incham barriga — não confunda só com ração.",
            ]),
            ("Ração molhada no brinquedo: por que amolece o cocô", [
                "Kong com pasta molhada congelada = água + grão desfeito + frio no estômago. A Maraca cagou mole. Pano com grão seco no gelo não. Recheio seco ou “tampa” de banana mínima, sem bloco de lama.",
            ]),
        ],
        [
            ("Quantas refeições para filhote de 2–3 meses?", "3 a 4. A Maraca ficou em 3. Não faça jejum longo para “segurar o cocô”."),
            ("Como medir sem copo da marca?", "Colher de sopa cheia e total do dia na embalagem de porte grande. Ajuste pelo cocô firme e pelo escore corporal."),
            ("Ração a granel é aceitável?", "Emergência curta. Oxida. Prefira saco fechado da linha filhotes raças grandes."),
            ("Brinquedo recheado sempre solta o intestino?", "Não, se o grão continuar seco. O problema foi a ração ensopada congelada em bloco."),
        ],
        'Comparativo de marcas: <a class="font-semibold underline" href="./racao-filhotes-porte-grande">ração filhotes porte grande</a>. Engolir rápido: <a class="font-semibold underline" href="./comedouro-lento">comedouro lento</a>. '
        f"Método: {CURSO_LINK}.",
        howto=True,
        ymyl=True,
    )

    article_page(
        "vacinas-v8-v10-e-vermifugo",
        "Vacinas",
        "Cuidados · Veterinário",
        "Vacina V8, V10 e vermífugo no filhote: ordem, intervalo e o que esperar",
        "Vacina V8, V10 e vermífugo no filhote | Guia do Adestramento",
        "Diferença V8 e V10, quantas doses até a rua, vermífugo pelo peso, repetir em 15 dias, calombo da injeção e o que não aplicar no mesmo dia.",
        "A Maraca tomou V10 agitada como se nada tivesse acontecido. Calombo no local. Vermífugo não foi no mesmo dia. Rua ainda não.",
        [
            ("V8 ou V10: o que muda na leptospirose", [
                "As duas cobrem cinomose, parvovirose, hepatite, adenovírus, parainfluenza e coronavirose. V10 soma sorotipos extra de leptospira. Em muitos protocolos urbanos o vet prefere V10.",
                "Não são duas vacinas no mesmo frasco mágico misturado em casa. É o imunizante múltiplo que o clínico escolhe. Raiva é outra, depois.",
            ]),
            ("Quantas doses até a rua (e a antirrábica)", [
                "Esquema clássico de filhote: 3 doses de múltipla com intervalo de ~21–30 dias. A Maraca: 1ª, 2ª marcada, 3ª mais tarde. Antirrábica em dose nessa fase, muitas vezes junto da 3ª ou 2–3 semanas depois — o vet manda.",
                "Rua e cão desconhecido esperam o esquema. Área da casa e vizinha vacinada são outro risco. Campanha de raiva gratuita existe na prefeitura; a múltipla do filhote em geral é paga na clínica.",
            ]),
            ("Vermífugo: dose pelo peso, repetir em 15 dias, barriga inchada", [
                "Pese (você, depois você+cão). Líquido para filhote é prático. Drontal Pup, Chemital, Baskken, Endogard — o vet ou o peso na bula. Ovos não morrem todos: segunda dose em ~15 dias.",
                "Barriga inchada + cocô mole sem verme visível ainda pode ser verme. Prostração, sangue, vômito: clínica, não espera o fim de semana.",
            ]),
            ("Calombo da injeção, prostração e o que não misturar no mesmo dia", [
                "Nódulo no local some em dias. Alarme: cresce, esquenta, escorre. Preguiça 24–48 h é comum. A Maraca não desacelerou — também acontece.",
                "Vermífugo e V10 no mesmo dia não é o ideal. Primeiro vermífugo, cocô firme uns dias, depois vacina — ou a ordem que o clínico da Maraca fechou.",
            ]),
        ],
        [
            ("V8 e V10 são a mesma vacina?", "São múltiplas diferentes na cobertura de leptospira. Quem decide é o veterinário. Não misture frascos em casa."),
            ("Posso passear na rua após a 1ª dose?", "Em geral não. Espere o protocolo completo e o ok do vet. A Maraca ficou em casa/área até o meio do esquema."),
            ("Vermífugo e vacina no mesmo dia?", "Evite. O organismo já trabalha. Separe alguns dias, salvo orientação explícita da clínica."),
            ("Calombo no local da injeção é normal?", "Pequeno e em regressão, sim. Aumentando, quente ou com secreção: ligue no vet."),
        ],
        'Depois do esquema: <a class="font-semibold underline" href="./guia-e-peitoral-filhote">guia e peitoral</a>. '
        f"Método: {CURSO_LINK}.",
        howto=True,
        ymyl=True,
    )

    article_page(
        "socializacao-filhote-com-outros-caes",
        "Socialização",
        "Cuidados · Outros cães",
        "Como socializar Pitbull filhote com um cão medroso (e com visitas)",
        "Como socializar Pitbull filhote com cão medroso | Guia do Adestramento",
        "Troca de cheiro, petisco no latido da vizinha, comando Deixa para lixo e rua só depois da V10 — o protocolo da Maraca com a Nina.",
        "Quem estava assustada, no fim, era a Maraca com o latido da Nina. O treino inverteu o filme que eu tinha na cabeça.",
        [
            ("Troca de cheiro antes do olho no olho", [
                "Pano com cheiro da outra. Depois visão com metros de corredor. Donos presentes. 3 a 5 minutos. Quem decide chegar é o cão tenso, não o filhote eufórico.",
            ]),
            ("Nina latiu? Petisco na hora — sem festa de perseguição", [
                "Latido vira previsão de frango. Não jogue a Maraca para “se resolver”. Não transforme em perseguição no muro. Frango é treino; ração do pote fica para a refeição.",
            ]),
            ("Comando Deixa: lixo, comida no chão e o futuro adulto", [
                "Ela ainda nem olhava o lixo. Ensinei cedo: mão fechada, “deixa”, desiste, prêmio da outra mão. Adulto de Pitbull com lixo é emergência. O comando nasce agora.",
            ]),
            ("Rua só depois do esquema vacinal", [
                "Parque e cão de rua esperam V10+raiva. Até lá, corredor, quintal, visita controlada. Socializar não é sinônimo de asfalto.",
            ]),
        ],
        [
            ("Meu filhote tem medo do cão vizinho. Como começo?", "Igual Maraca: você junto, distância, petisco no gatilho (latido), sessões curtas. Não force o focinho."),
            ("O outro cão é medroso. Solto os dois?", "Não. O menor (ou o tenso) manda na distância. Pitbull filhote brinca pesado demais para “ver no que dá”."),
            ("Quando ensinar Deixa?", "Já. Antes de ela achar o lixo interessante. Mão fechada, espera o focinho sair, prêmio melhor."),
            ("Posso ir à calçada só para cheirar?", "Se o vet ainda não liberou rua, calçada é rua. Espere. Use o quintal e o corredor."),
        ],
        'Passeio com controle: <a class="font-semibold underline" href="./guia-e-peitoral-filhote">guia e peitoral</a>. '
        f"Método: {CURSO_LINK}.",
        howto=True,
    )

    article_page(
        "enriquecimento-ambiental-filhote",
        "Enriquecimento",
        "Cuidados · Brinquedos",
        "Enriquecimento ambiental para filhote: papelão, pano congelado e rodízio",
        "Enriquecimento ambiental para filhote: papelão e rodízio | Guia do Adestramento",
        "Overdose de brinquedo agita. Regra dos 2 itens, cardápio do dia, pano com ração seca vs Kong molhado, e o que deixar quando você sai.",
        "A Maraca tinha bola recheável, galho de borracha, duas PET, papelão, vasilhas. Nada era novidade. Recolhi tudo. A cabeça acalmou.",
        [
            ("Overdose de brinquedo: por que 8 itens no chão agitam mais", [
                "Cérebro de filhote pula de objeto em objeto. Não termina nenhum. Ansiedade sobe. Menos item, mais foco, mais sono depois.",
            ]),
            ("A regra dos 2 itens e o cardápio do dia (manhã / tarde / noite)", [
                "Manhã: bola/comedouro lento com parte da ração, depois recolhe. Tarde/ausência: Kong ou pano só se seguro — na prática, borracha maciça. Noite: papelão ou PET com você olhando. Rodízio no dia seguinte.",
            ]),
            ("Pano congelado com ração seca vs Kong com ração molhada", [
                "Pano + grão seco + gelo: lambida, endorfina, cocô firme. Kong caseiro com ração ensopada: cocô mole. A lição foi úmido em bloco vs seco na superfície.",
            ]),
            ("O que deixar quando você sai (e o que só existe com supervisão)", [
                "Sai: água, caminha, um roedor seguro. Chega: papelão vira prêmio (fator novidade). PET e corda só juntos — fio e plástico engolem.",
            ]),
        ],
        [
            ("Quantos brinquedos deixar no chão?", "No máximo um ou dois por turno. O resto no armário. Novidade vale mais que quantidade."),
            ("Papelão todo dia?", "Lógica todo dia (destruir algo permitido). Caixa gigante não. Rolo, caixinha, PET no rodízio."),
            ("Pano congelado solta o intestino?", "Com ração seca da rotina, a Maraca não amoleceu. O problema foi a pasta molhada no Kong."),
            ("Vasilha vazia no chão?", "Tira. Vira objeto de tédio. Ração só na hora da refeição."),
        ],
        'Quando o caseiro não basta: <a class="font-semibold underline" href="./kong-puppy">Kong Puppy</a> e <a class="font-semibold underline" href="./comedouro-lento">comedouro lento</a>. '
        f"Método: {CURSO_LINK}.",
        howto=True,
    )


def build_products():
    products = [
        dict(
            slug="kong-classic-vs-puppy",
            crumb="Kong Classic",
            kicker="Produtos · Mordedor",
            h1="Kong Classic ou Puppy: qual comprar em 2026?",
            title="Kong Classic ou Puppy: qual comprar em 2026? | Guia do Adestramento",
            desc="Puppy rosa/azul, Classic vermelho e Extreme preto: quando o Pitbull estoura o Puppy, tamanho M vs G e alternativas Odontopet/Benebone.",
            lead="O Puppy é a fase da Maraca. O Classic é o próximo recibo. O Extreme é se ela destruir o vermelho. O Senior roxo não entra na fila.",
            product_name="KONG Classic (transição a partir do Puppy)",
            brand="KONG",
            rating="4.7",
            review_body="Na quitinete, o filhote ainda pede Puppy. Eu já olho o Classic vermelho M/G para os 6–9 meses, quando a borracha macia ceder. P não. Senior não.",
            kicker_ok=True,
            ml="https://lista.mercadolivre.com.br/kong-classic",
            amz="https://www.amazon.com.br/s?k=kong+classic",
            price_amz="99.90",
            price_ml="89.90",
            pros=["Mesmo formato recheável do Puppy", "Borracha de adulto aguenta Pitbull", "Upgrade claro aos 6–9 meses"],
            cons=["Cedo demais rasga menos, mas o filhote precisa do Puppy agora", "Extreme preto é excesso se o vermelho ainda aguenta"],
            specs=[("Linhas", "Puppy → Classic → Extreme"), ("Cor Classic", "Vermelho"), ("Evitar", "Senior roxo"), ("Tamanho", "M ou G para Pitbull")],
            verdict_h2="Veredito: Puppy agora, Classic no calendário",
            verdict="Compre o Puppy Medium/Large hoje. Anote o Classic para quando aparecer sulco fundo na borracha macia. Não pule para o preto “por garantia”.",
            h2s=[
                ("Puppy, Classic vermelho e Extreme preto: borracha e idade", [
                    "Rosa/azul = filhote. Vermelho = Classic adulto. Preto = Extreme. Roxo = idoso. A Maraca no roxo seria pedaço na garganta.",
                    "O formato é o mesmo abacaxi oco. Muda a dureza. Recheio e freezer continuam valendo no Classic.",
                ]),
                ("Quando o filhote de Pitbull estoura o Puppy", [
                    "Entre 6 e 9 meses a mandíbula fecha. Sulco, borda mastigada, borracha cede. Aí troca. Antes, o Classic é desconforto na gengiva de leite.",
                ]),
                ("Tamanho M vs G e risco de engolir o P", [
                    "P/X-Small não. M cobre 7–16 kg na tabela da marca; G se o peito já é de cão grande. Pitbull filhote cresce rápido demais para o P.",
                ]),
                ("Odontopet, Benebone e nacionais: quando o dobro do Kong se paga", [
                    "Nylon (Nylabone/Benebone) dura no morde-morde e não recheia igual. Odontopet Dura Lagosta entra no rodízio com supervisão. O Kong paga o preço na ocupação com ração. Os dois não se excluem: regra dos 2 itens.",
                ]),
            ],
            faqs=[
                ("Já posso comprar o Classic para o filhote de 3 meses?", "Eu não. Gengiva de leite pede Puppy. Classic entra quando a borracha macia perder."),
                ("Extreme preto para Pitbull filhote?", "Não. É para adulto que já destruiu o vermelho."),
                ("Kong Puppy G ou Classic M?", "Agora: Puppy M ou G. Depois: Classic M ou G conforme o peso da época."),
                ("Nylabone substitui o Kong?", "Substitui durabilidade, não o recheio congelado. No rodízio da Maraca os dois teriam vez."),
            ],
        ),
        dict(
            slug="pipi-pode-educa-cao",
            crumb="Pipi Pode",
            kicker="Produtos · Sanitário",
            h1="Pipi Pode / Educa Cão funciona sozinho?",
            title="Pipi Pode / Educa Cão funciona sozinho? | Guia do Adestramento",
            desc="Atrativo sanitário Pipi Pode e Educa Cão: o que o olfato entende, por que não substitui rotina e enzimático, e o papel do tapete Durapads.",
            lead="O frasco ajuda o nariz. Não leva o filhote no quintal às 7h. Sem relógio, você só perfuma o erro.",
            product_name="Atrativo sanitário Pipi Pode / Educa Cão",
            brand="Educa Cão",
            rating="3.9",
            review_body="Na Maraca o enzimático e o horário pesaram mais. Pipi Pode é extra se o alvo é o quintal. Não compre antes do Herbalvet.",
            ml="https://lista.mercadolivre.com.br/pipi-pode-caes",
            amz="https://www.amazon.com.br/s?k=pipi+pode+educa+cao",
            price_amz="39.90",
            price_ml="34.90",
            pros=["Aponta o olfato para um canto", "Barato como complemento", "Kit Pode/Não Pode faz sentido em apartamento sem quintal"],
            cons=["Não funciona sozinho", "Quintal de cimento já é o alvo — priorize enzimático na sala"],
            specs=[("Tipo", "Atrativo / repelente sanitário"), ("Uso", "Complemento da rotina"), ("Prioridade", "Depois do enzimático"), ("Tapete", "Durapads só como apoio")],
            verdict_h2="Veredito: só depois da rotina e do Herbalvet",
            verdict="Se o banheiro é o quintal, o dinheiro primeiro vai no enzimático da sala. Pipi Pode entra se o nariz dela ainda não “lê” o cimento.",
            h2s=[
                ("Atrativo sanitário: o que o olfato do filhote entende", [
                    "Essência que marca “faça aqui”. O cérebro associa o cheiro ao ato se você já a leva no horário. Sem o ato, é só cheiro no cimento.",
                ]),
                ("Por que não substitui rotina, quintal e enzimático", [
                    "Acordou, comeu, brincou: quintal. Sala marcada: Herbalvet. O spray atrativo não apaga ureia velha nem ensina o relógio.",
                ]),
                ("Kit Pipi Pode + Pipi Não Pode: quando vale o dinheiro", [
                    "Apartamento só com tapete: o “não pode” na sala e o “pode” no tapete ajudam. Quitinete com quintal: o “não pode” na sala compete com o enzimático. Eu priorizaria um só sistema.",
                ]),
                ("Tapete higiênico Durapads: apoio, não banheiro eterno", [
                    "Longe da ração e da água. Se o alvo é quintal, o tapete é plano B de noite, não carreira. Senão você treina plástico para a vida.",
                ]),
            ],
            faqs=[
                ("Educa Cão é o mesmo que Pipi Pode?", "São nomes de linha de atrativo/repelente sanitário. O mecanismo é olfato + rotina. Confira o rótulo (atrativo vs. educador de “não faça aqui”)."),
                ("Comprei o spray e ela continua na sala. Falhou?", "Provavelmente falta horário e falta apagar o cheiro velho. Vá ao HowTo de xixi e ao Herbalvet."),
                ("Passo no quintal e na sala?", "Atrativo no banheiro certo. Enzimático no errado. Não misture os dois no mesmo metro."),
                ("Tapete substitui o quintal?", "Só se você aceitar tapete para sempre. A Maraca foi treinada para o cimento."),
            ],
        ),
        dict(
            slug="casinha-plastico-furacao-pet",
            crumb="Casinha",
            kicker="Produtos · Descanso",
            h1="Casinha de plástico nº 5 vale a pena para Pitbull filhote?",
            title="Casinha de plástico nº 5 para Pitbull filhote | Guia do Adestramento",
            desc="Plástico vs madeira (pulga), Furacão Pet / Tánatela 2 em 1, número 4 vs 5 no crescimento e a caixa de sapato até a casinha chegar.",
            lead="A Maraca dormia na caixa de sapato com pano. A casinha de plástico é o upgrade: lava, não vira hotel de pulga, teto que vira caminha no calor.",
            product_name="Casinha plástica 2 em 1 nº 5 (Furacão Pet / Tánatela)",
            brand="Furacão Pet",
            rating="4.6",
            review_body="Para quitinete e área, plástico nº 5 cobre o crescimento. Madeira na área úmida é pulga. Caixa de sapato aguenta a espera do frete, não o adulto.",
            ml="https://lista.mercadolivre.com.br/casinha-cachorro-plastico-numero-5",
            amz="https://www.amazon.com.br/s?k=casinha+plastico+cachorro+n5",
            price_amz="189.90",
            price_ml="169.90",
            pros=["Lava fácil", "2 em 1 (teto vira caminha)", "Nº 5 acompanha o porte grande"],
            cons=["Ocupa área na quitinete", "Filhote pode roer a borda no começo — supervisione"],
            specs=[("Material", "Plástico"), ("Tamanho", "Nº 4 filhote curto / Nº 5 crescimento"), ("Evitar", "Madeira em área úmida"), ("Interino", "Pano/camiseta com seu cheiro")],
            verdict_h2="Veredito: plástico nº 5, não madeira",
            verdict="Compre a de plástico 2 em 1 no maior tamanho que a área comporta. Madeira perde para pulga e chuva. A caixa de sapato é ponte, não destino.",
            h2s=[
                ("Plástico ou madeira: pulga, calor e quitinete", [
                    "Madeira em área de serviço: fresta, umidade, pulga. Plástico lava com enzimático. Calor: tire o teto no 2 em 1 e vira caminha.",
                ]),
                ("Furacão Pet / Tánatela 2 em 1: iglu que vira caminha", [
                    "O modelo que eu busquei para a Maraca: iglu tradicional ou 2 em 1 com teto removível. Confira se a listagem é nº 5 e se o teto sai de verdade.",
                ]),
                ("Número 4 vs 5 no crescimento de um porte grande", [
                    "Nº 4 fica apertado rápido. Nº 5 cobre meses de peito alargando. Medida interna importa mais que a foto. Pitbull não é Spitz.",
                ]),
                ("Caixa de sapato e coberta: o que usa até a casinha chegar", [
                    "Toca funciona porque é pequena e cheira a você. Não negue a caixa até o plástico chegar. Só tire se ela urinar dentro — separe banheiro e cama.",
                ]),
            ],
            faqs=[
                ("Casinha de madeira é mais “natural”?", "Na área úmida é mais pulga. Para a Maraca eu iria de plástico."),
                ("Nº 4 serve para filhote de Pitbull?", "Por poucas semanas. Nº 5 evita comprar duas vezes."),
                ("Ela recusa a casinha e volta para a caixa.", "Coloque o pano da caixa dentro da plástica. Não force. A toca antiga ainda vale."),
                ("Posso deixar a casinha na sala?", "Pode, se o banheiro for o quintal. Cama longe do xixi."),
            ],
        ),
        dict(
            slug="portao-pet-de-pressao",
            crumb="Portão pet",
            kicker="Produtos · Contenção",
            h1="Portão pet de pressão vale a pena em apartamento pequeno?",
            title="Portão pet de pressão em apartamento | Guia do Adestramento",
            desc="Como bloquear sala e cozinha sem porta, altura de 70 a 85 cm, ferro de pressão vs papelão e extensor para vão largo.",
            lead="Da sala até a cozinha não havia porta. Papelão é treino para o Pitbull adulto. Portão de pressão é o que me deixou dormir.",
            product_name="Portão de segurança pet de pressão (ferro)",
            brand="Genérico / grade pet",
            rating="4.8",
            review_body="Na quitinete o portão de ferro bem travado separou cozinha e sala. Filhote não derruba só encostando. Calibre a pressão. Papelão não é plano A.",
            ml="https://lista.mercadolivre.com.br/portao-pet-pressao",
            amz="https://www.amazon.com.br/s?k=portao+pet+pressao",
            price_amz="149.90",
            price_ml="129.90",
            pros=["Fecha vão sem obra", "Segura o filhote à noite", "Mapa de cômodos fica visível"],
            cons=["Adulto testa se estiver frouxo", "Vão irregular precisa de extensor"],
            specs=[("Tipo", "Pressão / tension gate"), ("Material", "Ferro"), ("Altura típica", "70 a 85 cm"), ("Extra", "Extensor e trava")],
            verdict_h2="Veredito: sim, se a casa não tem porta no vão",
            verdict="É o produto de manejo que mais pagou a paz na quitinete. Compre ferro, trava, meça o vão duas vezes. Altura padrão de 70 a 85 cm segura o filhote; o adulto precisa de treino e sem móveis de apoio.",
            h2s=[
                ("Como impedir a passagem da sala para a cozinha sem porta", [
                    "Barreira na linha do vão. Sem isso o treino de xixi e de “não comer lixo” vaza. Papelão e cadeira são noite única, não sistema.",
                ]),
                ("Altura, força do filhote e o que muda no adulto", [
                    "Portões de pressão padrão têm 70 a 85 cm. Filhote de 3 kg não escala isso com calma. Adulto usa sofá como escada. Tire móveis de apoio. Recalibre a pressão.",
                ]),
                ("Ferro de pressão vs papelão e móvel improvisado", [
                    "Papelão ela já destrói por lazer. Móvel desliza. Ferro com trava é o que eu deixaria enquanto durmo.",
                ]),
                ("Grade, extensor e vão mais largo que o portão", [
                    "Vão de corredor ou porta larga pede extensor da mesma marca (10 cm, 15 cm ou 20 cm). Meça o vão duas vezes. Sem extensor o portão fica frouxo e o filhote testa.",
                ]),
            ],
            faqs=[
                ("Pitbull consegue pular o portão de pressão?", "Portões de pressão padrão têm cerca de 70 cm a 85 cm de altura. Funcionam perfeitamente para filhotes, cães pequenos/médios ou como barreira de treino. Um adulto grande determinado consegue pular se não houver supervisão ou treino."),
                ("O portão de pressão estraga a parede ou o batente?", "Não. Ele utiliza manípulos de borracha que fixam por pressão, dispensando furos na parede — ideal para apartamentos alugados."),
                ("Filhote derruba portão de pressão?", "Se estiver frouxo, sim. Ajuste os manípulos até travar no máximo. Estruturas em ferro/aço aramado resistem muito bem a filhotes."),
                ("E se o meu vão for mais largo que o portão?", "Basta utilizar extensores encaixáveis (disponíveis em tamanhos como 10 cm, 15 cm ou 20 cm) para ajustar ao tamanho exato da sua porta ou corredor."),
            ],
        ),
        dict(
            slug="guia-e-peitoral-filhote",
            crumb="Guia e peitoral",
            kicker="Produtos · Passeio",
            h1="Guia e peitoral para filhote de 3 meses: o que comprar",
            title="Guia e peitoral para filhote de 3 meses | Guia do Adestramento",
            desc="Guia de nylon 1,5 a 2 m, por que retrátil ensina a puxar, peitoral vs coleira no crescimento e o que a guia faz em casa até a V10.",
            lead="Rua ainda não. Guia em casa é segurança no corredor, não passeio de parque. Retrátil ensina o oposto do que eu quero.",
            product_name="Guia de nylon 1,5–2 m + peitoral ajustável",
            brand="Genérico / guia lisa",
            rating="4.5",
            review_body="Para a Maraca aos 3 meses: guia lisa curta e peitoral que ainda vai ser trocado aos 6 meses. Retrátil fora da lista. Coleira fina some no pescoço que engrossa.",
            ml="https://lista.mercadolivre.com.br/guia-nylon-cachorro-2-metros",
            amz="https://www.amazon.com.br/s?k=guia+nylon+cachorro+2m+peitoral",
            price_amz="49.90",
            price_ml="39.90",
            pros=["Controle sem ensinar a puxar", "Barata", "Útil no corredor antes da rua"],
            cons=["Peitoral fica pequeno rápido", "Retrátil parece prática e estraga o treino"],
            specs=[("Guia", "Nylon 1,5 a 2 m"), ("Evitar", "Retrátil"), ("Peitoral", "Ajustável, troca ~6 meses"), ("Rua", "Só após V10")],
            verdict_h2="Veredito: lisa curta agora, retrátil nunca no treino",
            verdict="Compre uma guia de fita e um peitoral que você aceite trocar. Não invista em retrátil “para crescer com ela”.",
            h2s=[
                ("Guia de nylon 1,5 a 2 m: controle sem ensinar a puxar", [
                    "Comprimento curto = cão perto. No corredor da Nina isso evita disparo. A guia é freio, não punição.",
                ]),
                ("Por que guia retrátil é péssima para treino", [
                    "A tensão constante ensina: puxar aumenta o mundo. Perigosa em escada e rua. Para filhote de Pitbull, não.",
                ]),
                ("Peitoral vs coleira no crescimento (troca por volta dos 6 meses)", [
                    "Pescoço de filhote muda. Peitoral reparte a força. Coleira fina enterra. Aos 6 meses quase tudo fica pequeno — compre ajustável, não “definitivo”.",
                ]),
                ("Passeio só depois da V10: o que a guia faz em casa até lá", [
                    "Ensaiar vestir, andar até a porta, parar no sentar. Sem asfalto. Quando o vet liberar, o equipamento já não é novidade assustadora.",
                ]),
            ],
            faqs=[
                ("Qual comprimento de guia?", "1,5 a 2 m de nylon. Não retrátil."),
                ("Peitoral ou coleira no filhote?", "Peitoral ajustável para o puxão. Coleira de identificação pode ficar, mas o passeio/treino eu faria no peitoral."),
                ("Posso usar a guia em casa sem vacina completa?", "Sim, dentro de casa/corredor privado. Rua não."),
                ("Tenho que trocar aos 6 meses?", "Provável. Peito de Pitbull explode. Já entre no preço."),
            ],
        ),
        dict(
            slug="racao-filhotes-porte-grande",
            crumb="Ração",
            kicker="Produtos · Alimentação",
            h1="Melhor ração para filhote de Pitbull: NutriSano, Golden ou Premier?",
            title="Melhor ração para filhote de Pitbull: NutriSano, Golden, Premier | Guia do Adestramento",
            desc="Por que Dog Chow Minis e granel falham, NutriSano/Multidog/Golden/Premier, saco 3 kg vs 15 kg e o cocô como medidor.",
            lead="A loja empurrou Dog Chow Minis porque tinha. O intestino da Maraca e o porte dela pediam filhotes de raça grande em saco fechado.",
            ymyl=True,
            product_name="Ração filhotes raças grandes (NutriSano / Golden / Premier)",
            brand="NutriSano / Golden / Premier",
            rating="4.6",
            review_body="Voltei para linha de porte grande (NutriSano quando acho, Golden Filhotes/Mega ou Premier Fórmula filhotes grandes). Dog Chow a granel e Minis foram o erro barato.",
            ml="https://lista.mercadolivre.com.br/racao-golden-filhotes-racas-grandes",
            amz="https://www.amazon.com.br/s?k=racao+golden+filhotes+porte+grande",
            price_amz="219.90",
            price_ml="199.90",
            pros=["Fórmula de crescimento de porte grande", "Saco fechado não oxida igual granel", "Cocô firme quando a quantidade acerta"],
            cons=["15 kg é dinheiro na frente", "Balcão tenta empurrar o que tem na gaiola"],
            specs=[("Linha", "Filhotes raças grandes"), ("Evitar", "Minis/pequenos e granel crônico"), ("Saco", "3 kg para teste, 15 kg no preço"), ("Medidor", "Cocô + tabela")],
            verdict_h2="Veredito: porte grande em saco, não Minis a granel",
            verdict="Se achar NutriSano filhotes, ótimo — a Maraca já comeu. Se não, Golden ou Premier de raças grandes. Não aceite “é tudo a mesma proteína” no balcão.",
            h2s=[
                ("Por que Dog Chow Minis/Pequenos e granel falham nesse porte", [
                    "Minis é outra curva de cálcio/energia. Granel perde crocante e controle de lote. O papo “está no mercado há décadas” não muda o rótulo.",
                ]),
                ("NutriSano, Multidog, Golden Filhotes/Mega e Premier Fórmula", [
                    "NutriSano e Multidog compartilham fábrica em alguns relatos de loja — útil na transição. Golden Filhotes/Mega e Premier Fórmula raças grandes são fáceis de achar em 15 kg. Compare a linha filhotes, não o adulto.",
                ]),
                ("Saco de 3 kg vs 15 kg: preço, oxigênio e o papo do balcão", [
                    "3 kg testa aceitação. 15 kg cai o kg. Adulto Pitbull come ~12–15 kg/mês — o filhote ainda não. Não compre 15 kg de fórmula errada para “economizar”.",
                ]),
                ("Quantidade em colheres e o cocô como medidor", [
                    "Tabela da embalagem + colher padrão. Cocô firme = acertou. Mole demais: quantidade, troca brusca ou verme — não só “marca ruim”.",
                ]),
            ],
            faqs=[
                ("Golden Mega filhotes serve?", "Linha de porte grande sim. Confira se é filhotes, não adulto, no saco que você está pagando."),
                ("Premier é obrigatória?", "Não. É uma linha consistente de raças grandes. NutriSano/Golden também entram se forem a fórmula certa."),
                ("Posso misturar Dog Chow até acabar?", "Sim, em rampa (75/25…). Não trave nela se for Minis."),
                ("15 kg no filhote de 3 kg?", "Só se o kg compensar e você armazenar fechado, seco. Senão 3 kg até estabilizar o intestino."),
            ],
        ),
        dict(
            slug="comedouro-lento",
            crumb="Comedouro lento",
            kicker="Produtos · Alimentação",
            h1="Comedouro lento vale a pena para filhote que engole ração?",
            title="Comedouro lento para filhote que engole ração | Guia do Adestramento",
            desc="Soluço e ar na barriga, bola recheável, Colmeia Buddy, Stark Pet, Pet Games, furo largo demais e vs Kong seco.",
            lead="A Maraca devorava e soluça. Furo largo da bola largava o grão de uma vez. Precisava de labirinto, não de copo com tampa furada larga.",
            product_name="Comedouro lento / bola recheável (Stark, Pet Games, Buddy Colmeia)",
            brand="Pet Games / Buddy Toys / Stark Pet",
            rating="4.4",
            review_body="Vale se o furo for estreito o bastante para ela trabalhar. A bola de futebol americano com boca larga falhou. Kong seco e Colmeia fazem o mesmo serviço com mais foco.",
            ml="https://lista.mercadolivre.com.br/comedouro-lento-caes",
            amz="https://www.amazon.com.br/s?k=comedouro+lento+cachorro",
            price_amz="59.90",
            price_ml="44.90",
            pros=["Quebra o engolir em 10 segundos", "Gasta cabeça na refeição", "Labirinto Pet Games ocupa de verdade"],
            cons=["Furo largo = dinheiro jogado", "Deixar a refeição inteira no chão o dia todo vira tédio"],
            specs=[("Tipos", "Labirinto, bola, colmeia"), ("Furo", "Afunilado"), ("Uso", "Parte da porção, depois recolhe"), ("Vs Kong", "Kong congela; comedouro é refeição")],
            verdict_h2="Veredito: sim, se o desenho obrigar a língua a trabalhar",
            verdict="Compre labirinto ou colmeia, não “bola genérica de pet shop”. Recolha quando acabar a porção daquele turno.",
            h2s=[
                ("Soluço, ar na barriga e ração que some em segundos", [
                    "Engole ar com o grão. Soluço pós-refeição na Maraca era isso, não “frio na barriga” místico. Comedouro lento alonga.",
                ]),
                ("Bola recheável, Colmeia Buddy, Stark Pet e Pet Games", [
                    "Mini Fit e Labirinto Pet Games aparecem com nota alta nas lojas. Colmeia Buddy afunila. Stark é faixa de preço menor. Olhe o furo, não o marketing.",
                ]),
                ("Furo largo demais: o grão cai de uma vez", [
                    "Se em dois giros o pote esvazia, é comedouro inútil. Kong L ou colmeia forçam língua e giro.",
                ]),
                ("Comedouro lento vs Kong seco vs bandeja espalhada", [
                    "Bandeja/toalha com grãos é grátis e funciona. Kong seco ocupa mais. Comedouro é o meio-termo da refeição da manhã. Recolhe depois.",
                ]),
            ],
            faqs=[
                ("Comedouro lento causa cocô mole?", "Não por si. Mole veio de ração ensopada congelada, não do labirinto seco."),
                ("Posso deixar a bola o dia todo?", "Não. Terminou a porção, recolhe. Senão vira mais um item de overdose."),
                ("Qual marca você compraria?", "Labirinto Pet Games ou Colmeia se o furo for estreito. Conferir na foto do anúncio."),
                ("Filhote de 3 kg usa o tamanho grande?", "Tamanho em que o focinho entra e o grão não cai em avalanche. Médio costuma bastar."),
            ],
        ),
        dict(
            slug="guia-completo-adestramento-canino",
            crumb="Guia Completo",
            kicker="Produtos · Curso",
            h1="Guia Completo de Adestramento Canino 2026: vale a pena?",
            title="Guia Completo de Adestramento Canino 2026: vale a pena? | Guia do Adestramento",
            desc="O que o diário da Maraca não cobre sozinho, xixi/limites/mordedura como método vs produto, garantia de 7 dias e curso vs Kong+enzimático vs aula particular.",
            lead="O diário resolve o chão da quitinete. O curso empacota progresso semana a semana, suporte e o que fazer quando o treino trava — sem milagre em 7 dias.",
            product_name="Guia Completo de Adestramento Canino",
            brand="Guia do Adestramento",
            rating="4.9",
            review_body="O funil que eu uso no site: dica grátis (papelão, pano), produto que paga a conta (Kong, Herbalvet) e o programa para quem quer o método amarrado. Não substitui veterinário nem aula em caso de agressão.",
            ml="https://www.guiadoadestramento.com.br/reviews/guia-completo-adestramento-canino",
            amz="https://www.guiadoadestramento.com.br/reviews/guia-completo-adestramento-canino",
            price_amz="197.00",
            price_ml="197.00",
            pros=["Progressão semana a semana", "Linguagem de tutor, não de palco", "Encaixa no que já testei com a Maraca"],
            cons=["Exige consistência diária", "Não substitui vet nem caso de agressão grave"],
            specs=[("Formato", "Programa online / Hotmart"), ("Garantia", "7 dias (oferta da home)"), ("Foco", "Xixi, boca, limites, rotina"), ("Público", "Tutor de filhote/porte grande em casa")],
            verdict_h2="Veredito: vale se você quer o método amarrado, não um frasco a mais",
            verdict="Se você só precisa apagar xixi na sala, comece no Herbalvet e na rotina. Se precisa da sequência inteira com suporte, o Guia Completo é o produto digital deste site.",
            h2s=[
                ("O programa fecha o que o diário da Maraca não cobre sozinho?", [
                    "O chat é caso único: uma cadela, uma quitinete, dois meses. O curso generaliza horários, critérios e o que fazer quando o seu filhote não é a Maraca.",
                ]),
                ("Xixi, limites e mordedura: o que é método e o que é produto", [
                    "Método: relógio, ignore pulo, redirecione boca, mapa de cômodos. Produto: Kong, enzimático, portão. Um não anula o outro. O curso organiza os dois.",
                ]),
                ("Garantia, suporte e o que não é milagre em 7 dias", [
                    "A home fala em garantia de 7 dias e nota 4.9/5. Filhote não zera xixi em uma semana só porque o cartão passou. Recaída existe. Consistência pesa.",
                ]),
                ("Curso vs Kong + enzimático vs aula particular", [
                    "Kong+Herbalvet resolvem boca e cheiro. Curso resolve a sequência. Aula particular entra em medo intenso, agressão, trava. A Maraca ainda não pediu aula. O vizinho medroso pediria se a apresentação saísse do controle.",
                ]),
            ],
            faqs=[
                ("O curso substitui as reviews de produto?", "Não. Você ainda vai precisar de enzimático e de um mordedor. O curso não é um Kong em PDF."),
                ("Serve para Pitbull adulto?", "Os princípios sim. A dentição e a janela de 8–12 semanas não. Adulto com agressão: profissional no ambiente."),
                ("Tem milagre em 7 dias?", "Não. A garantia de reembolso não é promessa de xixi zerado em uma semana."),
                ("Preciso de clicker?", "Não é obrigatório. Palavra-marcador funciona. Há ficha extra de clicker no site se você quiser a ferramenta."),
            ],
        ),
    ]
    for p in products:
        product_page(p)


def build_hub():
    groups = [
        (
            "Características da raça e da fase",
            [
                ("/reviews/pitbull-filhote-2-meses", "Pitbull filhote de 2 meses", "Peso, Red Nose, janela de 8 a 12 semanas."),
                ("/reviews/temperamento-pitbull-filhote", "Temperamento", "Energia, mouthing, latido, rosnar no pote."),
                ("/reviews/crescimento-peso-e-castracao", "Crescimento e castração", "14–23 kg, escore, cio."),
                ("/reviews/pitbull-e-outros-caes", "Pitbull e outros cães", "Nina, Poodle, visitas."),
            ],
        ),
        (
            "Cuidados e adestramento no dia a dia",
            [
                ("/reviews/xixi-e-coco-no-lugar-certo", "Xixi e cocô no lugar certo", "Quintal, relógio, enzimático."),
                ("/reviews/filhote-mordendo-tudo", "Filhote mordendo tudo", "Sofá, pé, papelão, Kong."),
                ("/reviews/filhote-pulando-nas-pessoas", "Pular nas pessoas", "Quatro patas, 20 kg no futuro."),
                ("/reviews/limites-cao-em-quitinete", "Limites na quitinete", "8 h fora, portão, choro."),
                ("/reviews/alimentacao-filhote-porte-grande", "Alimentação", "Colheres, granel, cocô mole."),
                ("/reviews/vacinas-v8-v10-e-vermifugo", "Vacinas e vermífugo", "V8/V10, raiva, 15 dias."),
                ("/reviews/socializacao-filhote-com-outros-caes", "Socialização", "Cheiro, Deixa, rua depois."),
                ("/reviews/enriquecimento-ambiental-filhote", "Enriquecimento", "Rodízio, pano, overdose."),
            ],
        ),
        (
            "Produtos testados (reviews)",
            [
                ("/reviews/kong-puppy", "Kong Puppy", "Hero da dentição."),
                ("/reviews/kong-classic-vs-puppy", "Kong Classic vs Puppy", "Quando subir de linha."),
                ("/reviews/herbalvet-eliminador-enzimatico", "Herbalvet T.A.", "Ureia na sala."),
                ("/reviews/pipi-pode-educa-cao", "Pipi Pode / Educa Cão", "Atrativo, não mágica."),
                ("/reviews/casinha-plastico-furacao-pet", "Casinha plástica nº 5", "Não madeira."),
                ("/reviews/portao-pet-de-pressao", "Portão de pressão", "Cozinha sem porta."),
                ("/reviews/guia-e-peitoral-filhote", "Guia e peitoral", "Sem retrátil."),
                ("/reviews/racao-filhotes-porte-grande", "Ração porte grande", "NutriSano, Golden, Premier."),
                ("/reviews/comedouro-lento", "Comedouro lento", "Furo estreito."),
                ("/reviews/guia-completo-adestramento-canino", "Guia Completo", "Curso Hotmart."),
                ("/reviews/clicker-para-adestramento-vale-a-pena", "Clicker", "Ficha extra já no ar."),
            ],
        ),
    ]
    cards = []
    items = []
    pos = 1
    for h2, lista in groups:
        inner = []
        for href, name, blurb in lista:
            inner.append(
                f'<a href="{href}" class="block rounded-2xl border border-stone-200 bg-white p-5 shadow-sm hover:border-amber-300"><h3 class="text-lg font-bold text-stone-900">{name}</h3><p class="mt-2 text-sm text-stone-600">{blurb}</p></a>'
            )
            items.append(
                {
                    "@type": "ListItem",
                    "position": pos,
                    "item": {"@type": "WebPage", "name": name, "url": BASE + href},
                }
            )
            pos += 1
        cards.append(
            f'<section class="mb-14"><h2 class="text-2xl font-bold tracking-tight text-stone-900 mb-6">{h2}</h2><div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">{"".join(inner)}</div></section>'
        )
    graph = [
        org(),
        {
            "@type": "ItemList",
            "@id": f"{BASE}/reviews#itemlist",
            "name": "Reviews detalhados — Guia do Adestramento 2026",
            "description": "Características, cuidados e produtos testados com a Maraca.",
            "url": f"{BASE}/reviews",
            "itemListOrder": "https://schema.org/ItemListUnordered",
            "numberOfItems": len(items),
            "itemListElement": items,
        },
    ]
    body = f"""  <main>
    <section class="bg-linear-to-b from-amber-50 to-stone-50 border-b border-amber-100">
      <div class="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8 py-12">
        <h1 class="text-3xl font-bold tracking-tight text-stone-900">Minhas Avaliações</h1>
        <p class="mt-3 max-w-2xl text-stone-600">Diário de campo com a Maraca, Pitbull Red Nose em quitinete. Sem teoria de palco.</p>
      </div>
    </section>
    <div class="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8 py-12">
      {"".join(cards)}
    </div>
  </main>"""
    html = shell(
        "Reviews | Guia do Adestramento",
        "Características de Pitbull filhote, cuidados de adestramento e produtos testados na quitinete.",
        f"{BASE}/reviews",
        graph,
        body,
        "",
        "reviews",
    )
    write(PUBLIC / "reviews.html", html)


def inst_shell(title, desc, path, graph, h1, inner, active, robots=""):
    robots_tag = f'\n  <meta name="robots" content="{robots}">' if robots else ""
    css = "/output.css"
    ld = dump({"@context": "https://schema.org", "@graph": graph})
    body = f"""  <main>
    <div class="mx-auto max-w-3xl px-6 pt-16 pb-20">
      <h1 class="text-3xl md:text-4xl mb-8 font-semibold text-stone-900 border-b border-stone-200 pb-4">{h1}</h1>
      <div class="space-y-8 text-base md:text-lg leading-relaxed text-stone-700">
        {inner}
      </div>
    </div>
  </main>"""
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="preload" href="{css}" as="style">
  <link rel="stylesheet" href="{css}">{robots_tag}
  <title>{title}</title>
  <link rel="canonical" href="{BASE}{path}" />
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Guia do Adestramento">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{BASE}{path}">
  <meta name="description" content="{desc}">
  <script type="application/ld+json">
{ld}
  </script>
</head>
<body class="antialiased bg-stone-50 text-stone-900">
{nav("", active)}
{body}
{footer("")}
</body>
</html>
"""
    write(PUBLIC / f"{path.strip('/')}.html", html)


def build_institutional():
    inst_shell(
        "Sobre o projeto “Guia do Adestramento”",
        "Quem escreve o Guia do Adestramento: Philipe, diário da Maraca em Volta Redonda, transparência de afiliados.",
        "/quem-somos",
        [
            person(),
            {**org(), "founder": {"@id": f"{BASE}/#philipe"}},
            {**website(), "author": {"@id": f"{BASE}/#philipe"}},
            {
                "@type": "AboutPage",
                "@id": f"{BASE}/quem-somos#webpage",
                "url": f"{BASE}/quem-somos",
                "name": "Quem Somos | Guia do Adestramento",
                "description": "Conheça o Guia do Adestramento, o diário da Maraca e os critérios das reviews.",
                "inLanguage": "pt-BR",
                "isPartOf": {"@id": f"{BASE}/#website"},
                "mainEntity": {"@id": f"{BASE}/#philipe"},
            },
        ],
        "Sobre o projeto “Guia do Adestramento”",
        """
        <p>Criei o <strong>Guia do Adestramento</strong> para documentar o que funciona no chão — não no palco. A régua é a Maraca, Pitbull Red Nose filhote, em uma quitinete em <strong>Volta Redonda, RJ</strong>.</p>
        <h2 class="text-2xl font-semibold text-stone-900">Meu objetivo</h2>
        <p>Traduzir dentição, xixi, limites e produto em linguagem de quem volta do trabalho e encontra o sofá. Sem aversivo de grito e puxão como método.</p>
        <h2 class="text-2xl font-semibold text-stone-900">Como faço minhas recomendações</h2>
        <p>Testo no dia a dia, cruzo rótulo e o que o filhote realmente usa. Comissão de afiliado não escolhe o veredito. O detalhe está na <a class="underline" href="metodologia">Metodologia</a>.</p>
        <h2 class="text-2xl font-semibold text-stone-900">Compromisso de qualidade</h2>
        <p>Segurança (dente de leite, supervisão), ética e custo-benefício. Papelão grátis entra no texto; Kong entra quando o grátis não segura as 8 horas fora.</p>
        <h2 class="text-2xl font-semibold text-stone-900">Transparência e links de afiliado</h2>
        <p>Amazon e Mercado Livre: se você compra pelo link, posso receber comissão <strong>sem aumentar o preço</strong>. Detalhe na <a class="underline" href="politica-de-privacidade">Política de Privacidade</a>.</p>
        <h2 class="text-2xl font-semibold text-stone-900">Para quem este site é indicado</h2>
        <ul class="list-disc pl-5 space-y-2"><li>Tutor de filhote de porte grande em apartamento pequeno.</li><li>Quem precisa de xixi no quintal e boca fora do móvel.</li><li>Quem quer produto durável, não milagre em 7 dias.</li></ul>
        <h2 class="text-2xl font-semibold text-stone-900">Fale comigo</h2>
        <p>Philipe · Volta Redonda, RJ · resposta em até 2 dias úteis pelo <a class="underline" href="contato">contato</a> ou <a class="underline" href="mailto:philipefdev@gmail.com">philipefdev@gmail.com</a>.</p>
        """,
        "about",
    )

    inst_shell(
        "Metodologia | Guia do Adestramento",
        "Como o Philipe analisa adestramento e produtos: teste real com a Maraca, ética, segurança e custo-benefício.",
        "/metodologia",
        [
            person(),
            {**org(), "founder": {"@id": f"{BASE}/#philipe"}},
            website(),
            {
                "@type": "WebPage",
                "@id": f"{BASE}/metodologia#webpage",
                "url": f"{BASE}/metodologia",
                "name": "Metodologia | Guia do Adestramento",
                "description": "Como cada review de adestramento é feita: diário de campo, segurança e custo-benefício.",
                "inLanguage": "pt-BR",
                "isPartOf": {"@id": f"{BASE}/#website"},
                "author": {"@id": f"{BASE}/#philipe"},
                "publisher": {"@id": f"{BASE}/#organization"},
                "datePublished": "2026-09-11",
                "dateModified": "2026-09-11",
            },
        ],
        "Guia do Adestramento — nossa metodologia de análise",
        """
        <p>Não tenho laboratório. Tenho uma cadela, uma quitinete e o hábito de anotar o que a boca e o intestino respondem.</p>
        <blockquote class="border-l-4 border-amber-500 bg-amber-50 rounded-r-xl p-5 italic">Prefiro um pano congelado que funcionou a um slogan de “adestra em 7 dias”.</blockquote>
        <h2 class="text-2xl font-medium text-stone-900 mb-3">Como escolho o que analisar</h2>
        <p>O que a Maraca encontrou de verdade: Kong, enzimático, ração de porte grande, portão, casinha, guia. Não cubro o pet shop inteiro.</p>
        <h2 class="text-2xl font-medium text-stone-900 mb-3">Fonte e critério de comparação</h2>
        <p>Diário de campo, rótulo, bula, o que o filhote usa sozinho em 8 h. Eixos: ética (sem aversivo), segurança (engasgo, dente de leite), adequação ao temperamento, custo-benefício.</p>
        <h2 class="text-2xl font-medium text-stone-900 mb-3">O passo a passo da análise</h2>
        <p><strong>1.</strong> Problema real (xixi na sala, sofá, pulo). <strong>2.</strong> Solução de custo zero. <strong>3.</strong> Produto se o grátis não segura. <strong>4.</strong> Efeito colateral (cocô mole, overdose de brinquedo). <strong>5.</strong> Veredito para um perfil — Pitbull filhote em espaço pequeno.</p>
        <h2 class="text-2xl font-medium text-stone-900 mb-3">Como fecho o veredito</h2>
        <p>Nota editorial, não média de marketplace. Comissão não entra na conta.</p>
        <h2 class="text-2xl font-medium text-stone-900 mb-3">Imparcialidade</h2>
        <p>Dog Chow Minis levou texto duro porque falhou no porte. Kong Puppy levou texto bom porque ocupou a boca. Os dois podem ter link de afiliado.</p>
        <h2 class="text-2xl font-medium text-stone-900 mb-3">Revisão e atualização</h2>
        <p>Atualizo quando o peso, a vacina ou o produto muda de linha (Puppy → Classic). Data no rodapé das fichas: setembro de 2026.</p>
        """,
        "home",
    )

    contato_inner = """
        <p>Eu mesmo respondo. Sou o Philipe. Até <strong>2 dias úteis</strong>.</p>
        <h2 class="text-xl font-bold text-stone-900">Como falar comigo</h2>
        <ul class="space-y-2"><li><strong>E-mail:</strong> <a class="text-amber-800 underline" href="mailto:philipefdev@gmail.com">philipefdev@gmail.com</a></li>
        <li><strong>WhatsApp:</strong> <a class="text-amber-800 underline" href="https://wa.me/5524999173920">+55 24 99917-3920</a></li>
        <li><strong>Onde:</strong> Volta Redonda, RJ</li></ul>
        <h2 class="text-xl font-bold text-stone-900">Enviar mensagem</h2>
        <form action="https://api.web3forms.com/submit" method="POST" class="space-y-6 rounded-2xl border border-stone-200 bg-white p-6">
          <input type="hidden" name="access_key" value="921cad7b-2476-41b0-ab4a-a68cb90c88e6">
          <input type="hidden" name="subject" value="Contato — Guia do Adestramento">
          <input type="hidden" name="redirect" value="https://www.guiadoadestramento.com.br/contato-obrigado">
          <input type="hidden" name="botcheck" value="">
          <div><label class="block text-sm font-bold mb-2" for="nome">Nome</label>
          <input class="w-full rounded-xl border border-stone-200 bg-stone-50 px-4 py-3" type="text" id="nome" name="name" autocomplete="name"></div>
          <div><label class="block text-sm font-bold mb-2" for="email">Email *</label>
          <input class="w-full rounded-xl border border-stone-200 bg-stone-50 px-4 py-3" type="email" id="email" name="email" required autocomplete="email"></div>
          <div><label class="block text-sm font-bold mb-2" for="mensagem">Como posso te ajudar? *</label>
          <textarea class="w-full rounded-xl border border-stone-200 bg-stone-50 px-4 py-3" id="mensagem" name="message" rows="4" required placeholder="Ex.: xixi na sala, Kong, ração de porte grande…"></textarea></div>
          <div class="flex items-start gap-3"><input type="checkbox" id="lgpd" name="lgpd_consent" value="1" required class="mt-1">
          <label for="lgpd" class="text-sm">Li a <a class="underline" href="politica-de-privacidade">Política de Privacidade</a>. *</label></div>
          <button class="w-full rounded-xl bg-amber-500 py-4 font-bold text-stone-900 hover:bg-amber-400" type="submit">Enviar mensagem</button>
        </form>
        <h2 class="text-xl font-bold text-stone-900">Sobre o que você pode escrever</h2>
        <p>Filhote, produto citado nas reviews, correção de fato, parceria. Não atendo emergência veterinária por formulário — vá à clínica.</p>
        <h2 class="text-xl font-bold text-stone-900">Onde estou</h2>
        <p>Volta Redonda, Rio de Janeiro, Brasil.</p>
    """
    graph_c = [
        {
            **org(),
            "email": "philipefdev@gmail.com",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Volta Redonda",
                "addressRegion": "RJ",
                "addressCountry": "BR",
            },
            "contactPoint": {
                "@type": "ContactPoint",
                "contactType": "customer support",
                "email": "philipefdev@gmail.com",
                "availableLanguage": ["pt-BR"],
                "url": "https://wa.me/5524999173920",
            },
        },
        website(),
        {
            "@type": "ContactPage",
            "@id": f"{BASE}/contato#webpage",
            "url": f"{BASE}/contato",
            "name": "Contato | Guia do Adestramento",
            "description": "Fale com o Philipe em Volta Redonda, RJ.",
            "inLanguage": "pt-BR",
            "isPartOf": {"@id": f"{BASE}/#website"},
        },
    ]
    inst_shell(
        "Guia do Adestramento — fale comigo",
        "Fale com o Philipe em Volta Redonda, RJ. E-mail, formulário ou WhatsApp — resposta em até 2 dias úteis.",
        "/contato",
        graph_c,
        "Guia do Adestramento — fale comigo",
        contato_inner,
        "contato",
    )

    write(
        PUBLIC / "contato-obrigado.html",
        shell(
            "Mensagem recebida | Guia do Adestramento",
            "Recebemos sua mensagem. Resposta em até 2 dias úteis.",
            f"{BASE}/contato-obrigado",
            [
                org(),
                {
                    "@type": "WebPage",
                    "@id": f"{BASE}/contato-obrigado#webpage",
                    "url": f"{BASE}/contato-obrigado",
                    "name": "Mensagem recebida",
                    "isPartOf": {"@id": f"{BASE}/#website"},
                },
            ],
            """  <main>
    <div class="mx-auto max-w-lg px-6 py-24 text-center">
      <p class="text-sm font-semibold text-amber-800 mb-2">Contato</p>
      <h1 class="text-2xl sm:text-3xl font-bold text-stone-900 mb-4">Mensagem recebida</h1>
      <p class="text-stone-600 mb-8">Obrigado. Respondo em até <strong>2 dias úteis</strong> no e-mail informado. Urgência: WhatsApp na página de contato.</p>
      <div class="flex flex-col sm:flex-row gap-3 justify-center">
        <a href="/" class="rounded-xl bg-amber-500 px-6 py-3 font-semibold text-stone-900">Voltar ao início</a>
        <a href="contato" class="rounded-xl border border-stone-200 px-6 py-3 font-semibold">Nova mensagem</a>
      </div>
    </div>
  </main>""",
            "",
            "contato",
        ).replace("<meta name=\"description\"", "<meta name=\"robots\" content=\"noindex, nofollow\">\n  <meta name=\"description\"", 1),
    )

    inst_shell(
        "Política de Privacidade | Guia do Adestramento",
        "Dados do formulário, cookies, Analytics e links de afiliados no Guia do Adestramento.",
        "/politica-de-privacidade",
        [
            org(),
            website(),
            {
                "@type": "PrivacyPolicy",
                "@id": f"{BASE}/politica-de-privacidade#webpage",
                "url": f"{BASE}/politica-de-privacidade",
                "name": "Política de Privacidade | Guia do Adestramento",
                "description": "Como tratamos dados, cookies e afiliados.",
                "isPartOf": {"@id": f"{BASE}/#website"},
                "publisher": {"@id": f"{BASE}/#organization"},
                "datePublished": "2026-09-11",
                "dateModified": "2026-09-11",
            },
        ],
        "Política de Privacidade | Guia do Adestramento",
        """
        <p>Operado por <strong>Philipe</strong>, Volta Redonda, RJ. Atualização: <strong>11 de setembro de 2026</strong>.</p>
        <h2 class="text-2xl font-medium text-stone-900 mb-3">Quais dados coleto</h2>
        <ul class="list-disc pl-5 space-y-2"><li>Formulário: nome, e-mail, mensagem.</li><li>WhatsApp, se você iniciar.</li><li>Navegação via Analytics, se estiver ativo.</li><li>Cliques de afiliado (Amazon, Mercado Livre).</li></ul>
        <p>Não há newsletter nem login.</p>
        <h2 class="text-2xl font-medium text-stone-900 mb-3">Para que uso seus dados</h2>
        <p>Responder você. Melhorar o conteúdo. Atribuir comissão se houver compra. Não envio e-mail marketing.</p>
        <h2 class="text-2xl font-medium text-stone-900 mb-3">Com quem os dados são tratados</h2>
        <p>Web3Forms (formulário), Google (Analytics, se houver), redes de afiliados, WhatsApp/Meta se você chamar. Não vendo lista de e-mails.</p>
        <h2 class="text-2xl font-medium text-stone-900 mb-3">Cookies</h2>
        <p>Essenciais, análise e afiliados. Você pode bloquear no navegador.</p>
        <h2 class="text-2xl font-medium text-stone-900 mb-3">Links de afiliados</h2>
        <p>Comissão possível, <strong>sem aumentar o preço</strong>. O veredito não é vendido.</p>
        <h2 class="text-2xl font-medium text-stone-900 mb-3">Seus direitos (LGPD)</h2>
        <p>Acesso, correção, exclusão, informação. Escreva para philipefdev@gmail.com.</p>
        <h2 class="text-2xl font-medium text-stone-900 mb-3">Retenção e contato</h2>
        <p>Mensagens de contato pelo tempo de responder e obrigação legal. Dúvida: <a class="underline" href="contato">contato</a>.</p>
        """,
        "home",
    )

    inst_shell(
        "Termos e Condições | Guia do Adestramento",
        "Termos de uso do Guia do Adestramento: conteúdo editorial, afiliados e limitação de responsabilidade.",
        "/termos-e-condicoes",
        [
            org(),
            website(),
            {
                "@type": "TermsOfService",
                "@id": f"{BASE}/termos-e-condicoes#webpage",
                "url": f"{BASE}/termos-e-condicoes",
                "name": "Termos e Condições | Guia do Adestramento",
                "isPartOf": {"@id": f"{BASE}/#website"},
                "publisher": {"@id": f"{BASE}/#organization"},
                "datePublished": "2026-09-11",
                "dateModified": "2026-09-11",
            },
        ],
        "Termos e Condições | Guia do Adestramento",
        """
        <p>Ao usar o site você concorda com estes termos. Philipe, Volta Redonda, RJ. Atualização: <strong>11 de setembro de 2026</strong>.</p>
        <h2 class="text-2xl font-medium text-stone-900 mb-3">Sobre o nosso conteúdo</h2>
        <p>Reviews são opinião editorial com base no diário da Maraca e na <a class="underline" href="metodologia">Metodologia</a>. Não são laudo veterinário nem garantia de resultado no seu cão.</p>
        <h2 class="text-2xl font-medium text-stone-900 mb-3">Uso do conteúdo e propriedade intelectual</h2>
        <p>Cite trecho curto com crédito e link. Não reproduza ficha inteira sem autorização.</p>
        <h2 class="text-2xl font-medium text-stone-900 mb-3">Comentários e cadastro</h2>
        <p>Não há comentários públicos nem área logada.</p>
        <h2 class="text-2xl font-medium text-stone-900 mb-3">Limitação de responsabilidade</h2>
        <p>Emergência (diarreia com sangue, prostração, engasgo): veterinário. Produtos de terceiros seguem a loja. Links de afiliado não tornam este site vendedor.</p>
        <h2 class="text-2xl font-medium text-stone-900 mb-3">Alterações e contato</h2>
        <p>Posso atualizar estes termos. Dúvida: <a class="underline" href="contato">contato</a>.</p>
        """,
        "home",
    )


def build_sitemap():
    urls = [
        ("/", "1.0"),
        ("/reviews", "0.9"),
        ("/quem-somos", "0.4"),
        ("/metodologia", "0.5"),
        ("/contato", "0.4"),
        ("/politica-de-privacidade", "0.3"),
        ("/termos-e-condicoes", "0.3"),
    ]
    slugs = [
        "pitbull-filhote-2-meses",
        "temperamento-pitbull-filhote",
        "crescimento-peso-e-castracao",
        "pitbull-e-outros-caes",
        "xixi-e-coco-no-lugar-certo",
        "filhote-mordendo-tudo",
        "filhote-pulando-nas-pessoas",
        "limites-cao-em-quitinete",
        "alimentacao-filhote-porte-grande",
        "vacinas-v8-v10-e-vermifugo",
        "socializacao-filhote-com-outros-caes",
        "enriquecimento-ambiental-filhote",
        "kong-puppy",
        "kong-classic-vs-puppy",
        "herbalvet-eliminador-enzimatico",
        "pipi-pode-educa-cao",
        "casinha-plastico-furacao-pet",
        "portao-pet-de-pressao",
        "guia-e-peitoral-filhote",
        "racao-filhotes-porte-grande",
        "comedouro-lento",
        "guia-completo-adestramento-canino",
        "clicker-para-adestramento-vale-a-pena",
    ]
    for s in slugs:
        urls.append((f"/reviews/{s}", "0.8"))
    body = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, pr in urls:
        body.append(
            f"  <url><loc>{BASE}{loc}</loc><lastmod>2026-09-11</lastmod><priority>{pr}</priority></url>"
        )
    body.append("</urlset>")
    (PUBLIC / "sitemap.xml").write_text("\n".join(body) + "\n", encoding="utf-8")
    print("wrote public/sitemap.xml")
    (PUBLIC / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nDisallow: /contato-obrigado\nSitemap: {BASE}/sitemap.xml\n",
        encoding="utf-8",
    )
    print("wrote public/robots.txt")


def build_home():
    ranking = [
        (
            "1",
            "Kong Puppy",
            "/reviews/kong-puppy",
            "Hero da dentição na quitinete: recheio, freezer e boca fora do sofá.",
        ),
        (
            "2",
            "Xixi e cocô no lugar certo",
            "/reviews/xixi-e-coco-no-lugar-certo",
            "Quintal é banheiro. Relógio depois de acordar, comer e brincar. Sem briga.",
        ),
        (
            "3",
            "Filhote mordendo tudo",
            "/reviews/filhote-mordendo-tudo",
            "Mouthing não é raiva. Papelão, pano congelado e Kong no rodízio.",
        ),
        (
            "4",
            "Herbalvet T.A.",
            "/reviews/herbalvet-eliminador-enzimatico",
            "Veja não apaga ureia. Enzimático na marca da sala, não perfume.",
        ),
        (
            "5",
            "Limites na quitinete",
            "/reviews/limites-cao-em-quitinete",
            "Portão, toca e 8 h sozinha sem teatro. Espaço pequeno pede mapa claro.",
        ),
        (
            "6",
            "Guia Completo de Adestramento",
            "/reviews/guia-completo-adestramento-canino",
            "Quando o diário e o produto não fecham o caso: curso, suporte e o que não é milagre.",
        ),
    ]
    faqs = [
        (
            "Em quanto tempo o filhote para de fazer xixi na sala?",
            "Aos 2 meses o acidente faz parte. Com relógio (acordar, comer, brincar) e enzimático na marca errada, muitos avançam entre 4 e 6 meses. Bronca atrasada não ensina.",
        ),
        (
            "Kong Puppy resolve a mordedura sozinho?",
            "Não. Ele ocupa a boca. Sem rodízio, supervisão e “não” no sofá, o móvel continua alvo. É o melhor mordedor recheável que usei com a Maraca — não é babá.",
        ),
        (
            "Posso socializar na rua antes da V10?",
            "Rua e chão de praça esperam o protocolo. Cheiro, colo e cães vacinados de confiança entram antes. Detalhe na ficha de vacinas e na de socialização.",
        ),
        (
            "Filhote de Pitbull aguenta 8 horas sozinho?",
            "Aos poucos, com toca, portão e item ocupado. Não é abandono se a saída é trabalho e o mapa da casa está treinado. Choro nos primeiros minutos é comum; destruição depois pede enriquecimento, não só bronca.",
        ),
        (
            "Latido em quitinete é falta de adestramento?",
            "Às vezes é tédio, campainha ou vizinho no corredor. Reforço do silêncio e gestão de janela pesam mais que coleira de choque. Temperamento de Pitbull filhote já traz energia; o manejo segura.",
        ),
    ]
    itemlist = {
        "@type": "ItemList",
        "@id": f"{BASE}/#itemlist",
        "name": "O que realmente segura móvel, xixi e limites em 2026",
        "description": "Soluções testadas com a Maraca, Pitbull Red Nose em quitinete em Volta Redonda.",
        "url": f"{BASE}/",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i,
                "item": {
                    "@type": "WebPage",
                    "name": name,
                    "url": BASE + href,
                    "description": blurb,
                },
            }
            for i, (_, name, href, blurb) in enumerate(ranking, 1)
        ],
    }
    graph = [
        org(),
        {
            **website(),
            "description": "Adestramento de Pitbull filhote na prática: diário da Maraca, reviews de produtos e rotina em quitinete.",
        },
        {
            "@type": "WebPage",
            "@id": f"{BASE}/#webpage",
            "url": f"{BASE}/",
            "name": "Adestramento de Pitbull filhote na prática: o que funciona em casa (2026)",
            "description": "Diário de campo com a Maraca em Volta Redonda. Xixi, mordedura, Kong, enzimático e limites em espaço pequeno — sem teoria de palco.",
            "isPartOf": {"@id": f"{BASE}/#website"},
            "publisher": {"@id": f"{BASE}/#organization"},
            "mainEntity": {"@id": f"{BASE}/#itemlist"},
        },
        itemlist,
        {
            "@type": "FAQPage",
            "@id": f"{BASE}/#faq",
            "url": f"{BASE}/#faq",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": a},
                }
                for q, a in faqs
            ],
        },
    ]
    cards = "".join(
        f"""          <a href="{href}" class="block rounded-2xl border border-stone-200 bg-white p-6 shadow-sm hover:border-amber-300">
            <p class="text-xs font-bold uppercase tracking-wider text-amber-800 mb-2">{n}º</p>
            <h3 class="text-lg font-bold text-stone-900">{name}</h3>
            <p class="mt-2 text-sm text-stone-600">{blurb}</p>
          </a>"""
        for n, name, href, blurb in ranking
    )
    mais = [
        ("/reviews/pitbull-filhote-2-meses", "Pitbull filhote de 2 meses"),
        ("/reviews/temperamento-pitbull-filhote", "Temperamento"),
        ("/reviews/crescimento-peso-e-castracao", "Crescimento e castração"),
        ("/reviews/pitbull-e-outros-caes", "Pitbull e outros cães"),
        ("/reviews/filhote-pulando-nas-pessoas", "Pular nas pessoas"),
        ("/reviews/alimentacao-filhote-porte-grande", "Alimentação porte grande"),
        ("/reviews/vacinas-v8-v10-e-vermifugo", "Vacinas V8/V10"),
        ("/reviews/socializacao-filhote-com-outros-caes", "Socialização"),
        ("/reviews/enriquecimento-ambiental-filhote", "Enriquecimento"),
        ("/reviews/kong-classic-vs-puppy", "Kong Classic vs Puppy"),
        ("/reviews/pipi-pode-educa-cao", "Pipi Pode"),
        ("/reviews/casinha-plastico-furacao-pet", "Casinha plástica"),
        ("/reviews/portao-pet-de-pressao", "Portão pet"),
        ("/reviews/guia-e-peitoral-filhote", "Guia e peitoral"),
        ("/reviews/racao-filhotes-porte-grande", "Ração filhotes"),
        ("/reviews/comedouro-lento", "Comedouro lento"),
        ("/reviews/clicker-para-adestramento-vale-a-pena", "Clicker"),
    ]
    mais_html = "".join(
        f'<li><a class="text-amber-800 underline hover:text-amber-950" href="{h}">{n}</a></li>'
        for h, n in mais
    )
    faq_blocks = faq_html(faqs)
    body = f"""  <main>
    <section class="bg-linear-to-b from-amber-50 to-stone-50 border-b border-amber-100">
      <div class="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8 py-12 lg:py-16">
        <p class="mb-4 inline-flex items-center gap-2 rounded-full border border-amber-200 bg-white px-3 py-1 text-xs font-medium uppercase tracking-wider text-amber-800">Diário da Maraca · Volta Redonda · 2026</p>
        <h1 class="max-w-3xl text-3xl font-bold tracking-tight text-stone-900 sm:text-4xl lg:text-5xl">Adestramento de Pitbull filhote na prática: o que funciona em casa (2026)</h1>
        <p class="mt-5 max-w-2xl text-lg text-stone-600">Pare o xixi na sala, a boca no sofá e o caos da quitinete com o que eu testo no chão — não em palco de curso. A Maraca é Pitbull Red Nose. O laboratório é 30 m².</p>
        <div class="mt-8 flex flex-wrap gap-3">
          <a href="/reviews" class="inline-flex items-center justify-center rounded-full bg-amber-500 px-6 py-3 text-sm font-semibold text-stone-900 hover:bg-amber-400">Ver todas as análises</a>
          <a href="#ranking" class="inline-flex items-center justify-center rounded-full border border-stone-300 bg-white px-6 py-3 text-sm font-semibold text-stone-800 hover:bg-stone-50">O que eu usaria de novo</a>
        </div>
      </div>
    </section>

    <section class="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8 py-16">
      <h2 class="text-3xl font-bold tracking-tight text-stone-900">Um guia feito no chão da quitinete — não em teoria de manual</h2>
      <p class="mt-5 max-w-3xl text-lg leading-relaxed text-stone-600">Eu sou o Philipe. A Maraca chegou com 2 meses, patas grandes e energia de porte que a casa não tem. O que você lê aqui nasceu de acidente na área, sofá roído, 8 h fora e vizinho no corredor — não de script de Hotmart.</p>
      <p class="mt-4 max-w-3xl text-lg leading-relaxed text-stone-600">Cada ficha diz o que funcionou, o que foi gasto inútil e quando o próximo passo é produto, rotina ou curso. Comissão de afiliado não escreve o veredito.</p>
    </section>

    <section class="bg-white py-16">
      <div class="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl font-bold tracking-tight text-stone-900">Comparativo do que realmente segura móvel, xixi e limites</h2>
        <p class="mt-4 max-w-2xl text-stone-600">Três frentes. Confundir as três é comprar Kong esperando que o filhote aprenda sozinho onde urinar.</p>
        <div class="mt-10 grid gap-6 md:grid-cols-3">
          <article class="rounded-2xl border border-stone-200 p-6">
            <h3 class="font-semibold text-stone-900">Rotina</h3>
            <p class="mt-2 text-sm text-stone-600">Horário de quintal, “quatro patas”, portão, 8 h sozinha. Custa disciplina, não cartão.</p>
          </article>
          <article class="rounded-2xl border border-stone-200 p-6">
            <h3 class="font-semibold text-stone-900">Produto</h3>
            <p class="mt-2 text-sm text-stone-600">Kong, Herbalvet, portão, casinha. Acelera o que a rotina já apontou. Sem mapa, vira enfeite.</p>
          </article>
          <article class="rounded-2xl border border-stone-200 p-6">
            <h3 class="font-semibold text-stone-900">Curso</h3>
            <p class="mt-2 text-sm text-stone-600">Fecha o que o diário não cobre: progressão semana a semana e suporte quando o treino trava.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8 py-16">
      <h2 class="text-3xl font-bold tracking-tight text-stone-900">Como escolher método, produto e rotina para filhote de porte grande</h2>
      <p class="mt-5 max-w-3xl text-lg leading-relaxed text-stone-600">Pitbull filhote cresce rápido. O que cabe na boca aos 3 meses não cabe aos 7. Comece pelo problema do dia (xixi, boca, pulo, latido), leia a ficha de cuidado, só então abra a de produto. Ração e vacina não são “extra”: sem saúde o treino não pega.</p>
      <p class="mt-4 max-w-3xl text-lg leading-relaxed text-stone-600">Ética: sem grito, sem coleira de choque, sem “quebra de dominância”. Reforço do acerto e gestão do ambiente. A <a class="font-semibold underline" href="/metodologia">metodologia</a> explica o critério.</p>
    </section>

    <section id="ranking" class="bg-white py-16">
      <div class="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl font-bold tracking-tight text-stone-900">Ranking das soluções testadas com a Maraca em 2026</h2>
        <p class="mt-4 max-w-2xl text-stone-600">Seis pontos de partida. O hub tem o restante.</p>
        <div class="mt-10 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
{cards}
        </div>
      </div>
    </section>

    <section class="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8 py-16">
      <h2 class="text-3xl font-bold tracking-tight text-stone-900">Prós e contras de treinar um Pitbull em espaço pequeno</h2>
      <div class="mt-10 grid gap-8 md:grid-cols-2">
        <div class="rounded-2xl border border-emerald-100 bg-emerald-50/70 p-8">
          <h3 class="text-xl font-semibold text-emerald-900">Prós</h3>
          <ul class="mt-5 space-y-3 text-emerald-950">
            <li class="flex gap-3"><span class="mt-0.5 font-bold text-emerald-600">+</span> Você vê tudo: o xixi, a boca, o pulo</li>
            <li class="flex gap-3"><span class="mt-0.5 font-bold text-emerald-600">+</span> Toca, portão e relógio cabem em 30 m²</li>
            <li class="flex gap-3"><span class="mt-0.5 font-bold text-emerald-600">+</span> Enriquecimento caseiro (papelão, pano, Kong) rende mais que quintal vazio</li>
          </ul>
        </div>
        <div class="rounded-2xl border border-rose-100 bg-rose-50/70 p-8">
          <h3 class="text-xl font-semibold text-rose-900">Contras</h3>
          <ul class="mt-5 space-y-3 text-rose-950">
            <li class="flex gap-3"><span class="mt-0.5 font-bold text-rose-500">−</span> Energia de porte grande em sala única</li>
            <li class="flex gap-3"><span class="mt-0.5 font-bold text-rose-500">−</span> Latido e vizinho: margem de erro menor</li>
            <li class="flex gap-3"><span class="mt-0.5 font-bold text-rose-500">−</span> 8 h sozinha exige toca e item — não milagre</li>
          </ul>
        </div>
      </div>
    </section>

    <section id="faq" class="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8 py-16">
      <h2 class="text-3xl font-bold tracking-tight text-stone-900">Perguntas frequentes (xixi, Kong, vacina, 8 h sozinha, latido)</h2>
      <div class="mx-auto mt-10 max-w-3xl space-y-4">
{faq_blocks}
      </div>
    </section>

    <section class="bg-white py-16">
      <div class="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl font-bold tracking-tight text-stone-900">Outras análises que valem a sua atenção</h2>
        <ul class="mt-8 grid gap-3 sm:grid-cols-2 lg:grid-cols-3 text-stone-700">
          {mais_html}
        </ul>
      </div>
    </section>

    <section class="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8 py-16">
      <div class="rounded-3xl bg-amber-500 px-8 py-12 text-center sm:px-16">
        <h2 class="text-3xl font-bold tracking-tight text-amber-950">Todas as análises do Guia do Adestramento</h2>
        <p class="mx-auto mt-4 max-w-xl text-lg text-amber-950/80">Características da raça, cuidados do dia a dia e produtos testados com a Maraca.</p>
        <a href="/reviews" class="mt-8 inline-flex items-center justify-center rounded-full bg-stone-950 px-10 py-4 text-lg font-bold text-white hover:bg-black">Abrir o hub de reviews</a>
      </div>
    </section>
  </main>"""
    html = shell(
        "Adestramento de Pitbull filhote na prática: o que funciona em casa (2026) | Guia do Adestramento",
        "Diário da Maraca em Volta Redonda: xixi, mordedura, Kong, enzimático e limites em quitinete. Sem teoria de palco.",
        f"{BASE}/",
        graph,
        body,
        "/",
        "home",
    )
    write(PUBLIC / "index.html", html)


def main():
    build_home()
    build_articles()
    build_howtos()
    build_products()
    build_hub()
    build_institutional()
    build_sitemap()
    (ROOT / "vercel.json").write_text(
        '{\n  "outputDirectory": "public",\n  "cleanUrls": true\n}\n',
        encoding="utf-8",
    )
    print("updated vercel.json")


if __name__ == "__main__":
    main()
