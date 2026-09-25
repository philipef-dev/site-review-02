# Arquitetura de páginas — Guia do Adestramento (site 02)

Domínio: `https://www.guiadoadestramento.com.br`  
URLs limpas, no padrão do site 01 (`/` + `/reviews` + `/reviews/{slug}` + institucionais).

## Fonte

`02/conteudo base.md` — diário de campo de **~2 meses** com a Maraca (Pitbull Red Nose, filhote, quitinete em Volta Redonda). ~756 KB / 11 mil linhas.

Não entra no site: trechos pessoais fora de adestramento (motel, namoradas, maconha), meta-conversa de SEO do LavadorasPro nem tutoriais de editor.

Eixos de conteúdo que o próprio chat pede para o blog:

1. Troca de dentes e destruição de móveis  
2. Limites em espaço pequeno (quitinete, 8 h fora)  
3. Xixi e cocô no lugar certo + limpador enzimático  
4. Funil: dica gratuita → produto durável (Kong, Herbalvet) → curso Hotmart

---

## Tópicos extraídos do diário

### Características

| Tópico | O que o chat cobre |
|---|---|
| Pitbull filhote ~2 meses | Peso 3–6 kg, patas grandes, cabeça quadrada, orelhas em rosa, pelagem curta |
| Red Nose / linhagens | Trufa rosada, blaze branco, APBT vs American Bully vs Blue Nose |
| Temperamento | Alta energia, curiosidade, mouthing, janela de socialização 8–12 semanas |
| Latido | Raça pouco latidora; comparado a Poodle/Pinscher/York |
| Crescimento | +~3 kg/mês; fêmea adulta APBT 14–23 kg; peito alarga |
| Proteção de recurso | Rosnar no pote ao aproximar a mão (filhote) |
| Sono e corpo | Tremor/chute dormindo, soluço por comer rápido, lamber vs morder |
| Castração e cio | Quando castrar, programa público, cio some após cirurgia |

### Cuidados

| Tópico | O que o chat cobre |
|---|---|
| Xixi/cocô no lugar certo | Quintal vs sala vs área; pós-sono, pós-ração, pós-brincadeira; sem briga |
| Odor residual | Veja/cloro não apagam ureia; enzimático sim |
| Mordedura | Pés, mãos, sofá, tapete, chinelo, boné, cortina, parede, rodo, móveis |
| Pular nas pessoas | Ignorar, 4 patas no chão, redirecionar para brinquedo |
| Limites na quitinete | Sala liberada, cozinha/quarto off; portão de pressão; 8 h sozinha |
| Choro na porta | Abrir só no silêncio; neutralidade em saída/chegada |
| Alimentação | 3 refeições, colheres, jejum perigoso, troca gradual, fezes moles |
| Vacinas | V8 vs V10, doses, raiva, calombo da injeção, vermífugo no mesmo dia |
| Vermífugo | Drontal, Chemital, Baskken, Endogard; repetir 15 dias; barriga inchada |
| Socialização | Nina (Poodle média medrosa), muro 1,70 m, visitas, comando Deixa |
| Enriquecimento | Papelão, pano congelado, PET, rodízio (máx. 1–2 itens), overdose de estímulo |
| Guia e passeio | Só após esquema vacinal; guia 1,5–2 m; retrátil não |
| Banho, chuva, frio | Área coberta, casinha, caixa de sapato como toca |
| Nome e rotina | Atender pelo nome; não mendigar na mesa; não pular na cama adulto |

### Produtos (citados para review/afiliado)

