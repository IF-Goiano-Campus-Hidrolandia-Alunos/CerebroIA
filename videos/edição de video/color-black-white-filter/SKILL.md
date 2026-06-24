---
name: "color-black-white-filter"
description: "Tratamento de cor e estética de imagem aplicando correção de black white filter via FFmpeg no Video-Use."
---

# Skill de Edição: COLOR: Black White Filter

## Descrição Operacional
Esta skill define as diretrizes para aplicar o conceito de **COLOR: Black White Filter** em fluxos de trabalho do BlackHole-Agent integrados com **Video-Use** (edição por transcrição/cortes) e **HyperFrames** (render de animações baseadas em HTML).

## Diretrizes de Execução
1. Avalie a imagem bruta para identificar necessidades de ajuste de black white filter.
2. Configure as propriedades de vídeo do filtro FFmpeg de cores no script de edição.
3. Aplique e faça o render de teste de um frame para comparar antes e depois.

## Notas Técnicas
- Use filtros de vídeo nativos do FFmpeg como 'eq', 'curves' ou 'hue' para ajustes sem perdas secundárias.
- Cuidado com excesso de saturação em tons vermelhos e amarelos que afetam tons de pele.
