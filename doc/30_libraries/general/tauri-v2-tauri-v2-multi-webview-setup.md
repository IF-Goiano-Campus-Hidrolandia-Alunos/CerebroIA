---
tags: ['tauriv2desktop', 'documentacao', 'tauri', 'desktop']
updated: 2026-06-21
---

## Definição

Instruções e padrões de desenvolvimento no Tauri v2 para Tauri V2 Tauri V2 Multi Webview Setup.

## Contexto

Essencial para construir a aplicação Desktop rápida e segura, integrando comandos Rust e o WebView.

## Detalhes

- Configuração e APIs necessárias no Tauri v2.
- Mecanismo de comunicação e tratamento de eventos no frontend e no backend.
- Segurança de dados e melhores práticas de isolamento de processos.

### Exemplo de Implementação Prática

```json
{
  "identifier": "default",
  "permissions": [
    "core:path:allow-app-data-write",
    "core:event:allow-emit",
    "core:event:allow-listen",
    "core:window:allow-close",
    "core:window:allow-minimize"
  ]
}
```

## Links

- [[00_MOC]]
- [[30_libraries/dotnet_arch/guia-organizacao-para]]
- [[30_libraries/dotnet_arch/guia-dataview-obsidian]]
