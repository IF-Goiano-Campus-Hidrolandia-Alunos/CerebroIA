---
tags: [video, python, ffmpeg, pillow, opencv, automacao, plantiumai, referencia]
updated: 2026-06-24
---

# Estúdio de vídeo em Python — modelo de referência

Pipeline de edição de vídeo **dirigido por agente**, local e determinístico. Código em
`scripts/video_studio.py` (+ `scripts/video_editor.py` p/ cortes de silêncio,
`videos/make_gemini_edit.py` p/ o pipeline lean). Doc operacional completa: `videos/README.md`.

## Princípio (economia de tokens)

- **Mídia é trabalho determinístico → 100% local** via **FFmpeg 7 + Pillow + OpenCV** (zero tokens).
- O LLM só **decide o quê** (cortes, textos, posições, cores); **nunca move bytes**.
- As decisões vivem em **JSON ("recipe")**. Reeditar = mudar o JSON e re-rodar (sem reler o vídeo).
- Único custo de token: inspecionar quadros (Read em PNGs do `_work/`), e é pontual.

## CLI (`python scripts/video_studio.py <cmd>`)

| Comando | Faz |
|---|---|
| `render <recipe.json>` | pipeline completo (remove marca + overlay animado em sequência PNG + export) |
| `renderlean <recipe.json>` | pipeline LEAN estilo Gemini (~9–12 s, 1 passada ffmpeg) |
| `overlay <spec.json> <out.png>` | gera só o card/lower-third (PNG RGBA) |
| `probe <video>` | metadados |

Deps: `Pillow`, `numpy`, `opencv-python-headless` (`videos/requirements.txt`) + **ffmpeg/ffprobe 7.x no PATH**.

## Schema do `recipe_*.json`

```jsonc
{
  "input": "videos para editar/SEU.mp4",      // entrada (pasta NÃO versionada)
  "fps": 24,
  "watermark": {                               // remoção de marca d'água
    "method": "unblend",                       // unblend | inpaint | patch
    "type": "star4", "center": [x, y],          // unblend: des-mistura marca semi-transp.
    "outer": 44, "inner": 15, "dilate": 6,      //   preservando TEXTO por baixo
    "amax": 0.85, "strength": 1.2, "dark_t": 8.0, "clean_residual": true, "lo": 22, "hi": 55
  },
  "watermark_tmp": "_work/_clean.mp4",         // scratch
  "logo": {                                    // sobrepõe o badge no lugar da marca
    "file": "assets/logo_badge_circular.png",
    "center": [x, y], "diam": 108, "opacity": 0.92, "start": 0.5, "end": 7.2, "fade": 0.4
  },
  "outputs": [                                 // múltiplos perfis de export
    { "file": "videos editados/SEU_youtube.mp4", "audio": true,  "logo": true,  "crf": 18, "preset": "slow", "abr": "192k" },
    { "file": "videos editados/SEU_site_mudo.mp4", "audio": false, "logo": false, "crf": 20, "preset": "slow" }
  ]
}
```

**Marca d'água — 3 métodos:** `unblend` (des-mistura α; **preserva texto** — use quando cobre legenda) ·
`inpaint` (OpenCV TELEA, reconstrói fundo; borra texto) · `patch` (remendo de folha nativo ffmpeg, rápido).
Evite `delogo` (deixa fantasma em marcas semi-transparentes).

## Schema de `captions_*.json` / `intro_*.json` (cards)

```jsonc
{ "width":1280, "height":720, "radius":14, "card_fill":[16,20,27,255],
  "cards": [
    { "box":[x,y,w,h], "tag":"Sensor", "accent":[80,210,140],
      "title":"...", "desc":"...", "title_size":18, "desc_size":14 }
  ] }
```
Design do card: painel escuro + barra de acento à esquerda + tag em caixa-alta + título + descrição.

## Backends de referência (metodologia)
- **browser-use/video-use** — agente edita por linguagem natural lendo transcrição/timeline (não frames crus). Nosso `video_studio.py` implementa esse padrão local.
- **heygen/hyperframes** — HTML/CSS/JS → MP4 com alfa (headless Chrome + GSAP) p/ motion graphics ricos. Backend **opcional**; hoje fade simples do ffmpeg basta.

## Template
Recipe-modelo para copiar: `videos/recipe_TEMPLATE.json`.

## Links
- [[gsap-scroll-video-scrub-keyframes]] — preparar MP4 p/ scroll-scrub (keyframes densos)
- [[gsap-scrolltrigger-pin-sticky-overflow]] — embutir o vídeo na landing
- [[plantiumai-features-pos-login]]
