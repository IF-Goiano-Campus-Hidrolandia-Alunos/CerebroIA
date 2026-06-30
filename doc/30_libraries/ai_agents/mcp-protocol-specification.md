---
tags: [mcp, model-context-protocol, protocolo, especificacao, ai-agents]
updated: 2026-06-30
author: Colaborador1
---

## Definição

Model Context Protocol (MCP) é um protocolo aberto que padroniza a comunicação bidirecional e segura entre aplicações de IA (hosts/clientes) e fontes de dados ou ferramentas externas (servidores).

## Contexto

Utilizado para evitar integrações proprietárias ("ad-hoc") e unificar como modelos de linguagem interagem de forma nativa com arquivos locais, APIs, bancos de dados e compiladores de código.

## Detalhes

### 1. Arquitetura de Comunicação
- **MCP Host:** A aplicação principal com o modelo de linguagem integrado (ex: Claude Desktop, IDE, ou a engine IgnisEngine no "Agent Mode").
- **MCP Client:** O módulo interno do Host que gerencia conexões ativas com um ou mais servidores.
- **MCP Server:** O processo ou serviço leve que expõe capacidades declarativas ao cliente por meio do protocolo.

### 2. Três Pilares de Funcionalidades (Capabilities)
- **Recursos (Resources):**
  - Fontes de dados estáticas ou dinâmicas que o servidor torna legíveis pela IA (ex: arquivos locais, logs, esquemas de BD).
  - Acessados via URIs customizadas (ex: `file://projeto/src/Main.java`).
- **Prompts:**
  - Templates reutilizáveis fornecidos pelo servidor para simplificar tarefas (ex: modelo de revisão de código, gerador de testes).
- **Ferramentas (Tools):**
  - Funções executáveis que a IA pode decidir chamar para realizar ações no mundo real (ex: compilar projeto, salvar imagem, disparar comando).
  - Definidas via JSON Schema de entrada e retornando texto, imagem ou dados estruturados.

### 3. Camadas de Transporte Disponíveis
- **Stdio (Standard Input/Output):**
  - Indicado para integrações locais na mesma máquina.
  - O cliente inicia o servidor como um subprocesso filho.
  - A comunicação ocorre escrevendo requisições JSON-RPC no `stdin` do servidor e lendo as respostas no `stdout`.
  - **Crítico:** O servidor deve enviar logs e mensagens de erro exclusivamente via `stderr` para não corromper o fluxo de mensagens estruturadas do `stdout`.
- **SSE (Server-Sent Events):**
  - Indicado para integrações em rede/remotas.
  - O cliente envia dados usando chamadas HTTP POST tradicionais.
  - O servidor envia atualizações assíncronas e respostas de volta ao cliente via canal SSE unidirecional de longa duração.

### 4. Protocolo de Mensagens
Baseia-se em **JSON-RPC 2.0** com mensagens divididas em:
- **Requests:** Enviados pelo cliente esperando uma resposta (métodos: `initialize`, `resources/list`, `tools/call`).
- **Responses:** Retornos estruturados do servidor vinculados ao ID da requisição original.
- **Notifications:** Mensagens unilaterais que não requerem resposta, enviadas por qualquer uma das partes (ex: `notifications/resources/list_changed`).

## Links

- [[mcp-java-sdk-usage]]
- [[../../10_projects/Colaborador1/ignisengine/00_spec/ignisengine-mcp-integration-spec]]
