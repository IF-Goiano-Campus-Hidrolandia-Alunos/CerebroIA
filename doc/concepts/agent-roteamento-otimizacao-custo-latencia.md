---
tags: [agente, design, workflow, roteamento]
context: "Base de Conhecimento PlantiuIA - Fase 4"
description: "Algoritmo para escolher entre LLMs pequenos locais ou LLMs robustos em nuvem dependendo da complexidade do prompt."
---

# Otimização Multicritério de Custo-Latência

## Contexto Geral
Esta documentação técnica faz parte do vault especializado em engenharia de software e inteligência artificial da PlantiuIA.

## Definição e Conceito
Algoritmo para escolher entre LLMs pequenos locais ou LLMs robustos em nuvem dependendo da complexidade do prompt.

No desenvolvimento de sistemas complexos e otimizados, este conceito atua como pilar de engenharia para viabilizar inferências locais ágeis ou interações autônomas confiáveis de agentes inteligentes.

## Exemplo Prático de Código / Implementação

```python
# Exemplo técnico prático de: Otimização Multicritério de Custo-Latência
model = "local_llama3" if request_complexity == 'low' else "gpt4_cloud"
```

## Notas Adicionais e Boas Práticas
- Garanta que este módulo passe por etapas de validação em sandbox antes da promoção para produção.
- Limite a quantidade de acessos à memória para evitar gargalos na CPU ou NPU local.
- Mantenha logs legíveis e estruturados para depuração.
