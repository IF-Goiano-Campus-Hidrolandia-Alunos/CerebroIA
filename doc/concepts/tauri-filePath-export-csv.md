---
tags: [tauri, rust, desktop, fix]
updated: 2026-06-27
---

## Definição

No Tauri v2, `blocking_save_file()` retorna `Option<FilePath>` onde `FilePath` é um enum — não possui o método `to_path_buf()`.

## Contexto

Corrigido em `desktop/src-tauri/src/lib.rs` durante build de CI do PlantiumAI (commit `aeb161c`).

## Detalhes

- `FilePath` tem variantes `Path(PathBuf)` e `Url(url::Url)` — usar pattern matching
- Import necessário: `use tauri_plugin_dialog::{DialogExt, FilePath};`
- Substituir `path.to_path_buf().map_err(...)` por `if let Some(FilePath::Path(path_buf)) = file_path`
- O caso `FilePath::Url` não é esperado em save-dialog; cair no `else` retornando erro é correto

## Links

- [[tauri-icons-build]]
