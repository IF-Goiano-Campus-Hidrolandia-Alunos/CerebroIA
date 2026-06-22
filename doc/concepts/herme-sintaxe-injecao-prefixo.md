---
tags: [hermes, prompt, function-calling, sintaxe]
context: "Base de Conhecimento PlantiuIA - Fase 4"
description: "Forçar as primeiras palavras da resposta do assistente (ex: abrindo a tag <thought>) para guiar o início da inferência."
---

# Técnicas de Injeção de Prefixo de Resposta

## Contexto Geral
Esta documentação técnica faz parte do vault especializado em engenharia de software e inteligência artificial da PlantiuIA.

## Definição e Conceito
Forçar as primeiras palavras da resposta do assistente (ex: abrindo a tag <thought>) para guiar o início da inferência.

No desenvolvimento de sistemas complexos e otimizados, este conceito atua como pilar de engenharia para viabilizar inferências locais ágeis ou interações autônomas confiáveis de agentes inteligentes.

## Exemplo Prático de Código / Implementação

```python
# Exemplo técnico prático de: Técnicas de Injeção de Prefixo de Resposta
assistant_prefix = "<|im_start|>assistant\n<thought>"
```

## Notas Adicionais e Boas Práticas
- Garanta que este módulo passe por etapas de validação em sandbox antes da promoção para produção.
- Limite a quantidade de acessos à memória para evitar gargalos na CPU ou NPU local.
- Mantenha logs legíveis e estruturados para depuração.
