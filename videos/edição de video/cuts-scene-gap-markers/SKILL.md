---
name: "cuts-scene-gap-markers"
description: "Técnica de edição de cortes estruturais focada em scene gap markers para dinamizar o ritmo do vídeo final."
---

# Skill de Edição: CUTS: Scene Gap Markers

## Descrição Operacional
Esta skill define as diretrizes para aplicar o conceito de **CUTS: Scene Gap Markers** em fluxos de trabalho do BlackHole-Agent integrados com **Video-Use** (edição por transcrição/cortes) e **HyperFrames** (render de animações baseadas em HTML).

## Diretrizes de Execução
1. Analise os timestamps de vídeo e áudio gerados pelo Video-Use.
2. Identifique os pontos exatos para iniciar e terminar o corte de scene gap markers.
3. Execute o corte e aplique transições adequadas para manter a continuidade narrativa.

## Notas Técnicas
- Ajuste os parâmetros de precisão de frames (seek preciso com '-ss' antes do '-i' no FFmpeg).
- Verifique se a troca de cenas não interrompe a fala no meio de uma sílaba.
