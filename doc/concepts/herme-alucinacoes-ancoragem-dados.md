---
tags: [hermes, prompt, function-calling, alucinacoes]
context: "Base de Conhecimento PlantiuIA - Fase 4"
description: "Processo de forçar o Hermes a apenas responder baseando-se em fatos recuperados em tempo de execução."
---

# Grounding e Ancoragem de Dados

## Contexto Geral
Esta documentação técnica faz parte do vault especializado em engenharia de software e inteligência artificial da PlantiuIA.

## Definição e Conceito
Processo de forçar o Hermes a apenas responder baseando-se em fatos recuperados em tempo de execução.

No desenvolvimento de sistemas complexos e otimizados, este conceito atua como pilar de engenharia para viabilizar inferências locais ágeis ou interações autônomas confiáveis de agentes inteligentes.

## Exemplo Prático de Código / Implementação

```python
# Exemplo técnico prático de: Grounding e Ancoragem de Dados
grounding_prompt = "Se a resposta não estiver no contexto, diga claramente que não sabe."
```

## Notas Adicionais e Boas Práticas
- Garanta que este módulo passe por etapas de validação em sandbox antes da promoção para produção.
- Limite a quantidade de acessos à memória para evitar gargalos na CPU ou NPU local.
- Mantenha logs legíveis e estruturados para depuração.
