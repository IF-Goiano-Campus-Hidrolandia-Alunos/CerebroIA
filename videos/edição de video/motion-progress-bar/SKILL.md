---
name: "motion-progress-bar"
description: "Criação de uma barra horizontal ou circular na tela que avança conforme a duração do vídeo, gerada via HyperFrames."
---

# Skill de Edição: Barra de Progresso Animada

## Descrição Operacional
Esta skill define as diretrizes para aplicar o conceito de **Barra de Progresso Animada** em fluxos de trabalho do BlackHole-Agent integrados com **Video-Use** (edição por transcrição/cortes) e **HyperFrames** (render de animações baseadas em HTML).

## Diretrizes de Execução
1. Crie uma div HTML com largura de 0% a 100% que avança ao longo da linha do tempo.
2. Utilize animações CSS de transição linear mapeadas com a duração total do clipe.
3. Renderize a barra como um overlay transparente na parte superior ou inferior da tela.

## Notas Técnicas
- HyperFrames facilita a renderização disso aplicando a propriedade CSS 'animation-play-state' proporcional ao frame atual.
- Mantenha a barra fina e sutil (2px a 4px de altura) para evitar distrações visuais excessivas.
