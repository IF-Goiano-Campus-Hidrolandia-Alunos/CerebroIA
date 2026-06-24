---
name: "motion-image-broll-overlay"
description: "Desenvolvimento de motion graphics e animações de overlay contendo image broll overlay usando HTML/CSS/JS e HyperFrames."
---

# Skill de Edição: MOTION: Image Broll Overlay

## Descrição Operacional
Esta skill define as diretrizes para aplicar o conceito de **MOTION: Image Broll Overlay** em fluxos de trabalho do BlackHole-Agent integrados com **Video-Use** (edição por transcrição/cortes) e **HyperFrames** (render de animações baseadas em HTML).

## Diretrizes de Execução
1. Projete o layout visual em HTML/CSS utilizando a biblioteca HyperFrames.
2. Crie a animação interativa para image broll overlay utilizando GSAP ou CSS keyframes.
3. Renderize o clipe MP4 com canal alfa e sobreponha ao vídeo bruto via Video-Use.

## Notas Técnicas
- Mantenha as animações leves para garantir o processamento rápido do headless Chrome.
- Sempre utilize 'requestAnimationFrame' ou o ticker do GSAP para garantir taxa de quadros (FPS) constante.
