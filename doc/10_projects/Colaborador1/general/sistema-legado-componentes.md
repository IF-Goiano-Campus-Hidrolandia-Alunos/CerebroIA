---
tags: [legacy, reuse, plantiumai]
updated: 2026-06-10
---

## Definição

Inventário dos componentes do `SistemaLegado/` (Python/FastAPI + JS vanilla) reaproveitáveis no novo sistema desktop.

## Stack Legada

- Backend: Python 3.13, FastAPI, SQLAlchemy async, SQLite (aiosqlite)
- IA: AI Gateway multi-provider (Claude, GPT, Gemini, Ollama, SmolLM3 GGUF local via llama-cpp)
- Frontend: HTML/CSS/JS vanilla
- Sem comunicação serial real — sensores apenas simulados via API

## Componentes Reaproveitáveis (alta prioridade)

- `services/sensor_service.py`: faixas de validação (VALID_RANGES por sensor), classificação de umidade (dry/low/optimal/high/saturated), geração de alertas com thresholds, simulador realista (variação gradual + hora do dia)
- `core/circuit_breaker.py`: Circuit Breaker completo (CLOSED/OPEN/HALF_OPEN, failure threshold, recovery timeout)
- `services/irrigation_service.py`: decisão híbrida IA + fallback por regras (rule_based_decision com 4 níveis de urgência)
- `models/schemas.py`: schemas Pydantic (Plant, SensorReading, Analysis) — base para modelos de dados do novo sistema
- `core/ai_gateway.py` + `providers/`: arquitetura multi-provider com failover

## Faixas de Sensores (VALID_RANGES)

- soil_moisture: 0-100 % | air_temperature: -10 a 60 °C | air_humidity: 0-100 %
- light_level: 0-150000 lux | soil_temperature: -5 a 50 °C | co2_level: 200-2000 ppm | ph_level: 0-14

## Thresholds de Negócio

- Umidade ideal default: 35-65 %
- Crítico seco: < ideal_min * 0.5 | Encharcado: > ideal_max * 1.2
- Irrigação por regra (`rule_based_decision`, fallback sem IA): < ideal_min*0.6 → crítico (25 min); < ideal_min → médio (15 min); > ideal_max → não irrigar (alerta drenagem); senão → ideal.

## AI Gateway — modos e failover (`core/ai_gateway.py`)

- 5 modos de operação: `local_only`, `api_only`, `hybrid_prefer_api`, `hybrid_prefer_local`, `smart_failover`.
- Provedores: local GGUF (llama-cpp), Ollama, Claude, OpenAI, Gemini, BlackBox, MiniMax — cada um com Circuit Breaker próprio.
- Failover: tenta provedores na ordem do modo, pulando os com CB em OPEN; se todos OPEN, força tentar todos (último recurso). Métricas: total/sucesso/failover + histórico das últimas 100 req.
- `chat()` (texto, JSON ou freeform) e `analyze_image()` (visão) com o mesmo failover.
- **Reuso na plataforma web:** portar o padrão gateway+circuit-breaker para uma rota serverless (ex.: análise de planta por foto / decisão de irrigação) usando os modelos Claude mais recentes como provedor primário.

## Não Reaproveitar

- Frontend vanilla (substituído por UI premium)
- Scripts instalar.bat/.sh (substituídos por instalador nativo)
- venv/ e __pycache__ (artefatos)

## Links

- [[40_external_cache/especificacao-plantiumai]]
- [[10_projects/Colaborador1/general/novo-sistema-arquitetura]]
