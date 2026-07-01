# Implementacao do Servidor MCP no IgnisEngine

Este documento detalha a implementacao final do servidor Model Context Protocol (MCP) no IgnisEngine. A arquitetura foi desenvolvida para permitir a co-criacao de jogos de forma programatica por agentes de IA autônomos (como Gemini, Claude e Claude Code), expondo os subsistemas nativos do motor de jogos.

---

## 1. Arquitetura Geral

O servidor MCP do IgnisEngine foi implementado utilizando a versao 2.0.0 do SDK Java oficial do Model Context Protocol (`io.modelcontextprotocol.sdk`). Ele opera utilizando o transporte local baseada em Stdio (Standard Input / Standard Output) para troca bidirecional de mensagens JSON-RPC 2.0.

```
       [ IA Cliente ] (ex: Claude Desktop, Gemini)
             │
             ▼ (Stdio - JSON-RPC 2.0)
   ┌────────────────────────────────────────────────────────┐
   │ IgnisEngine (Processo Headless)                        │
   │                                                        │
   │  ┌────────────────────────┐                            │
   │  │   StdioTransport       │                            │
   │  └──────────┬─────────────┘                            │
   │             ▼                                          │
   │  ┌────────────────────────┐                            │
   │  │   McpSyncServer        │                            │
   │  └──────────┬─────────────┘                            │
   │             ▼                                          │
   │  ┌────────────────────────┐                            │
   │  │   IgnisMcpBridge       ├───────┐ (runOnFxThread)    │
   │  └────────────────────────┘       │                    │
   │                                   ▼                    │
   │                       ┌──────────────────────┐         │
   │                       │ JavaFX Thread        │         │
   │                       │ (Scene, Compilador)  │         │
   │                       └──────────────────────┘         │
   └────────────────────────────────────────────────────────┘
```

### Thread-Safety e Integração JavaFX
O pipeline do JavaFX opera estritamente sob uma única thread principal (JavaFX Application Thread). Como o servidor MCP gerencia a escuta do canal Stdio em threads separadas, a classe `com.ignis.mcp.IgnisMcpBridge` encapsula o despacho seguro de tarefas síncronas utilizando `Platform.runLater` e sincronizacao via `CompletableFuture`. Isso evita excecoes de concorrência ao modificar a estrutura interna do projeto ou disparar compilacoes em threads secundarias.

---

## 2. Ponto de Entrada e Execução Headless

A inicializacao do servidor MCP foi acoplada ao ponto de entrada principal do editor do motor, na classe `com.ignis.editor.fx.IgnisEditorApp`.

### Argumentos de Inicialização
Para rodar o motor no modo MCP, deve-se passar o argumento `--mcp-server` seguido pelo caminho absoluto da pasta do projeto alvo:

```bash
java -jar IgnisEngine.jar --mcp-server "C:/caminhos/meu-projeto-ignis"
```

### Fluxo de Inicialização
1. **Verificação de Flag**: O metodo `main(String[] args)` do `IgnisEditorApp` faz o parse dos argumentos. Se a flag estiver presente, a interface grafica padrao do editor (janelas JavaFX) nao e exibida.
2. **Headless JavaFX**: O runtime do JavaFX e inicializado em segundo plano via `Platform.startup(() -> {})` para manter ativas as estruturas necessarias de gerenciamento de loops e bridges de UI.
3. **Silenciamento do Console**: A saida padrao do console e redirecionada para a saida de erros (`System.setOut(System.err)`). Isso e fundamental para evitar que logs aleatorios de depuracao do motor ou de bibliotecas de terceiros sejam despejados na saida padrao (stdout), o que corromperia o barramento de pacotes JSON-RPC do MCP.
4. **Instanciação do Servidor**: O `com.ignis.mcp.McpServerManager` e acionado, configurando o `StdioServerTransportProvider` e o mapeador Jackson, inicializando o servidor e registrando todas as ferramentas.

---

## 3. Módulos de Ferramentas Registrados

As ferramentas foram segmentadas em cinco classes especializadas sob o pacote `com.ignis.mcp.tools`:

