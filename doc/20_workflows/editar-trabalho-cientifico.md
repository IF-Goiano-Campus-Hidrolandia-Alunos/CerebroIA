---
tags: [plantiumai, trabalho-cientifico, workflow, banca]
updated: 2026-06-19
---

# Editar Trabalho Científico PlantiumAI

## Objetivo
- Adequar o documento ao formato de Trabalho Científico, com escrita objetiva e moderada, separando o que já existe do que será implementado.

## Regras de tipo de documento
- Remover toda referência a "TCC" e "Trabalho de Conclusão de Curso".
- Usar na folha de rosto: "Trabalho Científico apresentado pelos alunos do curso de Engenharia de Software como requisito parcial para avaliação acadêmica."

## Regra de título
- Título oficial: "PLANTIUMAI: Desenvolvimento de um Sistema Inteligente de Monitoramento para Micro Estufas e Hortas Verticais Utilizando Sensores IoT, Visão Computacional e Inteligência Artificial".
- Não citar containers, plataforma web ou Raspberry Pi no título.

## Regra de separação protótipo x futuro
- Funcionalidade implementada usa: "o protótipo implementa", "o sistema realiza", "os dados são armazenados", "a aplicação foi desenvolvida".
- Funcionalidade planejada usa: "pretende-se implementar", "a arquitetura proposta prevê", "o sistema poderá", "futuramente", "considera-se".
- Nunca misturar as duas categorias no mesmo bloco.

## Linguagem moderada
- Substituir garante, comprova, elimina, revoluciona, transforma.
- Usar pode auxiliar, pode contribuir, sugere, foi observado, apresenta potencial, os resultados indicam.

## Siglas
- Primeira ocorrência: nome completo seguido da sigla entre parênteses.
- Ocorrências seguintes: somente a sigla.

## Termos técnicos
- Explicar em linguagem simples: CapEx, OpEx, MQTT, SQLite, tokio, Tauri, YOLO, mAP, IA multimodal, Circuit Breaker, Fail-safe, TurboQuantização, NDJSON.

## Itálico e aspas
- Itálico para palavras estrangeiras e termos técnicos destacados.
- Aspas somente para citações e trechos de fontes.

## Datas e citações
- Evitar "em 2026", "durante 2026", "no ano de 2026".
- Citar por autor e ano, diferenciando pessoa de empresa.

## Custos
- Todo valor citado precisa de tabela, memória de cálculo e justificativa.
- Anexo A custos do hardware; Anexo B custos operacionais; Anexo C custos de implantação.
- Starlink: registrar plano, valor mensal e motivo da escolha.

## Análise econômica
- Usar TAM, SAM e SOM como métricas de dimensionamento de mercado.

## Limitações e considerações finais
- Limitações entram nas Considerações Finais, não em seção separada.
- Considerações Finais com no mínimo três parágrafos: problema e importância; resultados; limitações e trabalhos futuros.

## Regra de sumário
- O documento é um artigo expandido e não possui sumário.
- Remover a página do sumário e qualquer índice interno; não criar sumário manual nem automático.

## Regra de tabelas de hardware
- Tabela 1 contém apenas o kit do protótipo funcional: ESP32, sensores, válvula, relé, sensor de fluxo, fonte, cabos, estrutura e roteador.
- Tabela 2 contém os componentes previstos para a evolução: Raspberry Pi, câmera USB, cartão SD, nuvem, dashboard web, aplicativo móvel, IA local e bot WhatsApp.
- O Raspberry Pi não faz parte do protótipo atual e deve aparecer apenas na arquitetura futura, como dispositivo de borda opcional.

## Correções pontuais recorrentes
- Referir VarejoIN como empresa, não como plataforma.
- Sigla na primeira ocorrência: nome completo seguido da sigla entre parênteses, inclusive para termos em inglês (Capital Expenditure (CapEx); Software as a Service (SaaS)).

## Validação
- Conferir ausência das palavras TCC e Trabalho de Conclusão de Curso.
- Conferir título idêntico ao oficial.
- Conferir que toda funcionalidade futura está marcada com verbo de planejamento.
- Conferir que todo valor monetário possui tabela e justificativa correspondente.
- Conferir expansão de cada sigla na primeira ocorrência.
