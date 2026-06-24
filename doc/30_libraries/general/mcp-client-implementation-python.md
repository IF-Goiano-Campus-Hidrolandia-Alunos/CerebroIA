---
tags: ['mcpmodelcontextprotocol', 'documentacao', 'mcp', 'protocolo', 'claude']
updated: 2026-06-21
---

## Definição

Protocolo e especificações de integração do Model Context Protocol (MCP) para MCP Client Implementation Python.

## Contexto

Permite que agentes de IA e o Claude Desktop acessem arquivos, bancos de dados e ferramentas locais de forma padronizada.

## Detalhes

- Arquitetura de conexão cliente-servidor usando JSON-RPC 2.0.
- Definição de esquemas de ferramentas (tools) e recursos expostos pelo servidor.
- Configuração e provisionamento seguro do canal de transporte (Stdio ou SSE).

### Exemplo de Implementação Prática

```python
# Servidor MCP básico em Python
import asyncio
from mcp.server.models import InitializationOptions
import mcp.types as types
from mcp.server import Notification, Server
import mcp.server.stdio

server = Server("meu-servidor-mcp-python")

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="calculo_local",
            description="Executa cálculos de borda",
            inputSchema={"type": "object", "properties": {"expression": {"type": "string"}}}
        )
    ]

async def main():
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, InitializationOptions(server_name="calc-mcp", server_version="1.0.0"))

if __name__ == "__main__":
    asyncio.run(main())
```

## Links

- [[00_MOC]]
- [[30_libraries/dotnet_arch/guia-organizacao-para]]
- [[30_libraries/dotnet_arch/guia-dataview-obsidian]]