### A. CoreTools (`com.ignis.mcp.tools.CoreTools`)
Garante controle estrutural sobre a arvore de arquivos e automacao do compilador integrado do IgnisEngine.
- `get_project_tree`: Varre e retorna recursivamente a hierarquia de pastas e arquivos do projeto (ignorando pastas compiladas ou temporarias).
- `create_script`: Cria um novo script Java no diretorio `scripts/` do projeto, usando o template basico da engine.
- `read_script_content`: Le e retorna o codigo-fonte completo de um script.
- `write_script_content`: Sobrescreve o codigo-fonte de um script Java existente.
- `compile_project`: Aciona o compilador JDK do `ScriptManager` para testar os scripts criados pelo agente.

### B. AudioTools (`com.ignis.mcp.tools.AudioTools`)
Fornece edicao de audio WAV PCM de 16 bits, estéreo, 44100Hz através do `WavAudioProcessor`.
- `read_wav_info`: Extrai duracao, taxas de amostragem e contagem de canais do arquivo de audio.
- `trim_wav`: Corta um segmento temporal do audio definindo pontos de inicio e fim em segundos.
- `apply_wav_fades`: Aplica fade-in e fade-out lineares no arquivo.
- `mix_wav_tracks`: Mixa multiplos arquivos WAV em posicoes temporais especificas em uma unica trilha master.

### C. ImageTools (`com.ignis.mcp.tools.ImageTools`)
Manipulacao de imagens baseado no modelo de camadas ARGB `ImageDocument`.
- `create_image_document`: Inicializa uma nova imagem em branco na memoria com largura e altura.
- `add_image_layer`: Cria uma camada de desenho nomeada.
- `import_image_to_layer`: Decodifica uma imagem em Base64 e a desenha em uma camada especifica com transparência.
- `composite_and_save_image`: Combina todas as camadas visiveis em SRC_OVER e salva como PNG no diretorio de assets do projeto.
- `save_flat_image_asset`: Salva dados Base64 diretamente em um arquivo PNG plano no projeto.

### D. NoteTools (`com.ignis.mcp.tools.NoteTools`)
Interage com o gerenciador de wiki do motor (anotacoes em arquivos JSON em `notes/`).
- `list_wiki_notes`: Retorna a lista de nomes de arquivos e titulos de notas disponiveis.
- `create_wiki_note`: Inicializa uma nova nota JSON contendo estrutura base.
- `read_wiki_note`: Retorna o titulo e conteudo (HTML/Texto) da pagina de anotações.
- `write_wiki_note`: Atualiza o titulo e conteudo HTML da nota.

### E. AnimationTools (`com.ignis.mcp.tools.AnimationTools`)
Permite estruturar configuracoes de animacao de sprites serializadas por `AnimationIO` (`.anim.json`).
- `list_animations`: Lista os nomes das animacoes configuradas, loop, easing e contagem de frames.
- `create_animation`: Inicializa um arquivo de animacao configurando loop e curvas de easing (LINEAR, EASE_IN, EASE_OUT, EASE_IN_OUT).
- `add_animation_frame`: Adiciona um frame de sprite na timeline da animacao com duracao especifica em segundos.
- `read_animation_json`: Retorna a representacao JSON crua da animacao.

---

## 4. Integração de Clientes Externos (Configuração)

Para configurar uma IA cliente (como o Claude Desktop) para usar o servidor MCP do IgnisEngine, adicione a seguinte configuracao ao arquivo `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "ignis-engine": {
      "command": "java",
      "args": [
        "-jar",
        "C:/Users/thyag/OneDrive/Desktop/IgnisEngine-main/target/ignis-engine-1.0.0.jar",
        "--mcp-server",
        "C:/Users/thyag/OneDrive/Desktop/IgnisEngine-main/project"
      ]
    }
  }
}
```

---

## 5. Autoria e Licença

Todo o modulo e especificacoes do MCP no IgnisEngine foram desenhados e implementados em conformidade com as regras do motor.

- **Autor**: ThyagoToledo
- **Licenca**: Reservada / IgnisEngine Corp.
