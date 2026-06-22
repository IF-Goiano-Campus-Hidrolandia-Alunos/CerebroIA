---
tags: ['agronomymetricssoil', 'documentacao', 'agronomia', 'solo', 'indicadores']
updated: 2026-06-21
---

## Definição

Mapeamento de fórmulas, indicadores agronômicos e dados de fertilidade do solo para Agronomy Acidez Solo pH Escala Correcao Calcario.

## Contexto

Fornece inteligência de negócio baseada em ciência de solos para otimizar plantios e adubações.

## Detalhes

- Fórmulas químicas de acidez, saturação de bases e necessidades de calagem.
- Cálculos de evapotranspiração potencial e balanço hídrico na agricultura.
- Limites toleráveis e faixas ideais de umidade e compactação para diversas culturas.

### Exemplo de Implementação Prática

```python
# Avaliação de compactação e umidade do solo com faixas de controle
# Ponto de murcha permanente (PMP) e Capacidade de campo (CC)

def avaliar_estado_solo(umidade_lida, tipo_solo="argiloso"):
    # Parâmetros de solo padrões (umidade volumétrica %)
    parametros = {
        "arenoso": {"pmp": 8.0, "cc": 18.0},
        "argiloso": {"pmp": 20.0, "cc": 38.0},
        "misto": {"pmp": 12.0, "cc": 26.0}
    }
    
    limites = parametros.get(tipo_solo, parametros["misto"])
    
    if umidade_lida < limites["pmp"]:
        return "CRÍTICO: Abaixo do Ponto de Murcha. Irrigar urgentemente!"
    elif umidade_lida < (limites["pmp"] + 5.0):
        return "ATENÇÃO: Próximo ao limite hídrico inferior."
    elif umidade_lida > limites["cc"]:
        return "ATENÇÃO: Solo saturado (Encharcado). Perigo de anoxia radicular."
    else:
        return "IDEAL: Umidade disponível na faixa de capacidade de campo."

print(avaliar_estado_solo(umidade_lida=28.5, tipo_solo="argiloso"))
```

## Links

- [[00_MOC]]
- [[concepts/guia-organizacao-para]]
- [[concepts/guia-dataview-obsidian]]
