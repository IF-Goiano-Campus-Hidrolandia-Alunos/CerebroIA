# Auto-correcao estilo Kaggle via CSV e Gestao de Gabaritos

Este documento descreve o funcionamento da correcao automatica de arquivos CSV enviados por alunos e a gestao de gabaritos pelos tutores.

## 1. Funcionamento do Auto-Scorer (Estilo Kaggle)
Os alunos nas etapas de código (`fill-blanks` e `from-scratch`) podem submeter um arquivo CSV com suas previsões.
- **Formato esperado**: Um arquivo CSV com colunas `id` e `valor` (separador `,` ou `;`).
- **Lógica de Comparação**:
  - Para pilares de classificação (VC e NLP): Calcula a **Acuracia** (fração de predições corretas em relação ao gabarito).
  - Para pilares de regressão (AM): Calcula o **RMSE** (Root Mean Squared Error) das notas previstas em relação ao gabarito.
- **Conversão em Pontos**: A métrica final obtida é avaliada com base nas baselines e alvos definidos em `grading.ts` para computar a pontuação final (0 a 25 ou 30 pontos).

## 2. Gestao de Gabaritos (Answer Keys)
Os gabaritos são mantidos no banco de dados na tabela `answer_keys`.
- **Cadastro (POST /api/admin/answer-key)**: O tutor envia um CSV com as respostas reais, que é processado e armazenado como um dicionário JSONB.
- **Consulta Completa (GET /api/admin/answer-key?pillar=...&stage=...)**: Retorna a chave do gabarito completo (permitindo download).
- **Download no Painel**: Adicionado botão "Baixar gabarito (CSV)" no painel do tutor. Ele reconverte os dados JSONB em um arquivo CSV para download.
- **Semeador de Templates (Seed)**: Na inicialização do banco (`ensureSchema` em `_db.ts`), se a tabela estiver vazia, são semeados automaticamente gabaritos de exemplo (templates) de 10 linhas para os 6 pares de pilar/etapa de código.

## 3. Controle de Submissoes (Anti-Spam)
- **Cooldown**: Intervalo mínimo de 4 segundos entre submissões de um mesmo integrante (para evitar travamentos e sobrecargas no banco).
- **Limite de Tentativas**: Teto de no máximo 10 tentativas por etapa para incentivar a revisão do código local antes de submeter.
