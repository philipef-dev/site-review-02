# Relatório as-built — Guia do Adestramento (site 02)

Use este arquivo para analisar o site **como está no HTML local**, cruzando com `PLANEJAMENTO_SEO_KEYWORD_IDEAS.md`. Não invente página, URL, H1 ou produto fora das duas listas. O que não existe no HTML está marcado como **não existe no HTML**. Proposta de página nova tem de repetir essa marca.

**Domínio:** `https://www.guiadoadestramento.com.br`  
**Data deste relatório:** 17 de outubro de 2026, tarde (substitui a versão da manhã do mesmo dia)  
**Plano de pautas:** `PLANEJAMENTO_SEO_KEYWORD_IDEAS.md` (Ubersuggest, 11 de outubro de 2026, SD ≤ 35)  
**Padrão:** HTML estático + Tailwind v4 · URLs limpas (Vercel `cleanUrls`) · JSON-LD `@graph`  
**Funil desejado:** dica grátis → produto com link de loja → curso Hotmart (`https://go.hotmart.com/H107966532E`)

**Fonte editorial:** diário da Maraca (Pitbull Red Nose filhote, quitinete em Volta Redonda).  
**Não publicar:** motel, namoradas, maconha, meta-SEO de outro site, sonho, meme, gif, The Sims, coelho, gato, “cachorro mordendo sapo”, “cachorro mordendo porco espinho”. O projeto 01 (LavadorasPro) não entra neste relatório.

Este relatório descreve o arquivo local. Não afirma o que já está em produção.

---

## O que o Gemini deve responder

1. O quick win do planejamento, menos pastor alemão e shih tzu, está no HTML. Dizer se alguma página nova ainda compete com o pilar ou com o guia de xixi, em vez de apoiá-los.
2. A home não usa mais a chave do pilar no `<title>` nem no `WebPage.name`. O H1 é de Pitbull. O corpo ainda tem um H2 “Como adestrar um filhote de cachorro” e a frase no parágrafo do hero. Dizer se isso ainda canibaliza o pilar ou se é só link interno aceitável.
3. A fase 2 (pastor alemão e shih tzu) pode começar agora, ou falta algum ajuste nas páginas de 17/10 antes disso.
4. O `ItemList` do hub tem 36 URLs, mas a ordem do JSON não é a ordem visível. Dizer se vale reordenar ou deixar.

Não sugerir página de raça com volume 0 ou 10. Não sugerir URL própria de Durapads. Não sugerir página de sonho, meme, sapo ou ouriço.

---

## Contagem em 17/10, tarde

| Status | Qtde | O que é |
|---|---:|---|
| HTML total | 44 | 8 institucionais (inclui home, hub e `/contato-obrigado`) + 36 fichas em `/reviews/` |
| No sitemap | 43 | `/contato-obrigado` fica de fora. `lastmod` das páginas desta tarde: `2026-10-17` |
| Hub `/reviews` | 1 | 17 produtos + 14 cuidados + 5 características. `numberOfItems`: 36 |
| Pautas do plano no ar | 9 | Pilar, mordida, crianças, autolesão, xixi no lugar certo, xixi dormindo, xixi de alegria, xixi com sangue, quitinete |
| Pautas do plano ausentes | 2 | Pastor alemão e shih tzu. Fase 2. **Não existem no HTML** |

Infra: `vercel.json` com `outputDirectory: public` e `cleanUrls: true`.

---

## Status do planejamento SEO

Volumes são os do Ubersuggest no planejamento. Não somar variantes como se fossem buscas independentes.

