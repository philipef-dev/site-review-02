# Relatório as-built — Guia do Adestramento (site 02)

Use este arquivo para analisar o site **como está no HTML publicado**, não o briefing de planejamento. Compare H1/H2 reais, schema e funil. Não invente páginas fora desta lista. O que não existe no HTML está marcado como **falta fazer**.

**Domínio:** `https://www.guiadoadestramento.com.br`  
**Data deste relatório:** 9 de outubro de 2026  
**Relatório anterior:** 11 de setembro de 2026 (substituído por este)  
**Padrão:** HTML estático + Tailwind v4 · URLs limpas (Vercel `cleanUrls`) · JSON-LD `@graph`  
**Intenção do dono:** o site é mais comercial do que informacional. O dinheiro vem de afiliado (Mercado Livre e Amazon) e do curso. Guias de cuidado continuam no ar, mas não lideram a home nem o hub.

**Fonte editorial:** `02/conteudo base.md` — diário da Maraca (Pitbull Red Nose filhote, quitinete em Volta Redonda).  
**Lista de ofertas:** `02/lista-de-produtos.md`  
**Funil desejado:** dica grátis → produto com link de loja → curso Hotmart.

**Não publicar:** motel, namoradas, maconha, meta-SEO de outro site. O projeto 01 (LavadorasPro) não entra neste relatório e não foi alterado.

---

## Feito agora — checkout do curso (9 out 2026, noite)

Página única: `/reviews/guia-completo-adestramento-canino`  
Arquivo: `public/reviews/guia-completo-adestramento-canino.html`  
Link de afiliado, informado pelo dono: `https://go.hotmart.com/H107966532E`

### O que saiu dessa ficha

- As duas ofertas falsas do schema (`seller` Amazon e Mercado Livre, `offers.url` apontando para a própria URL da review).
- Os botões visíveis de Mercado Livre e Amazon.

### O que está no HTML local agora

Um único botão de compra, no card do topo: **Comprar na Hotmart**.

- `href`: `https://go.hotmart.com/H107966532E`
- `rel`: `sponsored nofollow noopener noreferrer`
- `target`: `_blank`

Schema `Product` → `offers` (objeto único, não array):

| Campo | Valor |
|---|---|
| `seller.name` | `Hotmart` |
| `offers.url` | `https://go.hotmart.com/H107966532E` |
| `price` | `37.00` |
| `priceCurrency` | `BRL` |
| `priceValidUntil` | `2026-12-31` |
| `availability` | `InStock` |
| `itemCondition` | `NewCondition` |

H1 e H2 dessa ficha não mudaram. A linha de autoria diz “Atualizado em outubro de 2026”. No sitemap, o `lastmod` dessa URL é `2026-10-09`.

Conferido no navegador, no HTML local: o único link de compra da página é o da Hotmart, e o JSON-LD lido no DOM traz `price` `37.00`.

### O que já foi para o `main` e o que ainda não

- Commit `ceabcd7` (`fix: aponta o curso para o checkout da Hotmart`), já em `origin/main`: link, `seller` Hotmart, botão “Comprar na Hotmart” e `lastmod` do curso. Nesse commit o `price` ainda era `197.00`.
- Alteração **só local, ainda sem commit e sem push**: `price` de `197.00` para `37.00`.
- Enquanto esse arquivo não for publicado, `https://www.guiadoadestramento.com.br/reviews/guia-completo-adestramento-canino` continua servindo o preço `197.00`.

### O que esta alteração não fez

- O bloco “Quero o Guia Completo em Vídeo” saiu das fichas de produto. Não existe mais guia em vídeo. A ficha do curso na Hotmart continua no ar.
- A home, o hub e `lista-de-produtos.md` não receberam o link `H107966532E`.
- O projeto 01 não foi alterado.

---

## O que já está no ar

| Status | Qtde | O que é |
|---|---|---|
| HTML total | 35 | 8 institucionais (inclui home, hub e `/contato-obrigado`) + 27 fichas em `/reviews/` |
| No sitemap | 34 | `/contato-obrigado` fica de fora (noindex) |
| Home | 1 | Quadro comparativo de 12 produtos logo após o hero |
| Hub `/reviews` | 1 | Seção **Produtos testados** é a primeira |
| Características | 4 | Sem mudança de H1/H2 desde 11/09 |
| Cuidados | 8 | Assinatura de ração saiu deste bloco e foi para produtos |
| Produtos / ofertas | 15 | 11 do mapa de setembro + Kong Classic + Kong Extreme + Nylabone + Assinatura |

