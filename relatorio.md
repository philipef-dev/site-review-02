# Relatório para o Gemini — páginas do site + links de afiliado

Use este arquivo como briefing fechado. **Não invente páginas.** Trabalhe só com o inventário abaixo.

**Site:** Guia do Adestramento  
**Domínio:** `https://www.guiadoadestramento.com.br`  
**Data:** 22 de setembro de 2026  
**Total HTML no ar:** 32 páginas  
**Funil editorial:** dica grátis (papelão, pano congelado) → produto físico (Kong, Herbalvet, ração) → curso Hotmart

**Projeto:** HTML estático em `public/`. Em produção a Vercel usa `cleanUrls` (URLs sem `.html`).

---

## O que eu preciso que você faça

Gere **links de afiliado reais** (Amazon Associados BR, Mercado Livre Afiliados, Petz, Cobasi e Hotmart) para cada produto da lista.

Hoje os botões do site apontam para **busca genérica** (`amazon.com.br/s?k=...` e `lista.mercadolivre.com.br/...`) **sem tag de afiliado**. Na ficha de assinatura os `href` ainda são placeholder (`#INSERIR-LINK-DE-AFILIADO-AQUI-...`).

### Regras

1. Prefira **página de produto específica** (ASIN na Amazon / item ID no ML), não busca.
2. Se o SKU sumiu, devolva o **ASIN/item mais próximo** da mesma linha (tamanho, volume, fórmula filhotes).
3. Devolva **Amazon e Mercado Livre** para cada item físico, salvo quando o produto só existe em um marketplace.
4. Assinatura de ração: **Petz Compra Programada**, **Cobasi Assinatura** e **Amazon Assine e Economize**.
5. Curso: **link de afiliado Hotmart** (hoje o CTA aponta para a própria ficha).
6. Não gere link para o que o site **desaconselha** (Dog Chow Minis a granel, guia retrátil, casinha de madeira, Veja/Lysoform no xixi, Kong Senior roxo, Kong Extreme para filhote, clicker como “obrigatório”).
7. Vermífugo (Drontal, Chemital) é YMYL: só liste se o programa de afiliados permitir; senão marque “não afiliar”.
8. Não invente preço. Se achar preço, marque como “cotação do dia, conferir”.

### Formato de resposta (obrigatório)

Para cada produto, uma tabela:

| Campo | Valor |
|---|---|
| Produto | nome comercial + variante |
| Prioridade | P1 / P2 / P3 |
| Página do site | URL canônica |
| Query de busca atual (Amazon) | URL que está no HTML hoje |
| Query de busca atual (ML) | URL que está no HTML hoje |
| Amazon — URL afiliado | `https://www.amazon.com.br/...tag=SEU-TAG` |
| Amazon — ASIN | |
| Mercado Livre — URL afiliado | |
| Mercado Livre — item ID | |
| Outro canal | Petz / Cobasi / Hotmart se couber |
| Observação | tamanho, volume, “não recomendado para filhote”, etc. |

No final: lista colável `produto → amazon | mercadolivre` para eu substituir os `href` no HTML.

---

## Inventário de páginas (32)

Base: `https://www.guiadoadestramento.com.br`

### Institucionais e hub (8)

| # | URL | Arquivo | H1 | Precisa de afiliado? |
|---|---|---|---|---|
| 1 | `/` | `public/index.html` | Adestramento de Pitbull filhote na prática: o que funciona em casa (2026) | Não (aponta para fichas) |
| 2 | `/reviews` | `public/reviews.html` | Minhas Avaliações | Não |
| 3 | `/quem-somos` | `public/quem-somos.html` | Sobre o projeto “Guia do Adestramento” | Não |
| 4 | `/metodologia` | `public/metodologia.html` | Guia do Adestramento — nossa metodologia de análise | Não |
| 5 | `/contato` | `public/contato.html` | Guia do Adestramento — fale comigo | Não |
| 6 | `/contato-obrigado` | `public/contato-obrigado.html` | Mensagem recebida | Não (`noindex`) |
| 7 | `/politica-de-privacidade` | `public/politica-de-privacidade.html` | Política de Privacidade \| Guia do Adestramento | Não |
| 8 | `/termos-e-condicoes` | `public/termos-e-condicoes.html` | Termos e Condições \| Guia do Adestramento | Não |

### Características — Article (4)

| # | URL | H1 |
|---|---|---|
| 9 | `/reviews/pitbull-filhote-2-meses` | Características de um Pitbull filhote de 2 meses |
| 10 | `/reviews/temperamento-pitbull-filhote` | Temperamento do Pitbull filhote: energia, boca e latido |
| 11 | `/reviews/crescimento-peso-e-castracao` | Crescimento do Pitbull: peso, porte adulto e quando castrar |
| 12 | `/reviews/pitbull-e-outros-caes` | Pitbull filhote e outros cães: como apresentar sem atropelo |

