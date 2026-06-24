---
tags: [hermes, prompt, function-calling, sintaxe]
context: "Base de Conhecimento PlantiuIA - Fase 4"
description: "Formatação correta para alimentar o modelo com o resultado de uma chamada de ferramenta no formato ChatML."
---

# Sintaxe para Envio de Resultados de Ferramentas

## Contexto Geral
Esta documentação técnica faz parte do vault especializado em engenharia de software e inteligência artificial da PlantiuIA.

## Definição e Conceito
Formatação correta para alimentar o modelo com o resultado de uma chamada de ferramenta no formato ChatML.

No desenvolvimento de sistemas complexos e otimizados, este conceito atua como pilar de engenharia para viabilizar inferências locais ágeis ou interações autônomas confiáveis de agentes inteligentes.

## Exemplo Prático de Código / Implementação

```python
# Exemplo técnico prático de: Sintaxe para Envio de Resultados de Ferramentas
tool_result_block = "<|im_start|>tool\n{\"result\": \"sucesso\"}<|im_end|>"
```

## Notas Adicionais e Boas Práticas
- Garanta que este módulo passe por etapas de validação em sandbox antes da promoção para produção.
- Limite a quantidade de acessos à memória para evitar gargalos na CPU ou NPU local.
- Mantenha logs legíveis e estruturados para depuração.
