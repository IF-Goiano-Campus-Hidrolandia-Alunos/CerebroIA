---
tags: ['tauriv2desktop', 'documentacao', 'tauri', 'desktop']
updated: 2026-06-21
---

## Definição

Instruções e padrões de desenvolvimento no Tauri v2 para Tauri V2 Window Close Prevent To Tray.

## Contexto

Essencial para construir a aplicação Desktop rápida e segura, integrando comandos Rust e o WebView.

## Detalhes

- Configuração e APIs necessárias no Tauri v2.
- Mecanismo de comunicação e tratamento de eventos no frontend e no backend.
- Segurança de dados e melhores práticas de isolamento de processos.

### Exemplo de Implementação Prática

```javascript
// Gerenciamento e arraste de janelas customizadas no Tauri v2
import { getCurrentWindow } from '@tauri-apps/api/window';

const appWindow = getCurrentWindow();

// Cria um botão de fechar customizado
document.getElementById('titlebar-close').addEventListener('click', () => {
  appWindow.close();
});

// Minimizar
document.getElementById('titlebar-minimize').addEventListener('click', () => {
  appWindow.minimize();
});

// Arraste de janela manual (CSS class .titlebar precisa ter cursor: pointer)
document.getElementById('titlebar-drag-area').addEventListener('mousedown', (e) => {
  if (e.target.id === 'titlebar-drag-area') {
    appWindow.startDragging();
  }
});
```

## Links

- [[00_MOC]]
- [[30_libraries/dotnet_arch/guia-organizacao-para]]
- [[30_libraries/dotnet_arch/guia-dataview-obsidian]]
