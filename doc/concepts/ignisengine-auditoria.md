---
tags: [ignisengine, audit, bugfix, performance]
updated: 2026-06-12
---

## Definição

Auditoria técnica profunda do IgnisEngine (2026-06-12) com correções definitivas. Relatório: `IgnisEngine/doc/AUDIT_2026-06-12.md`.

## Correções

- Leak de file handle: IgnisSoundEngine.loadClip não fechava AudioInputStream após clip.open() → try/finally fecha streams
- Threads de áudio: pool de 32 non-daemon → ThreadFactory daemon "IgnisAudio", 8 vozes (anti-órfão)
- getInstance() do áudio sincronizado (race na lazy-init)
- Export C++: main.cpp usava SCENE_MAINSCENE fixo → alias canônico SCENE_MAIN (mainScene do projeto, fallback 1ª cena, nullptr se vazio) + dedupe de símbolos
- ScriptManager: sem JDK (JRE/builds), usa classes pré-compiladas em scripts/compiled/ e loga uma vez (sem erro por script)

## Melhorias

- AssetResolver.loadImage: cache de sprites compartilhado, invalidação por mtime (recarrega em edição externa); centralizou 7 loadSprite idênticos

## Verificado sem ação

- Serialização de cena robusta (formatos legados ok)
- Catches "silenciosos" benignos (input inválido, save best-effort)
- Render usa BufferStrategy corretamente

## Links

- [[concepts/ignisengine-builder]]
- [[concepts/ignisengine-animation]]
