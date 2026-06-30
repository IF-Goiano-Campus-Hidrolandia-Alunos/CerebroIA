---
name: Canvas Rendering Security
description: Habilidade tecnica para security utilizando canvas rendering com foco em animacao estrategica e intencional.
---

# Canvas Rendering - Security

Esta skill descreve as diretrizes praticas e operacionais para a execucao de security usando canvas-rendering.

## Diretrizes de Execucao

1. **Restricao e Proposito**: Nao crie animacoes em excesso. Use canvas-rendering de forma pontual para resolver necessidades especificas de comunicacao, engajamento ou guia visual.
2. **Coesao**: Alinhe o setup de canvas-rendering com o design system global, respeitando curvas de duracao coesas.
3. **Performance**: Implemente security garantindo que a renderizacao ocorra por hardware (GPU) e respeite a acessibilidade de movimento.
4. **Otimizacao**: Evite redesenhos desnecessarios no DOM (evitar Reflows e Repaints repetitivos).

## Como Aplicar
- Setup: Inicie configuracoes limpas no monorepo.
- Debugging: Inspecione com ferramentas de perfil de frames do navegador.
- Integration: Combine de forma fluida com componentes reativos.
