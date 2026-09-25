# Relatório as-built — Guia do Adestramento (site 02)

Use este arquivo para analisar o site **como está no HTML publicado**, não o briefing de planejamento. Compare H1/H2/H3 reais, schema e funil. Não invente páginas fora desta lista.

**Domínio:** `https://www.guiadoadestramento.com.br`  
**Data deste relatório:** 11 de setembro de 2026  
**Padrão:** HTML estático + Tailwind v4 · URLs limpas (Vercel `cleanUrls`) · JSON-LD `@graph` no padrão do site 01 (LavadorasPro)

**Fonte editorial:** `02/conteudo base.md` — diário da Maraca (Pitbull Red Nose filhote, quitinete em Volta Redonda). Funil: dica grátis (papelão, pano congelado) → produto (Kong, Herbalvet) → curso Hotmart.

**Não publicar:** motel, namoradas, maconha, meta-SEO de outro site.

---

## O que foi feito nesta entrega

| Status | Qtde | O que é |
|---|---|---|
| Criada agora | 27 | Hub, 4 características, 8 cuidados, 8 produtos, 6 institucionais |
| Reescrita | 1 | Home `/` (ItemList passou a apontar para URLs reais, não âncoras `#`) |
| Já existia | 3 | `/reviews/kong-puppy`, `/reviews/herbalvet-eliminador-enzimatico`, `/reviews/clicker-para-adestramento-vale-a-pena` |
| **Total HTML** | **31** | Inclui `/contato-obrigado` (noindex, fora do sitemap) |

Infra: `02/vercel.json` com `outputDirectory: public` e `cleanUrls: true`. CSS/JS e menu usam caminhos relativos + `.html` para o Live Server; em produção a Vercel serve a URL limpa.

---

## Inventário por pilar

| Pilar | Páginas | Schema principal |
|---|---|---|
| Home | 1 | `WebPage` + `ItemList` (6 itens reais) + `FAQPage` |
| Hub | 1 | `ItemList` (23 fichas) |
| Características | 4 | `Article` + `FAQPage` |
| Cuidados | 8 | `HowTo` + `FAQPage` |
| Produtos | 11 (8 novas + 3 já no ar) | `Product` + `FAQPage` |
| Institucional | 6 | `AboutPage`, metodologia `WebPage`, `ContactPage`, `WebPage` noindex, `PrivacyPolicy`, `TermsOfService` |

ItemList da home aponta para:

1. `/reviews/kong-puppy`
2. `/reviews/xixi-e-coco-no-lugar-certo`
3. `/reviews/filhote-mordendo-tudo`
4. `/reviews/herbalvet-eliminador-enzimatico`
5. `/reviews/limites-cao-em-quitinete`
6. `/reviews/guia-completo-adestramento-canino`

Fichas de review incluem `Organization` + `WebSite` + `WebPage` + `BreadcrumbList` (Início → Reviews → página) + entidade principal + `FAQPage`.

---

## Home — `/` — REESCRITA

**Arquivo:** `public/index.html`  
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

**H3** (sob o comparativo e o ranking)

- Rotina · Produto · Curso
- Kong Puppy · Xixi e cocô no lugar certo · Filhote mordendo tudo · Herbalvet T.A. · Limites na quitinete · Guia Completo de Adestramento
- Prós · Contras

**Schema:** Organization, WebSite, WebPage, ItemList, FAQPage. Sem `Product` na home (o curso vive na ficha).

---

## Hub — `/reviews` — CRIADA

**Arquivo:** `public/reviews.html`  
**H1:** Minhas Avaliações

**H2**

1. Características da raça e da fase
2. Cuidados e adestramento no dia a dia
3. Produtos testados (reviews)

**H3** (cards)

- Características: Pitbull filhote de 2 meses · Temperamento · Crescimento e castração · Pitbull e outros cães
- Cuidados: Xixi e cocô no lugar certo · Filhote mordendo tudo · Pular nas pessoas · Limites na quitinete · Alimentação · Vacinas e vermífugo · Socialização · Enriquecimento
- Produtos: Kong Puppy · Kong Classic vs Puppy · Herbalvet T.A. · Pipi Pode / Educa Cão · Casinha plástica nº 5 · Portão de pressão · Guia e peitoral · Ração porte grande · Comedouro lento · Guia Completo · Clicker

