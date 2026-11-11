# Roteiro Passo a Passo: Lançamento do `guiadoadestrador.com.br`

Este guia contém a sequência exata de tarefas para você organizar as mídias, ajustar o projeto na sua máquina e colocar o novo domínio virgem no ar via Vercel.

---

## 📌 ETAPA 1: Organizar e Baixar as Imagens (No seu Notebook)

Você já fez o principal: transferiu as fotos da **Maraca** e converteu para `.webp`. Agora falta concluir a preparação das mídias:

### 1.1. Baixar as Imagens dos Produtos
* Baixe as imagens oficiais dos produtos/brinquedos que você analisa nos artigos (ex: Kong, guias, peitorais).
* Converta essas imagens de produto para `.webp` (pode usar o mesmo conversor online ou ferramenta que usou para as fotos da Maraca).

### 1.2. Padronizar a Nomenclatura dos Arquivos
Renomeie todos os arquivos com letras minúsculas, usando hífen e nomes descritivos com palavras-chave de SEO:

* **Fotos da Maraca:**
  * `maraca-pitbull-treino-obediencia.webp`
  * `maraca-filhote-passeio-coleira.webp`
  * `philipe-e-maraca-adestramento.webp` (para o "Sobre o Autor")
* **Imagens de Produtos:**
  * `brinquedo-kong-classic-vermelho.webp`
  * `guia-unificada-adestramento-caes.webp`

---

## 📌 ETAPA 2: Adicionar as Imagens no Código (IDE / Cursor / VSCode)

### 2.1. Mover os arquivos para a pasta do projeto
Copie todas as imagens em `.webp` para dentro do diretório de ativos estáticos da sua aplicação:
```text
seu-projeto/
└── public/
    └── assets/
        └── images/
            ├── maraca-pitbull-treino-obediencia.webp
            ├── brinquedo-kong-classic-vermelho.webp
            └── ...
```

### 2.2. Inserir as tags `<img>` nos artigos HTML/JSX
Em cada página de artigo ou review, insira o código HTML otimizado para SEO e velocidade:

```html
<!-- Exemplo de foto real da Maraca no artigo -->
<img 
  src="/assets/images/maraca-pitbull-treino-obediencia.webp" 
  alt="Cadela Maraca realizando treino de obediência e comando senta" 
  width="800" 
  height="533" 
  loading="lazy" 
  class="rounded-xl shadow-md my-6 w-full object-cover"
/>
```

---

## 📌 ETAPA 3: Alterar a Marca no Código

Abra a ferramenta de substituição global na sua IDE (Ctrl + Shift + F ou Cmd + Shift + F) e atualize os textos do site antigo para a nova marca:

1. **Substituir o Nome da Marca:**
   * De: `Guia do Adestramento`
   * Para: `Guia do Adestrador`
2. **Atualizar a URL Base nos Metadados:**
   * URL canônica: `https://www.guiadoadestrador.com.br`
3. **Verificar os elementos de SEO:**
   * `title`
   * `meta description`
   * `canonical URL`
   * Tags de Open Graph (`og:url`, `og:site_name`, `og:title`)

---

## 📌 ETAPA 4: Registrar o Novo Domínio no Registro.br

1. Acesse **[registro.br](https://registro.br)**.
2. Pesquise por `guiadoadestrador.com.br`.
3. Conclua o registro (R$ 40,00 por 1 ano).
4. Deixe a tela do Registro.br aberta para configurar o DNS no próximo passo.

---

## 📌 ETAPA 5: Deploy do Código e Conexão na Vercel

### 5.1. Subir o Código Atualizado (Git Push)
No terminal da sua IDE, faça o push das alterações:
```bash
git add .
git commit -m "feat: atualiza marca para Guia do Adestrador e adiciona imagens em webp"
git push origin main
```

### 5.2. Conectar o Novo Domínio na Vercel
1. Acesse o painel da **Vercel** no seu projeto existente.
2. Vá em **Settings** > **Domains**.
3. Digite `guiadoadestrador.com.br` e clique em **Add**.
4. A Vercel exibirá as instruções de DNS (Servidores de Nome / NS ou Apontamento A / CNAME).
5. Vá no **Registro.br**, abra o painel do seu domínio `guiadoadestrador.com.br`, clique em **Alterar DNS** e insira os servidores indicados pela Vercel.
6. Na Vercel, defina `guiadoadestrador.com.br` como o **Primary Domain**.

---

## 📌 ETAPA 6: Pós-Lançamento e Reindexação

1. **Testar o Site no Ar:** Acesse `https://www.guiadoadestrador.com.br` e confira se todas as imagens carregam rápido e sem erros 404.
2. **Google Search Console (GSC):**
   * Crie uma nova propriedade no Search Console para `https://www.guiadoadestrador.com.br`.
   * Envie o seu sitemap (ex: `https://www.guiadoadestrador.com.br/sitemap.xml`).
   * Solicite a indexação manual da página inicial e dos artigos principais.