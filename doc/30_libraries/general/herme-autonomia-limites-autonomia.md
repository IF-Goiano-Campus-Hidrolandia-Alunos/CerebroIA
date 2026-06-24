---
tags: [hermes, prompt, function-calling, autonomia]
context: "Base de Conhecimento PlantiuIA - Fase 4"
description: "Configuração de travas duras onde o Hermes é proibido de agir sem autorização (ex: transações financeiras)."
---

# Definição de Limites de Autonomia

## Contexto Geral
Esta documentação técnica faz parte do vault especializado em engenharia de software e inteligência artificial da PlantiuIA.

## Definição e Conceito
Configuração de travas duras onde o Hermes é proibido de agir sem autorização (ex: transações financeiras).

No desenvolvimento de sistemas complexos e otimizados, este conceito atua como pilar de engenharia para viabilizar inferências locais ágeis ou interações autônomas confiáveis de agentes inteligentes.

## Exemplo Prático de Código / Implementação

```python
# Exemplo técnico prático de: Definição de Limites de Autonomia
requires_signoff = ['make_payment', 'delete_database']
```

## Notas Adicionais e Boas Práticas
- Garanta que este módulo passe por etapas de validação em sandbox antes da promoção para produção.
- Limite a quantidade de acessos à memória para evitar gargalos na CPU ou NPU local.
- Mantenha logs legíveis e estruturados para depuração.
