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

## Auditoria de Mouse e UX (2026-06-15)

- **Bug do Mouse Warping:** Exceção `IllegalComponentStateException` em `getLocationOnScreen()` causada por teleportes do Robot AWT em canvas off-screen sob JavaFX. Corrigido adicionando a cláusula `isShowing()`, suspendendo o warp com segurança sob JavaFX.
- **Loop de Seleção Infinita & Arrastes Presos:** JavaFX context menus consumiam eventos `MOUSE_RELEASED`, deixando a ferramenta de arraste (`currentDragMode = CENTER`) ativa em AWT. A mudança de seleção em seguida aplicava as coordenadas antigas ao novo objeto, gerando saltos de posição, sobreposição física e loops rápidos de colisão/seleção. Corrigido com o método `game.cancelDrag()` ao abrir menus contextuais e mudar a seleção, e com a flag reentrante `suppressSelectionEvents` em `IgnisEditorApp.java`.
- **Separação de Botões do Mouse:** Configurado clique esquerdo simples (`PRIMARY`) estritamente para seleção de objetos de cena. Menus de contexto (HUDs) abertos exclusivamente no clique direito (`SECONDARY`) na Hierarchy, Viewport e Assets.
- **Abertura de Scripts via Assets:** Integração da árvore de assets com o editor interno `FxCodeEditor`. Clique duplo esquerdo em arquivos `.java` ou opção "Abrir no Editor do Ignis" no menu de contexto abre o script nativamente.

## Melhorias

- AssetResolver.loadImage: cache de sprites compartilhado, invalidação por mtime (recarrega em edição externa); centralizou 7 loadSprite idênticos

## Verificado sem ação

- Serialização de cena robusta (formatos legados ok)
- Catches "silenciosos" benignos (input inválido, save best-effort)

## Links

- [[concepts/ignisengine-builder]]
- [[concepts/ignisengine-animation]]
