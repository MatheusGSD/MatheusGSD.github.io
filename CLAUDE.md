# dalmolin.dev — notas para o agente

Site pessoal de Matheus Dalmolin (projetos, textos, sobre; currículo e hobbies virão depois). Só em português por enquanto
(decisão de 06/11: sem página em inglês). O usuário escreve em português; responda em português. Plano e decisões (06/11/2026) na memória `site-pessoal-dalmolin-dev`.

## Como funciona
- Astro 7, estático. `npm run build` → `dist/`; publicação pelo GitHub Actions (`.github/workflows/deploy.yml`) no repo
  `MatheusGSD/MatheusGSD.github.io`, com domínio `dalmolin.dev` (`public/CNAME`).
- Visual = variante C do protótipo (coluna fixa à esquerda + fluxo de tudo o que foi publicado). Tokens e fontes do artigo
  da apuração (Archivo, Source Sans 3, IBM Plex Mono, via @fontsource); acento verde-azulado #0f8a7e. Claro/escuro pelo sistema.
- Conteúdo: um arquivo por item em `src/content/projetos/` e `src/content/textos/` (esquema em `src/content.config.ts`).
  Print de projeto: `public/img/projetos/<print>-claro.webp` e `-escuro.webp` (960×600).
- Textos com `url` são HTML pronto, gerado no repo do projeto. O artigo da apuração vem de `C:\dev\apuracao\site\gerar_artigo.py`,
  que grava `public/textos/swing-simples-segundo-turno/` (index.html + artigo_og.png). Não editar esse HTML à mão.
  Textos sem `url` são Markdown e viram `/textos/<slug>/`.
- Os filtros Tudo/Projetos/Textos são páginas (`/`, `/projetos/`, `/textos/`), sem JavaScript.
- Projetos publicados no GitHub Pages sem domínio próprio aparecem sozinhos em `dalmolin.dev/<repo>/` (efeito do site de
  usuário com domínio). Estar no ar não é estar na lista: a lista é `src/content/projetos/`.

## Conferência
`npm run build && python ferramentas/confere.py`: 6 páginas × (1280/390 px, claro/escuro), erros de console, rolagem lateral
e links internos quebrados; capturas em `ferramentas/_capturas/`. `python ferramentas/og.py` refaz `public/og.png`.
`python ferramentas/retrato.py [foto]` refaz `src/retrato.json`, o retrato em ASCII da ficha do Sobre (recorta o fundo
com torch/transformers). A foto de origem fica em `ferramentas/_foto/retrato.png`, fora do git.
A bio (`src/site.ts`) é a do X do usuário, escolhida por ele. Não usar o Lattes (desatualizado, segundo ele).

## Fora do main
`_prototipo_inicio/` (protótipos A/B/C da página inicial) e `_referencias/` (quadros de referências que o usuário rejeitou)
ficam fora do git do main.