| Produto | Papel no diário |
|---|---|
| KONG Puppy (rosa/azul) | Hero: dentição, rechear, congelar |
| KONG Classic (vermelho) / Extreme (preto) | Upgrade 6–9 meses; evitar Senior (roxo) |
| Odontopet Dura Lagosta, Spinner, Benebone/Nylabone | Alternativas nacionais / nylon |
| Corda / cabo de guerra | Só com supervisão |
| Bola recheável, Colmeia Buddy, Pet Games | Comedouro lento / ocupação |
| Garrafa PET, caixa de papelão, pano congelado | Custo zero (conteúdo + ponte para Kong) |
| NutriSano, Golden Filhotes/Mega, Premier, GranPlus, Multidog | Ração filhote porte grande |
| Dog Chow a granel / Minis e Pequenos | Contraponto (evitar) |
| Herbalvet T.A. | Eliminador enzimático escolhido |
| Enzymac, Sanol Pipi Safe, Vanish Enzimático, Hysteril | Concorrentes / menções |
| Pipi Pode / Educa Cão / Xixi Pode | Atrativo sanitário (não é mágica) |
| Tapete Durapads | Apoio no treino |
| Casinha plástico Furacão Pet / Tánatela nº 4–5 | Plástico > madeira (pulgas) |
| Portão pet de pressão | Bloquear cozinha/quarto |
| Guia nylon 1,5–2 m + peitoral | Retrátil não |
| Vermífugo Drontal Pup / Chemital | Saúde |
| Curso Hotmart (Guia Completo) | Produto digital do funil |

---

## Mapa de URLs (30 páginas)

| URL | Pilar | Schema principal |
|---|---|---|
| `/` | Home | `WebPage` + `ItemList` + `FAQPage` |
| `/reviews` | Hub | `ItemList` |
| `/reviews/pitbull-filhote-2-meses` | Características | `Article` + `FAQPage` |
| `/reviews/temperamento-pitbull-filhote` | Características | `Article` + `FAQPage` |
| `/reviews/crescimento-peso-e-castracao` | Características | `Article` + `FAQPage` |
| `/reviews/pitbull-e-outros-caes` | Características | `Article` + `FAQPage` |
| `/reviews/xixi-e-coco-no-lugar-certo` | Cuidados | `HowTo` + `FAQPage` |
| `/reviews/filhote-mordendo-tudo` | Cuidados | `HowTo` + `FAQPage` |
| `/reviews/filhote-pulando-nas-pessoas` | Cuidados | `HowTo` + `FAQPage` |
| `/reviews/limites-cao-em-quitinete` | Cuidados | `HowTo` + `FAQPage` |
| `/reviews/alimentacao-filhote-porte-grande` | Cuidados | `HowTo` + `FAQPage` |
| `/reviews/vacinas-v8-v10-e-vermifugo` | Cuidados | `HowTo` + `FAQPage` |
| `/reviews/socializacao-filhote-com-outros-caes` | Cuidados | `HowTo` + `FAQPage` |
| `/reviews/enriquecimento-ambiental-filhote` | Cuidados | `HowTo` + `FAQPage` |
| `/reviews/kong-puppy` | Produtos | `Product` + `FAQPage` |
| `/reviews/kong-classic-vs-puppy` | Produtos | `Product` + `FAQPage` |
| `/reviews/herbalvet-eliminador-enzimatico` | Produtos | `Product` + `FAQPage` |
| `/reviews/pipi-pode-educa-cao` | Produtos | `Product` + `FAQPage` |
| `/reviews/casinha-plastico-furacao-pet` | Produtos | `Product` + `FAQPage` |
| `/reviews/portao-pet-de-pressao` | Produtos | `Product` + `FAQPage` |
| `/reviews/guia-e-peitoral-filhote` | Produtos | `Product` + `FAQPage` |
| `/reviews/racao-filhotes-porte-grande` | Produtos | `Product` + `FAQPage` |
| `/reviews/comedouro-lento` | Produtos | `Product` + `FAQPage` |
| `/reviews/guia-completo-adestramento-canino` | Produtos | `Product` + `FAQPage` |
| `/quem-somos` | Institucional | `AboutPage` + `Person` |
| `/metodologia` | Institucional | `WebPage` + `Person` |
| `/contato` | Institucional | `ContactPage` |
| `/contato-obrigado` | Institucional | `WebPage` (fora do sitemap) |
| `/politica-de-privacidade` | Institucional | `PrivacyPolicy` |
| `/termos-e-condicoes` | Institucional | `TermsOfService` |

