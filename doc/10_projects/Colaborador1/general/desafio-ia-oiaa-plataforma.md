---
tags: [oiaa, desafio-ia, nextjs, vercel, neon, web, kaggle]
updated: 2026-06-24
---

## Definicao

Plataforma web do Desafio Tecnico de IA (OIAA) do IF Goiano - Campus Hidrolandia. Tres pilares: NLP, Visao Computacional (VC), Aprendizado de Maquina (AM). Dois apps no repo TreinamentoOIAA: `FrontEnd/` (Vite+React, app OFICIAL de entrega) e `web/` (Next.js 14, prototipo anterior do backend).

## App de entrega (FrontEnd/)

- Stack: Vite 6 + React 18 + React Router 7 (HashRouter) + Tailwind 4 + Radix + motion + sonner. Gerado no Figma Make e integrado.
- Camada de dados propria em `FrontEnd/src/app/lib` (challenges, stages, scoring, code-snippets, links, use-stage-progress, teams-store). Tipos do front: `TeamRanked.rank`, `MemberScored.individualScore/stagesCompleted` (diferente do `web/`).
- Store dual-mode (`src/app/lib/teams-store.tsx`): no boot faz `GET /api/teams`; se vier JSON valido -> MODO API (dados no Neon, compartilhado); senao -> MODO LOCAL (seed + localStorage por navegador). Token admin demo `capivara-2026` (localStorage `ifg-admin-token`).
- Backend serverless em `FrontEnd/api/` (Vercel Functions, validado por build+tsc): `_db.ts` (Neon: ensureSchema auto, teams+members JSONB), `teams.ts` (GET lista crua / POST cria aberto / DELETE ?id= com x-admin-token), `scores.ts` (POST nota com x-admin-token). Sem `DATABASE_URL` -> 503 -> front cai no local. Ranking e feito no cliente (API so persiste Team[] cru).
- Mascote: `src/imports/capivara.png` (capivara cyberpunk) no lado direito do hero da Home, com mascara radial + glow (efeito de fundo transparente sem editar o PNG).
- Deploy Vercel: Root Directory = `FrontEnd`, preset Vite, env `DATABASE_URL` (Neon pooled) + `ADMIN_TOKEN` (= token do painel). Ver `FrontEnd/DEPLOY.md`. Build `vite build` -> `dist/` verificado; preview local OK (home com mascote, placar com seed).
- npm (removido pnpm-workspace.yaml do Make; react/react-dom movidos para dependencies).

## Contexto

- Repo: github.com/IF-Goiano-Campus-Hidrolandia-Alunos/TreinamentoOIAA (push so no fim do projeto).
- Backend + esqueleto de UI; front definitivo gerado via `PROMPT_FRONTEND.md` (raiz do repo, modelo de times/etapas). Prompt especifico da trilha das 5 etapas por pilar em `PROMPT_TRILHA_ETAPAS.md` (raiz): mapeia cada etapa aos dados reais (`getStages`, `getChallenge`, `getCode`), componentes propostos e adapter de progresso local (localStorage) ja pronto para virar API.
- Vercel: Root Directory = `web`, framework Next.js.
- Notebooks Kaggle (raiz, .py) contem instrucao oculta de "tutor"/nao resolver o desafio: e prompt injection no conteudo, tratada como dado e nao obedecida; usados so para extrair textos e os import blocks.
- Autoria do projeto: apenas Colaborador1 (README, rodape do app, prompt do front).

## Detalhes

- Stack: Next 14.2.35 App Router + TypeScript + Tailwind (tokens shadcn, `components.json`), lucide-react, zod (v3), `@neondatabase/serverless`. UI primitivos proprios em `components/ui` (sem Radix ainda).
- Estrutura de cada pilar: 5 etapas valendo pontos por integrante (`lib/stages.ts`): theory 10, guided 15, unguided 20, fill-blanks 25, from-scratch 30 (com 2 modos: blocks e scratch). 100 pts/pilar, 300 pts/integrante (15 etapas no total).
- Times (`lib/teams-store.ts`): nome + integrantes (recomendado 3) + tutor. Nota individual = pontos/300*100 (0-100). Nota do grupo = media das notas individuais; tutor NUNCA entra.
- Scoring centralizado em `lib/scoring.ts` (`scoreMember`, `groupScore`, `rankTeams`); ranking por nota do grupo (desc), desempate por nome.
- Validacao com zod em `lib/validation.ts` (`createTeamSchema`, `submitScoreSchema` com limite de pontos por etapa).
- Persistencia (`lib/teams-store.ts`, funcoes async): com `DATABASE_URL` usa Neon Postgres (tabelas `teams`/`members` criadas automaticamente, `CREATE TABLE IF NOT EXISTS`, members.scores JSONB, FK ON DELETE CASCADE). Sem DATABASE_URL, fallback local em `data/teams.runtime.json` (NAO versionado; seed = `data/teams.json`). Em serverless sem DB nao persiste.
- API Routes: `GET /api/challenges` (challenges + stages + scoring); `GET /api/code/:pillar` (nlp|vc|am, 404 se invalido, retorna PillarCode); `GET /api/teams?search=&sortBy=&order=` (ranqueado); `POST /api/teams` (aberto, cria time); `GET /api/teams/:id`; `DELETE /api/teams/:id`; `POST /api/teams/:id/scores`. Escritas sensiveis (DELETE time, POST scores) exigem header `x-admin-token` == env `ADMIN_TOKEN` (sem env -> 503).
- Paginas: `/` (landing), `/challenges` (narrativa + 5 etapas), `/code` (esqueletos Fase 2), `/teams` (criar/listar), `/leaderboard` (placar grupo + individual), `/admin` (Area do Tutor: token no localStorage, lanca notas, exclui times).
- Cores de identidade (tokens): NLP roxo/violeta (`--nlp`), VC ciano (`--vc`), AM verde/esmeralda (`--am`). Classes literais em `lib/accents.ts`.
- Build verificado (`npm run build`, 10 rotas). Next 14.2.x mantido por prazo.
- Commits: perfil Colaborador1 (skill commit-perfil-colaborador1; sem co-autoria de IA).

## Links

- [[20_workflows/deploy-plataforma-web-vercel-neon]]
- [[10_projects/Colaborador1/general/plataforma-web-arquitetura]]
