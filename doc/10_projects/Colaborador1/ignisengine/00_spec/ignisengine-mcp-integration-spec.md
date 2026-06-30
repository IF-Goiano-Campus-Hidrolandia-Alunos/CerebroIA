---
tags: [ignisengine, spec, mcp, integracao, planeamento]
updated: 2026-06-30
author: Colaborador1
---

# Especificacao de Integracao: Model Context Protocol (MCP) no IgnisEngine

Definição do escopo, requisitos e fluxo para integrar a especificação MCP no motor 2D IgnisEngine, permitindo co-criação assistida por IA.

## Escopo (In-Scope)

### 1. IgnisEngine como MCP Server (Exposição de Controle)
Permitir que agentes de IA externos (como Claude Desktop, Cursor ou extensões de IDE) controlem o motor para criar jogos de forma iterativa por meio de ferramentas nativas:
- **Ferramentas de Asset Management:** Criar, deletar ou listar sprites, texturas e arquivos de áudio no projeto.
- **Ferramentas de Scene Graph:** Adicionar, remover e listar Nodes 2D (ex: SpriteNode, CameraNode, RigidbodyNode) na cena ativa.
- **Ferramentas de Build & Run:** Compilar o projeto atual, iniciar a simulação do jogo e gerar logs de depuração.

### 2. IgnisEngine como MCP Host/Client (Consumo de Ferramentas)
Permitir que o "Agent Mode" interno (console de IA integrado no motor) se conecte a servidores MCP externos para aumentar suas capacidades locais:
- Conexão nativa com servidores de busca na web, leitura de arquivos locais ou utilitários git para automatizar o versionamento do projeto direto pela engine.

### 3. Transporte Baseado em Stdio
- Implementar o canal de transporte local Stdio para comunicação de baixo tempo de resposta em ambiente single-user.

---

## Fora de Escopo (Out-of-Scope)

- **Servidor SSE Multi-Usuário:** Inicialmente, a engine não funcionará como servidor de rede (SSE) exposto na nuvem; a integração será exclusivamente local e de usuário único.
- **Interface Visual de Conexão (No-Code Graph):** Toda a configuração de conexão com servidores externos será feita via arquivo de configuração estruturado (JSON/YAML).

---

## Resolucao de Ambiguidade

> [!IMPORTANT]
> A principal restrição técnica é a concorrência na árvore de cena Java (Scene Graph Thread-Safety).

### Perguntas Resolvidas

- **Pergunta:** Como executar chamadas de ferramentas da IA que modificam a cena (ex: instanciar um novo SpriteNode) de forma segura sem lançar exceções de concorrência de thread?
  - **Decisão:** O manipulador de ferramentas do servidor MCP não executará as alterações diretamente na thread de processamento de rede/stdio. Todas as operações que alteram o estado do motor serão encapsuladas em tarefas (`Runnable`) e enfileiradas no gerenciador de tarefas do loop principal da engine (`EngineTaskManager.runLater(...)`).
- **Pergunta:** Onde ficará armazenada a configuração de servidores MCP que o cliente da engine pode ler?
  - **Decisão:** Criaremos o arquivo `ignis-mcp-settings.json` na raiz do projeto do jogo, com formato idêntico ao `claude_desktop_config.json`, facilitando a portabilidade.

---

## Plano de Validacao e Testes

### Validacao Manual de Fluxo (Dry-Run)
1. Iniciar o motor IgnisEngine em modo servidor MCP stdio via linha de comando:
   `java -jar IgnisEngine.jar --mcp-server`
2. Configurar o arquivo de conexão do Claude Desktop para iniciar o `IgnisEngine.jar` como subprocesso.
3. Pedir para o Claude: *"Adicione um nó de colisão na minha cena do jogo"* e validar se o nó foi instanciado e renderizado em tempo real na janela ativa do motor.

## Links

- [[../03_context/ignisengine-mcp-architecture]]
- [[../../../../30_libraries/ai_agents/mcp-protocol-specification]]
