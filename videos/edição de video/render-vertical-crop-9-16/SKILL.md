---
name: "render-vertical-crop-9-16"
description: "Configurações de exportação, codec e otimização de renderização focadas em vertical crop 9 16."
---

# Skill de Edição: RENDER: Vertical Crop 9 16

## Descrição Operacional
Esta skill define as diretrizes para aplicar o conceito de **RENDER: Vertical Crop 9 16** em fluxos de trabalho do BlackHole-Agent integrados com **Video-Use** (edição por transcrição/cortes) e **HyperFrames** (render de animações baseadas em HTML).

## Diretrizes de Execução
1. Defina as configurações de codec e perfil de compressão adequados para vertical crop 9 16.
2. Configure o Video-Use para acionar a biblioteca de render correspondente.
3. Execute o render final e valide o tamanho do arquivo e qualidade visual.

## Notas Técnicas
- Use aceleração de hardware (ex: h264_nvenc ou h264_amf) se disponível na máquina do usuário.
- Garanta que os metadados do vídeo estejam otimizados para streaming na web (faststart).
