---
name: "motion-animated-captions"
description: "Criação de legendas ultra dinâmicas com realce palavra por palavra (efeito karaoke) usando CSS e animações GSAP no HyperFrames."
---

# Skill de Edição: Legendas Animadas (Estilo Shorts/TikTok)

## Descrição Operacional
Esta skill define as diretrizes para aplicar o conceito de **Legendas Animadas (Estilo Shorts/TikTok)** em fluxos de trabalho do BlackHole-Agent integrados com **Video-Use** (edição por transcrição/cortes) e **HyperFrames** (render de animações baseadas em HTML).

## Diretrizes de Execução
1. Converta o arquivo de legenda do Video-Use (.srt ou JSON de timestamps) em spans HTML com classes dinâmicas.
2. Aplique estilizações modernas: texto centralizado, borda preta grossa (text-shadow) e fonte de impacto (ex: Montserrat/Impact).
3. Crie animações GSAP de escala (pop) e mudança de cor para destacar a palavra ativa no momento exato da fala.

## Notas Técnicas
- HyperFrames garante que a sincronização palavra por palavra seja idêntica frame a frame, pois roda baseado em timestamps virtuais.
- Mantenha a legenda no terço médio-inferior para não sobrepor rostos ou informações críticas.
