---
tags: [ai, llm, optimization, tokens, prompts]
updated: 2026-06-21
---

## Definição

Guia prático de otimização de contexto e uso de tokens para interações de desenvolvimento com IAs (como Claude e ChatGPT).

## Contexto

LLMs possuem limites de contexto de entrada e saída (input/output tokens) e cobram por isso. Manter o prompt limpo, focado e usar referências locais diminui o consumo redundante em até 95%.

## Práticas Recomendadas

### 1. Instruções para Alteração de Código (Modo de Diffs)
Ao solicitar ou escrever alterações em arquivos extensos:
- **Evite reescrever o arquivo inteiro**: Peça apenas blocos diff padrão (com `+` e `-` ou chunks direcionados). Reescrever um arquivo de 1000 linhas consome milhares de tokens de saída redundantes.
- **Peça blocos focados**: Exemplo: "Altere apenas a função `initCharts` no arquivo X, mantendo o restante inalterado".

### 2. Hierarquia de Contexto (Hot vs Warm vs Cold)
- **Hot (Uso Imediato)**: O arquivo `CLAUDE.md` e a tarefa ativa atual (`task.md`).
- **Warm (Referências)**: Notas do vault (como `doc/concepts/` e schemas do Drizzle). A IA deve ler apenas a nota específica usando links diretos, e não o repositório inteiro.
- **Cold (Histórico)**: Documentação antiga ou relatórios antigos. Devem ser compactados ou referenciados apenas por IDs/hashes.

### 3. Redução de Ruído no Prompt
- **Sem floreios**: Escreva em formato bullet points. IAs processam melhor e consomem menos tokens se eliminarmos textos introdutórios/conclusivos inúteis.
- **MCP (Model Context Protocol)**: Utilize MCP para que a IA busque diretamente o arquivo ou linha necessária (usando grep/search) em vez de ler o diretório todo.

### 4. Economia de Tokens com Prompt Caching
- **Regras Estáveis no Início**: Modelos modernos (como Claude 3.5/4) cacheiam o contexto que não muda frequentemente. Coloque os esquemas de banco de dados (`schema.ts`) e o `CLAUDE.md` no início da mensagem para aproveitar o cache de prompt (reduz o custo em até 90%).

---

## Links

- [[concepts/vault-system]]
- [[concepts/token-optimization]]
- [[concepts/protocolo-handoff-sessao]]
