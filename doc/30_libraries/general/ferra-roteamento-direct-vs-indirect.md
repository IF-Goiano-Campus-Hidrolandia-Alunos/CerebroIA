---
tags: [mcp, ferramentas, sandbox, roteamento]
context: "Base de Conhecimento PlantiuIA - Fase 4"
description: "Estratégia para decidir se o agente chama a ferramenta sem permissão (direta) ou precisa de aviso visual (indireta)."
---

# Chamada de Ferramenta Direta vs Indireta

## Contexto Geral
Esta documentação técnica faz parte do vault especializado em engenharia de software e inteligência artificial da PlantiuIA.

## Definição e Conceito
Estratégia para decidir se o agente chama a ferramenta sem permissão (direta) ou precisa de aviso visual (indireta).

No desenvolvimento de sistemas complexos e otimizados, este conceito atua como pilar de engenharia para viabilizar inferências locais ágeis ou interações autônomas confiáveis de agentes inteligentes.

## Exemplo Prático de Código / Implementação

```python
# Exemplo técnico prático de: Chamada de Ferramenta Direta vs Indireta
is_direct = tool_metadata.trust_level == 'trusted'
```

## Notas Adicionais e Boas Práticas
- Garanta que este módulo passe por etapas de validação em sandbox antes da promoção para produção.
- Limite a quantidade de acessos à memória para evitar gargalos na CPU ou NPU local.
- Mantenha logs legíveis e estruturados para depuração.
