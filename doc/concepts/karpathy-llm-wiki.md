---
tags: [metodo, ia, llm, vault, knowledge-base, karpathy, token-economy]
updated: 2026-06-14
source: https://github.com/julianoczkowski/karpathy-llm-wiki
---

## Definição

"LLM Wiki Pattern" (Andrej Karpathy, abr/2026): base de conhecimento em arquivos markdown mantida pelo proprio LLM, que substitui RAG/vector DB e reduz drasticamente o uso de tokens (relato real: -95% vs RAG ingenuo).

## Contexto

Para agentes (ex: Claude Code) navegarem conhecimento lendo so o necessario. Casa com este Vault. Ver [[concepts/vault-system]] e [[concepts/token-optimization]].

## Estrutura de pastas

- `raw/` — documentos-fonte brutos; nunca modificados apos ingestao (arquivo/fonte da verdade; toda pagina do wiki rastreia ate aqui).
- `wiki/` — markdown que o LLM mantem por completo: paginas de entidade, paginas de conceito, resumos, index e log.
- `index.md` — indice de navegacao (carregado primeiro; aponta para as paginas).
- `log.md` — registro do que foi ingerido/alterado.
- `CLAUDE.md` (Claude Code) ou `AGENTS.md` (Codex) — config que transforma o agente num mantenedor disciplinado do wiki: como estruturar paginas, como ingerir novas fontes, como formatar respostas.

## Economia de tokens

- O agente le `index.md` (pequeno) e abre so a pagina especifica → contexto minimo.
- Limite pratico: confiavel abaixo de ~50k–100k tokens de conteudo compilado; acima disso o proprio `index.md` deixa de caber num unico contexto (precisa dividir/hierarquizar indices).

## Aplicacao ao nosso Vault

- Ja temos o equivalente: `00_MOC.md` = index; `concepts/`+`workflows/` = wiki; regra "Check Local First" = ler index + pagina especifica.
- Para alinhar 100% ao padrao Karpathy faltaria: pasta `raw/` (fontes brutas imutaveis), um `log.md`, e um arquivo de config de mantenedor (skill vault-manager ja cumpre parte disso).

## Links

- [[concepts/vault-system]]
- [[concepts/token-optimization]]
