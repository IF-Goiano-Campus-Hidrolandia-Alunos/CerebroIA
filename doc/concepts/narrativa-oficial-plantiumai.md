---
tags: [plantiumai, narrativa, escopo]
updated: 2026-06-19
---

# Narrativa Oficial PlantiumAI

## Definição
- O PlantiumAI é um sistema inteligente de monitoramento para micro estufas e hortas verticais que usa sensores IoT, visão computacional e inteligência artificial para apoiar a tomada de decisão do produtor.

## Foco
- Monitoramento de micro estufas e ambientes de cultivo protegido.
- Containers aparecem apenas como aplicação opcional e caso de uso futuro.

## Dor principal
- Carência de leitura do equilíbrio biológico (biocenose) do ambiente, que dificulta o ajuste adequado da irrigação.
- Consequências associadas: desperdício de água, risco de doenças, necessidade de acompanhamento constante.

## Dores secundárias
- Desperdício de água.
- Falta de automação.
- Dificuldade de monitoramento remoto.
- Dificuldade de registrar histórico.
- Ausência de alertas inteligentes.
- Baixa previsibilidade da produção.

## Protótipo já implementado
- Hardware: ESP32, sensores ambientais e de solo, comunicação serial USB, MQTT via Wi-Fi.
- Software: Tauri 2, Rust, React, SQLite, tokio.
- Fluxo: ESP32, serial USB ou MQTT, thread Rust com tokio, parser e validação, SQLite, eventos Tauri, React, regras de irrigação, IA.
- Resiliência: Circuit Breaker e modo de fallback por regra local.

## Arquitetura futura
- Sincronização em nuvem.
- Painel web.
- Aplicativo móvel.
- IA local com TurboQuantização.
- Raspberry Pi opcional como hub de borda.
- Visão computacional com YOLO na borda.
- Funcionamento híbrido local e nuvem.
- Múltiplos usuários.
- Integração conversacional via bot do WhatsApp.

## Vícios de IA a evitar
- Linguagem de marketing com promessas absolutas.
- Afirmar como pronto o que ainda é planejado.
- Reuso de números sem tabela e memória de cálculo.
- Excesso de datas literais.
- Aspas para destaque em vez de citação.