---

## Características — Article + FAQ — CRIADAS

### `/reviews/pitbull-filhote-2-meses`

**H1:** Características de um Pitbull filhote de 2 meses

**H2**

1. Peso, porte e patas grandes: o que o corpo já antecipa
2. Cabeça, orelhas em rosa e pelagem (Red Nose, blaze, brindle)
3. APBT, American Bully e Blue Nose: o que muda no filhote
4. Janela de 8 a 12 semanas: por que essa fase não espera
5. Perguntas frequentes (FAQ)

### `/reviews/temperamento-pitbull-filhote`

**H1:** Temperamento do Pitbull filhote: energia, boca e latido

**H2**

1. Alta energia e curiosidade: picos de brincadeira e sono profundo
2. Fase da mordedura (mouthing): dente de leite, não maldade
3. Pitbull late pouco? O que isso muda no prédio
4. Rosnar no pote: proteção de recurso em filhote
5. Perguntas frequentes (FAQ)

### `/reviews/crescimento-peso-e-castracao`

**H1:** Crescimento do Pitbull: peso, porte adulto e quando castrar

**H2**

1. Do filhote de ~3 kg à fêmea de 14 a 23 kg
2. Como checar escore corporal em casa
3. Quando castrar e o que muda no cio
4. Programa público de castração (documentos, fila)
5. Perguntas frequentes (FAQ)

### `/reviews/pitbull-e-outros-caes`

**H1:** Pitbull filhote e outros cães: como apresentar sem atropelo

**H2**

1. Pitbull vs Poodle: corpo pesado contra brincadeira leve
2. Cão medroso do outro lado do muro: cheiro, distância e petisco
3. Com quantos meses apresentar (e o papel da vacina)
4. Visitas em casa: porta, petisco e cantinho do sossego
5. Perguntas frequentes (FAQ)

---

## Cuidados — HowTo + FAQ — CRIADAS

### `/reviews/xixi-e-coco-no-lugar-certo`

**H1:** Como ensinar o filhote a fazer xixi e cocô no lugar certo

**H2**

1. Quintal é banheiro, área é descanso: separe os espaços
2. Os três horários que não podem falhar (acordar, comer, brincar)
3. Por que Veja e cloro não apagam o cheiro para o cão
4. Pipi Pode ajuda — e o que ele não faz sozinho
5. Perguntas frequentes (FAQ)

### `/reviews/filhote-mordendo-tudo`

**H1:** Como fazer o filhote parar de morder móveis, pés e sofá

**H2**

1. Não é pirraça: é gengiva e mandíbula de Pitbull
2. Substituição direcionada: do chinelo para o objeto certo
3. Pano congelado e caixa de papelão: o que testei de graça
4. Quando o Kong (e o que não deixar sozinho)
5. Perguntas frequentes (FAQ)

### `/reviews/filhote-pulando-nas-pessoas`

**H1:** Como ensinar o filhote a não pular nas pessoas

**H2**

1. Ignore o pulo, recompense as 4 patas no chão
2. Cabeça na altura do rosto: o que o filhote entende como convite
3. Visitas na porta: petisco no chão, não no colo
4. O que é fofo aos 3 kg vira problema aos 20 kg
5. Perguntas frequentes (FAQ)

### `/reviews/limites-cao-em-quitinete`

**H1:** Como criar um Pitbull em quitinete sem ele invadir quarto e cozinha

**H2**

1. Restrição de ambiente: sala sim, resto não
2. Portão de pressão: altura, força e o que segura à noite
3. Oito horas fora: o que deixar no chão (e o que recolher)
4. Choro na porta e chegada neutra
5. Perguntas frequentes (FAQ)

### `/reviews/alimentacao-filhote-porte-grande`

