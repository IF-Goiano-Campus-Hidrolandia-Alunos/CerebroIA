# Handoff de Sessão - 2026-06-22

## 1. Estado Atual
- Dashboard pós-login de alta fidelidade (ECharts + design system `pl-*`) distribuído em subrotas do Next.js (`/app`, `/app/locais`, `/app/sensores`, `/app/alertas`, `/app/configuracoes`) — dados ainda **simulados** (`web/src/lib/plantium-demo.ts`).
- Rodada de funcionalidades concluída e commitada/pushada (branch `main`):
  - Ícone oficial no shell; perfil com dados reais da sessão.
  - **Reset de senha seguro** (token hasheado + email plugável) → `/recuperar-senha`, `/redefinir-senha`.
  - **Login Google** (Auth.js v5, provider condicional).
  - **Unidades** nos tooltips dos gráficos técnicos.
  - **Clima** Open-Meteo (`/api/clima`) + `WeatherCard`.
  - **Relatório PDF em Python/ReportLab** (`web/api/pdf/relatorio.py`) + exportação CSV no client.
- Docs no vault: [[concepts/plantiumai-features-pos-login]], [[concepts/seguranca-fluxo-reset-senha]] (linkadas no 00_MOC).

## 2. Pendências (próximos passos)
1. **Secrets na Vercel:** `DATABASE_URL` + `DATABASE_URL_UNPOOLED` (login/perfil reais), `AUTH_GOOGLE_ID`/`AUTH_GOOGLE_SECRET` (Google), `RESEND_API_KEY` + `EMAIL_FROM` (email de reset).
2. **Dados reais:** ligar dashboard e PDF à tabela `readings` com escopo `company_id` (hoje simulado).
3. **Verificar deploy da função Python** (`web/api/pdf/relatorio.py`) na Vercel; se não for detectada no projeto Next, usar fallback Node (`@react-pdf/renderer`/`pdf-lib`).
4. **Rate limiting** distribuído (Upstash/Vercel KV) em reset e `/api/ingest`.
5. INMET como fonte de clima adicional (`INMET_STATION`).

## 3. Observações
- CSP é restritiva (`connect-src 'self'`): manter integrações externas server-side (clima e PDF são same-origin; Google é navegação top-level).
- Pesquisa de apoio rodou via workflow; 4 agentes caíram por limite de sessão (reset 23:50) — achados de vault/Vercel-Python preservados nas notas.