Arquivos: `public/{slug}.html` na raiz; fichas em `public/reviews/{slug}.html`.  
Todo `@graph` inclui `Organization` `#organization` e, nas fichas, `WebSite` + `BreadcrumbList` (Início → Reviews → página), como no site 01.

`ItemList` da home aponta para URLs reais (não âncoras `#`):

1. Kong Puppy  
2. Como ensinar xixi e cocô no lugar certo  
3. Filhote mordendo tudo  
4. Herbalvet  
5. Limites em quitinete  
6. Guia Completo (Hotmart)

---

## Home — `/`

**H1:** Adestramento de Pitbull filhote na prática: o que funciona em casa (2026)

**H2**

1. Um guia feito no chão da quitinete — não em teoria de manual  
2. Comparativo do que realmente segura móvel, xixi e limites  
3. Como escolher método, produto e rotina para filhote de porte grande  
4. Ranking das soluções testadas com a Maraca em 2026  
5. Prós e contras de treinar um Pitbull em espaço pequeno  
6. Perguntas frequentes (xixi, Kong, vacina, 8 h sozinha, latido)  
7. Outras análises que valem a sua atenção  
8. Todas as análises do Guia do Adestramento

**JSON-LD:** `Organization` + `WebSite` + `WebPage` + `ItemList` (6 itens acima) + `FAQPage`.  
O `Product` do curso e do Kong vive na ficha, não na home (padrão do site 01).

---

## Hub — `/reviews`

**H1:** Minhas Avaliações

**H2**

1. Características da raça e da fase  
2. Cuidados e adestramento no dia a dia  
3. Produtos testados (reviews)

Nomes das fichas entram como **H3** nos cards.

**JSON-LD:** `Organization` + `ItemList` unordered, `numberOfItems` 22 (4 + 8 + 10 fichas).

---

## Características — `Article` + `FAQPage`

Grafo: `Organization` + `WebSite` + `WebPage` + `BreadcrumbList` + `Article` + `FAQPage`.

### `/reviews/pitbull-filhote-2-meses`

- **H1:** Características de um Pitbull filhote de 2 meses  
- **H2:** Peso, porte e patas grandes: o que o corpo já antecipa  
- **H2:** Cabeça, orelhas em rosa e pelagem (Red Nose, blaze, brindle)  
- **H2:** APBT, American Bully e Blue Nose: o que muda no filhote  
- **H2:** Janela de 8 a 12 semanas: por que essa fase não espera  
- **H2:** Perguntas frequentes (FAQ)

### `/reviews/temperamento-pitbull-filhote`

- **H1:** Temperamento do Pitbull filhote: energia, boca e latido  
- **H2:** Alta energia e curiosidade: picos de brincadeira e sono profundo  
- **H2:** Fase da mordedura (mouthing): dente de leite, não maldade  
- **H2:** Pitbull late pouco? O que isso muda no prédio  
- **H2:** Rosnar no pote: proteção de recurso em filhote  
- **H2:** Perguntas frequentes (FAQ)

### `/reviews/crescimento-peso-e-castracao`

- **H1:** Crescimento do Pitbull: peso, porte adulto e quando castrar  
- **H2:** Do filhote de ~3 kg à fêmea de 14 a 23 kg  
- **H2:** Como checar escore corporal em casa  
- **H2:** Quando castrar e o que muda no cio  
- **H2:** Programa público de castração (documentos, fila)  
- **H2:** Perguntas frequentes (FAQ)

### `/reviews/pitbull-e-outros-caes`

- **H1:** Pitbull filhote e outros cães: como apresentar sem atropelo  
- **H2:** Pitbull vs Poodle: corpo pesado contra brincadeira leve  
- **H2:** Cão medroso do outro lado do muro: cheiro, distância e petisco  
- **H2:** Com quantos meses apresentar (e o papel da vacina)  
- **H2:** Visitas em casa: porta, petisco e cantinho do sossego  
- **H2:** Perguntas frequentes (FAQ)

