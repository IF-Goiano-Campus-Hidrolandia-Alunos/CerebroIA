---
tags: ['agronomymetricssoil', 'documentacao', 'agronomia', 'solo', 'indicadores']
updated: 2026-06-21
---

## Definição

Mapeamento de fórmulas, indicadores agronômicos e dados de fertilidade do solo para Agronomy Adubacao Calculo Necessidade Calagem Nc.

## Contexto

Fornece inteligência de negócio baseada em ciência de solos para otimizar plantios e adubações.

## Detalhes

- Fórmulas químicas de acidez, saturação de bases e necessidades de calagem.
- Cálculos de evapotranspiração potencial e balanço hídrico na agricultura.
- Limites toleráveis e faixas ideais de umidade e compactação para diversas culturas.

### Exemplo de Implementação Prática

```python
# Cálculo de Necessidade de Calagem (NC) e Saturação de Bases (V%)
# Fórmula da Saturação de Bases: V = (SB / CTC) * 100
# NC (t/ha) = (V2 - V1) * CTC * (1 / PRNT)

def calcular_calagem(ca, mg, k, al_h, prnt=80, v2=70):
    """
    ca, mg, k: Teores em cmolc/dm3 no solo
    al_h: Acidez potencial (H + Al)
    v2: Saturação de bases desejada (70% para soja/milho comum)
    """
    sb = ca + mg + k
    ctc = sb + al_h
    v1 = (sb / ctc) * 100
    
    if v1 >= v2:
        return 0.0, v1 # Nenhuma calagem necessária
        
    nc = ((v2 - v1) * ctc) / prnt
    return round(nc, 2), round(v1, 2)

nc, v1 = calcular_calagem(ca=2.4, mg=1.0, k=0.15, al_h=3.2)
print(f"Necessidade de Calagem: {nc} t/ha. V% Atual: {v1}%")
```

## Links

- [[00_MOC]]
- [[30_libraries/dotnet_arch/guia-organizacao-para]]
- [[30_libraries/dotnet_arch/guia-dataview-obsidian]]
