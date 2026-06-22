---
tags: ['agronomymetricssoil', 'documentacao', 'agronomia', 'solo', 'indicadores']
updated: 2026-06-21
---

## Definição

Mapeamento de fórmulas, indicadores agronômicos e dados de fertilidade do solo para Agronomy Fertirrigacao Aplicacao Nutrientes Agua.

## Contexto

Fornece inteligência de negócio baseada em ciência de solos para otimizar plantios e adubações.

## Detalhes

- Fórmulas químicas de acidez, saturação de bases e necessidades de calagem.
- Cálculos de evapotranspiração potencial e balanço hídrico na agricultura.
- Limites toleráveis e faixas ideais de umidade e compactação para diversas culturas.

### Exemplo de Implementação Prática

```python
# Estimativa de Evapotranspiração de Referência (ET0) simplificada (Hargreaves-Samani)
# ET0 = 0.0023 * Ra * (TD ** 0.5) * (Tmean + 17.8)

def evapotranspiracao_hargreaves(tmax, tmin, lat, dia_ano):
    """
    tmax, tmin: Temperaturas extremas diárias em °C
    lat: Latitude em graus decimais (ex: -22.5 para Sul)
    dia_ano: Dia Juliano (1 a 365)
    """
    import math
    
    tmean = (tmax + tmin) / 2.0
    td = tmax - tmin
    
    # Cálculo de radiação solar extraterrestre (Ra) com base na órbita terrestre
    dr = 1 + 0.033 * math.cos(2 * math.pi * dia_ano / 365.0)
    rad_lat = lat * math.pi / 180.0
    declinacao = 0.409 * math.sin(2 * math.pi * dia_ano / 365.0 - 1.39)
    ws = math.acos(-math.tan(rad_lat) * math.tan(declinacao))
    
    ra = 37.6 * dr * (ws * math.sin(rad_lat) * math.sin(declinacao) + 
                       math.cos(rad_lat) * math.cos(declinacao) * math.sin(ws))
    
    et0 = 0.0023 * (ra / 2.45) * (td ** 0.5) * (tmean + 17.8)
    return round(max(et0, 0.0), 2)
```

## Links

- [[00_MOC]]
- [[concepts/guia-organizacao-para]]
- [[concepts/guia-dataview-obsidian]]