---

## Cuidados — `HowTo` + `FAQPage`

Grafo: igual ao Article, trocando a entidade principal por `HowTo` com `step`.

### `/reviews/xixi-e-coco-no-lugar-certo`

- **H1:** Como ensinar o filhote a fazer xixi e cocô no lugar certo  
- **H2:** Quintal é banheiro, área é descanso: separe os espaços  
- **H2:** Os três horários que não podem falhar (acordar, comer, brincar)  
- **H2:** Por que Veja e cloro não apagam o cheiro para o cão  
- **H2:** Pipi Pode ajuda — e o que ele não faz sozinho  
- **H2:** Perguntas frequentes (FAQ)

### `/reviews/filhote-mordendo-tudo`

- **H1:** Como fazer o filhote parar de morder móveis, pés e sofá  
- **H2:** Não é pirraça: é gengiva e mandíbula de Pitbull  
- **H2:** Substituição direcionada: do chinelo para o objeto certo  
- **H2:** Pano congelado e caixa de papelão: o que testei de graça  
- **H2:** Quando o Kong (e o que não deixar sozinho)  
- **H2:** Perguntas frequentes (FAQ)

### `/reviews/filhote-pulando-nas-pessoas`

- **H1:** Como ensinar o filhote a não pular nas pessoas  
- **H2:** Ignore o pulo, recompense as 4 patas no chão  
- **H2:** Cabeça na altura do rosto: o que o filhote entende como convite  
- **H2:** Visitas na porta: petisco no chão, não no colo  
- **H2:** O que é fofo aos 3 kg vira problema aos 20 kg  
- **H2:** Perguntas frequentes (FAQ)

### `/reviews/limites-cao-em-quitinete`

- **H1:** Como criar um Pitbull em quitinete sem ele invadir quarto e cozinha  
- **H2:** Restrição de ambiente: sala sim, resto não  
- **H2:** Portão de pressão: altura, força e o que segura à noite  
- **H2:** Oito horas fora: o que deixar no chão (e o que recolher)  
- **H2:** Choro na porta e chegada neutra  
- **H2:** Perguntas frequentes (FAQ)

### `/reviews/alimentacao-filhote-porte-grande`

- **H1:** Quanto de ração dar para filhote de Pitbull (e quando o cocô mole denuncia erro)  
- **H2:** Colheres, refeições e por que jejum de 12 h é perigoso  
- **H2:** Granel vs saco fechado: Dog Chow Minis não é ração de porte grande  
- **H2:** Como trocar de marca sem derrubar o intestino  
- **H2:** Ração molhada no brinquedo: por que amolece o cocô  
- **H2:** Perguntas frequentes (FAQ)

### `/reviews/vacinas-v8-v10-e-vermifugo`

- **H1:** Vacina V8, V10 e vermífugo no filhote: ordem, intervalo e o que esperar  
- **H2:** V8 ou V10: o que muda na leptospirose  
- **H2:** Quantas doses até a rua (e a antirrábica)  
- **H2:** Vermífugo: dose pelo peso, repetir em 15 dias, barriga inchada  
- **H2:** Calombo da injeção, prostração e o que não misturar no mesmo dia  
- **H2:** Perguntas frequentes (FAQ)

### `/reviews/socializacao-filhote-com-outros-caes`

- **H1:** Como socializar Pitbull filhote com um cão medroso (e com visitas)  
- **H2:** Troca de cheiro antes do olho no olho  
- **H2:** Nina latiu? Petisco na hora — sem transformar em festa de perseguição  
- **H2:** Comando Deixa: lixo, comida no chão e o futuro adulto  
- **H2:** Rua só depois do esquema vacinal  
- **H2:** Perguntas frequentes (FAQ)

### `/reviews/enriquecimento-ambiental-filhote`

