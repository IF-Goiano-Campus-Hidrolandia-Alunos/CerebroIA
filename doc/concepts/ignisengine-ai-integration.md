---
tags: [ignisengine, ai, architecture, decision]
updated: 2026-06-12
---

## Definição

Arquitetura do Módulo de Integração com IA do IgnisEngine: design desacoplado usando Clean Architecture para suportar múltiplos provedores de forma segura e rate-limited.

## Contexto

Item 5 do roadmap, implementado em 2026-06-12. Substitui a lógica Swing acoplada legada.

## Detalhes

- **AIServiceProvider**: Interface genérica para chamadas de rede e processamento JSON de provedores de IA.
- **GeminiProvider**: Implementação para o modelo Gemini 2.5 Flash, usando HttpClient (Java 11+) e fallback HTTP URLConnection.
- **AIIntegration**: Controlador centralizado de serviços de IA. Armazena chaves e configurações com segurança em `~/.ignis/ai_settings.json` (fora da pasta do projeto e do versionamento Git), migrando chaves legadas e aplicando rate limits locais.
- **AuxiliaryPanel**: Camada de visualização Swing simplificada. Oferece dropdown para seleção de provedores (Gemini, OpenAI, Claude) e áreas de interação para os modos ASK e AGENT.

## Links

- [[concepts/ignisengine-roadmap]]
