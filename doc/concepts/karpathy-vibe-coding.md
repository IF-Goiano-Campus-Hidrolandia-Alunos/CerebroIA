---
tags: [metodo, ia, llm, workflow, karpathy, vibe-coding]
updated: 2026-06-14
---

## Definição

"Vibe coding" (termo de Andrej Karpathy, 2025): programar descrevendo a intenção em linguagem natural para um LLM, aceitar as sugestões e iterar por feedback, sem ler o código de perto.

## Contexto

Estilo para prototipagem rápida e projetos descartáveis/fim de semana. Para o IgnisEngine, aplica-se ao fluxo de desenvolvimento assistido por IA. Ver [[concepts/ignisengine-ai-integration]] e [[concepts/token-optimization]].

## Princípios

- Descrever o que quer em linguagem natural (até por voz); deixar o LLM gerar.
- Aceitar diffs, rodar, colar o erro de volta, repetir — iteração rápida.
- Não revisar cada linha; tratar o código como meio, não como artefato a estudar.
- Trocar de abordagem quando travar, em vez de depurar a fundo.

## Quando usar / Quando NÃO usar

- Bom: protótipos, MVPs, scripts, explorar ideias, ferramentas internas.
- Evitar: código crítico/produção, segurança, partes que exigem entendimento profundo e manutenção longa.

## Riscos

- Perda de entendimento do próprio código (dívida de conhecimento).
- Depuração por tentativa e erro; bugs sutis passam.
- Acúmulo de código não compreendido; difícil manter/escalar.
- Mitigação: revisar e testar antes de promover de protótipo a produção; pedir explicação do código ao LLM.

## Links

- [[concepts/ignisengine-ai-integration]]
- [[concepts/token-optimization]]