Infra: `02/vercel.json` com `outputDirectory: public` e `cleanUrls: true`.

---

## O que entrou depois de 11 de setembro

### Páginas novas (já no sitemap)

| URL | lastmod no sitemap | Papel |
|---|---|---|
| `/reviews/kong-classic` | 2026-10-09 | Produto. Borracha vermelha, transição pós-filhote |
| `/reviews/kong-extreme` | 2026-10-09 | Produto. Borracha preta, mordida destrutiva |
| `/reviews/nylabone-puppy-chew-toy` | 2026-10-02 | Produto. Nylon no rodízio; não substitui o Kong |
| `/reviews/assinatura-racao-filhote` | 2026-09-17 | Oferta recorrente Petz, Cobasi e Amazon. Não é anúncio único de ML/Amazon |

### Home `/` — quadro comercial

- Novo H2, **primeiro da página**, logo abaixo do hero: **Quadro comparativo dos produtos testados com a Maraca em 2026**.
- Subtítulo: “Compare uso e o que conferir na compra. Clique no produto para ler o review.”
- Botão do hero: **Ver quadro comparativo** (`#comparativo`).
- Colunas: Produto · Uso · Conferir · Destaque · Mercado Livre · Amazon.
- Coluna do produto fica fixa no celular; a tabela rola na horizontal.
- 12 linhas, nesta ordem: Kong Puppy · Kong Extreme · Kong Classic · Herbalvet T.A. · Portão pet de pressão · Casinha Furacão Pet nº 5 · Premier Filhotes raças grandes · Comedouro lento Pet Games · Guia e peitoral · Nylabone Puppy · Pipi Pode / Educa Cão · Clicker com pulseira.
- Links de loja são os mesmos das fichas (`meli.la` e `link.amazon`). Não há coluna de preço.
- O comparativo de três cartões (Rotina · Produto · Curso) **continua** mais abaixo. Não é a tabela.
- Ranking visual da home passou a ter Kong Extreme em 2º. ItemList da home também: posição 2 agora é `/reviews/kong-extreme` (antes era xixi). São 7 itens, mistura de produto e guia.

### Hub `/reviews` — produtos na frente

- H1 continua **Minhas Avaliações**.
- Texto de abertura: “Produtos que eu testei com a Maraca e compraria de novo. Mais abaixo, o diário de cuidados e da raça.”
- Ordem visível dos H2:
  1. Produtos testados (reviews) — 15 cards
  2. Características da raça e da fase — 4 cards
  3. Cuidados e adestramento no dia a dia — 8 cards
- **Assinatura de ração** saiu de Cuidados e entrou em Produtos, ao lado de Ração porte grande.
- Meta description do hub passou a abrir pelos produtos.

### Fichas cujo H1/H2 mudou em relação ao relatório de 11/09

- `/reviews/guia-e-peitoral-filhote` — H1 novo: foco em 4 a 6 meses, fita larga, modelo H. O H1 antigo (“filhote de 3 meses”) não vale mais.
- `/reviews/racao-filhotes-porte-grande` — veredito novo: Minis só na emergência; saco fechado de porte grande.
- `/reviews/portao-pet-de-pressao` — último H2 de corpo agora é “Grade, extensor e vão mais largo que o portão” (não fala mais do muro de 1,70 m nesse H2).
- Nas fichas de produto geradas em setembro, **Ficha técnica virou H2** (antes o relatório anotava H3). Vale para Classic vs Puppy, Herbalvet não (essa ficha antiga segue o padrão próprio), Pipi Pode, casinha, portão, guia, ração, comedouro e curso.

---

## Inventário atual

| Pilar | Páginas | Schema principal |
|---|---|---|
| Home | 1 | `WebPage` + `ItemList` (7 URLs reais) + `FAQPage`. O quadro de 12 **não** está no ItemList |
| Hub | 1 | `ItemList` com `numberOfItems: 27` |
| Características | 4 | `Article` + `FAQPage` |
| Cuidados | 8 | `HowTo` + `FAQPage` |
| Produtos e ofertas | 15 | `Product` + `FAQPage` (assinatura é oferta recorrente, não um SKU de loja) |
| Institucional | 6 | `AboutPage`, metodologia `WebPage`, `ContactPage`, `WebPage` noindex, `PrivacyPolicy`, `TermsOfService` |

ItemList da **home** (ordem real):

