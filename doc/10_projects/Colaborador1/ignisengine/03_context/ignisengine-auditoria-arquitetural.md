---
tags: [ignisengine, auditoria, arquitetura, debt]
updated: 2026-06-14
---

## Definição

Auditoria arquitetural do IgnisEngine (2026-06-14). Doc completo: `IgnisEngine/doc/ARCHITECTURE_AUDIT.md`. Ver também auditoria anterior [[10_projects/Colaborador1/ignisengine/03_context/ignisengine-auditoria]].

## Diagnóstico

- Modularidade macro boa (Builder, marketplace, sub-editores, UI in-game desacopláveis).
- Coesão/manutenibilidade comprometidas por monolitos: Editor.java 5580 (71 usos Swing), Game.java 2003, IgnisScript 1610, AudioEditorFrame 1317, IgnisSampleCollisions 1215.
- Render preso ao AWT: Game extends Canvas + BufferStrategy + Graphics2D; GameObject.render(Graphics). Define a estratégia JavaFX (ponte).
- Dependências: só org.json (ótimo, baixa superfície).
- Sem testes automatizados; plugins sem sandbox; serialização JSON manual por classe; AssetResolver sem cache.

## Melhorias-chave

1. Extrair painéis do Editor.java. 2. Camada Renderer desacoplada (BufferedImage). 3. Quebrar Game.java. 4. Testes (serialização/colisão). 5. Loader de plugins com sandbox. 6. Separar exemplos de produção em IgnisSampleCollisions.

## Links

- [[10_projects/Colaborador1/ignisengine/03_context/ignisengine-dividas-tecnicas]]
- [[10_projects/Colaborador1/ignisengine/03_context/ignisengine-javafx-migracao]]
- [[10_projects/Colaborador1/ignisengine/03_context/ignisengine-inventario]]
