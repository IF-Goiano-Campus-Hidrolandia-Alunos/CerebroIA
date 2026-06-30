---
name: Gesture Navigation Debugging
description: Habilidade tecnica para debugging utilizando gesture navigation com foco em animacao estrategica e intencional.
---

# Gesture Navigation - Debugging

Esta skill descreve as diretrizes praticas e operacionais para a execucao de debugging usando gesture-navigation.

## Diretrizes de Execucao

1. **Restricao e Proposito**: Nao crie animacoes em excesso. Use gesture-navigation de forma pontual para resolver necessidades especificas de comunicacao, engajamento ou guia visual.
2. **Coesao**: Alinhe o setup de gesture-navigation com o design system global, respeitando curvas de duracao coesas.
3. **Performance**: Implemente debugging garantindo que a renderizacao ocorra por hardware (GPU) e respeite a acessibilidade de movimento.
4. **Otimizacao**: Evite redesenhos desnecessarios no DOM (evitar Reflows e Repaints repetitivos).

## Como Aplicar
- Setup: Inicie configuracoes limpas no monorepo.
- Debugging: Inspecione com ferramentas de perfil de frames do navegador.
- Integration: Combine de forma fluida com componentes reativos.
