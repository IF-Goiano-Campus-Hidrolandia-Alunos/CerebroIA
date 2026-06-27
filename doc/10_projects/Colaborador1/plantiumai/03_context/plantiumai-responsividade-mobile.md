---
tags: [plantiumai, web, mobile, responsivo, css, animacao, ux]
updated: 2026-06-26
---

# PlantiumAI — Responsividade mobile e animações da landing

Polimento mobile do `web/` (landing + `/planos`). Commit `fix(web): polir responsividade mobile`
+ `docs(planos)` (push para `PlantiumAI/PlantiumAI` e `ThyagoToledo/PlantiumAI`, jun/2026).

## Causa raiz crítica — CSP bloqueava a hidratação em dev
O `next.config.mjs` tinha `script-src 'self' 'unsafe-inline'` **sem `'unsafe-eval'`**. Em **desenvolvimento**, o webpack do Next avalia módulos via `eval()` (HMR/source maps); a CSP bloqueava o `eval` → **a hidratação do React falhava em dev**: login ficava em branco, `/planos` sem interatividade, animações não rodavam, preview não hidratava e screenshots travavam. Em **produção** o Next não usa `eval`, então a CSP atual funciona — por isso o site no ar estava ok.
**Fix:** liberar `'unsafe-eval'` **só em dev** (`process.env.NODE_ENV !== "production"`), mantendo a CSP restrita em produção. Commit `fix(web): liberar 'unsafe-eval' na CSP em dev`. Sintoma diagnóstico: `input.checked=true` mostrava o menu (CSS puro) mas `button.click()` do React não reagia e `__reactFiber` não existia no DOM.

## Problemas corrigidos
- **Navbar mobile espremida**: as abas centrais viravam um carrossel com scroll horizontal apertado (`scrollWidth` ~344px em ~162px).
- **"Tela preta" no scroll**: a seção de vídeo (`#plf-video-sticky`) tinha `height:100vh` e o `<video>` ficava `paused` sem `poster` → vão preto de tela cheia no celular.
- **Login**: NÃO era bug — renderiza normal a 390px (card visível, tema escuro ok). O screenshot do preview trava por causa do `backdrop-filter`, não por falha de layout.

## Soluções
- **Menu de Abas em Carrossel Horizontal**: Em resolucoes menores de 960px, as abas centrais de navegacao (`.plf-tabs`) nao sao ocultadas ou colocadas sob um menu hamburguer. Em vez disso, elas se organizam em um carrossel horizontal suave (`overflow-x: auto; white-space: nowrap; scrollbar-width: none;`). Isso permite navegacao direta e imediata de qualquer ponto, eliminando a complexidade de menus abertos/fechados.
- **Ocultacao Inteligente de Titulo**: Para economizar espaco horizontal em smartphones (abaixo de 768px), o titulo textual da marca (`.plf-nav-title` - "PlantiumAI") e ocultado, preservando apenas o icone circular e as abas de navegacao centrais.
- **Navbar Unificada e Fixa**: Ambas as paginas (Home Page e `/planos`) compartilham o mesmo layout de Header fixo (`fixed top-[18px] z-40 max-w-[1180px] mx-auto px-6`) com efeito glassmorphism e links reativos apontando para as ancoras da homepage.

- **Vídeo**: `poster="/landing/hero.jpg"` + `background` de fallback no `#plf-video-sticky` (nunca preto) + `height:62vh` em `max-width:760px`.
- **Animações "premium" (scroll-reveal)**: fade-up dos blocos + cascata (`plf-stagger` nos grids `.plf-flow/.plf-pillars/.plf-team`) via `IntersectionObserver`, easing `cubic-bezier(.16,1,.3,1)`. Respeita `prefers-reduced-motion`.

## Performance do vídeo de scrub (carregamento "instantâneo")
O `public/videos/PlantiumAI_site_mudo.mp4` tinha **11MB @ 8.5 Mbps** (720p/10s) → a seção de scrub demorava a aparecer no PC enquanto as outras carregavam. Recomprimido com `ffmpeg` para **2.7MB**: `-an -c:v libx264 -crf 24 -preset slow -g 10 -movflags +faststart -vf scale=1280:720`. O **`+faststart`** (moov atom no início) é crítico — sem ele o navegador baixa o arquivo todo antes de exibir/seekar. `-g 10` = keyframes densos p/ scrub fluido. Poster passou a ser o **1º frame do próprio vídeo** (`videos/video-poster.jpg`, gerado com `ffmpeg -vframes 1`), eliminando o "pulo" hero→vídeo; o fundo de fallback do `#plf-video-sticky` usa a mesma imagem. Original guardado fora do repo (scratchpad). Commit `perf(web): otimizar video do scrub`.

## Regras de robustez (importante)
- Classes que **escondem** conteúdo (`opacity:0` do reveal/stagger) são adicionadas **via JS**, nunca estáticas no markup. Sem JS/hidratação → conteúdo permanece visível (degrada bem).
- Elementos já na viewport recebem `.plf-in` no MESMO tick do `.plf-reveal` → sem flicker (visível→some→volta).

## Arquivos
- `web/src/components/landing.tsx` (navbar, vídeo, JS do reveal)
- `web/src/app/landing.css` (transições, reveal/stagger, vídeo mobile e carrossel de abas)
- `web/src/app/planos/page.tsx` (mesma navbar fixa e unificada com abas e plf-root)
- Docs de negócio na raiz do repo: `tabelaprecos.md`, `lucro_rentavel.md` (3 planos + rentabilidade, base no Trabalho Científico).

## Links
- [[plantiumai-features-pos-login]]
- [[redesenho-pagina-planos]]
- [[narrativa-oficial-plantiumai]]
- [[plantiumai-web-preview-hydration]]
