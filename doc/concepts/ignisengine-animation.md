---
tags: [ignisengine, animation, architecture, decision]
updated: 2026-06-12
---

## Definição

Sistema de animação 2D do IgnisEngine: módulo desacoplado `com.ignis.animation` com modelo puro (sem Swing nem dependência do core) e Animator runtime.

## Contexto

Item 4 do roadmap, tier 2D implementado em 2026-06-12. Doc: `IgnisEngine/doc/ANIMATION_GUIDE.md`.

## Detalhes

- Modelo: AnimationFrame (sprite relativo + duração s), SpriteAnimation (timeline + loop; spritePathAt(t)), Animator (anima e expõe frame atual)
- Desacoplamento: Animator NUNCA importa GameObject; expõe getCurrentSpritePath(), GameObject aplica via tickAnimator(dt)
- Passo fixo 1/60 s por tick (loop do jogo a 60 ticks/s)
- Frames resolvem via AssetResolver.loadImage (cache compartilhado por mtime); caminhos relativos ao projeto (portável/Git)
- Restauração: ao parar simulação, Animator.reset() e sprite pré-animação é restaurado (preserva estado do editor)
- Blend: play(nome, waitForCurrent=true) enfileira próxima animação até a atual (não-loop) terminar
- Persistência: por entidade na cena (campo "animator", aditivo/retrocompatível) + assets/animations/*.anim.json (AnimationIO)
- Editor: Tools > Animation Editor (Ctrl+Shift+A) — timeline, FPS, preview, save, assign ao objeto selecionado
- 3D (skeletal/blend trees/state machine): planejado; modelo desenhado para receber sem reescrever integração

## Validação

- Testes: progressão de frames, loop wrap, hold em não-loop, round-trip JSON e round-trip de cena (com/sem animador)
- Regressão: Game 01 (sem animador) roda e fecha limpo

## Links

- [[concepts/ignisengine-roadmap]]
- [[concepts/ignisengine-image-editor]]