**H1:** Quanto de ração dar para filhote de Pitbull (e quando o cocô mole denuncia erro)

**H2**

1. Colheres, refeições e por que jejum de 12 h é perigoso
2. Granel vs saco fechado: Dog Chow Minis não é ração de porte grande
3. Como trocar de marca sem derrubar o intestino
4. Ração molhada no brinquedo: por que amolece o cocô
5. Perguntas frequentes (FAQ)

### `/reviews/vacinas-v8-v10-e-vermifugo`

**H1:** Vacina V8, V10 e vermífugo no filhote: ordem, intervalo e o que esperar

**H2**

1. V8 ou V10: o que muda na leptospirose
2. Quantas doses até a rua (e a antirrábica)
3. Vermífugo: dose pelo peso, repetir em 15 dias, barriga inchada
4. Calombo da injeção, prostração e o que não misturar no mesmo dia
5. Perguntas frequentes (FAQ)

### `/reviews/socializacao-filhote-com-outros-caes`

**H1:** Como socializar Pitbull filhote com um cão medroso (e com visitas)

**H2**

1. Troca de cheiro antes do olho no olho
2. Nina latiu? Petisco na hora — sem festa de perseguição
3. Comando Deixa: lixo, comida no chão e o futuro adulto
4. Rua só depois do esquema vacinal
5. Perguntas frequentes (FAQ)

### `/reviews/enriquecimento-ambiental-filhote`

**H1:** Enriquecimento ambiental para filhote: papelão, pano congelado e rodízio

**H2**

1. Overdose de brinquedo: por que 8 itens no chão agitam mais
2. A regra dos 2 itens e o cardápio do dia (manhã / tarde / noite)
3. Pano congelado com ração seca vs Kong com ração molhada
4. O que deixar quando você sai (e o que só existe com supervisão)
5. Perguntas frequentes (FAQ)

---

## Produtos — Product + FAQ

Nas 8 fichas novas, o bloco de prós/contras/CTAs não usa H2; entram **H3 Ficha técnica** e **H2 Veredito** antes do corpo.

### `/reviews/kong-puppy` — JÁ EXISTIA (não regenerada)

**H1:** Kong Puppy vale a pena? Avaliação do brinquedo Kong para filhote de Pitbull

**H2**

1. O que torna o brinquedo Kong para cachorro a melhor escolha na troca de dentes?
2. Kong Puppy Small, Medium ou Large: qual tamanho escolher para filhote de porte grande?
3. Kong Puppy vs Kong Classic: quando fazer a transição para a borracha vermelha?
4. Kong Puppy vs Nylabone Puppy: qual dura mais com morde-morde forte?
5. Recheio seco vs molhado: como rechear sem soltar o intestino do filhote
6. Perguntas frequentes sobre os brinquedos do Kong (FAQ)

**H3** (seleção): Kong Puppy Small · Medium · Kong cachorro grande · Ficha técnica · Veredito · Troca de dentes · Depois dos 6–9 meses · tabela comparativa · petisqueira · Guia Completo · Classic e Nylabone

### `/reviews/kong-classic-vs-puppy` — CRIADA

**H1:** Kong Classic ou Puppy: qual comprar em 2026?

**H3:** Ficha técnica

**H2**

1. Veredito: Puppy agora, Classic no calendário
2. Puppy, Classic vermelho e Extreme preto: borracha e idade
3. Quando o filhote de Pitbull estoura o Puppy
4. Tamanho M vs G e risco de engolir o P
5. Odontopet, Benebone e nacionais: quando o dobro do Kong se paga
6. Perguntas frequentes (FAQ)

### `/reviews/herbalvet-eliminador-enzimatico` — JÁ EXISTIA (não regenerada)

**H1:** Desinfetante Herbalvet T.A. vale a pena? Para que serve, como usar e diluição prática

**H2**

