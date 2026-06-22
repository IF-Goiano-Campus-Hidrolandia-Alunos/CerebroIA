---
tags: [hermes, prompt, function-calling, prompts]
context: "Base de Conhecimento PlantiuIA - Fase 4"
description: "Melhores práticas para envolver a entrada do usuário com tags de contexto para evitar confusão de instrução (jailbreak)."
---

# Estruturação de Query do Usuário

## Contexto Geral
Esta documentação técnica faz parte do vault especializado em engenharia de software e inteligência artificial da PlantiuIA.

## Definição e Conceito
Melhores práticas para envolver a entrada do usuário com tags de contexto para evitar confusão de instrução (jailbreak).

No desenvolvimento de sistemas complexos e otimizados, este conceito atua como pilar de engenharia para viabilizar inferências locais ágeis ou interações autônomas confiáveis de agentes inteligentes.

## Exemplo Prático de Código / Implementação

```python
# Exemplo técnico prático de: Estruturação de Query do Usuário
user_prompt = f"<user_query>{user_input}</user_query>"
```

## Notas Adicionais e Boas Práticas
- Garanta que este módulo passe por etapas de validação em sandbox antes da promoção para produção.
- Limite a quantidade de acessos à memória para evitar gargalos na CPU ou NPU local.
- Mantenha logs legíveis e estruturados para depuração.
