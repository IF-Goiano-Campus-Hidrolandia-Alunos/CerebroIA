---
tags: ['mcpmodelcontextprotocol', 'documentacao', 'mcp', 'protocolo', 'claude']
updated: 2026-06-21
---

## Definição

Protocolo e especificações de integração do Model Context Protocol (MCP) para MCP Construindo Servidor MCP Nodejs.

## Contexto

Permite que agentes de IA e o Claude Desktop acessem arquivos, bancos de dados e ferramentas locais de forma padronizada.

## Detalhes

- Arquitetura de conexão cliente-servidor usando JSON-RPC 2.0.
- Definição de esquemas de ferramentas (tools) e recursos expostos pelo servidor.
- Configuração e provisionamento seguro do canal de transporte (Stdio ou SSE).

### Exemplo de Implementação Prática

```javascript
// Servidor MCP básico em Node.js usando o SDK Oficial
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server({ name: "meu-servidor-mcp", version: "1.0.0" }, { capabilities: { tools: {} } });

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [{
    name: "consultar_dados",
    description: "Consulta informações úteis na base local",
    inputSchema: { type: "object", properties: { query: { type: "string" } }, required: ["query"] }
  }]
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "consultar_dados") {
    const query = request.params.arguments?.query;
    return { content: [{ type: "text", text: `Resultado da busca por: ${query}` }] };
  }
  throw new Error("Ferramenta não encontrada");
});

const transport = new StdioServerTransport();
await server.connect(transport);
```

## Links

- [[00_MOC]]
- [[concepts/guia-organizacao-para]]
- [[concepts/guia-dataview-obsidian]]
