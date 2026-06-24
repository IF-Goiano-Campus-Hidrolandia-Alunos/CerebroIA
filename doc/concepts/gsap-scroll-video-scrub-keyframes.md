---
tags: [gsap, scrolltrigger, video, ffmpeg, performance]
updated: 2026-06-23
---

## Definição

Vídeo controlado por scroll (scrub via `video.currentTime`) só fica fluido se o MP4 tiver keyframe em **todos os frames** — senão o navegador "pula" para o keyframe mais próximo e a imagem quase não muda.

## Contexto

Landing PlantiumAI (`web/src/components/landing.tsx`): seção `#demo-video` com GSAP ScrollTrigger (`scrub`) sincronizando `video.currentTime` com o progresso da rolagem. Gravações de tela vêm com keyframes esparsos (ex.: só em 0s e 7,75s num clipe de 10s) → parece "não animado".

## Detalhes

- Diagnóstico: `ffprobe -select_streams v:0 -skip_frame nokey -show_entries frame=pts_time` lista os keyframes. Poucos = problema.
- Correção (re-encode all-intra + faststart):
  `ffmpeg -y -i in.mp4 -an -c:v libx264 -preset slow -crf 20 -g 1 -keyint_min 1 -sc_threshold 0 -pix_fmt yuv420p -movflags +faststart out.mp4`
- Trade-off: arquivo cresce muito (2,5 MB → 10 MB num 10s/720p), pois todo frame vira keyframe. Aceitável para clipes curtos.
- Browser precisa de `Accept-Ranges: bytes` (seek). `muted` + `playsinline` para autoplay/scrub. Após trocar o arquivo, **hard refresh** (cache do vídeo).
- Acessibilidade: em `prefers-reduced-motion` trocar scrub por loop autoplay em altura normal (sem scroll-jacking).
- Alternativa se ficar pesado: sequência de frames/sprite em vez de vídeo.

## Links

- [[gsap-scrolltrigger-animacoes-scroll]]
- [[design-page-scroll-jacking-snap]]
- [[css-scroll-driven-animations-native]]