| # | Pauta | URL | HTML |
|---|---|---|---|
| 1 | Mordida em pessoas e objetos | `/reviews/filhote-mordendo-tudo` | Feito. H3 “Mordeu criança” aponta para a página de crianças |
| 2 | Xixi no lugar errado | `/reviews/xixi-e-coco-no-lugar-certo` | Feito. Linka para dormindo, alegria e, na frase de sangue, para a página YMYL |
| 3 | Xixi dormindo / na cama | `/reviews/cachorro-faz-xixi-dormindo` | No ar. `HowTo` + `FAQPage` |
| 4 | Autolesão | `/reviews/cachorro-se-mordendo-pata-e-rabo` | No ar. `Article` + `FAQPage`, sem `HowTo`. Kong e Nylabone só depois de “veterinário descartou doença” |
| 5 | Pilar do silo | `/reviews/como-adestrar-um-filhote-de-cachorro` | Title igual ao plano. H1: “Como adestrar um filhote de cachorro em casa, sem bronca”. Sem H2 “por raça” (D3 e D4 não existem) |
| 6 | Xixi com sangue | `/reviews/cachorro-faz-xixi-com-sangue` | No ar. `Article` + `FAQPage`. Sem botão de compra. Herbalvet só no final, como limpeza do piso, em link de texto |
| 7 | Mordida em crianças | `/reviews/cachorro-mordendo-criancas` | No ar. `HowTo` + `FAQPage`. Kong Puppy e curso |
| 8 | Xixi de alegria | `/reviews/cachorro-faz-xixi-de-alegria` | No ar. `HowTo` + `FAQPage`. Durapads, Herbalvet e curso. O pilar também linka esta URL na chegada |
| 9 | Apartamento | `/reviews/limites-cao-em-quitinete` | Title novo, lead com “adestrar filhote em apartamento”, caixa do portão `https://link.amazon/B07ea7ffA`, links para pilar, mordida e xixi |
| 10 | Pastor alemão e shih tzu | `/reviews/como-adestrar-filhote-de-pastor-alemao` e `/reviews/como-adestrar-filhote-de-shih-tzu` | **Não existem no HTML** |

Fora do recorte quick win (SD > 35), o plano manda não otimizar no lançamento: “adestrar cachorro filhote” (110, SD 41), “adestrar filhote” (40, SD 40), “adestrador filhotes” (40, SD 40), “onde cachorro faz xixi” (30, SD 36), “adestrar pug filhote” (10, SD 38). “Adestrador filhotes” continua só como FAQ de preço no pilar.

---

## Silo: o que o HTML liga

### Guias

- Pilar → xixi no lugar certo, mordida, pulo nas pessoas, xixi de alegria, quitinete, Kong Puppy, curso.
- Mordida → pilar, xixi, página de crianças, Kong Puppy, kit de borracha, Nylabone (segunda opção).
- Xixi no lugar certo → pilar, mordida, xixi dormindo, xixi de alegria, xixi com sangue (na frase clínica), Herbalvet, Educa Cão. Durapads tem botão de loja e **não** tem ficha. O link interno “experiência com o tapete” aponta para `/reviews/pipi-pode-educa-cao`.
- Xixi dormindo → xixi no lugar certo, pilar e, se houver sangue, a página YMYL.
- Xixi de alegria → xixi no lugar certo, pilar, quitinete.
- Xixi com sangue → xixi no lugar certo só em “depois que o veterinário liberar”.
- Crianças → mordida e pilar.
- Autolesão → mordida (diferença entre morder gente e morder a si) e pilar.
- Quitinete → pilar, mordida, xixi, ficha do portão.

### Fichas de dinheiro que devolvem o guia

Bloco no final da página, antes do rodapé:

| Ficha | Âncora | Destino |
|---|---|---|
| Kong Puppy, Kong Classic, Kong Extreme, Kong Classic vs Puppy, Nylabone, kit de borracha | guia de filhote mordendo tudo | `/reviews/filhote-mordendo-tudo` |
| Herbalvet, Pipi Pode / Educa Cão | guia de xixi e cocô no lugar certo | `/reviews/xixi-e-coco-no-lugar-certo` |
| Portão | guia de limites na quitinete e apartamento | `/reviews/limites-cao-em-quitinete` |
| Curso | guia completo de adestramento de filhotes | `/reviews/como-adestrar-um-filhote-de-cachorro` |

Kong Extreme e Kong Classic vs Puppy também devolvem o guia de mordida. No mesmo bloco, o Extreme aponta para o comparativo e o comparativo aponta para o Extreme.

### O que o silo ainda não faz

- Não há H2 “por raça” no pilar. Correto enquanto pastor alemão e shih tzu não existirem.
- A home lista o pilar no corpo. O `ItemList` da home (8 URLs) não inclui o pilar nem as cinco páginas novas.

---

## Home — `/`

**Title:** Guia do Adestramento: Produtos e Dicas Práticas para Filhotes | Guia do Adestramento  
**`WebPage.name` no JSON-LD:** Guia do Adestramento: Produtos e Dicas Práticas para Filhotes  
**H1:** Adestramento de Pitbull filhote na prática: o que funciona em casa (2026)

O `<title>` e o `WebPage.name` não repetem mais “Como adestrar um filhote de cachorro”.

O que ainda usa a chave no corpo:

- Parágrafo do hero: “Quem pergunta como adestrar um filhote de cachorro…”
- H2: “Como adestrar um filhote de cachorro”, com link para o pilar
- Outro link no bloco de prós e contras, âncora “como adestrar um filhote de cachorro”

