---
tags: [ia-local, blackhole-agent, comandos, cli, obsidian]
updated: 2026-06-21
---

## Definição

Os **Comandos de Barra** (Slash Commands) do BlackHole-Agent fornecem atalhos e utilitários interativos inspirados em assistentes de terminal modernos (como o ClaudeCode). Eles permitem gerenciar o histórico do chat, ler arquivos locais, disparar pesquisas diretas e alternar dinamicamente os modelos de Inteligência Artificial em tempo de execução.

## Contexto

Utilizados diretamente na interface de terminal do assistente (`agent.bat`). Os comandos interceptam o texto digitado pelo usuário antes de ser enviado à inferência do modelo local, economizando tempo de CPU/GPU e garantindo controle absoluto do contexto.

## Detalhes

### 💡 1. Tabela de Comandos de Barra

| Comando | Descrição | Exemplo de Uso |
| :--- | :--- | :--- |
| **`/help`** ou **`/?`** | Exibe a lista de comandos e explicações. | `/help` |
| **`/model`** | Lista os modelos locais suportados, suas dicas e indica qual está ativo. | `/model` |
| **`/model [ID]`** | Alterna dinamicamente o modelo de IA ativo. | `/model 2` |
| **`/clear`** | Limpa todo o histórico de conversas (retendo apenas o prompt do sistema). | `/clear` |
| **`/status`** | Exibe detalhes técnicos: modelo ativo, dispositivo (CPU/CUDA), número de mensagens e RAM estimada. | `/status` |
| **`/vault`** | Executa diretamente a leitura da estrutura de arquivos catalogados no vault. | `/vault` |
| **`/read [nota]`** | Abre e exibe o conteúdo de um arquivo do vault diretamente no console. | `/read 00_MOC.md` |
| **`/search [termo]`** | Dispara o fluxo de busca na web e compilação de notas no vault imediatamente. | `/search React Hooks` |
| **`/write [arq]`** | Cria ou edita um arquivo de script diretamente a partir da entrada do terminal. | `/write script.py` |
| **`/run [cmd]`** | Executa um comando do sistema operacional (útil para compilar/testar scripts). | `/run python script.py` |
| **`/video`** | Automatiza a edição de vídeo: corte de silêncio e inserção de legendas via FFmpeg. | `/video silences bruto.mp4` |
| **`/sair`** ou **`/exit`** | Salva a memória de diálogo e encerra o terminal de forma limpa. | `/sair` |

---

### 🧠 2. Catálogo de Modelos e Dicas de Utilidade

A alternância dinâmica de modelos permite adequar a IA à tarefa sem reiniciar a CLI. Cada modelo possui uma dica visual para guiar o desenvolvedor:

1.  **`Qwen/Qwen2.5-Coder-0.5B-Instruct`**
    *   **Dica**: `[Geral/Código - Rápido e ultra leve (500M) - Padrão]`
    *   **Uso Ideal**: Consultas rápidas, navegação de notas e execução em máquinas com pouca RAM (~2.3 GB RAM consumidos na CPU).
2.  **`Qwen/Qwen2.5-Coder-1.5B-Instruct`**
    *   **Dica**: `[Código/Raciocínio Avançado - Recomendado (1.5B)]`
    *   **Uso Ideal**: Desenvolvimento complexo, depuração de códigos e maior aderência ao formato JSON de ferramentas (~4.5 GB RAM na CPU).
3.  **`meta-llama/Llama-3.2-1B-Instruct`**
    *   **Dica**: `[Escrita/Conversação Geral - Respostas mais fluídas (1B)]`
    *   **Uso Ideal**: Redação de resumos, tradução ou conversações longas (~3.8 GB RAM na CPU).

> [!IMPORTANT]
> **Liberando RAM Ativamente**: Ao digitar `/model [ID]`, o script executa descarregamento ativo de memória (`del self.model`, `gc.collect()`, `empty_cache()`) para evitar que dois modelos coexistam na RAM, mantendo o consumo sob controle.

---

### 🎨 3. Autocompletação e Ghost-Text Interativos (UX Premium)

Integrado via biblioteca `prompt_toolkit`, a entrada de dados do BlackHole-Agent oferece recursos profissionais de UX:
1.  **Menu Dropdown Popup**: Ao iniciar um input com `/`, a CLI abre uma lista com todos os comandos disponíveis. Você pode navegar com as setas para cima/baixo e pressionar `Enter` para selecionar.
2.  **Ghost-Text (Sugestão Inline)**: Ao digitar as primeiras letras de um comando (ex: `/s`), o terminal exibe o restante do comando em cinza transparente (`tatus` ou `earch`). Pressione a **Seta para a Direita** ou a tecla **End** para aceitar a sugestão instantaneamente.
3.  **Histórico Navegável**: Pressionando a **Seta para Cima** no prompt em branco, é possível navegar por todas as mensagens enviadas na sessão corrente, agilizando tarefas repetitivas.

## Links

- [[00_MOC]]
- [[concepts/blackhole-agent-autonomia]]
- [[concepts/blackhole-agent-ui-premium]]
- [[concepts/agent-cerebro-otimizacao-memoria]]