1. Herbalvet para que serve e por que é superior ao cloro comum no xixi de cachorro?
2. Herbalvet como usar e diluir na garrafa PET para render em apartamento
3. Herbalvet ou Lysoform / Veja: qual o risco para as patas do filhote?
4. Herbalvet T.A. 1000ml vs 500ml: qual o preço e melhor custo-benefício na Amazon?
5. Herbalvet composição e ação contra parvovirose e odores fortes de ureia
6. Perguntas frequentes sobre o desinfetante Herbalvet Ourofino (FAQ)

**H3** (seleção): 500ml · 1000ml · Spray/Veja · Ficha técnica · Veredito · Sala/sofá · Puro vs treino · comparativo · Durapads + Pipi Pode · Guia Completo

### `/reviews/pipi-pode-educa-cao` — CRIADA

**H1:** Pipi Pode / Educa Cão funciona sozinho?

**H3:** Ficha técnica

**H2**

1. Veredito: só depois da rotina e do Herbalvet
2. Atrativo sanitário: o que o olfato do filhote entende
3. Por que não substitui rotina, quintal e enzimático
4. Kit Pipi Pode + Pipi Não Pode: quando vale o dinheiro
5. Tapete higiênico Durapads: apoio, não banheiro eterno
6. Perguntas frequentes (FAQ)

### `/reviews/casinha-plastico-furacao-pet` — CRIADA

**H1:** Casinha de plástico nº 5 vale a pena para Pitbull filhote?

**H3:** Ficha técnica

**H2**

1. Veredito: plástico nº 5, não madeira
2. Plástico ou madeira: pulga, calor e quitinete
3. Furacão Pet / Tánatela 2 em 1: iglu que vira caminha
4. Número 4 vs 5 no crescimento de um porte grande
5. Caixa de sapato e coberta: o que usa até a casinha chegar
6. Perguntas frequentes (FAQ)

### `/reviews/portao-pet-de-pressao` — CRIADA

**H1:** Portão pet de pressão vale a pena em apartamento pequeno?

**H3:** Ficha técnica

**H2**

1. Veredito: sim, se a casa não tem porta no vão
2. Como impedir a passagem da sala para a cozinha sem porta
3. Altura, força do filhote e o que muda no adulto
4. Ferro de pressão vs papelão e móvel improvisado
5. Grade, extensor e o muro de 1,70 m
6. Perguntas frequentes (FAQ)

### `/reviews/guia-e-peitoral-filhote` — CRIADA

**H1:** Guia e peitoral para filhote de 3 meses: o que comprar

**H3:** Ficha técnica

**H2**

1. Veredito: lisa curta agora, retrátil nunca no treino
2. Guia de nylon 1,5 a 2 m: controle sem ensinar a puxar
3. Por que guia retrátil é péssima para treino
4. Peitoral vs coleira no crescimento (troca por volta dos 6 meses)
5. Passeio só depois da V10: o que a guia faz em casa até lá
6. Perguntas frequentes (FAQ)

### `/reviews/racao-filhotes-porte-grande` — CRIADA

**H1:** Melhor ração para filhote de Pitbull: NutriSano, Golden ou Premier?

**H3:** Ficha técnica

**H2**

1. Veredito: porte grande em saco, não Minis a granel
2. Por que Dog Chow Minis/Pequenos e granel falham nesse porte
3. NutriSano, Multidog, Golden Filhotes/Mega e Premier Fórmula
4. Saco de 3 kg vs 15 kg: preço, oxigênio e o papo do balcão
5. Quantidade em colheres e o cocô como medidor
6. Perguntas frequentes (FAQ)

### `/reviews/comedouro-lento` — CRIADA

**H1:** Comedouro lento vale a pena para filhote que engole ração?

**H3:** Ficha técnica

**H2**

1. Veredito: sim, se o desenho obrigar a língua a trabalhar
2. Soluço, ar na barriga e ração que some em segundos
3. Bola recheável, Colmeia Buddy, Stark Pet e Pet Games
4. Furo largo demais: o grão cai de uma vez
5. Comedouro lento vs Kong seco vs bandeja espalhada
6. Perguntas frequentes (FAQ)

### `/reviews/guia-completo-adestramento-canino` — CRIADA

