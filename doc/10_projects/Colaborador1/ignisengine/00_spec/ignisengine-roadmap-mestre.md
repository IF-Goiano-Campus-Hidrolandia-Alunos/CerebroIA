---
tags: [ignisengine, roadmap, master, decision]
updated: 2026-06-14
---

## Definição

Roadmap Mestre do IgnisEngine: referência principal de evolução, por área, com prioridade/complexidade/dependências/benefício.

## Contexto

Auditoria de 2026-06-14. Documento completo no projeto: `IgnisEngine/doc/MASTER_ROADMAP.md`. Substitui o roadmap antigo de 10 itens como referência principal (ver [[10_projects/Colaborador1/ignisengine/00_spec/ignisengine-roadmap]]).

## Próximas Prioridades (ordenado)

1. Extrair painéis do `Editor.java` (5580 linhas) — pré-requisito da migração.
2. Camada `Renderer` desacoplada do toolkit (habilita ponte JavaFX + testes).
3. Fase 0 da migração JavaFX (deps + javafx-maven-plugin + pacote editor.fx).
4. Ponte de render (PoC Viewport JavaFX) + medir FPS.
5. Testes automatizados (serialização .ignis round-trip, colisões).
6. Loader de plugins com sandbox.
7. Quebrar `Game.java` (loop/render/input).
8. Validar exportação C++ do Builder.

## Áreas cobertas

Core, Editor, Renderização, Física/Colisões, Áudio, Animação, Builder, IA, Comunidade/Marketplace, Migração JavaFX. Cada uma com Concluído/Em andamento/Planejado.

## Links

- [[10_projects/Colaborador1/ignisengine/03_context/ignisengine-inventario]]
- [[10_projects/Colaborador1/ignisengine/03_context/ignisengine-auditoria-arquitetural]]
- [[10_projects/Colaborador1/ignisengine/03_context/ignisengine-javafx-migracao]]
- [[10_projects/Colaborador1/ignisengine/03_context/ignisengine-dividas-tecnicas]]
