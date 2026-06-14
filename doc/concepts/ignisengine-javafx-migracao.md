---
tags: [ignisengine, javafx, migracao, ui, decision, architecture]
updated: 2026-06-13
---

## Definição

Migração incremental da interface do editor IgnisEngine de Swing/AWT para JavaFX 17, mantendo o núcleo de render da engine.

## Contexto

Editor hoje é Swing/AWT: 38 arquivos usam swing/awt, monolito `editor/Editor.java` (~5962 linhas), núcleo `core/Game.java extends java.awt.Canvas` (BufferStrategy + Graphics2D). Plano completo no projeto: `IgnisEngine/doc/JAVAFX_MIGRATION_PLAN.md`.

## Decisões-Chave

- Branches (2026-06-14): `Legado` = versao estavel Swing + marketplace (preservada, nao migra); `main` = desenvolvimento da migracao JavaFX. Cada fase mergeavel; Legado e o ponto de retorno seguro.
- Incremental, não big-bang: Swing e JavaFX convivem durante a transição.
- Interop: `SwingNode` (embutir Swing na cena FX), `JFXPanel` (FX dentro de Swing), `SwingFXUtils` (BufferedImage ↔ WritableImage).
- Ponte de render do Viewport: render offscreen em BufferedImage (mesmo Graphics2D) → `SwingFXUtils.toFXImage` → `javafx.scene.canvas.Canvas` via AnimationTimer. Desacopla loop do jogo da janela; remove BufferStrategy no editor.
- Rejeitado: embutir Canvas AWT pesado direto na cena FX (heavyweight/lightweight quebra foco/render).
- Reescrever pipeline gráfico NÃO faz parte da migração.

## Fases

- F0 (FEITO, so na main): deps JavaFX 17 no pom.xml + javafx-maven-plugin + pacote `com.ignis.editor.fx`. Compila.
- F1 (FEITO, so na main): IgnisEditorApp (BorderPane/MenuBar/SplitPane) + ponte de render `Game.renderWorldTo` -> BufferedImage -> SwingFXUtils -> Canvas (AnimationTimer); Hierarchy nativa (TreeView); Inspector placeholder; cena de amostra. Rodar: `mvnw javafx:run`.
- F2 (FEITO, so na main): abrir projeto .ignis real (FileChooser -> IgnisProjectIO.load) no viewport; selecao Hierarchy<->viewport (contorno via Game.renderWorldTo com selected); Inspector GridPane editavel (nome/x/y/w/h/rot/visivel) escreve no GameObject ao vivo. Pendente: ToolBar, atalhos, Play/Stop.
- F3 (EM ANDAMENTO, so na main): dividida Claude/Gemini. Claude FEITO: BuildDialog nativo (FxBuildDialog), ToolBar (Abrir/Build/Play/Stop), atalhos (Ctrl+O/Ctrl+B/F5/F6), Play/Stop ligados ao loop (playWorld/start, stopWorld/stop, ScriptManager ao abrir projeto). Gemini FEITO: CommunityFrame->FxCommunityWindow. Pendente Gemini: Notes, Animation, ImageEditor/PaintCanvas, AudioEditor, editor de codigo (RichTextFX) — cada Fx* e ligada no menu pelo Claude. Pendente geral: rotear input do jogo para o viewport FX. Interop Swing segue como fallback.
- F4: tema CSS escuro, layout persistido em SplitPane/Stage, remover javafx-swing.

## Riscos

- Threading FX Application Thread vs EDT: Platform.runLater / SwingUtilities.invokeLater nas fronteiras.
- Custo da cópia de imagem por frame: reutilizar buffers, PixelBuffer se preciso.
- Empacotamento (JavaFX fora da JDK): jlink/jpackage ou shade; validar no Builder.
- Input do jogo via listeners AWT: remapear eventos do Canvas FX para `Input`.

## Links

- [[concepts/ignisengine-roadmap]]
- [[concepts/ignisengine-java-17]]
- [[concepts/ignisengine-marketplace]]
