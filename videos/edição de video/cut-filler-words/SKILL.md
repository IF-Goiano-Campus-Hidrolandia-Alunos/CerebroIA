---
name: "cut-filler-words"
description: "Identificação e remoção de vícios de linguagem como 'um', 'uh', 'tipo' e hesitações na fala usando a transcrição e Video-Use."
---

# Skill de Edição: Remoção de Palavras de Preenchimento

## Descrição Operacional
Esta skill define as diretrizes para aplicar o conceito de **Remoção de Palavras de Preenchimento** em fluxos de trabalho do BlackHole-Agent integrados com **Video-Use** (edição por transcrição/cortes) e **HyperFrames** (render de animações baseadas em HTML).

## Diretrizes de Execução
1. Gere a transcrição completa do vídeo utilizando o modelo Whisper / ElevenLabs integrado no Video-Use.
2. Localize as palavras de preenchimento (filler words) e seus respectivos timestamps.
3. Remova os trechos equivalentes de vídeo e áudio ajustando a trilha para colar as pontas sem distorção.

## Notas Técnicas
- Em cortes de palavras de preenchimento, aplique transições suaves de áudio para evitar estalos (clicks).
- Se o corte gerar um sobressalto visual (jump cut), adicione um leve zoom digital (ex: 1.1x) no clip seguinte para disfarçar o corte.
