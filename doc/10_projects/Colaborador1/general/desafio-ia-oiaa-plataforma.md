---
tags: [oiaa, desafio-ia, vite, react, vercel, neon, web, kaggle]
updated: 2026-06-25
---

## Definicao

Plataforma web do Desafio Tecnico de IA (OIAA) do IF Goiano - Campus Hidrolandia. Tres pilares: NLP, Visao Computacional (VC), Aprendizado de Maquina (AM). Repo TreinamentoOIAA com dois apps ligados: `FrontEnd/` (Vite+React) e `BackEnd/` (Vercel Functions + Neon). O antigo `web/` (Next.js) foi removido.

## Arquitetura (dois deploys Vercel ligados)

- Fluxo: FrontEnd --fetch(VITE_API_URL)--> BackEnd --SQL--> Neon Postgres.
- FrontEnd e BackEnd sao projetos Vercel separados, mesmo repo, Root Directory diferente.
- Guia completo de deploy em `DEPLOY.md` na raiz (nao versionado; .md exceto README estao no .gitignore).

## FrontEnd/

- Vite 6 + React 18 + React Router 7 (HashRouter) + Tailwind 4 + Radix + motion + sonner. npm.
- Camada de dados propria em `src/app/lib` (challenges, stages, scoring, code-snippets, links, use-stage-progress, teams-store). Conteudo de teoria/etapas/code e estatico; so times/notas vem do BackEnd.
- Store dual-mode (`src/app/lib/teams-store.tsx`): `API_BASE = import.meta.env.VITE_API_URL`; boot faz `GET ${VITE_API_URL}/api/teams` -> MODO API (Neon) se vier JSON; senao MODO LOCAL (seed + localStorage). Token admin demo `capivara-2026` (localStorage `ifg-admin-token`).
- Mascote `src/imports/capivara.png` no hero da Home (mascara radial + glow = fundo transparente sem editar PNG).
- Env: `VITE_API_URL`. Build `vite build` -> `dist/`.

## BackEnd/

- API serverless (Vercel Functions, framework Other) self-contained. `lib/types.ts`; `api/_db.ts` (Neon schema auto teams+members JSONB FK cascade + CORS + validacao); `api/teams.ts` (GET lista crua / POST cria aberto / DELETE ?id= x-admin-token / OPTIONS); `api/scores.ts` (POST nota x-admin-token). `public/index.html` = pagina de status na raiz. Retorna Team[] cru (ranking no front).
- Env: `DATABASE_URL` (Neon pooled), `ADMIN_TOKEN` (=token do painel), `ALLOWED_ORIGIN` (vazio -> CORS *). Sem DATABASE_URL -> 503 -> front usa local.

## Deploy ao vivo (Vercel, scope thyagos-projects-2a538c0c)

- FrontEnd: projeto `treinamento-oiaa` -> https://treinamento-oiaa.vercel.app
- BackEnd: projeto `treinamento-oiaa-slcq` -> https://treinamento-oiaa-slcq.vercel.app (404 na raiz e NORMAL; usar /api/*).
- Integracao validada em producao: criar/excluir time grava no Neon; `ADMIN_TOKEN=capivara-2026` confere; bundle do front embute a URL do back (modo API). Neon ligado via integracao Neon-Vercel (injeta DATABASE_URL/POSTGRES_*).
- Pegadinhas Vercel CLI: como agente roda `--non-interactive` e ignora stdin no `env add` -> usar `--value`. Var sensitive volta como "" no `env pull`; para `VITE_*` usar `--no-sensitive`. Mudou env -> precisa redeploy.

## Geral

- Cores: NLP roxo/violeta, VC ciano, AM verde/esmeralda. Prompts na raiz: PROMPT_FRONTEND.md, PROMPT_TRILHA_ETAPAS.md (locais, fora do git).
- Commits: perfil do usuario, sem co-autoria de IA. Repo: github.com/IF-Goiano-Campus-Hidrolandia-Alunos/TreinamentoOIAA.

## Auto-pontuacao (quiz + CSV), gabaritos e rate-limit

- Identidade do aluno: `members.access_code` (6 chars, indice unico, gerado no createTeam); `POST /api/identify` valida e o front guarda sessao (`ifg-member-session`). Submissoes assinam header `x-member-code`. CORS de `_db.ts` libera `Content-Type, x-admin-token, x-member-code, x-access-code` (faltar isso = "Failed to fetch" no quiz).
- Auto-grader (`POST /api/submit`, header x-member-code): `kind: quiz` (corrige por gabarito server-side, `QUIZZES` em BackEnd/lib; front NAO leva `correctIndex` no bundle), `kind: metric` (valor digitado -> `grading.ts`), `kind: csv` (estilo Kaggle). Grava em `submissions` (historico) e faz upsert do best-score em `member.scores`. Tabela: `submissions(id, member_id FK cascade, pillar, stage, points, detail jsonb, created_at)`.
- CSV auto-scorer: tutor cadastra gabarito por pilar/etapa em `POST /api/admin/answer-key` (CSV id,valor; metrica derivada do pilar: vc/nlp=accuracy, am=rmse) -> tabela `answer_keys(pillar,stage,metric,keys jsonb,updated_at, PK(pillar,stage))`. Aluno faz upload do CSV de previsoes -> servidor calcula accuracy/RMSE (`grading.ts computeAccuracy/computeRmse`, parser em `lib/csv.ts`) -> `calculateMetricPoints`. GET lista gabaritos, DELETE `?pillar=&stage=` remove. UI: aba "Gabaritos" no painel do tutor + upload no MetricSubmissionComponent. A prova de fraude (servidor calcula a metrica das previsoes reais).
- Rate-limit (`submit.ts`): cooldown global de 4s por integrante (429 "Aguarde Xs") + teto de 10 tentativas por etapa (429). Falha no controle nao bloqueia submissao legitima.
- Painel do tutor (`AdminPage`): abas Visao Geral (KPIs + 2 graficos recharts), Times e Codigos (mostra/copia access_code), Historico de Submissoes (`GET /api/admin/submissions`, busca), Lancar Notas (override manual via `/api/scores`), Gabaritos. Export CSV de notas, backfill de codigos (`/api/admin/backfill-codes`).
- Pegadinha corrigida: GETs de admin faziam SELECT sem `ensureSchema` -> 500 em DB/instancia nova ate outra rota criar a tabela; agora chamam `ensureSchema` (exportado). E o `vercel env add` ignora stdin como agente (usar `--value`); var `VITE_*` "sensitive" volta "" no `env pull` (usar `--no-sensitive`).
- Tudo validado ao vivo: quiz 200 (7/10), CSV 18/25 (0.75 acc), rate-limit 429. ADMIN_TOKEN = capivara-2026 (= token demo do painel).

## Links

- [[deploy-plataforma-web-vercel-neon]]
- [[plataforma-web-arquitetura]]
