---
name: "audio-bg-music-sync"
description: "Mixagem inteligente de música instrumental de fundo, aplicando atenuação automática (ducking) quando a voz do locutor estiver ativa."
---

# Skill de Edição: Sincronização de Trilha Sonora de Fundo

## Descrição Operacional
Esta skill define as diretrizes para aplicar o conceito de **Sincronização de Trilha Sonora de Fundo** em fluxos de trabalho do BlackHole-Agent integrados com **Video-Use** (edição por transcrição/cortes) e **HyperFrames** (render de animações baseadas em HTML).

## Diretrizes de Execução
1. Escolha uma trilha sonora livre de direitos autorais que combine com a energia do conteúdo.
2. Configure o Video-Use/FFmpeg para aplicar o filtro de sidechain/ducking (ex: filter_complex 'sidechaincompress').
3. Defina os volumes: trilha a -24dB enquanto fala e -12dB em pausas ou introduções.

## Notas Técnicas
- O compressor de áudio reativo reduz instantaneamente o volume da música sempre que detecta áudio no canal da voz humana.
- Adicione fade-in de 1.5s no início e fade-out de 3s no final da música.
