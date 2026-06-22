---
tags: [ia-local, blackhole-agent, ui, prompt-toolkit, terminal]
updated: 2026-06-21
---

## Definição

A **Interface de Usuário Premium (UX CLI)** do BlackHole-Agent é a camada visual e de entrada construída sobre o console do sistema operacional (CMD/PowerShell) para fornecer feedback visual avançado, autocompletação em tempo real e interatividade de comandos.

## Contexto

Garante que o desenvolvedor tenha uma experiência limpa e fluida (estilo Claude/Hermes), sem logs poluídos de bibliotecas de IA e com atalhos de autocompletar que eliminam erros de digitação.

## Detalhes

### 🌌 1. Estética e Logotipo ASCII (Gargantua)
*   **Arte Braille Unicode**: Desenha o buraco negro Gargantua no terminal clássico mapeando pixels para caracteres Braille (`U+2800` a `U+28FF`), atingindo uma resolução gráfica maior que a de caracteres comuns.
*   **Gradientes ANSI**: Aplica cores em degradê (tons de cinza escuro, azul, ciano, magenta e amarelo) para criar a ilusão de iluminação do disco de acreção.

### 🎨 2. Autocompletar Dropdown & Ghost-Text
A entrada é controlada pela biblioteca `prompt_toolkit`.
*   **Completer Dropdown (`SlashCommandCompleter`)**: Quando o usuário insere `/`, o terminal abre uma lista popup estilizada com os comandos disponíveis. O menu é navegado via setas do teclado e aceito com `Enter`. Diferente de completadores comuns, ele se ativa estritamente ao digitar `/` na raiz do input, evitando popups intrusivos durante o texto comum da conversa.
*   **Ghost-Text (`CommandAutoSuggest`)**: À medida que o usuário escreve, o restante do comando correspondente aparece em cinza transparente (ex: `/s` -> mostra `tatus` ou `earch`). O usuário aceita instantaneamente pressionando a **Seta Direita** ou a tecla **End**.
*   **Estilo Premium**: O menu de seleção foi estilizado com cores condizentes à estética BlackHole:
    ```python
    style = Style.from_dict({
        'completion-menu.completion': 'bg:#1e1e2e fg:#cdd6f4',
        'completion-menu.completion.current': 'bg:#89b4fa fg:#11111b bold',
        'scrollbar.background': 'bg:#313244',
        'scrollbar.button': 'bg:#f5c2e7',
    })
    ```

### 🔇 3. Supressão de Logs e Progress Bars
Para evitar que barras de download de pesos (`Loading weights`, downloads de tensores) ou warnings de tokenizador quebrem o spinner de carregamento na tela, as seguintes diretrizes são forçadas no início do processo:
- `HF_HUB_DISABLE_PROGRESS_BARS = 1`: Oculta progress bars de download de rede.
- `TRANSFORMERS_NO_ADVISORY_WARNINGS = 1`: Oculta warnings internos do tokenizer do Hugging Face.
- `TOKENIZERS_PARALLELISM = false`: Desabilita forks paralelos do tokenizador que geram avisos no terminal.

## Links

- [[00_MOC]]
- [[concepts/blackhole-agent-comandos]]
- [[concepts/blackhole-agent-autonomia]]