1. `/reviews/kong-puppy`
2. `/reviews/kong-extreme`
3. `/reviews/xixi-e-coco-no-lugar-certo`
4. `/reviews/filhote-mordendo-tudo`
5. `/reviews/herbalvet-eliminador-enzimatico`
6. `/reviews/limites-cao-em-quitinete`
7. `/reviews/guia-completo-adestramento-canino`

ItemList do **hub** tem as 27 fichas, mas a ordem do JSON-LD ainda começa por características. A ordem **visível** começa por produtos. Quantidade bate; a ordem não.

---

## Home — `/` — estado em 9/10

**Arquivo:** `public/index.html`  
**H1:** Adestramento de Pitbull filhote na prática: o que funciona em casa (2026)

**H2, nesta ordem**

1. Quadro comparativo dos produtos testados com a Maraca em 2026
2. Um guia feito no chão da quitinete — não em teoria de manual
3. Comparativo do que realmente segura móvel, xixi e limites
4. Como escolher método, produto e rotina para filhote de porte grande
5. Ranking das soluções testadas com a Maraca em 2026
6. Prós e contras de treinar um Pitbull em espaço pequeno
7. Perguntas frequentes (xixi, Kong, vacina, 8 h sozinha, latido)
8. Outras análises que valem a sua atenção
9. Todas as análises do Guia do Adestramento

**H3 do ranking (7 cards, não são os 12 do quadro)**

1. Kong Puppy
2. Kong Extreme
3. Xixi e cocô no lugar certo
4. Filhote mordendo tudo
5. Herbalvet T.A.
6. Limites na quitinete
7. Guia Completo de Adestramento

**H3 do comparativo de três frentes (não é a tabela):** Rotina · Produto · Curso · e mais abaixo Prós · Contras.

**Schema:** Organization, WebSite, WebPage, ItemList (7), FAQPage. Sem `Product` na home.

---

## Hub — `/reviews` — estado em 9/10

**Arquivo:** `public/reviews.html`  
**H1:** Minhas Avaliações

**H2**

1. Produtos testados (reviews)
2. Características da raça e da fase
3. Cuidados e adestramento no dia a dia

**H3 — produtos (15)**

Kong Puppy · Kong Classic · Kong Extreme · Kong Classic vs Puppy · Herbalvet T.A. · Pipi Pode / Educa Cão · Casinha plástica nº 5 · Portão de pressão · Guia e peitoral · Ração porte grande · Assinatura de ração · Comedouro lento · Guia Completo · Clicker · Nylabone Puppy

**H3 — características (4)**

Pitbull filhote de 2 meses · Temperamento · Crescimento e castração · Pitbull e outros cães

**H3 — cuidados (8)**

Xixi e cocô no lugar certo · Filhote mordendo tudo · Pular nas pessoas · Limites na quitinete · Alimentação · Vacinas e vermífugo · Socialização · Enriquecimento

O card do Clicker ainda diz “Ficha extra já no ar.”

---

## Por que o quadro tem 12 e o hub tem 15

Os 12 do quadro são produtos com botão de Mercado Livre **e** Amazon na própria linha. Os 3 que estão só no hub:

| Ficha | Por que não entrou no quadro |
|---|---|
| Kong Classic vs Puppy | Compara dois Kongs que já têm linha própria |
| Assinatura de ração | CTAs são Petz, Cobasi e Amazon Assine, não um anúncio |
| Guia Completo | Curso na Hotmart (`https://go.hotmart.com/H107966532E`). Não é anúncio de ML/Amazon |

Rótulos diferentes para o mesmo produto: “Premier Filhotes raças grandes” (quadro) = “Ração porte grande” (hub). O mesmo acontece com casinha, portão, comedouro e clicker.

---

## Páginas novas ou reescritas — H1/H2 atuais

### `/reviews/kong-classic` — NOVA

**H1:** Kong Classic vale a pena? Avaliação do brinquedo Kong vermelho para cães adultos

**H2**

1. O que torna o Kong Classic vermelho o padrão para cão adulto de mordida moderada?
2. Medium, Large ou XL: qual tamanho escolher por peso e abertura de mandíbula?
3. Rosa, vermelho, preto e roxo: onde o Classic entra na linha KONG?
4. Ração seca, patê e freezer: como rechear o vermelho
5. Perguntas frequentes sobre o Kong Classic vermelho (FAQ)

**H3:** Medium · Large · XL · Ficha técnica · Mordida moderada · Mordida que abre o vermelho · tabela vs Puppy vs Extreme · petisqueira · curso

### `/reviews/kong-extreme` — NOVA

**H1:** Kong Extreme vale a pena? Avaliação do brinquedo Kong preto para mordida forte

