---
tags: [ignisengine, audit, bugfix, performance]
updated: 2026-06-16
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

## Correções de Bugs e Performance — Editor FX (2026-06-16)

Rodada Gemini (commit `39b5367`) + complemento Claude (commit `e9a9fd5`), repo `URSoftware/IgnisEngine`. Relatório no projeto: `doc/CORRECOES_BUGS_FX_2026-06-16.md`.

- **Loop de seleção infinita (trocar de objeto sozinho):** o `addSelectionListener` despachava via `Platform.runLater`; lambdas enfileiradas rodavam com `selected` desatualizado, gerando ping-pong entre objetos sobrepostos. Corrigido com guarda `if (game.getSelectedObject() == go && selected != go)` — notificações obsoletas são descartadas. Reforçado por `handleMouseRelease` deixar de chamar `notifySelectionListeners()` redundantemente (o Inspector FX já sincroniza via AnimationTimer).
- **Arrastes presos de gizmo / saltos de coordenadas:** o `currentDragMode` ficava preso em `CENTER` ao dispensar o menu de contexto. Corrigido com `viewportMenu.setOnHidden(e -> game.cancelDrag())`.
- **Ordenação da Cena invertida:** "Mover para o topo/fundo" agiam ao contrário (render desenha índice 0 ao fundo, N no topo). Invertidos os parâmetros em `buildSceneMenu`/`buildHierarchyContextMenu` (topo→`Integer.MAX_VALUE`, fundo→`0`).
- **"Mover para cima" era no-op:** `Game.moveEntityToIndex` decrementava `newIndex` quando `> currentIndex`, anulando o movimento. Removido o `newIndex--` (o clamp pós-remoção já garante o intervalo válido).
- **Clique direito não selecionava o item sob o cursor (Hierarchy e Assets):** o `TreeView` do JavaFX só seleciona no clique esquerdo, então o menu de contexto operava na seleção anterior. Corrigido com `cellFactory` que seleciona a célula no `SECONDARY` press — na Hierarchy (Gemini) e no Asset Browser (Claude, `e9a9fd5`).
- **Travadas/uso de CPU (repaints AWT):** o `Game extends Canvas` disparava `repaint()` (pipeline AWT/BufferStrategy) inútil sob o editor FX (que renderiza por `AnimationTimer`/`renderWorldTo`). Adicionada flag `suppressAwtRepaint` + `setSuppressAwtRepaint`; o `repaint()` é ignorado e a flag é ligada no `IgnisEditorApp`.

## Melhorias

- AssetResolver.loadImage: cache de sprites compartilhado, invalidação por mtime (recarrega em edição externa); centralizou 7 loadSprite idênticos

## Verificado sem ação

- Serialização de cena robusta (formatos legados ok)
- Catches "silenciosos" benignos (input inválido, save best-effort)

## Links

- [[10_projects/Colaborador1/ignisengine/03_context/ignisengine-builder]]
- [[10_projects/Colaborador1/ignisengine/03_context/ignisengine-animation]]
