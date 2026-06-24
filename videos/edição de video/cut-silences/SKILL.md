---
name: "cut-silences"
description: "Detecção e remoção automática de trechos sem áudio utilizando a ferramenta Video-Use baseado no tempo de silêncio configurável."
---

# Skill de Edição: Corte de Silêncios Autônomo

## Descrição Operacional
Esta skill define as diretrizes para aplicar o conceito de **Corte de Silêncios Autônomo** em fluxos de trabalho do BlackHole-Agent integrados com **Video-Use** (edição por transcrição/cortes) e **HyperFrames** (render de animações baseadas em HTML).

## Diretrizes de Execução
1. Analise o arquivo de áudio ou transcrição gerada pelo Video-Use para encontrar pausas sem fala.
2. Ajuste o limiar de silêncio (geralmente entre -30dB e -45dB) com duração mínima de 0.5s.
3. Execute os cortes e verifique se o fluxo do diálogo soa natural, sem cortar o início ou fim de palavras.

## Notas Técnicas
- Utilize o Video-Use para mapear os trechos de fala e gerar o Edit Decision List (EDL) inicial.
- Evite cortes muito secos que eliminem respirações necessárias; mantenha um 'headroom' de 50ms a 100ms de áudio.
