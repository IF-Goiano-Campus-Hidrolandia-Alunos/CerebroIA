---
name: Scroll Trigger Setup
description: Habilidade tecnica para setup utilizando scroll trigger com foco em animacao estrategica e intencional.
---

# Scroll Trigger - Setup

Esta skill descreve as diretrizes praticas e operacionais para a execucao de setup usando scroll-trigger.

## Diretrizes de Execucao

1. **Restricao e Proposito**: Nao crie animacoes em excesso. Use scroll-trigger de forma pontual para resolver necessidades especificas de comunicacao, engajamento ou guia visual.
2. **Coesao**: Alinhe o setup de scroll-trigger com o design system global, respeitando curvas de duracao coesas.
3. **Performance**: Implemente setup garantindo que a renderizacao ocorra por hardware (GPU) e respeite a acessibilidade de movimento.
4. **Otimizacao**: Evite redesenhos desnecessarios no DOM (evitar Reflows e Repaints repetitivos).

## Como Aplicar
- Setup: Inicie configuracoes limpas no monorepo.
- Debugging: Inspecione com ferramentas de perfil de frames do navegador.
- Integration: Combine de forma fluida com componentes reativos.
