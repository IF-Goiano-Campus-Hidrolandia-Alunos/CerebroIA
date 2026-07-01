---
tags: [ignisengine, context, mcp, http, bridge, ia, integracao]
updated: 2026-06-30
author: Colaborador1
---

# Bridge HTTP do MCP e Interface de IA & MCP no Editor

Complementa [[ignisengine-mcp-architecture]] e [[ignisengine-mcp-implementation]].
Documenta o segundo transporte do MCP (HTTP por URL) e a interface nas
Configurações do editor para ativar o servidor e copiar a URL local.

---

## 1. Visão geral

Além do transporte **STDIO** (`McpServerManager`, já documentado), o motor passou a
expor as mesmas ferramentas por um **bridge HTTP local com URL copiável**. Isso
permite que agentes que não lançam o processo — em especial IAs usando **APIs
gratuitas do Gemini e da NVIDIA** e a futura **IA embarcada** — se conectem por URL.

| Transporte | Classe | Uso |
|-----------|--------|-----|
| STDIO | `com.ignis.mcp.McpServerManager` | Claude Desktop, Cursor (`--mcp <projeto>`) |
| HTTP (URL) | `com.ignis.mcp.McpHttpBridge` | Gemini/NVIDIA e IA embarcada (via URL local) |

A **fonte canônica** das ferramentas é `com.ignis.mcp.IgnisToolRegistry` — descreve
nome, descrição, schema JSON e executor de forma independente do SDK, garantindo
**paridade** entre STDIO, HTTP e a IA agêntica. Execução na thread de UI via
`IgnisMcpBridge.runOnFxThread(...)`.

```
   Claude/Cursor ─────▶ McpServerManager (STDIO) ─┐
   Gemini/NVIDIA ─────▶ McpHttpBridge (HTTP/URL) ─┼─▶ IgnisToolRegistry ─▶ ScriptManager/Game
   IA embarcada  ─────▶ (in-process)             ─┘        (thread de UI)
```

---

## 2. Interface no editor

`Configurações → IA & MCP → Servidor MCP` (`FxSettingsWindow`):

- **Ativar/desativar servidor MCP** (habilitado só com projeto aberto).
- **Porta** (padrão `8790`).
- **Expor na rede/VPN (0.0.0.0)** — permite conexão de outras máquinas; sem isso,
  escuta apenas em `127.0.0.1`.
- **Token** Bearer opcional (`Authorization: Bearer <token>`).
- **URL** exibida + botão **Copiar URL**.

Estado persistido em `~/.ignis/editor-prefs.json` (`mcpEnabled`, `mcpPort`,
`mcpExposeNetwork`, `mcpToken`). Se habilitado, sobe automaticamente ao abrir o
projeto (`IgnisEditorApp.maybeAutoStartMcp()`) e encerra no fechamento do editor.

---

## 3. Endpoints HTTP

Base `http://<host>:<porta>` (ex.: `http://127.0.0.1:8790`).

| Método | Caminho | Descrição |
|--------|---------|-----------|
| `GET`  | `/health` | `{"status":"ok","tools":N,"authRequired":bool}` |
| `GET`  | `/mcp/tools` | Ferramentas com `name`, `description`, `inputSchema` |
| `POST` | `/mcp/call` | `{"name":"...","arguments":{...}}` → `{"ok":true,"result":"..."}` |

```bash
curl http://127.0.0.1:8790/mcp/tools
curl -X POST http://127.0.0.1:8790/mcp/call \
  -H "Content-Type: application/json" \
  -d '{"name":"get_project_tree","arguments":{}}'
```

Implementado com `com.sun.net.httpserver.HttpServer` (embutido no JDK, **sem novas
dependências no `pom.xml`**).

---

## 4. Ferramentas registradas

**Base (sempre, 7):** `get_project_tree`, `list_scripts`, `read_script`,
`write_script`, `create_script`, `compile_project`, `read_file` (anti
path-traversal). Delegam ao `com.ignis.core.ScriptManager` do projeto ativo.

**Cena e Play (+8, só com editor vivo):** quando o bridge roda dentro do editor
JavaFX, o `IgnisEditorApp` registra o contexto vivo via
`McpService.setEditorContext(game, play, stop, refresh, save)` →
`IgnisToolRegistry.attachLiveEditor(...)`, habilitando:

| Ferramenta | Args | Efeito |
|-----------|------|--------|
| `list_scene_objects` | — | Lista GameObjects da cena |
| `create_object` | `name`,`type?`,`x?`,`y?`,`width?`,`height?` | Cria forma (square/circle/triangle/star/pentagon/player) |
| `set_object_transform` | `name`,`x?`,`y?`,`width?`,`height?`,`rotation?` | Move/redimensiona/rotaciona |
| `set_object_sprite` | `name`,`path` | Define sprite |
| `delete_object` | `name` | Remove objeto da cena |
| `attach_script` | `objectName`,`scriptName` | Anexa IgnisScript |
| `play_game` / `stop_game` | — | Play/Stop reais do editor |
| `save_project` | — | Salva a cena `.ignis` |

Como `GameObject` é abstrato, `create_object` usa fábrica de formas concretas. Os
hooks chamam os métodos reais do editor (`playWorld`/`stopWorld`/`refreshHierarchy`/
`saveProjectSilently`) na thread de UI. No modo headless (`--mcp`) só existem as 7
base. **Exige reiniciar o editor após rebuild** (Java não tem hot-reload).

Assim um agente monta e testa um jogo de ponta a ponta pela URL: criar objetos →
anexar script → salvar → Play → observar → Stop.

---

## 5. Segurança

- Bind local por padrão (`127.0.0.1`); exposição de rede é explícita.
- Token Bearer opcional em `/mcp/tools` e `/mcp/call` (`/health` fica aberto).
- Anti path-traversal em `read_file` (resolução canônica dentro da raiz).
- Ao expor na VPN/LAN, recomenda-se sempre definir token.

---

## 6. Pendências

- Migrar o `McpServerManager` (STDIO) para consumir o `IgnisToolRegistry` (hoje
  registra ferramentas legadas direto no SDK — duplicação).
- Avaliar transporte MCP-over-HTTP oficial (SSE) para clientes MCP nativos por rede.
- Expandir o registry (cena, assets, animação, áudio) e painel de auditoria de
  chamadas.

Relacionados: [[ignisengine-agentic-ai-plan]], [[ignisengine-colaboracao-tempo-real]],
[[ignisengine-ai-integration]].