**H2**

1. O que torna o Kong Extreme preto a escolha para mordida destrutiva?
2. Kong Extreme Large, XL ou XXL: qual tamanho para cão adulto de porte grande?
3. Rosa, vermelho, preto e roxo: qual linha do Kong comprar?
4. Kong Extreme vs Kong Classic vs Nylabone Durável: qual aguenta o morde-morde?
5. Como rechear o Kong Extreme sem somar lanche em cima da tigela
6. Perguntas frequentes sobre o Kong Extreme preto (FAQ)

### `/reviews/nylabone-puppy-chew-toy` — NOVA

**H1:** Nylabone Puppy vale a pena? Mordedor de nylon para filhote de Pitbull

**H2**

1. O que é o Nylabone Puppy Chew Toy e por que ele existe?
2. Nylabone Puppy ou Kong Puppy: qual escolher primeiro?
3. Como o nylon se desgasta — e quando trocar
4. Qual Nylabone comprar para Pitbull filhote?
5. Nylabone com supervisão: a regra que não tem exceção
6. Nylabone vs Benebone: qual nylon para filhote?
7. Perguntas frequentes sobre o Nylabone Puppy (FAQ)

**H3:** Ficha técnica · Troca de dentes · Sozinho em casa · tabela vs Kong Puppy · curso

### `/reviews/assinatura-racao-filhote` — NOVA

**H1:** Vale a Pena Fazer Assinatura de Ração Online? Como Nunca Deixar Faltar Comida pro Filhote (e Evitar Diarreia)

**H2**

1. Ficha rápida — assinatura de ração
2. Veredito: sim — se a marca some no bairro e o filhote come de verdade
3. O perrengue de ficar sem ração (e por que isso não é “só um detalhe”)
4. Fome, má absorção e coprofagia: quando a tigela vazia vira comportamento
5. A solução: assinatura de ração recorrente (compra programada)
6. Como criar a primeira assinatura online em 3 passos
7. Perguntas frequentes (FAQ)
8. Conclusão: saúde de filhote é consistência — não heroísmo de última hora
9. Ative a assinatura agora

**CTAs reais:** Petz Compra Programada, Cobasi Assinatura, Amazon Programe e Poupe. Sem botão único de Mercado Livre.

### `/reviews/guia-e-peitoral-filhote` — H1/H2 REESCRITOS

**H1:** Guia e peitoral para Pitbull filhote de 4 a 6 meses: fita larga, não a baratinha

**H2**

1. Ficha técnica – peitoral modelo H + guia reforçada
2. Veredito: fita 25–30 mm e modelo H agora; fita fina, nunca
3. Guia lisa 1,5 a 2 m: fita 25–30 mm e mosquetão de aço com trava
4. Por que guia retrátil é péssima para treino (e perigosa no Pitbull)
5. Peitoral modelo H reforçado vs coleira fina no Pitbull de 4 a 6 meses
6. Passeio só depois da V10: o que a guia faz em casa até lá
7. Perguntas frequentes (FAQ)

### `/reviews/racao-filhotes-porte-grande` — VEREDITO REESCRITO

**H1:** Melhor ração para filhote de Pitbull: NutriSano, Golden ou Premier?

**H2**

1. Ficha técnica
2. Veredito: Minis só na emergência; porte grande em saco fechado
3. Por que Dog Chow Minis é emergência de balcão — e falha no Pitbull filhote
4. NutriSano, Multidog, Golden Filhotes/Mega e Premier Fórmula
5. Saco de 3 kg vs 10–15 kg: preço, oxigênio e o papo do balcão
6. Quantidade em colheres e o cocô como medidor
7. Perguntas frequentes (FAQ)

### `/reviews/portao-pet-de-pressao` — UM H2 MUDOU

**H1:** Portão pet de pressão vale a pena em apartamento pequeno?

**H2**

1. Ficha técnica
2. Veredito: sim, se a casa não tem porta no vão
3. Como impedir a passagem da sala para a cozinha sem porta
4. Altura, força do filhote e o que muda no adulto
5. Ferro de pressão vs papelão e móvel improvisado
6. Grade, extensor e vão mais largo que o portão
7. Perguntas frequentes (FAQ)

### `/reviews/guia-completo-adestramento-canino` — CHECKOUT HOTMART

**H1:** Guia Completo de Adestramento Canino 2026: vale a pena?

**H2**

