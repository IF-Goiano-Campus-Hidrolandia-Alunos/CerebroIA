---
tags: [mcp, java, sdk, desenvolvimento, programacao, client-server]
updated: 2026-06-30
author: Colaborador1
---

## Definição

Guia de utilização do SDK Java oficial do Model Context Protocol (`mcp-sdk-java`) para a implementação nativa de clientes e servidores de contexto em aplicações baseadas em JVM.

## Contexto

Aplicável em desenvolvimentos Java 17+ (como o motor 2D IgnisEngine) para expor APIs internas do motor ou integrar agentes externos com o ecossistema Java.

## Detalhes

### 1. Dependências do Maven/Gradle
Para incluir o SDK básico em um projeto Java puro, utilize as seguintes coordenadas de dependências:

**Maven (`pom.xml`):**
```xml
<dependency>
    <groupId>io.modelcontextprotocol.sdk</groupId>
    <artifactId>mcp</artifactId>
    <version>2.0.0</version>
</dependency>
```

**Gradle (`build.gradle`):**
```groovy
implementation 'io.modelcontextprotocol.sdk:mcp:2.0.0'
```

---

### 2. Criando um Servidor MCP em Java Puro
Exemplo de um servidor baseado em **Stdio** expondo ferramentas nativas de manipulação de assets da engine.

```java
import io.modelcontextprotocol.sdk.McpServer;
import io.modelcontextprotocol.sdk.transport.StdioServerTransport;
import io.modelcontextprotocol.sdk.model.Tool;
import io.modelcontextprotocol.sdk.model.CallToolResult;
import java.util.List;
import java.util.Map;

public class IgnisMcpServer {
    public static void main(String[] args) {
        // 1. Inicializar o transporte Stdio padrao
        StdioServerTransport transport = new StdioServerTransport();

        // 2. Criar e configurar o servidor MCP
        McpServer server = McpServer.builder(transport)
            .serverInfo("IgnisEngine-Server", "1.0.0")
            // Registrar uma ferramenta nativa da Engine
            .tool(new Tool(
                "create_sprite", 
                "Cria um novo sprite 2D na pasta de assets da engine",
                Map.of(
                    "type", "object",
                    "properties", Map.of(
                        "spriteName", Map.of("type", "string", "description", "Nome unico do asset"),
                        "filePath", Map.of("type", "string", "description", "Caminho da imagem de origem")
                    ),
                    "required", List.of("spriteName", "filePath")
                )
            ), argsMap -> {
                // Lambda de execucao da ferramenta acionada pela IA
                String spriteName = (String) argsMap.get("spriteName");
                String filePath = (String) argsMap.get("filePath");
                
                // Chamada de API nativa da engine (simulada)
                boolean success = true; // AssetManager.createSprite(spriteName, filePath);
                
                if (success) {
                    return new CallToolResult("Sprite criado com sucesso: " + spriteName);
                } else {
                    return new CallToolResult("Falha ao criar o sprite.");
                }
            })
            .build();

        // 3. Iniciar a escuta do servidor
        server.start();
        System.err.println("Ignis MCP Server rodando em Stdio...");
    }
}
```

---

### 3. Criando um Cliente MCP em Java Puro
Exemplo de cliente que inicia um servidor subprocesso (como uma ferramenta em Python ou Node.js) e consome suas ferramentas.

```java
import io.modelcontextprotocol.sdk.McpClient;
import io.modelcontextprotocol.sdk.transport.StdioClientTransport;
import io.modelcontextprotocol.sdk.model.CallToolResult;
import io.modelcontextprotocol.sdk.model.ListToolsResult;
import java.util.List;
import java.util.Map;

public class IgnisMcpClient {
    public static void main(String[] args) throws Exception {
        // 1. Configurar o transporte iniciando o processo do servidor local
        ProcessBuilder processBuilder = new ProcessBuilder("node", "c:\\caminho\\server.js");
        StdioClientTransport transport = new StdioClientTransport(processBuilder);

        // 2. Instanciar o cliente MCP
        McpClient client = McpClient.builder(transport)
            .clientInfo("IgnisEngine-Client", "1.0.0")
            .build();

        // 3. Conectar e iniciar handshake
        client.connect();

        // 4. Listar ferramentas disponiveis no servidor conectado
        ListToolsResult toolsResult = client.listTools().get();
        toolsResult.getTools().forEach(tool -> {
            System.out.println("Ferramenta encontrada: " + tool.getName() + " - " + tool.getDescription());
        });

        // 5. Invocar uma ferramenta do servidor
        CallToolResult result = client.callTool("read_file", Map.of("path", "c:\\src\\Main.java")).get();
        System.out.println("Resultado da chamada: " + result.getTextContent());

        // 6. Fechar conexao ao encerrar
        client.close();
    }
}
```

## Links

- [[mcp-protocol-specification]]
- [[../../10_projects/Colaborador1/ignisengine/03_context/ignisengine-mcp-architecture]]
