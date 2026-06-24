---
tags: [ignisengine, roadmap, decision, architecture]
updated: 2026-06-12
---

## Definição

Roadmap oficial de evolução do IgnisEngine: 10 módulos priorizados, todos como componentes desacoplados.

## Contexto

Motor 2D em Java puro (URSoftware). Consoles (Xbox/PlayStation) não suportam JVM, exigindo estratégia dupla de build. Documento completo no projeto: `IgnisEngine/doc/ROADMAP.md`.

## Prioridades

1. Builder multiplataforma (Java: Windows/Linux/macOS)
2. Exportação para C++ (Xbox, PlayStation, Switch futuro)
3. Editor de imagens integrado (sprites, camadas, texturas)
4. Sistema de animações (2D: timeline/keyframes; 3D: skeletal/blend trees)
5. Integração Gemini (expande Agent Mode existente; multi-provedor futuro)
6. Editor de áudio estilo DAW (multipista, mixagem, exportação)
7. Sistema de notas/documentação (estilo Notion, wiki interna)
8. Plataforma Comunidade/Workshop (estilo Steam Workshop)
9. Marketplace de plugins e assets (apenas URLs de repositórios Git)
10. Infraestrutura Vercel e catálogo online (validação, metadados, indexação)

## Decisões-Chave

- Builder com duas estratégias: distribuição JVM e geração de projetos C++ compiláveis
- Backend do marketplace recebe apenas URLs Git, nunca binários
- Segurança do marketplace: sandbox de plugins, permissões, análise de integridade
- IA já possui base no projeto (Gemini 2.5 Flash via Agent Mode); item 5 é expansão
- Todos os módulos desacoplados: manutenção independente e expansão futura

## Status

- Itens 1 e 2 implementados em 2026-06-12: ver [[10_projects/Colaborador1/ignisengine/03_context/ignisengine-builder]]
- Item 3 (editor de imagens) v1 implementada em 2026-06-12: ver [[10_projects/Colaborador1/ignisengine/03_context/ignisengine-image-editor]]
- Item 4 (animação) tier 2D implementado em 2026-06-12: ver [[10_projects/Colaborador1/ignisengine/03_context/ignisengine-animation]]
- Item 5 (integração Gemini/IA) v1 implementada em 2026-06-12: ver [[10_projects/Colaborador1/ignisengine/03_context/ignisengine-ai-integration]]
- Java oficial padronizado em 17 LTS: ver [[10_projects/Colaborador1/ignisengine/03_context/ignisengine-java-17]]
- Auditoria técnica + correções em 2026-06-12: ver [[10_projects/Colaborador1/ignisengine/03_context/ignisengine-auditoria]]

## Links

- [[10_projects/Colaborador1/ignisengine/03_context/ignisengine-builder]]
- [[00_rules/readme-structure-template]]
- [[20_workflows/sincronizacao-git-automatico]]
