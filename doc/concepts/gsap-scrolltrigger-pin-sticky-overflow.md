---
tags: [gsap, scrolltrigger, css, sticky, nextjs, plantiumai, bug]
updated: 2026-06-24
---

## Definição

Numa seção de vídeo controlada por scroll, **não usar `position: sticky` para "prender" o vídeo** se houver ancestral com `overflow` ≠ `visible`. Use o **`pin` do ScrollTrigger** (que usa `position: fixed`, imune ao problema).

## Sintoma (bug real do PlantiumAI)

Num certo ponto da rolagem o vídeo aparecia **cortado no topo** e abaixo um **vão preto** enorme. Assinatura clássica de `position: sticky` quebrado.

## Causa-raiz

- `position: sticky` **para de funcionar** quando **qualquer ancestral** tem `overflow` diferente de `visible` (hidden/auto/scroll), inclusive `overflow-x: hidden`.
- O root da landing (`web/src/components/landing.tsx`) tem `overflow-x: hidden` (p/ conter os "orbs") → matou o sticky do `#plf-video-sticky`.

## Correção (padrão validado GSAP)

- Trocar CSS sticky pelo **pin do ScrollTrigger** no próprio bloco do vídeo:
  `ScrollTrigger.create({ trigger:'#plf-video-sticky', start:'top top', end:'+=250%', pin:true, pinSpacing:true, scrub:1, invalidateOnRefresh:true, onUpdate: self => { video.currentTime = video.duration*self.progress } })`
- `position: fixed` (usado pelo pin) **não é recortado** por `overflow:hidden` de ancestral (só `transform/filter/perspective` criam containing block p/ fixed).
- Chamar **`ScrollTrigger.refresh()`** após `loadedmetadata` e no `window.load` → recalcula posições quando imagens/fontes assentam (evita gaps/medidas defasadas).
- **Mobile/touch**: o seek rápido de `currentTime` trava (iOS bloqueia) → detectar `(max-width:760px),(pointer:coarse)` + `prefers-reduced-motion` e cair p/ **autoplay em loop** (sem pin).
- Cleanup no React: `st.kill()` + remover listeners no return do `useEffect`.

## Links

- [[gsap-scroll-video-scrub-keyframes]] — re-encode all-intra (keyframe por frame) p/ scrub fluido
- [[plantiumai-features-pos-login]]
