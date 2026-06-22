---
tags: [hermes, prompt, function-calling, prompts]
context: "Base de Conhecimento PlantiuIA - Fase 4"
description: "Uso correto dos tokens `<|im_end|>` e delimitadores XML como chaves para cortar a inferência no momento exato."
---

# Configuração de Tokens de Parada (Stop Tokens)

## Contexto Geral
Esta documentação técnica faz parte do vault especializado em engenharia de software e inteligência artificial da PlantiuIA.

## Definição e Conceito
Uso correto dos tokens `<|im_end|>` e delimitadores XML como chaves para cortar a inferência no momento exato.

No desenvolvimento de sistemas complexos e otimizados, este conceito atua como pilar de engenharia para viabilizar inferências locais ágeis ou interações autônomas confiáveis de agentes inteligentes.

## Exemplo Prático de Código / Implementação

```python
# Exemplo técnico prático de: Configuração de Tokens de Parada (Stop Tokens)
stop_tokens = ["<|im_end|>", "</tool_call>"]
```

## Notas Adicionais e Boas Práticas
- Garanta que este módulo passe por etapas de validação em sandbox antes da promoção para produção.
- Limite a quantidade de acessos à memória para evitar gargalos na CPU ou NPU local.
- Mantenha logs legíveis e estruturados para depuração.