**H2, nesta ordem:** quadro comparativo · guia feito no chão da quitinete · comparativo rotina/produto/curso · como adestrar um filhote de cachorro · ranking · prós e contras · FAQ · outras análises · todas as análises.

**ItemList (8):** Kong Puppy · Kong Classic · Kong Extreme · xixi · mordida · Herbalvet · quitinete · curso. O quadro de produtos da home não entra nesse ItemList.

Sitemap `lastmod`: 2026-10-17.

---

## Hub — `/reviews`

**H1:** Minhas Avaliações  
**`numberOfItems`:** 36

**Ordem visível**

1. Produtos testados — 17 cards (Kong Puppy até Nylabone, incluindo kit e guia unificada)
2. Cuidados — 14 cards. Os 9 antigos mais, no fim da seção: xixi dormindo, xixi de alegria, xixi com sangue, mordendo crianças, cachorro se mordendo
3. Características — 5 cards, começando por “Como adestrar um Pitbull”

O JSON-LD tem as 36 URLs. A ordem não é a visível: as cinco páginas novas estão nas posições 32 a 36, depois de características e dos itens que já ficavam no fim (“como adestrar um filhote”, “como adestrar um Pitbull”, “guia unificada”). Quantidade bate; a ordem não.

Sitemap `lastmod`: 2026-10-17.

---

## Páginas novas em 17/10 — H1 e H2 reais

Todas no sitemap com `lastmod` 2026-10-17. Nenhuma é proposta.

### `/reviews/cachorro-faz-xixi-dormindo`

**Title:** Cachorro faz xixi dormindo ou na cama: causas e o que fazer | Guia do Adestramento  
**H1:** Cachorro faz xixi dormindo ou na cama: filhote, emoção ou incontinência  
**Schema:** `HowTo` + `FAQPage`

**H2:** Filhote que faz xixi dormindo · Xixi na cama do dono e na própria caminha · Xixi sem perceber · O que fazer esta noite · Quando não é treino · Perguntas frequentes

Caixa: Herbalvet `https://link.amazon/B0hqXqFp3` e Durapads `https://link.amazon/B03swudgY`, com a frase de que não tratam incontinência.

### `/reviews/cachorro-faz-xixi-de-alegria`

**Title:** Cachorro faz xixi de alegria quando vê o dono: o que fazer | Guia do Adestramento  
**H1:** Cachorro faz xixi de alegria quando vê o dono: como cumprimentar sem poça  
**Schema:** `HowTo` + `FAQPage`

**H2:** Alegria, felicidade e quando fica feliz · Quando eu chego, quando vê o dono, quando recebe carinho · Xixi de medo · Protocolo de 7 dias na porta · O que não fazer · Perguntas frequentes

Caixa: Durapads, Herbalvet e e-book Hotmart.

### `/reviews/cachorro-faz-xixi-com-sangue`

**Title:** Cachorro faz xixi com sangue: o que pode ser e quando ir ao vet | Guia do Adestramento  
**H1:** Cachorro faz xixi com sangue: o que pode ser e quando ir ao veterinário  
**Schema:** `Article` + `FAQPage`. Sem `HowTo`.

**H2:** O que pode ser · Sinais que não esperam · Cor da urina sem transformar a página num laboratório · O que não fazer · Depois que o veterinário liberar · Perguntas frequentes

**H3:** Vermelho, rosa e sangue · Beterraba e alimento que muda a cor · Amarelo forte, transparente e o chão esbranquiçado

Sem botão de compra. No último H2, link de texto para Herbalvet na Amazon e para a ficha, com a frase de que limpeza não trata sangue.

### `/reviews/cachorro-mordendo-criancas`

**Title:** Cachorro mordendo crianças e bebê: como proteger a casa | Guia do Adestramento  
**H1:** Cachorro mordendo crianças e bebê: como proteger sem punir o filhote  
**Schema:** `HowTo` + `FAQPage`

**H2:** Por que o filhote morde criança e bebê · O que fazer na hora · Regra única para a casa · O que não fazer · Quando a mordida deixou marca · Perguntas frequentes

**H3:** Bebê no colo ou no chão · Criança que corre e agita · Visita e menino que chega gritando

Caixa: Kong Puppy `https://link.amazon/B08zoNPdv` e e-book Hotmart.

### `/reviews/cachorro-se-mordendo-pata-e-rabo`

**Title:** Cachorro se mordendo: pata, rabo e ferida — o que pode ser | Guia do Adestramento  
**H1:** Cachorro se mordendo: pata, rabo e ferida, e quando ir ao veterinário  
**Schema:** `Article` + `FAQPage`. Sem `HowTo`.