Sem CTA de compra. Afiliado entra só se o Gemini sugerir um bloco discreto apontando para fichas já existentes (Kong, ração) — **não criar produto novo**.

### Cuidados — HowTo (9)

| # | URL | H1 | Produtos citados no texto |
|---|---|---|---|
| 13 | `/reviews/xixi-e-coco-no-lugar-certo` | Como ensinar o filhote a fazer xixi e cocô no lugar certo | Herbalvet, Pipi Pode |
| 14 | `/reviews/filhote-mordendo-tudo` | Como fazer o filhote parar de morder móveis, pés e sofá | Kong Puppy |
| 15 | `/reviews/filhote-pulando-nas-pessoas` | Como ensinar o filhote a não pular nas pessoas | — (petisco / método) |
| 16 | `/reviews/limites-cao-em-quitinete` | Como criar um Pitbull em quitinete sem ele invadir quarto e cozinha | Portão pet de pressão |
| 17 | `/reviews/alimentacao-filhote-porte-grande` | Quanto de ração dar para filhote de Pitbull (e quando o cocô mole denuncia erro) | NutriSano, Golden, Premier |
| 18 | `/reviews/assinatura-racao-filhote` | Vale a Pena Fazer Assinatura de Ração Online? … | Petz, Cobasi, Amazon Recorrente **(placeholders)** |
| 19 | `/reviews/vacinas-v8-v10-e-vermifugo` | Vacina V8, V10 e vermífugo no filhote: ordem, intervalo e o que esperar | Drontal, Chemital (YMYL) |
| 20 | `/reviews/socializacao-filhote-com-outros-caes` | Como socializar Pitbull filhote com um cão medroso (e com visitas) | Petisco |
| 21 | `/reviews/enriquecimento-ambiental-filhote` | Enriquecimento ambiental para filhote: papelão, pano congelado e rodízio | Kong Puppy |

### Produtos — Product (11)

| # | URL | H1 | CTA hoje |
|---|---|---|---|
| 22 | `/reviews/kong-puppy` | Kong Puppy vale a pena? Avaliação do brinquedo Kong para filhote de Pitbull | Busca Amazon + ML |
| 23 | `/reviews/kong-classic-vs-puppy` | Kong Classic ou Puppy: qual comprar em 2026? | Busca Amazon + ML |
| 24 | `/reviews/herbalvet-eliminador-enzimatico` | Desinfetante Herbalvet T.A. vale a pena? … | Busca Amazon + ML |
| 25 | `/reviews/pipi-pode-educa-cao` | Pipi Pode / Educa Cão funciona sozinho? | Busca Amazon + ML |
| 26 | `/reviews/casinha-plastico-furacao-pet` | Casinha de plástico nº 5 vale a pena para Pitbull filhote? | Busca Amazon + ML |
| 27 | `/reviews/portao-pet-de-pressao` | Portão pet de pressão vale a pena em apartamento pequeno? | Busca Amazon + ML |
| 28 | `/reviews/guia-e-peitoral-filhote` | Guia e peitoral para filhote de 3 meses: o que comprar | Busca Amazon + ML |
| 29 | `/reviews/racao-filhotes-porte-grande` | Melhor ração para filhote de Pitbull: NutriSano, Golden ou Premier? | Busca Amazon + ML |
| 30 | `/reviews/comedouro-lento` | Comedouro lento vale a pena para filhote que engole ração? | Busca Amazon + ML |
| 31 | `/reviews/guia-completo-adestramento-canino` | Guia Completo de Adestramento Canino 2026: vale a pena? | Aponta para a própria URL (falta Hotmart) |
| 32 | `/reviews/clicker-para-adestramento-vale-a-pena` | Clicker para Cachorro: Clicker Adestramento Vale a Pena? 2026 | Busca Amazon + ML |

---

## Produtos que precisam de link de afiliado

### P1 — CTAs principais (trocar busca genérica por produto + tag)

Estes botões já existem no HTML. Prioridade máxima.