1. Ficha técnica
2. Veredito: vale se você quer o método amarrado, não um frasco a mais
3. O programa fecha o que o diário da Maraca não cobre sozinho?
4. Xixi, limites e mordedura: o que é método e o que é produto
5. Garantia, suporte e o que não é milagre em 7 dias
6. Curso vs Kong + enzimático vs aula particular
7. Perguntas frequentes (FAQ)

**Schema `offers`:** uma oferta, `seller` Hotmart, `url` `https://go.hotmart.com/H107966532E`, `price` `37.00`, `priceCurrency` `BRL`. O botão visível “Comprar na Hotmart” usa o mesmo link. O preço `37.00` está no arquivo local e ainda não foi publicado; o `main` publicado ainda tem `197.00`.

---

## Páginas sem mudança de H1/H2 desde 11/09

Conferidas de novo em 9/10. O outline do relatório antigo continua válido:

- Características: `pitbull-filhote-2-meses`, `temperamento-pitbull-filhote`, `crescimento-peso-e-castracao`, `pitbull-e-outros-caes`
- Cuidados: `xixi-e-coco-no-lugar-certo`, `filhote-mordendo-tudo`, `filhote-pulando-nas-pessoas`, `limites-cao-em-quitinete`, `alimentacao-filhote-porte-grande`, `vacinas-v8-v10-e-vermifugo`, `socializacao-filhote-com-outros-caes`, `enriquecimento-ambiental-filhote`
- Produtos antigos: `kong-puppy`, `kong-classic-vs-puppy` (só a posição da Ficha técnica, que agora é H2), `herbalvet-eliminador-enzimatico`, `pipi-pode-educa-cao`, `casinha-plastico-furacao-pet`, `comedouro-lento`, `clicker-para-adestramento-vale-a-pena`
- Institucionais: `quem-somos`, `metodologia`, `contato`, `contato-obrigado`, `politica-de-privacidade`, `termos-e-condicoes`

---

## Falta fazer

Itens abaixo **não estão resolvidos no HTML**. Proposta do Gemini deve dizer o que muda em página que já existe e o que seria página nova.

### Comercial — alinhar o que vende

1. Decidir o quadro da home: manter 12 (só SKU com ML + Amazon) ou chegar nos 15 do hub. Se entrar curso e assinatura, o CTA não pode ser o botão azul/âmbar de loja.
2. Decidir se o ranking de 7 cards e o ItemList de 7 URLs continuam misturando guia e produto, ou se passam a espelhar o quadro.
3. Unificar rótulos entre quadro e hub (Premier vs “Ração porte grande”, etc.).
4. Publicar o `price` `37.00` (está só no HTML local; o `main` ainda tem `197.00`). O CTA “Quero o Guia Completo em Vídeo” foi removido das fichas; não haverá guia em vídeo.
5. Reordenar o ItemList do hub para a ordem visível (produtos primeiro) ou marcar a lista como não ordenada de propósito. Hoje `numberOfItems` é 27 e a ordem do JSON ainda é a de setembro.
6. Atualizar `lastmod` de `/` e `/reviews` no sitemap. Os dois estão em 2026-10-02; o quadro e a reordem do hub são de 2026-10-09. Várias fichas reescritas (guia, ração, portão) ainda têm lastmod 2026-09-11.
7. Trocar o texto do card do Clicker no hub (“Ficha extra já no ar.”).

### Ofertas da lista que não têm ficha

Em `lista-de-produtos.md`, bloco P2. Existem só como CTA dentro de outras páginas. **Proposta, não existe como URL própria:**

- Petisqueira de adestramento (`meli.la/1J9vYQw`, `link.amazon/B088aQW3G`) — citada em Kong e Clicker
- Tapete Durapads (`meli.la/2Sqp9LE`, `link.amazon/B03swudgY`) — citado em Pipi Pode e Herbalvet

### Análise que o relatório de setembro pediu e o HTML ainda não fechou

1. Canibalização: xixi vs Pipi Pode vs Herbalvet; quatro páginas de Kong (Puppy, Classic, Extreme, Classic vs Puppy) mais Nylabone; alimentação vs ração vs assinatura.
2. Funil dica grátis → produto → curso: o quadro e o hub agora abrem pelo produto. O curso continua sem link de compra. Dizer se o H2 do funil está explícito ou só no corpo.
3. E-E-A-T / YMYL (vacina, castração, ração, assinatura, vermífugo): o tom de diário basta ou falta disclaimer de veterinário mais visível no H1/H2?
4. Clicker: manter ficha própria no bloco comercial ou só como apoio do curso e da petisqueira.

Não sugerir página nova sem marcar **proposta, não existe no HTML**.
