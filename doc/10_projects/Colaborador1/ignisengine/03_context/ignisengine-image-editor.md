---
tags: [ignisengine, image-editor, architecture, decision]
updated: 2026-06-12
---

## Definição

Arquitetura do editor de imagens integrado do IgnisEngine: módulo desacoplado `com.ignis.imageeditor` com modelo puro (sem Swing) e janela própria.

## Contexto

Item 3 do roadmap, v1 implementada em 2026-06-12. Doc completa: `IgnisEngine/doc/IMAGE_EDITOR_GUIDE.md`.

## Detalhes

- ImageDocument: canvas fixo + pilha de camadas ARGB com visibilidade/opacidade; modelo puro reutilizável (futuro: frames de animação)
- PaintCanvas: ferramentas (lápis, borracha, linha, retângulo, elipse, flood fill, conta-gotas), undo/redo por camada (25 passos), zoom 25%-800% nearest-neighbor
- ImageEditorFrame: menus, toolbar, painel de camadas, abrir/salvar PNG
- Integração: Tools > Image Editor no editor do motor; exportação achatada direto para project/assets/sprites
- Melhorias UX (v2): área de trabalho centralizada (GridBagLayout wrapper), atalho Ctrl + Wheel para zoom, renderização de grade pixelar (para zoom >= 4.0), círculo indicador visual do pincel dinâmico e barra de status HUD (coordenadas, pincel, zoom)
- Pendente para v2: ferramentas de seleção e transformação, formato próprio com camadas

## Links

- [[10_projects/Colaborador1/ignisengine/00_spec/ignisengine-roadmap]]
