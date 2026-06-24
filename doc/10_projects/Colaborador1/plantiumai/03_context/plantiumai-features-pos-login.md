---
tags: [plantiumai, web, dashboard, pdf, clima, oauth, nextjs]
updated: 2026-06-22
---

# PlantiumAI — features do app pós-login (jun/2026)

Estado do `web/` após a rodada de funcionalidades sobre o dashboard de alta fidelidade (ECharts, dados simulados em `lib/plantium-demo.ts`).

## Implementado
- **Ícone oficial** (`/logo-plantiumai.png`) no shell (sidebar, canto sup. esq.).
- **Perfil com dados reais** da sessão (nome/email/função do Neon) no painel "Meu perfil" e em Configurações — sem valores fixos.
- **Reset de senha seguro** — ver [[10_projects/Colaborador1/plantiumai/03_context/seguranca-fluxo-reset-senha]].
- **Login Google** (Auth.js v5): provider adicionado **condicionalmente** em `auth.ts` (só se `AUTH_GOOGLE_ID`/`AUTH_GOOGLE_SECRET`); `role` default `cliente` p/ contas OAuth; botão fiado no `/login`. Redirect URI: `https://<dominio>/api/auth/callback/google`.
- **Unidades nos gráficos técnicos**: tooltip ECharts com `valueFormatter` (°C, %, ppm, pH) via `baseOpt` em `lib/plantium-charts.ts`.
- **Clima (Open-Meteo, grátis, sem chave)**: `web/src/app/api/clima/route.ts` (server-side, cache 30 min, default Goiânia) + `components/app/weather-card.tsx` na visão geral. INMET fica como evolução (`INMET_STATION`).
- **Relatório PDF em Python (ReportLab)**: `web/api/pdf/relatorio.py` (função serverless da Vercel — ReportLab é puro Python, roda no runtime Python; WeasyPrint NÃO roda lá por libs nativas). Tema verde, capa/cabeçalho/rodapé "Página X de Y" (two-pass canvas), tabela de leituras + estado colorido, estatísticas e alertas. Front: `exportReport()` no contexto faz POST com os dados atuais → baixa PDF; CSV é gerado no client.

## Decisões-chave
- **PDF = Python/ReportLab na Vercel** (honra o pedido + viável). Pasta `web/api/` (Root Directory=web); rota `/api/pdf/*` p/ não colidir com o App Router (`/api/ingest`, `/api/clima`). Config: `web/requirements.txt`, `web/.python-version`, `web/vercel.json`.
- Tudo externo é chamado **server-side** (CSP `connect-src 'self'`): clima e PDF são same-origin; Google OAuth é navegação top-level.

## Secrets/env que o usuário precisa prover (Vercel)
- `DATABASE_URL` (pooled) + `DATABASE_URL_UNPOOLED` (migração) — **pendentes**, necessários p/ login/perfil reais.
- `AUTH_GOOGLE_ID` / `AUTH_GOOGLE_SECRET` — login Google (Google Cloud Console + redirect URI).
- `RESEND_API_KEY` + `EMAIL_FROM` — email de reset (sem isso o link só é logado no servidor).
- (opcional) `INMET_STATION`.

## Pendências
- Trocar dados simulados por leitura real de `readings` (escopo `company_id`) — dashboard e PDF.
- Rate limiting distribuído (Upstash/Vercel KV) em reset e ingestão.
- Verificar na Vercel se a função Python (`web/api/pdf/relatorio.py`) é detectada no projeto Next; fallback Node (`@react-pdf/renderer`/`pdf-lib`) se necessário.

## Links
- [[30_libraries/general/integracao-dashboard-pos-login]]
- [[10_projects/Colaborador1/general/plataforma-web-arquitetura]]
- [[10_projects/Colaborador1/plantiumai/03_context/seguranca-fluxo-reset-senha]]
- [[20_workflows/deploy-plataforma-web-vercel-neon]]
