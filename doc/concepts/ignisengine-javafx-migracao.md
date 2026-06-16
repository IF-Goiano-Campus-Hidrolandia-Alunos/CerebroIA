---
tags: [ignisengine, javafx, migracao, ui, decision, architecture]
updated: 2026-06-15
revisao: correcoes de selecao/inspector/picking/indicador-visual + numeros de linha pretos + autosave (2026-06-15)
---

## Definição

Migração incremental da interface do editor IgnisEngine de Swing/AWT para JavaFX 17, mantendo o núcleo de render da engine.

## Contexto

Editor hoje é Swing/AWT: 38 arquivos usam swing/awt, monolito `editor/Editor.java` (~5962 linhas), núcleo `core/Game.java extends java.awt.Canvas` (BufferStrategy + Graphics2D). Plano completo no projeto: `IgnisEngine/doc/JAVAFX_MIGRATION_PLAN.md`.

## Decisões-Chave

- Branches (2026-06-14): `Legado` = versao estavel Swing + marketplace (preservada, nao migra); `main` = desenvolvimento da migracao JavaFX. Cada fase mergeavel; Legado e o ponto de retorno seguro.
- Incremental, não big-bang: Swing e JavaFX convivem durante a transição.
- Interop: `SwingNode` (embutir Swing na cena FX), `JFXPanel` (FX dentro de Swing), `SwingFXUtils` (BufferedImage ↔ WritableImage).
- Ponte de render do Viewport: render offscreen in BufferedImage (mesmo Graphics2D) → `SwingFXUtils.toFXImage` → `javafx.scene.canvas.Canvas` via AnimationTimer. Desacopla loop do jogo da janela; remove BufferStrategy no editor.
- Rejeitado: embutir Canvas AWT pesado direto na cena FX (heavyweight/lightweight quebra foco/render).
- Reescrever pipeline gráfico NÃO faz parte da migração.

## Fases

- F0 (FEITO, so na main): deps JavaFX 17 no pom.xml + javafx-maven-plugin + pacote `com.ignis.editor.fx`. Compila.
- F1 (FEITO, so na main): IgnisEditorApp (BorderPane/MenuBar/SplitPane) + ponte de render `Game.renderWorldTo` -> BufferedImage -> SwingFXUtils -> Canvas (AnimationTimer); Hierarchy nativa (TreeView); Inspector placeholder; cena de amostra. Rodar: `mvnw javafx:run`.
- F2 (FEITO, so na main): abrir projeto .ignis real (FileChooser -> IgnisProjectIO.load) no viewport; selecao Hierarchy<->viewport (contorno via Game.renderWorldTo com selected); Inspector GridPane editavel (nome/x/y/w/h/rot/visivel) escreve no GameObject ao vivo. Pendente: ToolBar, atalhos, Play/Stop.
- F3 (CONCLUIDA na main): dividida Claude/Gemini. Claude FEITO: BuildDialog nativo (FxBuildDialog), ToolBar (Abrir/Build/Play/Stop), atalhos (Ctrl+O/Ctrl+B/F5/F6), Play/Stop ligados ao loop (playWorld/start, stopWorld/stop, ScriptManager ao abrir projeto). Gemini FEITO: FxCommunityWindow, FxNotesWindow, FxAnimationEditor, FxImageEditor/FxPaintCanvas, FxAudioEditor, FxCodeEditor.
- Fiacao do menu COMPLETA (2026-06-15, commit 63ad0ee): o menu Ferramentas da casca IgnisEditorApp abre SO janelas JavaFX (Audio/Imagens/Animacao/Notas/Comunidade/Editor de Codigo/Build) — sem fallback Swing. FxCodeEditor foi o ultimo a ser ligado: item -> ChoiceDialog com scripts do projeto (ScriptManager.listAvailableScripts) + "Novo script" (createNewScript) -> new FxCodeEditor(null, scriptManager, scriptName) (param Editor Swing = null, ja tratado por null-check).
- Input no viewport FX FEITO (2026-06-15, commit 63ad0ee): teclado/mouse do Canvas FX roteados ao singleton com.ignis.core.Input fabricando java.awt.event.KeyEvent/MouseEvent e chamando os callbacks AWT publicos do Input (IgnisEditorApp.wireFxInputToEngine). Puramente ADITIVO. Teclado so em Play; mouse sempre; Canvas focavel.
- F3.5 — Casca do editor (ciclo de vida de projeto + mecanicas) FEITO (2026-06-15, commit 9f0be7c): tudo ADITIVO (nada em com.ignis.core).
  - Tela de selecao de projeto ao abrir (FxProjectStartupDialog) com LISTA visual de projetos + recentes (★) — melhora o startup Swing (que so tinha 3 botoes New/Open/Exit).
  - Persistencia estilo VSCode (EditorPrefs) em user.home/.ignis/editor-prefs.json: ultimo projeto + recentes (MRU, dedupe, clearMissing). Submenu "Abrir recente".
  - Menu Arquivo completo: Novo/Abrir/Abrir-recente/Selecionar/Salvar(Ctrl+S)/Salvar-como(Ctrl+Shift+S)/Fechar/Trocar. currentProject mantido; o .ignis AGORA e gravado (antes o FX nunca chamava IgnisProjectIO.save). syncEntitiesToScene espelha doSaveProject.
  - Mecanicas: menu "Cena" + ContextMenu na Hierarchy + teclas (Delete/F2/Ctrl+D) — criar (EntityFactory), duplicar, deletar, renomear, reordenar z-order. Asset Browser: TreeView<File> do projeto (abre no duplo-clique).
