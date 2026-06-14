---
tags: [ignisengine, inventario, arquitetura]
updated: 2026-06-14
---

## Definição

Inventário dos sistemas do IgnisEngine: 75 arquivos .java, ~31.100 linhas, Java 17. Doc completo: `IgnisEngine/doc/PROJECT_INVENTORY.md`.

## Modelo (importante)

Não é ECS. É herança de `GameObject` (abstrato) + comportamento via scripts (`IgnisScript`) anexados; serialização JSON (.ignis). `Scene` = List<GameObject> + List<Camera>.

## Sistemas por estado

- Concluído: game loop (Game extends Canvas), GameObject/Scene/Transform/Camera/Input, serialização .ignis, prefabs, scripting (IgnisScript), áudio (engine + DAW), UI in-game (core/ui), editor principal, sub-editores (imagem/áudio/notas/animação 2D), Builder Java, runtime, marketplace (cliente + web).
- Parcial: assets (sem cache), colisões (sem física desacoplada), plugins (sem loader/sandbox).
- Experimental: exportação C++ (CppExportStrategy).
- Planejado: animação 3D, física rígida, migração JavaFX, multi-provedor IA.

## Monolitos (atenção)

Editor.java 5580, Game.java 2003, IgnisScript 1610, AudioEditorFrame 1317, IgnisSampleCollisions 1215.

## Links

- [[concepts/ignisengine-roadmap-mestre]]
- [[concepts/ignisengine-auditoria-arquitetural]]
