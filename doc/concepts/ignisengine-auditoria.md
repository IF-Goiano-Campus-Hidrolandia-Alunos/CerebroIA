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
- Viewport/Game Loop (Morte da Thread): `createBufferStrategy(3)` e `getDrawGraphics()` lançavam exceções em estado não-displayable, matando a thread de loop no startup. Corrigido com `isDisplayable()` e try-catch, protegendo a thread `run()` de forma resiliente contra qualquer erro.
- Play Mode / Concorrência: Conflito de acesso à lista `entities` entre a thread do loop e a EDT (Swing) causava exceções de concorrência. Modificado `entities`, `cameras` e `runtimeObjects` para `CopyOnWriteArrayList`.
- Seleção de Objetos: `setSelectedObject` não disparava redesenho, mantendo gizmos anteriores travados ou invisíveis. Adicionado `repaint()` na seleção.
- Script Serialization: Modificar variáveis do script no Inspector resetava para o padrão de código ao dar Play. Corrigido com salvamento em `pendingScriptVariables` a cada modificação nos editores (Boolean, GameObject, Text) e suporte a confirmação com tecla ENTER com devolução de foco para o canvas do jogo.

## Melhorias

- AssetResolver.loadImage: cache de sprites compartilhado, invalidação por mtime (recarrega em edição externa); centralizou 7 loadSprite idênticos

## Verificado sem ação

- Serialização de cena robusta (formatos legados ok)
- Catches "silenciosos" benignos (input inválido, save best-effort)

## Links

- [[concepts/ignisengine-builder]]
- [[concepts/ignisengine-animation]]