| ID | Produto | Marca / variante a achar | Página | Amazon hoje | Mercado Livre hoje |
|---|---|---|---|---|---|
| P1-01 | **Kong Puppy** | KONG Puppy rosa/azul, **Medium** (mínimo para Pitbull filhote); também **Large**. Evitar Small (risco de engolir) e Senior roxo | `/reviews/kong-puppy` | `https://www.amazon.com.br/s?k=kong+puppy+medium` | `https://lista.mercadolivre.com.br/kong-puppy` |
| P1-02 | **Kong Classic** | KONG Classic **vermelho**, tamanho **M ou G**. Não Extreme preto para filhote | `/reviews/kong-classic-vs-puppy` | `https://www.amazon.com.br/s?k=kong+classic` | `https://lista.mercadolivre.com.br/kong-classic` |
| P1-03 | **Herbalvet T.A.** | Ourofino, preferir **1000 ml**; também 500 ml | `/reviews/herbalvet-eliminador-enzimatico` | `https://www.amazon.com.br/s?k=herbalvet+t.a+ourofino+1000ml` | `https://lista.mercadolivre.com.br/herbalvet-t.a-ourofino` |
| P1-04 | **Pipi Pode / Educa Cão** | Atrativo sanitário Educa Cão (Pipi Pode). Kit Pipi Pode + Pipi Não Pode se existir | `/reviews/pipi-pode-educa-cao` | `https://www.amazon.com.br/s?k=pipi+pode+educa+cao` | `https://lista.mercadolivre.com.br/pipi-pode-caes` |
| P1-05 | **Casinha plástica nº 5** | Furacão Pet ou Tánatela **2 em 1**, número **5** (não nº 4; não madeira) | `/reviews/casinha-plastico-furacao-pet` | `https://www.amazon.com.br/s?k=casinha+plastico+cachorro+n5` | `https://lista.mercadolivre.com.br/casinha-cachorro-plastico-numero-5` |
| P1-06 | **Portão pet de pressão** | Grade de ferro de pressão (não retrátil de tecido). Altura que um Pitbull adulto não transponha | `/reviews/portao-pet-de-pressao` | `https://www.amazon.com.br/s?k=portao+pet+pressao` | `https://lista.mercadolivre.com.br/portao-pet-pressao` |
| P1-07 | **Guia + peitoral filhote** | Guia de **nylon lisa 1,5 a 2 m** + peitoral ajustável. **Não** guia retrátil | `/reviews/guia-e-peitoral-filhote` | `https://www.amazon.com.br/s?k=guia+nylon+cachorro+2m+peitoral` | `https://lista.mercadolivre.com.br/guia-nylon-cachorro-2-metros` |
| P1-08 | **Ração filhotes porte grande** | Ordem de preferência: **Golden Filhotes raças grandes / Golden Mega filhotes**, **Premier Fórmula filhotes raças grandes**, **NutriSano filhotes**, **GranPlus** / Multidog se a linha for porte grande. Saco **3 kg** (teste) e **15 kg** (preço). **Não** Dog Chow Minis | `/reviews/racao-filhotes-porte-grande` | `https://www.amazon.com.br/s?k=racao+golden+filhotes+porte+grande` | `https://lista.mercadolivre.com.br/racao-golden-filhotes-racas-grandes` |
| P1-09 | **Comedouro lento** | Priorizar **Labirinto Pet Games** ou **Colmeia Buddy** (furo estreito). Alternativa: Stark Pet. Evitar bola com boca larga | `/reviews/comedouro-lento` | `https://www.amazon.com.br/s?k=comedouro+lento+cachorro` | `https://lista.mercadolivre.com.br/comedouro-lento-caes` |
| P1-10 | **Clicker com pulseira** | Clicker de adestramento com pulseira. Veredito do site: **opcional** (estalo de dedos resolve). Mesmo assim precisa de link porque a ficha rankeia | `/reviews/clicker-para-adestramento-vale-a-pena` | `https://www.amazon.com.br/s?k=clicker+adestramento+cães+pulseira` | `https://lista.mercadolivre.com.br/clicker-adestramento-caes` |
| P1-11 | **Assinatura de ração — Petz** | Compra Programada Petz, ração filhotes porte grande | `/reviews/assinatura-racao-filhote` | *placeholder* `#INSERIR-LINK-DE-AFILIADO-AQUI-PETZ` | — |
| P1-12 | **Assinatura de ração — Cobasi** | Assinatura Cobasi | `/reviews/assinatura-racao-filhote` | *placeholder* `#INSERIR-LINK-DE-AFILIADO-AQUI-COBASI` | — |
| P1-13 | **Assinatura de ração — Amazon Recorrente** | Assine e Economize / entrega recorrente da mesma ração P1-08 | `/reviews/assinatura-racao-filhote` | *placeholder* `#INSERIR-LINK-DE-AFILIADO-AQUI-AMAZON` | — |
| P1-14 | **Guia Completo de Adestramento Canino** | Curso digital, checkout **Hotmart** (não Amazon/ML). CTA atual aponta para a própria ficha | `/reviews/guia-completo-adestramento-canino` | — | — |

**Hotmart:** devolver URL de afiliado do produto “Guia Completo de Adestramento Canino” (ou o nome comercial exato se o anúncio usar outro título). Se não achar o produto público, marcar “checkout ainda não publicado — não inventar URL”.

---

### P2 — já têm botão em fichas, mas são produtos secundários

