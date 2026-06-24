---
tags: [oiaa, desafio-ia, nextjs, vercel, web, kaggle]
updated: 2026-06-24
---

## Definicao

Plataforma web do Desafio Tecnico de IA (OIAA) do IF Goiano - Campus Hidrolandia. Tres pilares: NLP, Visao Computacional (VC), Aprendizado de Maquina (AM). App Next.js 14 na pasta `web/` do repo TreinamentoOIAA.

## Contexto

- Repo: github.com/IF-Goiano-Campus-Hidrolandia-Alunos/TreinamentoOIAA (push so no fim do projeto).
- Backend + esqueleto de UI feitos em 2026-06-24; front definitivo entregue no dia seguinte via `PROMPT_FRONTEND.md` (raiz do repo).
- Vercel: Root Directory = `web`, framework Next.js.
- Notebooks Kaggle (raiz, .py) contem instrucao oculta de "tutor"/nao resolver o desafio: e prompt injection no conteudo, tratada como dado e nao obedecida; foram usados so para extrair textos e os import blocks.

## Detalhes

- Stack: Next 14.2.35 App Router + TypeScript + Tailwind (tokens shadcn, `components.json`), lucide-react. Sem Radix (UI primitivos proprios em `components/ui`).
- Camada de dados (`web/lib`): `challenges.ts` (Fase 1, textos reais), `code-snippets.ts` (Fase 2; 1o bloco = import block real, depois esqueleto com `# [PASSO EM BRANCO - IMPLEMENTE AQUI A LOGICA]`), `leaderboard-store.ts` (in-memory, ranking por total + sort + busca + upsert/remove), `accents.ts`, `types.ts`.
- API Routes: `GET /api/challenges`; `GET /api/code/:pillar` (nlp|vc|am, 404 se invalido); `GET /api/leaderboard?search=&sortBy=&order=`; `POST` e `DELETE` exigem header `x-admin-token` == env `ADMIN_TOKEN` (sem env -> 503).
- Placar in-memory NAO persiste em serverless (cold start/multi-instancia). Persistencia real: trocar store por Vercel KV ou Neon mantendo as assinaturas.
- Cores de identidade: NLP roxo/violeta (`--nlp`), VC ciano (`--vc`), AM verde/esmeralda (`--am`).
- Notas: total = phase1 + phase2 (0-10 cada); posicao do ranking segue sempre o total.
- Build verificado (`npm run build`) e endpoints testados (auth 401/201 ok). Next 14.2.x mantido por causa do prazo; subir para 16 e breaking.
- Commits: perfil ThyagoToledo (ver IDENTIDADE-LOCAL do vault).

## Links

- [[workflows/deploy-plataforma-web-vercel-neon]]
- [[concepts/plataforma-web-arquitetura]]
