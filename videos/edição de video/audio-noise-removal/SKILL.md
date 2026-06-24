---
name: "audio-noise-removal"
description: "Tratamento automatizado de áudio para eliminação de zumbidos, ruídos de ar-condicionado e cliques na fala."
---

# Skill de Edição: Remoção de Ruído de Fundo de Áudio

## Descrição Operacional
Esta skill define as diretrizes para aplicar o conceito de **Remoção de Ruído de Fundo de Áudio** em fluxos de trabalho do BlackHole-Agent integrados com **Video-Use** (edição por transcrição/cortes) e **HyperFrames** (render de animações baseadas em HTML).

## Diretrizes de Execução
1. Extraia a faixa de áudio utilizando o Video-Use.
2. Aplique filtros de áudio (como afftdn ou anlmd do FFmpeg) para mitigar o ruído estático de fundo.
3. Ajuste o ganho final da voz para compensar eventuais atenuações causadas pelo de-noiser.

## Notas Técnicas
- Evite aplicar de-noise agressivo que distorça os agudos da voz humana, deixando-a com som 'metálico' ou subaquático.
- Use compressores de áudio dinâmicos para equilibrar falas sussurradas e gritos.
