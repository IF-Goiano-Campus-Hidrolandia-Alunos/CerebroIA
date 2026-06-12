---
tags: [ignisengine, builder, architecture, decision]
updated: 2026-06-12
---

## Definição

Arquitetura do Builder do IgnisEngine: módulo desacoplado (`com.ignis.builder`) com duas estratégias de compilação despachadas por plataforma.

## Contexto

Itens 1 e 2 do roadmap, implementados em 2026-06-12. Doc completa: `IgnisEngine/doc/BUILDER_GUIDE.md`.

## Detalhes

- Estratégias: JavaBuildStrategy (Windows/Linux/macOS, JVM) e CppExportStrategy (Xbox/PlayStation/Switch, projeto CMake)
- Entry point das distribuições: `com.ignis.runtime.GameRuntime` (carrega .ignis, desliga visuais de editor, entra em PLAYING)
- Config por projeto em `build.json` (nome, versão, resolução, targets, overrides por plataforma)
- Jar do motor gerado a partir do code source em execução (funciona de classes dir ou jar)
- Layout `projects/[Nome]/` preservado no pacote: caminhos relativos de assets resolvem contra o working dir (launcher faz cd)
- Export C++ gera `scene_data.h` (cenas como structs), copia conteúdo para `export/` e cria ponto de integração de SDK em `platform/`
- UI: BuildDialog no editor (menu Build, Ctrl+Shift+B); mesmo módulo roda headless via CLI
- Nintendo Switch visível porém desabilitado (planejamento futuro)

## Limitações Registradas

- Sprites com caminho absoluto fora do projeto não entram no pacote (corrigir no import de assets do editor)
- Build Java exige Java 17+ na máquina do jogador (jlink/jpackage planejado)
- Runtime C++ é esqueleto: portagem de tick/render/colisões pendente

## Links

- [[concepts/ignisengine-roadmap]]
