---
name: "cut-bad-takes"
description: "Remoção automática de tentativas anteriores com erros e filtragem de takes redundantes baseado em semelhança semântica de transcrição."
---

# Skill de Edição: Eliminação de Takes Duplicados

## Descrição Operacional
Esta skill define as diretrizes para aplicar o conceito de **Eliminação de Takes Duplicados** em fluxos de trabalho do BlackHole-Agent integrados com **Video-Use** (edição por transcrição/cortes) e **HyperFrames** (render de animações baseadas em HTML).

## Diretrizes de Execução
1. Analise o script de transcrição em busca de frases que se repetem consecutivamente.
2. Mantenha apenas o último take de cada sequência repetida, pois costuma ser a versão definitiva aprovada.
3. Descarte os takes anteriores e verifique a integridade do sentido antes de consolidar.

## Notas Técnicas
- Video-Use pode automatizar isso detectando alta similaridade entre blocos de texto sequenciais.
- Sempre verifique se o último take não possui interrupções abruptas ou falhas técnicas.
