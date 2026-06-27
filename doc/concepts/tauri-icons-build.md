---
tags: [tauri, icons, build, ci]
updated: 2026-06-27
---

## Definição

O `tauri::generate_context!()` valida na compile-time que todos os ícones listados em `tauri.conf.json > bundle > icon` existem no disco.

## Contexto

Corrigido em `desktop/src-tauri/` (commit `aeb161c`). CI quebrava com `No such file or directory` para `32x32.png`.

## Detalhes

- Ícones obrigatórios declarados no `tauri.conf.json`: `32x32.png`, `128x128.png`, `icon.ico`, `icon.png`
- Gerar a partir do ícone-fonte com Pillow: `img.resize((32, 32), Image.LANCZOS).save(...)`
- `icon.ico` deve conter múltiplos tamanhos (16, 32, 48, 256) para compatibilidade Windows
- O arquivo-fonte do projeto é `icons/PlantiumAI_Icon.png`

## Links

- [[tauri-filePath-export-csv]]
