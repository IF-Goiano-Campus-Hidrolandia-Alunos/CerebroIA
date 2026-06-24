---
tags: [readme, system]
updated: 2026-06-24
author: Colaborador1
---

# Vault – Sistema de Documentacao Otimizado para IA e Spec-Driven Development

Base de conhecimento local estruturada para economia de tokens e execucao de desenvolvimento orientada a especificacoes.

## Nova Estrutura Organizacional (doc/)

```
doc/
├── 00_rules/                ← Regras do sistema, diretrizes de IA e padroes
│   └── templates/           ← Modelos de notas (.md) para manter a padronizacao
├── 10_projects/             ← Projetos ativos e legados (divididos por autor)
│   ├── Colaborador1/        ← Projetos de Colaborador1 (ignisengine, plantiumai, etc.)
│   ├── Colaborador2/        ← Projetos de Colaborador2
│   └── shared/              ← Projetos colaborativos com atuacao conjunta
├── 20_workflows/            ← Guias passo-a-passo e processos (SOPs)
├── 30_libraries/            ← Conceitos e referencias tecnicas por dominio
│   ├── agronomy/            ← Referencia em agronomia e solos
│   ├── ai_agents/           ← Referencia em IA, LLMs e arquiteturas agenticas
│   ├── dotnet_arch/         ← Referencia em .NET, C# e arquitetura de software
│   └── general/             ← Conceitos gerais de desenvolvimento
└── 40_external_cache/       ← Cache de pesquisas externas e documentacoes de APIs
```

O arquivo `doc/00_MOC.md` na raiz de `doc/` e o indice centralizador de todo o Vault.

---

## Fluxo de Trabalho: Spec-Driven Development (SDD)

Todas as novas funcionalidades ou alteracoes arquiteturais de projetos devem seguir a metodologia SDD. A pasta de cada projeto ativo e divida em quatro subpastas obrigatorias:

1. **00_spec/:** Contem as especificacoes (`.spec.md`). Define o escopo (in-scope), o que esta fora de escopo (out-of-scope), analisa ambiguidades do projeto e define a arquitetura geral antes de qualquer escrita de codigo.
2. **01_plan/:** Contem os planos de implementacao (`.plan.md`). Mapeia os arquivos especificos a serem alterados, novos arquivos a serem criados, decisões tecnicas e o plano de testes/validacao.
3. **02_tasks/:** Contem checklists de tarefas (`.task.md`) de progresso ativo, quebrando o plano em partes atomicas e independentes.
4. **03_context/:** Armazena esquemas de banco de dados, mapeamento de rotas de API, glossarios e dicionarios de dados locais para preservar o contexto e evitar decaimento de memoria do agente de IA.

**Fluxo de Vida Obrigadorio de Feature:**
Especificar (Spec) → Planejar (Plan) → Obter Aprovacao Humana → Executar e Validar (Execute & Verify).

---

## Fluxo Obrigatorio do Agente de IA

Sempre que um agente de IA iniciar uma tarefa:

1. **Consultar Local Primeiro:**
   - Leia `doc/00_MOC.md` e a pasta correspondente.
   - Consuma apenas as notas especificas necessarias para a tarefa. Evite ler pastas completas sem necessidade para economizar tokens.

2. **Evitar Redundancia:**
   - Nao leia o Vault inteiro em loops.
   - Guarde em memoria apenas o que for relevante.

3. **Busca Externa + Registro:**
   - Caso falte informacao local, faca busca na internet.
   - Resuma e salve como conceito em `30_libraries/<dominio>/` ou em `40_external_cache/`.
   - Atualize os links correspondentes no `00_MOC.md`.

4. **Escrita Economica:**
   - Bullets, sem introducao ou prosa desnecessaria.
   - Codigo direto ao ponto.

---

## Regras de Ouro de Redacao

✓ Uma ideia = um arquivo.
✓ Definicao curta + bullets.
✓ Sem prosa introdutoria ou conclusiva.
✓ Datas corretas no cabecalho `updated:` de frontmatter YAML.
✓ Links atualizados no formato `[[pasta/nome-nota]]`.

✗ Markdown decorativo exagerado (negritos em excesso, cores).
✗ Listas aninhadas profundas.
✗ Uso de emojis (proibido em commits, documentacao e codigo).
✗ Textos longos e prolixos.

---

## Economia de Tokens

Exemplo pratico:
- Pergunta 1: "O que e X?" → Pesquisa + sintese = 5k tokens.
- Salva-se em: `30_libraries/general/x.md`.
- Pergunta 2: "Explique X novamente" → IA le o arquivo local = 200 tokens.
- **Economia:** 96% em sessoes futuras.
