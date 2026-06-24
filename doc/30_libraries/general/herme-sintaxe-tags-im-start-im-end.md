---
tags: [hermes, prompt, function-calling, sintaxe]
context: "Base de Conhecimento PlantiuIA - Fase 4"
description: "Como delimitar fisicamente os papéis da conversa no payload de entrada enviado ao motor de inferência."
---

# Uso das Tags Especiais im_start e im_end

## Contexto Geral
Esta documentação técnica faz parte do vault especializado em engenharia de software e inteligência artificial da PlantiuIA.

## Definição e Conceito
Como delimitar fisicamente os papéis da conversa no payload de entrada enviado ao motor de inferência.

No desenvolvimento de sistemas complexos e otimizados, este conceito atua como pilar de engenharia para viabilizar inferências locais ágeis ou interações autônomas confiáveis de agentes inteligentes.

## Exemplo Prático de Código / Implementação

```python
# Exemplo técnico prático de: Uso das Tags Especiais im_start e im_end
system_block = "<|im_start|>system\n{system_prompt}<|im_end|>"
```

## Notas Adicionais e Boas Práticas
- Garanta que este módulo passe por etapas de validação em sandbox antes da promoção para produção.
- Limite a quantidade de acessos à memória para evitar gargalos na CPU ou NPU local.
- Mantenha logs legíveis e estruturados para depuração.
