---
name: "audio-fade-in-out"
description: "Processamento e tratamento técnico de áudio para a funcionalidade de fade in out em vídeos digitais utilizando Video-Use."
---

# Skill de Edição: AUDIO: Fade In Out

## Descrição Operacional
Esta skill define as diretrizes para aplicar o conceito de **AUDIO: Fade In Out** em fluxos de trabalho do BlackHole-Agent integrados com **Video-Use** (edição por transcrição/cortes) e **HyperFrames** (render de animações baseadas em HTML).

## Diretrizes de Execução
1. Extraia o canal de áudio principal usando a infraestrutura do Video-Use.
2. Configure os filtros dinâmicos de áudio no FFmpeg para aplicar fade in out.
3. Exporte a trilha tratada e misture novamente ao vídeo, verificando a sincronia labial.

## Notas Técnicas
- A manipulação de áudio via script no Video-Use é mais eficiente que reprocessar o vídeo inteiro.
- Monitore os níveis de pico (peak levels) para não ultrapassar -1dB e evitar distorção digital.
