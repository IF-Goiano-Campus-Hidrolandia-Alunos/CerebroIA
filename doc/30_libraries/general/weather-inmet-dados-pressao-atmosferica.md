---
tags: ['weatherclimateapis', 'documentacao', 'clima', 'weather', 'api']
updated: 2026-06-21
---

## Definição

Conexão e consumo de dados meteorológicos de Weather INMET Dados Pressao Atmosferica focados na previsão e no monitoramento climático agrícola.

## Contexto

Permite estimar chuvas futuras, risco de geadas e programar adubações sem deriva no campo.

## Detalhes

- Autenticação e chaves de acesso para APIs governamentais e corporativas.
- Consumo de dados em tempo real e de séries históricas de temperatura, chuva e radiação.
- Tratamento de limites de requisição (Rate Limiting) e cache de consultas locais.

### Exemplo de Implementação Prática

```python
# Consumindo a API do INMET (Instituto Nacional de Meteorologia)
import requests
import pandas as pd

# URLs públicas do INMET para consulta de estações e dados diários
def buscar_dados_inmet_estacao(estacao_id, data_inicio, data_fim):
    """
    estacao_id: Código da estação (ex: A701 para Porto Alegre)
    data_inicio, data_fim: Formato YYYY-MM-DD
    """
    url = f"https://apitempo.inmet.gov.br/estacao/diaria/{data_inicio}/{data_fim}/{estacao_id}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        dados = response.json()
        
        # Converte dados JSON em DataFrame do pandas
        df = pd.DataFrame(dados)
        print(f"Colunas do INMET: {df.columns.tolist()}")
        return df
    except Exception as e:
        print(f"[Erro] Falha ao consultar INMET: {e}")
        return pd.DataFrame()
```

## Links

- [[00_MOC]]
- [[30_libraries/dotnet_arch/guia-organizacao-para]]
- [[30_libraries/dotnet_arch/guia-dataview-obsidian]]
