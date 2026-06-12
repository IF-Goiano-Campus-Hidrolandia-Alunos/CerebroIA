---
tags: [ignisengine, serialization, script, annotation]
updated: 2026-06-12
---

## Definição

Sistema estrito de exposição e persistência de variáveis em scripts do IgnisEngine através da annotation `@Serialize`.

## Contexto

Garantir o isolamento de variáveis internas de scripts, forçando o desenvolvedor a declarar explicitamente via reflection quais campos devem ser carregados, salvos e expostos no Inspector.

## Detalhes

- **Annotation Marcadora**: Apenas campos anotados com `@Serialize` são persistidos em cenas e prefabs.
- **Herança**: A reflexão percorre a hierarquia do script recursivamente até a classe base `IgnisScript` (excluindo os campos desta).
- **Sem Exceções**: Não há regra de fallback para expor campos sem a annotation.
- **Helper Centralizado**: Toda a lógica de varredura, conversão e desserialização foi extraída para `ScriptSerializationHelper` evitando duplicação entre `Scene`, `PrefabManager` e `Editor`.
- **DPI Icon Correction**: Ajuste no `AppIconHelper` para escalonamento síncrono com `BufferedImage` de alta qualidade, prevenindo problemas de dimensionamento de ícone no Windows.

## Links

- [[concepts/ignisengine-roadmap]]
- [[concepts/ignisengine-builder]]
