# Handoff de Sessao - 2026-06-25

## 1. Estado Atual (TreinamentoOIAA — branch main, tudo compilando)
- **Auto-correcao Estilo Kaggle**:
  - Alunos enviam CSV de previsões. O servidor compara com o gabarito cadastrado na tabela `answer_keys` e computa acurácia (VC e NLP) ou RMSE (AM).
  - Integrado no `MetricSubmissionComponent` para aceitar envio de arquivo CSV além de inserção manual de métrica.
- **Gestao de Gabaritos (Tutor)**:
  - Adicionada aba "Gabaritos (Auto-correcao)" no painel `/admin` que lista os gabaritos, contagem de linhas e data de atualização.
  - Implementado botão "Baixar gabarito (CSV)" que reconverte os dados JSONB em formato CSV legível e aciona download.
  - Implementado botão "Remover gabarito" (DELETE).
  - Implementado semeador automático de templates (seed) no `ensureSchema` com gabaritos fictícios de 10 linhas para os 6 cenários de código.
- **Controle e Cooldown**:
  - Cooldown de 4 segundos entre submissões de integrantes e limite estrito de 10 tentativas por etapa para evitar spam.

## 2. Documentacao do Vault
- Novo documento com arquitetura e regras de auto-correção por CSV: `doc/10_projects/Colaborador1/treinamento-oiaa/03_context/auto-correcao-csv.md`.
