---
tags: [ignisengine, debt, prioridades]
updated: 2026-06-14
---

## Definição

Dívidas técnicas do IgnisEngine priorizadas (2026-06-14). Detalhe: `IgnisEngine/doc/ARCHITECTURE_AUDIT.md` (seção 7).

## Prioridade Alta

- Editor.java monolítico (5580) — bloqueia JavaFX e manutenção. Esforço alto.
- Render acoplado ao AWT (Game extends Canvas) — define estratégia JavaFX. Esforço médio.
- Game.java com múltiplas responsabilidades (2003). Esforço médio-alto.

## Prioridade Média

- Plugins sem sandbox/loader real.
- Colisões sem motor de física desacoplado.
- Serialização JSON manual por classe (evolução de schema frágil).
- Exportação C++ a validar.
- Ausência de testes automatizados.

## Prioridade Baixa

- AssetResolver sem cache.

## Links

- [[10_projects/Colaborador1/ignisengine/03_context/ignisengine-auditoria-arquitetural]]
- [[10_projects/Colaborador1/ignisengine/00_spec/ignisengine-roadmap-mestre]]