Trocar busca genérica por SKU + tag. Aparecem em CTAs internos das fichas P1.

| ID | Produto | Onde aparece | Busca atual |
|---|---|---|---|
| P2-01 | **Nylabone Puppy** | `/reviews/kong-puppy` (alternativa de nylon; não substitui o Kong recheável) | Amazon `nylabone+puppy` |
| P2-02 | **Petisqueira de adestramento** | `/reviews/kong-puppy` e `/reviews/clicker-para-adestramento-vale-a-pena` | ML `petisqueira-adestramento` · Amazon `petisqueira+adestramento` |
| P2-03 | **Tapete higiênico Durapads** | `/reviews/herbalvet-eliminador-enzimatico` (apoio no treino, não banheiro eterno) | Amazon `tapete+higienico+durapads` |
| P2-04 | **Pipi Pode** (CTA cruzado na ficha Herbalvet) | `/reviews/herbalvet-eliminador-enzimatico` | ML `pipi-pode-educa-cao` |
| P2-05 | **Kong Classic** (CTA cruzado na ficha Puppy) | `/reviews/kong-puppy` | Amazon `kong+classic` — pode reutilizar P1-02 |

---

### P3 — citados no copy, sem CTA próprio (gerar link só se houver SKU claro)

| ID | Produto | Papel no site | Afiliar? |
|---|---|---|---|
| P3-01 | Odontopet Dura Lagosta / Spinner | Alternativa nacional ao Kong | Sim, se achar SKU |
| P3-02 | Benebone | Alternativa nylon | Sim |
| P3-03 | Kit Pipi Pode + Pipi Não Pode | Mencionado na ficha Pipi Pode | Sim, se o kit existir |
| P3-04 | Enzymac, Sanol Pipi Safe, Vanish Enzimático | Concorrentes do Herbalvet | Só se quiser comparativo; **Herbalvet é o escolhido** |
| P3-05 | GranPlus filhotes porte grande | Ração alternativa | Sim |
| P3-06 | Multidog filhotes | Alternativa à NutriSano | Sim, se for linha de porte grande |
| P3-07 | Mini Fit Pet Games | Comedouro | Sim, se SKU distinto do labirinto |
| P3-08 | Stark Pet comedouro lento | Faixa de preço menor | Sim |
| P3-09 | Kong Extreme preto | Só adulto que já destruiu o Classic | **Não** como CTA de filhote |
| P3-10 | Drontal Pup / Chemital | Vermífugo na ficha de vacinas | Só se política de afiliados permitir medicamentos pet |

---

## O que **não** afiliar (contraponto editorial)

| Item | Motivo no site |
|---|---|
| Dog Chow Minis / Pequenos e ração a granel | Fórmula errada para Pitbull em crescimento |
| Guia retrátil | Ensina a puxar; péssima para treino |
| Casinha de madeira | Pulga, calor, quitinete |
| Veja, Lysoform, cloro no xixi | Não quebram ureia; risco nas patas |
| Kong Puppy Small | Risco de engolir em porte grande |
| Kong Senior (roxo) | Fora da fila da Maraca |
| Kong Extreme para filhote | Excesso; gengiva de leite pede Puppy |
| Clicker como item “obrigatório” | Site recomenda estalo de dedos; o link existe só porque a ficha captura busca |

---

## Estado atual dos links (resumo técnico)

- **Nenhum `href` de Amazon tem `tag=` de Associados.**
- **Nenhum `href` de Mercado Livre tem tracking de afiliado.**
- JSON-LD `offers.url` nas fichas Product copia as mesmas buscas genéricas (exceto o curso, que aponta para a própria URL).
- Ficha `/reviews/assinatura-racao-filhote`: 5 blocos de CTA com `href="#INSERIR-LINK-DE-AFILIADO-AQUI-PETZ|COBASI|AMAZON"` e o texto visível `[INSERIR LINK DE AFILIADO AQUI]`.
- Ficha `/reviews/guia-completo-adestramento-canino`: botões “Ver no Mercado Livre” e “Ver na Amazon” estão **errados** (curso digital). Trocar por **um** botão Hotmart.

Quando devolver os links, indique também **quais `href` substituir** (arquivo + URL antiga → URL nova), para eu colar no HTML sem ambiguidade.

---

## Prompt curto para colar acima deste arquivo

> Você é meu assistente de afiliados para o site guiadoadestramento.com.br. Leia o relatório abaixo. Para cada produto P1 e P2, encontre o anúncio real na Amazon.com.br e no Mercado Livre, gere o link de afiliado (eu te passo a tag/ID se faltar) e devolva no formato de tabela pedido. Não invente páginas do site. Não recomende produtos da lista “não afiliar”. Para P1-11 a P1-13 use Petz, Cobasi e Amazon Recorrente. Para P1-14 use Hotmart.