- **H1:** Enriquecimento ambiental para filhote: papelão, pano congelado e rodízio  
- **H2:** Overdose de brinquedo: por que 8 itens no chão agitam mais  
- **H2:** A regra dos 2 itens e o cardápio do dia (manhã / tarde / noite)  
- **H2:** Pano congelado com ração seca vs Kong com ração molhada  
- **H2:** O que deixar quando você sai (e o que só existe com supervisão)  
- **H2:** Perguntas frequentes (FAQ)

---

## Produtos — `Product` + `FAQPage` (padrão exato do site 01)

Grafo: `Organization` + `WebSite` + `WebPage` + `BreadcrumbList` + `Product` (`brand`, `aggregateRating`, `review`, `offers` quando houver link real, `additionalProperty`) + `FAQPage`.

H2 padrão: veredito, o que isso significa na prática, comparativo, FAQ.

### `/reviews/kong-puppy`

- **H1:** Kong Puppy vale a pena para filhote de Pitbull?  
- **H2:** Kong Puppy é o melhor mordedor para a troca de dentes?  
- **H2:** Rosa/azul, tamanho M ou G, e por que não o Senior roxo  
- **H2:** Recheio seco vs molhado: intestino e tempo de ocupação  
- **H2:** Kong Puppy vs bola barata de pet shop vs pano congelado  
- **H2:** Perguntas frequentes (FAQ)

### `/reviews/kong-classic-vs-puppy`

- **H1:** Kong Classic ou Puppy: qual comprar em 2026?  
- **H2:** Puppy, Classic vermelho e Extreme preto: borracha e idade  
- **H2:** Quando o filhote de Pitbull estoura o Puppy  
- **H2:** Tamanho M vs G e risco de engolir o P  
- **H2:** Odontopet, Benebone e nacionais: quando o dobro do Kong se paga  
- **H2:** Perguntas frequentes (FAQ)

### `/reviews/herbalvet-eliminador-enzimatico`

- **H1:** Herbalvet T.A. vale a pena para xixi de filhote?  
- **H2:** Por que desinfetante comum não quebra a ureia  
- **H2:** Diluição na garrafa PET de 2 L (o que funciona na prática)  
- **H2:** Herbalvet vs Enzymac, Sanol Pipi Safe e Vanish Enzimático  
- **H2:** Sala, panos e quintal de cimento: onde passar (e onde não apagar o cheiro)  
- **H2:** Perguntas frequentes (FAQ)

### `/reviews/pipi-pode-educa-cao`

- **H1:** Pipi Pode / Educa Cão funciona sozinho?  
- **H2:** Atrativo sanitário: o que o olfato do filhote entende  
- **H2:** Por que não substitui rotina, quintal e enzimático  
- **H2:** Kit Pipi Pode + Pipi Não Pode: quando vale o dinheiro  
- **H2:** Tapete higiênico Durapads: apoio, não banheiro eterno  
- **H2:** Perguntas frequentes (FAQ)

### `/reviews/casinha-plastico-furacao-pet`

- **H1:** Casinha de plástico nº 5 vale a pena para Pitbull filhote?  
- **H2:** Plástico ou madeira: pulga, calor e quitinete  
- **H2:** Furacão Pet / Tánatela 2 em 1: iglu que vira caminha  
- **H2:** Número 4 vs 5 no crescimento de um porte grande  
- **H2:** Caixa de sapato e coberta: o que usa até a casinha chegar  
- **H2:** Perguntas frequentes (FAQ)

### `/reviews/portao-pet-de-pressao`

- **H1:** Portão pet de pressão vale a pena em apartamento pequeno?  
- **H2:** Como impedir a passagem da sala para a cozinha sem porta  
- **H2:** Altura, força do filhote e o que muda no adulto  
- **H2:** Ferro de pressão vs papelão e móvel improvisado  
- **H2:** Grade, extensor e o muro de 1,70 m  
- **H2:** Perguntas frequentes (FAQ)

### `/reviews/guia-e-peitoral-filhote`

