---
tags: [ignisengine, architecture, gameobject]
updated: 2026-06-14
---

## Definição

O `GameObject` é a classe central de entidades do IgnisEngine, representando qualquer objeto lógico, visual ou físico presente em uma cena.

## Contexto

Cada cena do motor (`Scene`) gerencia uma lista de `GameObject`s. Essas entidades são instanciadas, renderizadas e atualizadas no loop principal de execução (`Game`) e inspecionadas no painel do editor (`Editor`).

## Detalhes

- **Propriedades Principais**: Cada objeto possui identificador único (`id`), nome, posição bidimensional (`x`, `y`), rotação (graus), escala (`width`, `height`), cor para identificação no editor (`nameColor`), visibilidade (`visible`) e caminho do sprite (`spritePath`).
- **Sistema de Componentes Integrado**:
  - **Collider**: Representa a forma de colisão física ou trigger associada (Box/AABB, Circle, Polygon).
  - **Scripting**: Lista de nomes de scripts associados (`scriptNames`) e instâncias ativas (`scripts`) gerenciadas pelo `ScriptManager`.
  - **Animator**: Controlador de animações baseado em spritesheets.
- **Serialização**: Suas propriedades são persistidas em formato JSON por meio de `IgnisProjectIO` e `ScriptSerializationHelper` para manter e restaurar estados de variáveis nos scripts associados.

## Links

- [[ignisengine-serialization]]
- [[ignisengine-collision-system]]