**H1:** Guia Completo de Adestramento Canino 2026: vale a pena?

**H3:** Ficha técnica

**H2**

1. Veredito: vale se você quer o método amarrado, não um frasco a mais
2. O programa fecha o que o diário da Maraca não cobre sozinho?
3. Xixi, limites e mordedura: o que é método e o que é produto
4. Garantia, suporte e o que não é milagre em 7 dias
5. Curso vs Kong + enzimático vs aula particular
6. Perguntas frequentes (FAQ)

**Product:** brand Guia do Adestramento. `offers.url` aponta para a ficha até existir checkout Hotmart.

### `/reviews/clicker-para-adestramento-vale-a-pena` — JÁ EXISTIA (ficha extra, fora do mapa original de 10 produtos)

**H1:** Clicker para cachorro: clicker adestramento vale a pena? (click para adestramento em 2026)

**H2**

1. O que é clicker e como funciona no treino do filhote?
2. Clicker para cachorro vale a pena ou estalo de dedos resolve?
3. Kit completo: por que usar o clicker junto com a petisqueira para adestramento?
4. Qual o melhor click de adestrador para comprar em 2026?
5. Guia Completo de Adestramento em Vídeo: o clicker só funciona com o método
6. Perguntas Frequentes (FAQ)

**H3** (seleção): Clicker com pulseira · Petisqueira · Ficha técnica · Veredito · Apartamento · Passeio · Kong Puppy

---

## Institucionais — CRIADAS

### `/quem-somos`

**H1:** Sobre o projeto “Guia do Adestramento”

**H2:** Meu objetivo · Como faço minhas recomendações · Compromisso de qualidade · Transparência e links de afiliado · Para quem este site é indicado · Fale comigo

**Schema:** Person + Organization + WebSite + AboutPage

### `/metodologia`

**H1:** Guia do Adestramento — nossa metodologia de análise

**H2:** Como escolho o que analisar · Fonte e critério de comparação · O passo a passo da análise · Como fecho o veredito · Imparcialidade · Revisão e atualização

Eixos no lugar de PSI/vazão: ética (sem aversivo), teste real com filhote de porte grande, custo-benefício, segurança (dente de leite, supervisão).

### `/contato`

**H1:** Guia do Adestramento — fale comigo

**H2:** Como falar comigo · Enviar mensagem · Sobre o que você pode escrever · Onde estou

Formulário Web3Forms; redirect para `/contato-obrigado`.

### `/contato-obrigado`

**H1:** Mensagem recebida  
**Schema:** WebPage · `noindex` · fora do sitemap

### `/politica-de-privacidade`

**H1:** Política de Privacidade | Guia do Adestramento

**H2:** Quais dados coleto · Para que uso seus dados · Com quem os dados são tratados · Cookies · Links de afiliados · Seus direitos (LGPD) · Retenção e contato

### `/termos-e-condicoes`

**H1:** Termos e Condições | Guia do Adestramento

**H2:** Sobre o nosso conteúdo · Uso do conteúdo e propriedade intelectual · Comentários e cadastro · Limitação de responsabilidade · Alterações e contato

---

## Pedidos de análise (Gemini)

1. Cobertura vs briefing `arquitetura-para-gemini.md`: o que bate, o que driftou (sobretudo Kong Puppy, Herbalvet e Clicker, que não passaram pelo gerador).
2. Hierarquia H1/H2/H3: FAQ repetido; H3 “Ficha técnica” antes do Veredito nas 8 produtos novas; emojis só nas 3 fichas antigas.
3. Canibalização: xixi vs Pipi Pode vs Herbalvet; mordedura vs Kong Puppy vs Classic; alimentação vs ração.
4. Funil dica grátis → produto → curso: está explícito nas H2?
5. E-E-A-T e YMYL (vacina, castração, ração): o tom de diário basta ou falta disclaimer de veterinário mais visível no H1/H2?
6. Clicker extra: manter no hub ou unificar com o curso?

Não sugerir páginas novas fora deste inventário sem marcar como “proposta, não existe no HTML”.
