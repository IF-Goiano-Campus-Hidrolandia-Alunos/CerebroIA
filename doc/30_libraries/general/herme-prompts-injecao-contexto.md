---
tags: [hermes, prompt, function-calling, prompts]
context: "Base de Conhecimento PlantiuIA - Fase 4"
description: "Técnica para injetar manuais técnicos no prompt de forma que o Hermes priorize as regras do manual sobre seu conhecimento prévio."
---

# Injeção Segura de Contextos de Documentação

## Contexto Geral
Esta documentação técnica faz parte do vault especializado em engenharia de software e inteligência artificial da PlantiuIA.

## Definição e Conceito
Técnica para injetar manuais técnicos no prompt de forma que o Hermes priorize as regras do manual sobre seu conhecimento prévio.

No desenvolvimento de sistemas complexos e otimizados, este conceito atua como pilar de engenharia para viabilizar inferências locais ágeis ou interações autônomas confiáveis de agentes inteligentes.

## Exemplo Prático de Código / Implementação

```python
# Exemplo técnico prático de: Injeção Segura de Contextos de Documentação
context_prompt = f"<manual>{retrieved_doc}</manual>"
```

## Notas Adicionais e Boas Práticas
- Garanta que este módulo passe por etapas de validação em sandbox antes da promoção para produção.
- Limite a quantidade de acessos à memória para evitar gargalos na CPU ou NPU local.
- Mantenha logs legíveis e estruturados para depuração.