- Trabalho Gemini/usuario (2026-06-15): ferramentas de viewport (Mover/Rotacionar/Redimensionar/Zoom/Reset Cam/Focus Selected), Correcao de Bugs e Auditoria de Mouse (resolvido o loop de mouse warping do Robot em Game.java via isShowing(); separacao dos botoes: esquerdo=selecao, direito=menus de contexto em Hierarchy/Assets/subeditores), integracao do FxCodeEditor interno na arvore de Assets, ajuste visual da numeracao de linhas via CSS !important.
- Correcoes de selecao/inspector/picking/autosave FEITO (2026-06-15, commit 4715281, push em URSoftware/IgnisEngine):
  - Inspector agora atualiza ao clicar no viewport (selectEntity virou fonte unica e sempre chama setSelected; antes setSelected so era chamado pelo listener da arvore, que abortava por suppressSelectionEvents).
  - Selecao dupla removida (core e a fonte no botao esquerdo via handleMousePress; removido setOnMouseClicked). Clique direito nao mexe na selecao/drag do engine (SECONDARY nao vai a dispatchEvent; so menu de contexto).
  - Picking: getObjectAt(x,y,afterCurrent) CICLA entre objetos sobrepostos e respeita rotacao (hit-test rotacionado). Indicador visual: borda tracejada + alcas de canto no renderWorldTo (espelha renderSelection do Swing).
  - Regressao corrigida (revisao adversarial): clicar-e-arrastar objeto nao-selecionado num gesto unico nao cancela mais o drag (setSelected so cancela quando a selecao nao veio do engine).
  - FxCodeEditor: numeros de linha SEMPRE pretos sobre gutter claro (CSS !important + factory inline) — legiveis em qualquer tema.
  - Auto Save: item no menu Arquivo (EditorPrefs); autosave de scripts religado; autosave de projeto com dirty-flag, fora do Play, salvamento silencioso (sem Alert modal). Build mvnw compile = SUCCESS (86 fontes). PENDENTE: validacao manual em GUI.
- Roadmap pos-F4 (paridade pendente): undo/redo (Command), Inspector completo (Cor/Sprite/Collider/Camera/Scripts), anexar script a objeto, import imagem->sprite, prefabs (PrefabManager); backlog: multi-selecao, merge, drag-drop, console de erros, multi-cena, parentesco, multi-aba.
- F4 (proxima): tema CSS escuro unificado (ignis-dark.css substituindo ~96 setStyle inline), layout persistido em SplitPane/Stage, remover javafx-swing. BLOQUEIO: remover javafx-swing exige antes eliminar a ponte SwingFXUtils (extrair um Renderer desacoplado do toolkit).

## Riscos

- Threading FX Application Thread vs EDT: Platform.runLater / SwingUtilities.invokeLater nas fronteiras.
- Custo da cópia de imagem por frame: reutilizar buffers, PixelBuffer se preciso.
- Empacotamento (JavaFX fora da JDK): jlink/jpackage ou shade; validar no Builder.
- Input do jogo via listeners AWT: RESOLVIDO (2026-06-15) de forma aditiva — eventos do Canvas FX traduzidos para java.awt.event.KeyEvent/MouseEvent e enviados aos callbacks publicos do singleton Input, sem alterar o core (ver Fases). Resta validar em GUI.

## Links

- [[concepts/ignisengine-roadmap]]
- [[concepts/ignisengine-java-17]]
- [[concepts/ignisengine-marketplace]]
