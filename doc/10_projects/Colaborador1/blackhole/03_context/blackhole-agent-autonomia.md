---
tags: [ia-local, blackhole-agent, otimizacao, qwen, obsidian, autonomia]
updated: 2026-06-21
---

## Definição

O **BlackHole-Agent** (anteriormente conhecido como *Agente Cérebro*) é o assistente local integrado ao ecossistema PlantiuIA. Esta nota detalha as decisões de design, escolha do modelo, técnicas de mitigação de recusa (autonomia) e mapeamento de ferramentas no terminal.

## Contexto

Aplicado na execução offline do assistente via terminal (`agent.bat`). Destinado a desenvolvedores que precisam de buscas, consultas de notas e pesquisas web offline-first diretamente vinculadas ao Obsidian Vault.

## Detalhes

### 🌌 1. Identidade: BlackHole-Agent
O agente foi renomeado de *Agente Cérebro* para **BlackHole-Agent**, com uma interface inspirada na singularidade e estética terminal premium (buraco negro em ASCII/Braille Art). 
- A interface de boas-vindas exibe o cabeçalho `🌌 BLACKHOLE-AGENT v2.2`.
- As caixas de resposta e spinners de carregamento mostram `BlackHole-Agent`.

### 🧠 2. Escolha e Comparação de Modelos Locais
O agente roda localmente na CPU/GPU. A tabela abaixo detalha as opções disponíveis na família Qwen2.5-Coder (atualmente a melhor para tool-calling em escala reduzida):

| Modelo | Parâmetros | RAM (Torch float32 CPU) | RAM (Ollama / GGUF Q4_K_M) | Inteligência / Tool-calling |
| :--- | :--- | :--- | :--- | :--- |
| **Qwen2.5-Coder-0.5B-Instruct** (Atual) | 500M | ~2.3 GB | ~600 MB | Baixa/Média (requer ajuda de fuzzy parser e injeção) |
| **Qwen2.5-Coder-1.5B-Instruct** (Upgrade) | 1.5B | ~4.5 GB | ~1.2 GB | Alta (ótimo suporte a JSON e ferramentas nativas) |

> [!TIP]
> **Recomendação**: Para o menor consumo e melhor desempenho possível em CPU, é altamente recomendada a instalação do **Ollama** executando `qwen2.5-coder:1.5b`. A quantização de 4 bits nativa do Ollama permite rodar um modelo 3x mais inteligente consumindo apenas **1.2 GB** de RAM, eliminando completamente loops cognitivos.

### ⚙️ 3. Otimizações de Autonomia e Compatibilidade

Para garantir que o modelo pequeno de 500M (0.5B) funcione com autonomia similar a assistentes maiores (como o ClaudeCode), as seguintes técnicas foram implementadas no wrapper Python (`scripts/brain_researcher.py`):

1. **Prevenção de Recusas de Segurança (Refusal Bypassing)**:
   Modelos pequenos sofrem de alinhamento de segurança rígido que os faz recusar chamadas dizendo *"como assistente de IA, não tenho acesso a arquivos locais"*. 
   - **Solução**: O histórico é filtrado a cada turno para remover mensagens antigas de recusa da IA, prevenindo o "context locking" (onde a IA repete a recusa só porque viu que recusou no passado).
   - O prompt de sistema foi reforçado instruindo explicitamente o modelo de que ele possui ferramentas reais integradas.

2. **Normalização Heurística de Sintaxe e Tradução de Caracteres (Fuzzy Tool Matcher)**:
   Devido às limitações de tamanho de parâmetros, o modelo de 0.5B frequentemente comete erros ortográficos, muda a capitalização ou até utiliza caracteres cirílicos equivalentes gerados por erros de mapeamento do tokenizador (ex: `[LISTAR_VАULT]` contendo 'А' cirílico, ou `[ListAR_VUAULT]`).
   - **Solução**: Implementamos um normalizador de string inteligente (`detect_and_normalize_tool_call`) que traduz caracteres homóglifos cirílicos para latinos, remove emojis, converte a ação para maiúsculas e utiliza busca difusa (heurística) para inferir o comando correto (`LISTAR_VAULT`, `LER_NOTA` ou `PESQUISAR_TEMA`).

3. **Auto-Correção Inteligente de Nomes de Notas (Autocorrect Note Name)**:
   Caso o modelo tente ler uma nota digitando o nome incorretamente (ex: `TESTe_DO_Vaul.md` em vez de `TESTE_DO_Vault.md`), o normalizador executa uma busca por similaridade (`find_closest_note_name`) listando os arquivos markdown reais do vault e fazendo o match com o arquivo real mais provável, garantindo que o comando execute com sucesso sem emitir erros ao usuário.

4. **Injeção Dinâmica de Contexto do Vault (RAG Proativo)**:
   Interceptamos a entrada do usuário e, se contiver palavras-chave como "vault", "readme", "moc", "arquivos", etc., injetamos proativamente a lista de arquivos reais em uma mensagem de sistema no histórico. Isso dá à IA visibilidade total de arquivos existentes e evita que ela alucine nomes de arquivos ou alegue falta de acesso.

5. **Silenciamento Absoluto de Dependências**:
   Definido `HF_HUB_DISABLE_PROGRESS_BARS=1` e `TRANSFORMERS_NO_ADVISORY_WARNINGS=1` para evitar que barras de download e warnings poluam o terminal durante a inferência.

## Links

- [[00_MOC]]
- [[10_projects/Colaborador1/blackhole/03_context/blackhole-agent-comandos]]
- [[30_libraries/ai_agents/agent-cerebro-otimizacao-memoria]]
- [[30_libraries/general/quantizacao-modelos-ia]]
