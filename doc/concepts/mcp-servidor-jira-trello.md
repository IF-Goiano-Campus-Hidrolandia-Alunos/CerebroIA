---
tags: ['mcpmodelcontextprotocol', 'documentacao', 'mcp', 'protocolo', 'claude']
updated: 2026-06-21
---

## Definição

Protocolo e especificações de integração do Model Context Protocol (MCP) para MCP Servidor Jira Trello.

## Contexto

Permite que agentes de IA e o Claude Desktop acessem arquivos, bancos de dados e ferramentas locais de forma padronizada.

## Detalhes

- Arquitetura de conexão cliente-servidor usando JSON-RPC 2.0.
- Definição de esquemas de ferramentas (tools) e recursos expostos pelo servidor.
- Configuração e provisionamento seguro do canal de transporte (Stdio ou SSE).

### Exemplo de Implementação Prática

```json
{
  "mcpServers": {
    "meu-servidor": {
      "command": "node",
      "args": ["C:\\caminho\\para\\server.js"],
      "env": {
        "DATABASE_URL": "postgres://localhost/db",
        "API_KEY": "secret-key"
      }
    }
  }
}
```

## Links

- [[00_MOC]]
- [[concepts/guia-organizacao-para]]
- [[concepts/guia-dataview-obsidian]]
