---
tags: [ignisengine, arquitetura, java, design-pattern, adr]
updated: 2026-06-30
author: Colaborador1
---

# Arquitetura e Plano de Classes: Integração MCP no IgnisEngine

Este documento detalha o desenho de arquitetura de software, as classes Java recomendadas, a estratégia de concorrência e o plano de fases para implementar o Model Context Protocol (MCP) no motor IgnisEngine.

---

## 1. Visão Geral da Arquitetura

O subsistema MCP funcionará de forma desacoplada dos módulos principais do motor (Física, Renderizador, Som) para garantir que a engine possa operar com ou sem o suporte a agentes de IA.

```
+-----------------------------------------------------------+
|                      IgnisEngine                          |
|                                                           |
|  +--------------------+         +----------------------+  |
|  | EngineTaskManager  |<--------|   IgnisMcpBridge     |  |
|  | (Main Game Loop)   |  Queue  | (Thread Dispatcher)  |  |
|  +--------------------+         +----------------------+  |
|           ^                                ^              |
|           |                                | Invokes      |
|           v                                v              |
|  +------------------+           +----------------------+  |
|  |  SceneGraph 2D   |           |    IgnisMcpServer    |  |
|  | (Sprites, Nodes) |           | (SDK McpServer Wrap) |  |
|  +------------------+           +----------------------+  |
+--------------------------------------------^--------------+
                                             |
                                             | stdio (JSON-RPC)
                                             v
                                  +----------------------+
                                  | External AI Agent    |
                                  | (Claude Desktop, etc)|
                                  +----------------------+
```

---

## 2. Design das Classes Java (Proposta)

Para implementar a arquitetura, criaremos as seguintes classes no pacote `ursoftware.ignisengine.mcp`:

### 1. `IgnisMcpManager` (Fachada Principal)
- **Função:** Ponto de entrada único do subsistema MCP. Responsável por interpretar argumentos de linha de comando (`--mcp-server` ou `--mcp-client`) e gerenciar o ciclo de vida (inicialização e encerramento seguro) do cliente ou do servidor.

### 2. `IgnisMcpServer` (Servidor Wrapper)
- **Função:** Envelopa a classe `McpServer` do SDK oficial. Registra a lista de ferramentas declarativas e define os manipuladores de execução (*handlers*).
- **Exemplo de Métodos:**
  - `public void startServer()`
  - `private void registerEngineTools()`

### 3. `IgnisMcpBridge` (Ponte de Execução Thread-Safe)
- **Função:** Executa a tradução de parâmetros JSON recebidos das ferramentas para chamadas Java fortemente tipadas. Garante que qualquer modificação na cena do jogo seja despachada para execução síncrona na thread principal do motor.
- **Exemplo de Métodos:**
  - `public static void enqueueAction(Runnable task)`

### 4. `IgnisMcpClient` (Cliente Wrapper)
- **Função:** Envelopa o `McpClient` do SDK oficial. Lê as configurações do arquivo local `ignis-mcp-settings.json` e faz o gerenciamento dos processos filhos que rodam ferramentas de IA de terceiros.

---

## 3. Modelo de Concorrência e Threads

Como a comunicação via Stdio é bloqueante e assíncrona, o ecossistema funcionará com três grupos de threads principais:

1. **Stdio Reader Thread (SDK):** Bloqueia aguardando a entrada de dados JSON-RPC em `System.in`.
2. **Stdio Writer Thread (SDK):** Envia de forma serializada as respostas e notificações JSON-RPC para `System.out`.
3. **Engine Loop Thread (IgnisEngine):** Thread de renderização e lógica do jogo rodando a 60 FPS. É a única thread que tem permissão para ler/gravar na árvore de nós 2D. 
   - A `IgnisMcpBridge` insere as requisições na fila de eventos do loop principal, evitando erros críticos de concorrência de leitura e escrita em estruturas de cena.

---

## 4. Plano de Implementação (Fases)

### Fase 1: Integração de Dependências e CLI
- Adicionar a biblioteca oficial `io.modelcontextprotocol.sdk:mcp` nas dependências do projeto.
- Alterar a classe de entrada do motor (`Main.java`) para identificar o parâmetro `--mcp-server`. Se ativo, desabilitar outputs desnecessários no `stdout` que possam sujar o JSON-RPC.

### Fase 2: Implementação da Ponte de Execução (Bridge)
- Desenvolver a classe `IgnisMcpBridge` e integrá-la com o loop de eventos existente do motor.
- Criar mecanismos para enfileirar e consumir ações de modificação de nós em tempo real.

### Fase 3: Exposição de Ferramentas Iniciais (Servidor)
- Registrar ferramentas básicas no servidor:
  - `get_scene_tree`: Retorna a estrutura da cena atual em formato JSON.
  - `create_sprite_node`: Instancia uma imagem na tela do motor no meio da cena.
- Validar se a comunicação JSON-RPC funciona corretamente via subprocesso.

### Fase 4: Integração de Cliente e IA Interna
- Criar a classe `IgnisMcpClient` para carregar sub-ferramentas a partir de arquivos externos.
- Conectar o terminal de console de IA interna (Gemini) do motor para que ele possa utilizar essas ferramentas locais.

## Links

- [[../00_spec/ignisengine-mcp-integration-spec]]
- [[../../../../30_libraries/ai_agents/mcp-protocol-specification]]
- [[../../../../30_libraries/ai_agents/mcp-java-sdk-usage]]