**H2:** Pata, rabo e se mordendo não são a mesma causa · O que observar antes de decidir · Quando ir ao veterinário no mesmo dia · Se o veterinário descartou doença: o que mudar na rotina · Cachorro mordendo o ar · Perguntas frequentes

**H3:** Coceira, pulga, alergia e coxim · Dor e unha · Tédio e compulsão · Filhote perseguindo o próprio rabo

Caixa de Kong Puppy e Nylabone só depois do H2 em que o veterinário já descartou doença. Título da caixa: “Se a causa for boca sem ofício, não se for ferida”.

---

## Páginas do plano que já existiam e foram ajustadas hoje

### `/reviews/como-adestrar-um-filhote-de-cachorro`

**Title:** Como adestrar um filhote de cachorro: rotina da primeira semana | Guia do Adestramento  
**H1:** Como adestrar um filhote de cachorro em casa, sem bronca

O H3 “Não pular e a chegada em casa” linka para `/reviews/filhote-pulando-nas-pessoas` e para `/reviews/cachorro-faz-xixi-de-alegria`.

### `/reviews/filhote-mordendo-tudo`

**Title:** Cachorro mordendo: o que fazer com dono, pé, mão e móveis  
**H1:** Cachorro mordendo: o que fazer quando o filhote morde dono, pé e móveis

O H3 “Mordeu criança” resume a regra e linka para `/reviews/cachorro-mordendo-criancas`.

### `/reviews/xixi-e-coco-no-lugar-certo`

**Title:** Cachorro faz xixi no lugar errado: como ensinar o lugar certo  
**H1:** Como ensinar o filhote a fazer xixi e cocô no lugar certo

### `/reviews/limites-cao-em-quitinete`

**Title:** Como Adestrar Filhote em Apartamento e Quitinete: Limites e Rotina | Guia do Adestramento  
**H1:** Como criar um Pitbull em quitinete sem ele invadir quarto e cozinha  
**Lead:** contém “adestrar filhote em apartamento”.

**H2** (não mudaram): Restrição de ambiente · Portão de pressão · Oito horas fora · Choro na porta e chegada neutra · Perguntas frequentes

A caixa do portão entrou depois do primeiro parágrafo do H2 do portão. O H1 não foi trocado.

---

## Páginas no ar que o mapa de keywords não pediu

Não apagar por causa deste relatório. Não transformar nenhuma das duas em pastor alemão ou shih tzu.

- `/reviews/como-adestrar-pitbull` — H1: Como adestrar um Pitbull filhote em casa. Aponta para o pilar.
- `/reviews/melhores-acessorios-adestramento` — H1: Guia unificada e acessórios para adestrar filhotes. Cobre a petisqueira. A petisqueira não tem URL exclusiva.

---

## Curso — HTML local

**URL:** `/reviews/guia-completo-adestramento-canino`  
**H1:** Guia Completo de Adestramento Canino 2026: vale a pena?  
**Oferta:** `https://go.hotmart.com/H107966532E?dp=1`, `price` `37.00`, `priceCurrency` `BRL`  
Há bloco de retorno para o pilar.

---

## Falta fazer

1. Publicar `/reviews/como-adestrar-filhote-de-pastor-alemao` e `/reviews/como-adestrar-filhote-de-shih-tzu`. **Não existem no HTML.** Outline, H1 e produtos estão no planejamento, seções D3 e D4. Pastor belga entra como H2 do pastor alemão, sem URL própria. Pinscher, yorkshire, lulu e dachshund entram como H2 do shih tzu, sem URL própria.
2. Quando essas duas existirem, o pilar ganha o H2 “por raça” com link para as duas. Não criar esse H2 antes.
3. Decidir se o H2 e o parágrafo do hero da home, que ainda citam “como adestrar um filhote de cachorro”, devem continuar como estão (o link já vai para o pilar) ou se o H2 muda de texto.
4. Opcional: reordenar o `ItemList` do hub para a ordem visível. A quantidade 36 já está certa.

### Não fazer

- Página de sonho, livro dos sonhos, meme, gif, figurinha, The Sims ou Galinha Pintadinha.
- Página de “cachorro mordendo sapo” ou “cachorro mordendo porco espinho”.
- Página de coelho ou gato.
- Página por raça de volume 0 ou 10, fora os H2 previstos dentro de pastor alemão e shih tzu.
- URL própria de Durapads.
- Otimizar o pilar agora para “adestrar filhote” (SD 40) ou “adestrar cachorro filhote” (SD 41).
