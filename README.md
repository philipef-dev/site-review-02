# Guia do Adestramento

Site estático do **Guia do Adestramento** — um diário prático sobre adestramento de Pitbull filhote, com reviews de produtos, guias de comportamento e dicas de convivência em apartamento/quitinete.

**URL de produção:** [https://www.guiadoadestramento.com.br](https://www.guiadoadestramento.com.br)

## Estrutura do projeto

```
├── src/
│   └── input.css          # CSS de entrada (importa o Tailwind v4)
├── public/                 # Arquivos estáticos servidos em produção
│   ├── index.html          # Página inicial
│   ├── reviews.html        # Listagem de reviews
│   ├── reviews/            # Reviews individuais (artigos)
│   ├── quem-somos.html
│   ├── contato.html
│   ├── metodologia.html
│   ├── politica-de-privacidade.html
│   ├── termos-e-condicoes.html
│   ├── scripts/            # JavaScript do site
│   ├── output.css          # CSS compilado (gerado pelo Tailwind)
│   ├── sitemap.xml
│   └── robots.txt
├── bs-config.js            # Configuração do Browser-Sync (clean URLs)
├── package.json
└── README.md
```

## Tecnologias

- **HTML** estático com clean URLs (sem `.html` nos links)
- **Tailwind CSS v4** (compilação via `@tailwindcss/cli`)
- **Browser-Sync** para servidor local com live reload

## Pré-requisitos

- [Node.js](https://nodejs.org/) (v18 ou superior)
- npm (incluso com o Node.js)

## Instalação

```bash
npm install
```

## Rodando localmente

São necessárias **duas abas no terminal**:

### Aba 1 — Compilação do Tailwind (watch mode)

```bash
npm run dev
```

Monitora alterações nos arquivos HTML e recompila o `output.css` automaticamente.

### Aba 2 — Servidor local com live reload

```bash
npm run serve
```

Abre o navegador em `http://localhost:3000` com:
- **Clean URLs** funcionando (ex: `/reviews`, `/quem-somos`)
- **Live reload** automático ao editar qualquer arquivo em `public/`

## Build para produção

```bash
npm run build
```

Gera o `public/output.css` minificado. A pasta `public/` inteira é o que vai para o deploy.

## Scripts disponíveis

| Script          | Comando                        | Descrição                                      |
|-----------------|--------------------------------|-------------------------------------------------|
| `npm run dev`   | `tailwindcss -i ... --watch`   | Compila o Tailwind e monitora alterações         |
| `npm run build` | `tailwindcss -i ... --minify`  | Compila o Tailwind minificado para produção      |
| `npm run serve` | `browser-sync start --config`  | Servidor local com clean URLs e live reload      |
