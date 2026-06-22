---
tags: [hermes, prompt, function-calling, alucinacoes]
context: "Base de Conhecimento PlantiuIA - Fase 4"
description: "Algoritmo de validação que estima a porcentagem de sentenças geradas pelo modelo que estão presentes no contexto original."
---

# Cálculo de Groundedness Score

## Contexto Geral
Esta documentação técnica faz parte do vault especializado em engenharia de software e inteligência artificial da PlantiuIA.

## Definição e Conceito
Algoritmo de validação que estima a porcentagem de sentenças geradas pelo modelo que estão presentes no contexto original.

No desenvolvimento de sistemas complexos e otimizados, este conceito atua como pilar de engenharia para viabilizar inferências locais ágeis ou interações autônomas confiáveis de agentes inteligentes.

## Exemplo Prático de Código / Implementação

```python
# Exemplo técnico prático de: Cálculo de Groundedness Score
groundedness_score = count_supported_sentences(answer) / total_sentences
```

## Notas Adicionais e Boas Práticas
- Garanta que este módulo passe por etapas de validação em sandbox antes da promoção para produção.
- Limite a quantidade de acessos à memória para evitar gargalos na CPU ou NPU local.
- Mantenha logs legíveis e estruturados para depuração.
