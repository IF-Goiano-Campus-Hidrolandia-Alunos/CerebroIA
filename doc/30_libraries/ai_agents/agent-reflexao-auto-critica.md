---
tags: [agente, design, workflow, reflexao]
context: "Base de Conhecimento PlantiuIA - Fase 4"
description: "Etapa do loop onde o agente avalia o próprio resultado preliminar antes de enviá-lo ao usuário."
---

# Mecanismo de Auto-Crítica (Self-Criticism)

## Contexto Geral
Esta documentação técnica faz parte do vault especializado em engenharia de software e inteligência artificial da PlantiuIA.

## Definição e Conceito
Etapa do loop onde o agente avalia o próprio resultado preliminar antes de enviá-lo ao usuário.

No desenvolvimento de sistemas complexos e otimizados, este conceito atua como pilar de engenharia para viabilizar inferências locais ágeis ou interações autônomas confiáveis de agentes inteligentes.

## Exemplo Prático de Código / Implementação

```python
# Exemplo técnico prático de: Mecanismo de Auto-Crítica (Self-Criticism)
evaluation = evaluate_answer(raw_answer)
if evaluation.score < 0.8:
    raw_answer = refine_answer(raw_answer, evaluation.critique)
```

## Notas Adicionais e Boas Práticas
- Garanta que este módulo passe por etapas de validação em sandbox antes da promoção para produção.
- Limite a quantidade de acessos à memória para evitar gargalos na CPU ou NPU local.
- Mantenha logs legíveis e estruturados para depuração.
