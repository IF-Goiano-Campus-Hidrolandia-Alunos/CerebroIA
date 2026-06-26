---
name: Micro Interactions Integration
description: Habilidade tecnica para integration utilizando micro interactions com foco em animacao estrategica e intencional.
---

# Micro Interactions - Integration

Esta skill descreve as diretrizes praticas e operacionais para a execucao de integration usando micro-interactions.

## Diretrizes de Execucao

1. **Restricao e Proposito**: Nao crie animacoes em excesso. Use micro-interactions de forma pontual para resolver necessidades especificas de comunicacao, engajamento ou guia visual.
2. **Coesao**: Alinhe o setup de micro-interactions com o design system global, respeitando curvas de duracao coesas.
3. **Performance**: Implemente integration garantindo que a renderizacao ocorra por hardware (GPU) e respeite a acessibilidade de movimento.
4. **Otimizacao**: Evite redesenhos desnecessarios no DOM (evitar Reflows e Repaints repetitivos).

## Como Aplicar
- Setup: Inicie configuracoes limpas no monorepo.
- Debugging: Inspecione com ferramentas de perfil de frames do navegador.
- Integration: Combine de forma fluida com componentes reativos.
