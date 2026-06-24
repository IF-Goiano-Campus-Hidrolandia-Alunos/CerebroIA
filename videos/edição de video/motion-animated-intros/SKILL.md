---
name: "motion-animated-intros"
description: "Geração automática de aberturas de vídeo com títulos animados e transições visuais dinâmicas usando HTML/CSS/JS no HyperFrames."
---

# Skill de Edição: Intros Animadas com HyperFrames

## Descrição Operacional
Esta skill define as diretrizes para aplicar o conceito de **Intros Animadas com HyperFrames** em fluxos de trabalho do BlackHole-Agent integrados com **Video-Use** (edição por transcrição/cortes) e **HyperFrames** (render de animações baseadas em HTML).

## Diretrizes de Execução
1. Defina o título e a identidade visual da intro baseado no tema do vídeo.
2. Escreva animações em CSS/JS utilizando bibliotecas como GSAP para movimentar o logotipo e títulos.
3. Renderize o arquivo MP4 correspondente usando o motor headless Chrome do HyperFrames.

## Notas Técnicas
- Otimize o carregamento de fontes e recursos estáticos locais na intro para evitar frames piscando em branco (flash of unstyled text).
- Adicione uma música de impacto na intro ajustando os níveis de decibéis para não sobressair ao áudio principal.