- **H1:** Guia e peitoral para filhote de 3 meses: o que comprar  
- **H2:** Guia de nylon 1,5 a 2 m: controle sem ensinar a puxar  
- **H2:** Por que guia retrátil é péssima para treino  
- **H2:** Peitoral vs coleira no crescimento (troca por volta dos 6 meses)  
- **H2:** Passeio só depois da V10: o que a guia faz em casa até lá  
- **H2:** Perguntas frequentes (FAQ)

### `/reviews/racao-filhotes-porte-grande`

- **H1:** Melhor ração para filhote de Pitbull: NutriSano, Golden ou Premier?  
- **H2:** Por que Dog Chow Minis/Pequenos e granel falham nesse porte  
- **H2:** NutriSano, Multidog, Golden Filhotes/Mega e Premier Fórmula  
- **H2:** Saco de 3 kg vs 15 kg: preço, oxigênio e o papo do balcão  
- **H2:** Quantidade em colheres e o cocô como medidor  
- **H2:** Perguntas frequentes (FAQ)

### `/reviews/comedouro-lento`

- **H1:** Comedouro lento vale a pena para filhote que engole ração?  
- **H2:** Soluço, ar na barriga e ração que some em segundos  
- **H2:** Bola recheável, Colmeia Buddy, Stark Pet e Pet Games  
- **H2:** Furo largo demais: o grão cai de uma vez  
- **H2:** Comedouro lento vs Kong seco vs bandeja espalhada  
- **H2:** Perguntas frequentes (FAQ)

### `/reviews/guia-completo-adestramento-canino`

- **H1:** Guia Completo de Adestramento Canino 2026: vale a pena?  
- **H2:** O programa fecha o que o diário da Maraca não cobre sozinho?  
- **H2:** Xixi, limites e mordedura: o que é método e o que é produto  
- **H2:** Garantia, suporte e o que não é milagre em 7 dias  
- **H2:** Curso vs Kong + enzimático vs aula particular  
- **H2:** Perguntas frequentes (FAQ)

Product: brand `Guia do Adestramento`; nota 4.9 / 1.200 só se a oferta real confirmar (hoje está na home). `offers.url` aponta para a ficha até existir checkout Hotmart.

---

## Institucionais (H2 iguais ao site 01)

### `/quem-somos`

- **H1:** Sobre o projeto “Guia do Adestramento”  
- **H2:** Meu objetivo · Como faço minhas recomendações · Compromisso de qualidade · Transparência e links de afiliado · Para quem este site é indicado · Fale comigo  

Critério de E-E-A-T: diário da Maraca (quitinete, Volta Redonda), não laboratório.

### `/metodologia`

- **H1:** Guia do Adestramento — nossa metodologia de análise  
- **H2:** Como escolho o que analisar · Fonte e critério · Passo a passo · Veredito · Imparcialidade · Revisão e atualização  

Eixos no lugar de PSI/vazão: ética (sem aversivo), teste real com filhote de porte grande, custo-benefício, segurança (dente de leite, supervisão).

### `/contato` · `/contato-obrigado` · `/politica-de-privacidade` · `/termos-e-condicoes`

Mesmos H1/H2 e tipos Schema.org do site 01 (`ContactPage`, `WebPage`, `PrivacyPolicy`, `TermsOfService`).

---

## JSON-LD — modelos (copiar e trocar SLUG)

**Ficha Article** — ver `reforco-positivo` antigo; trocar headline/url.

**Ficha HowTo** — `step` alinhado aos H2 de procedimento.

**Ficha Product** — igual WAP WL 1820 do site 01: `brand`, `aggregateRating`, `review` (autor Philipe Ferreira), `offers` Amazon/ML quando houver, `additionalProperty` (tamanho, borracha, diluição, etc.).

FAQ visível na página = mesmo texto do `FAQPage`.

---

## Infra

No `vercel.json` do 02: `"cleanUrls": true` além de `outputDirectory: "public"`.
