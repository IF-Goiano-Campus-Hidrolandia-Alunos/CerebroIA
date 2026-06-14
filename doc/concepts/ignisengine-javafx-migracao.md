---
tags: [ignisengine, javafx, migracao, ui, decision, architecture]
updated: 2026-06-13
---

## Definição

Migração incremental da interface do editor IgnisEngine de Swing/AWT para JavaFX 17, mantendo o núcleo de render da engine.

## Contexto

Editor hoje é Swing/AWT: 38 arquivos usam swing/awt, monolito `editor/Editor.java` (~5962 linhas), núcleo `core/Game.java extends java.awt.Canvas` (BufferStrategy + Graphics2D). Plano completo no projeto: `IgnisEngine/doc/JAVAFX_MIGRATION_PLAN.md`.

## Decisões-Chave

- Incremental, não big-bang: Swing e JavaFX convivem durante a transição.
- Interop: `SwingNode` (embutir Swing na cena FX), `JFXPanel` (FX dentro de Swing), `SwingFXUtils` (BufferedImage ↔ WritableImage).
- Ponte de render do Viewport: render offscreen em BufferedImage (mesmo Graphics2D) → `SwingFXUtils.toFXImage` → `javafx.scene.canvas.Canvas` via AnimationTimer. Desacopla loop do jogo da janela; remove BufferStrategy no editor.
- Rejeitado: embutir Canvas AWT pesado direto na cena FX (heavyweight/lightweight quebra foco/render).
- Reescrever pipeline gráfico NÃO faz parte da migração.

## Fases

- F0: deps JavaFX 17 no pom.xml + javafx-maven-plugin + pacote novo `com.ignis.editor.fx` (Swing intacto).
- F1: casca `Application`/BorderPane + ponte de render; Hierarchy/Inspector ainda via SwingNode.
- F2: painéis nativos (Hierarchy=TreeView, Inspector=GridPane/binding, MenuBar/ToolBar).
- F3: janelas-ferramenta uma a uma (BuildDialog→Community→Notes→Animation→ImageEditor→AudioEditor).
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
