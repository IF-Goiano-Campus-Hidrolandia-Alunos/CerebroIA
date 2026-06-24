---
name: "motion-lower-thirds"
description: "Criação de terços inferiores animados com nome e cargo do palestrante renderizados de forma determinística via HyperFrames (HTML/CSS/GSAP)."
---

# Skill de Edição: Lower Thirds Animados com HyperFrames

## Descrição Operacional
Esta skill define as diretrizes para aplicar o conceito de **Lower Thirds Animados com HyperFrames** em fluxos de trabalho do BlackHole-Agent integrados com **Video-Use** (edição por transcrição/cortes) e **HyperFrames** (render de animações baseadas em HTML).

## Diretrizes de Execução
1. Crie uma estrutura HTML simples contendo o nome e cargo com fontes profissionais (ex: Inter/Sora).
2. Use GSAP para animar a entrada (ex: slide-in + fade-in) e saída (slide-out + fade-out).
3. Renderize a animação com HyperFrames gerando um vídeo com canal alpha (RGBA) ou use overlay cromakey verde.

## Notas Técnicas
- Use 'transparency: true' na configuração de renderização do HyperFrames ou um background '#00ff00' sólido para chroma key.
- Sincronize a duração do vídeo renderizado no HyperFrames com a fala do palestrante no Video-Use.
