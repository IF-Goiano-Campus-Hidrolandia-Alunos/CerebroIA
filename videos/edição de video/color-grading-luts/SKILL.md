---
name: "color-grading-luts"
description: "Ajuste de perfil de cores cinematográficas e correção cromática automática usando filtros de LUT via Video-Use/FFmpeg."
---

# Skill de Edição: Aplicação de LUTs de Cores

## Descrição Operacional
Esta skill define as diretrizes para aplicar o conceito de **Aplicação de LUTs de Cores** em fluxos de trabalho do BlackHole-Agent integrados com **Video-Use** (edição por transcrição/cortes) e **HyperFrames** (render de animações baseadas em HTML).

## Diretrizes de Execução
1. Identifique o perfil de cores da gravação bruta (Log, Rec709, etc.).
2. Selecione e aplique um arquivo .cube de LUT apropriado para o estilo desejado (ex: Warm, Teal & Orange, Moody).
3. Ajuste a intensidade do filtro para garantir tons de pele realistas e pretos profundos mas não esmagados.

## Notas Técnicas
- FFmpeg pode ser acionado por scripts do Video-Use usando o filtro 'lut3d'.
- Sempre verifique a fidelidade dos tons de pele ('skin tones') usando vetorscópio ou histograma se disponíveis.
