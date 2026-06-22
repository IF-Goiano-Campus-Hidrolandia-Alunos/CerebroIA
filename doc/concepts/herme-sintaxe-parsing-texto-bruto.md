---
tags: [hermes, prompt, function-calling, sintaxe]
context: "Base de Conhecimento PlantiuIA - Fase 4"
description: "Expressões regulares e tratamentos de string para limpar tokens residuais de formatação que vazam na saída da API."
---

# Parsing de Saída ChatML Bruta

## Contexto Geral
Esta documentação técnica faz parte do vault especializado em engenharia de software e inteligência artificial da PlantiuIA.

## Definição e Conceito
Expressões regulares e tratamentos de string para limpar tokens residuais de formatação que vazam na saída da API.

No desenvolvimento de sistemas complexos e otimizados, este conceito atua como pilar de engenharia para viabilizar inferências locais ágeis ou interações autônomas confiáveis de agentes inteligentes.

## Exemplo Prático de Código / Implementação

```python
# Exemplo técnico prático de: Parsing de Saída ChatML Bruta
clean_output = raw_output.replace("<|im_end|>", "").strip()
```

## Notas Adicionais e Boas Práticas
- Garanta que este módulo passe por etapas de validação em sandbox antes da promoção para produção.
- Limite a quantidade de acessos à memória para evitar gargalos na CPU ou NPU local.
- Mantenha logs legíveis e estruturados para depuração.
