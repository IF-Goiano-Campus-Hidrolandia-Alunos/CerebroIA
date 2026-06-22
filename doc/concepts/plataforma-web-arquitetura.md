---
tags: [plantiumai, web, arquitetura, vercel, neon, nextjs]
updated: 2026-06-21
---

# Plataforma Web PlantiumAI — Arquitetura

## Definição
- Plataforma web multiusuário (SaaS) que estende o protótipo desktop: empresas e clientes acessam dashboards de sensores na nuvem. Hospedada na **Vercel**, banco **Neon Postgres**.

## Stack
- **Next.js (App Router)** + TypeScript + Tailwind, reusando `packages/ui` (`@plantium/ui`).
- **Auth.js (NextAuth)** — credenciais + sessão JWT, papéis `empresa` / `cliente`.
- **Drizzle ORM** + `@neondatabase/serverless` (HTTP driver, ideal p/ serverless Vercel).
- Reaproveita regras de negócio do desktop/legado (faixas de sensores, irrigação) — ver [[concepts/sistema-legado-componentes]] e [[concepts/penetrometro-desktop-dominio]].

## Estrutura de rotas
- `/` landing institucional (ex-HomePage) → CTA login.
- `/login`, `/signup` (auth).
- `/app/*` dashboard protegido (ex-Interface): visão da empresa, locais, sensores, tokens.
- `middleware.ts` protege `/app/*`; redireciona não autenticado para `/login`.

## Modelo de dados (Neon)
- `companies` (e-mail, endereço, localização) · `users` (nome, login, hash senha, role empresa/cliente, company_id).
- `locations` (tipo: estufa | plantacao_vertical | container) por empresa.
- `sensors` (tipo, location_id, device_token_id) · `device_tokens` (token de firmware, hash, escopo).
- `readings` (leituras por sensor: umidade, temp, CO2, pH, luz, ts).

## Token de firmware (segurança sensor↔plataforma)
- Dashboard gera token por dispositivo; firmware envia no header/payload.
- Servidor valida hash → identifica empresa/sensor dono → autoriza ingestão.
- Tokens são hasheados no banco (nunca em texto puro); rotacionáveis/revogáveis.

## Segurança (padrão de indústria)
- Senhas com hash (bcrypt/argon2), sessões httpOnly+secure, CSRF do Auth.js.
- Security headers + CSP no `next.config`; rate limiting nas rotas de auth/ingestão.
- Segredos só em env vars da Vercel; `DATABASE_URL` do Neon nunca commitado.

## Deploy
- Ver [[workflows/deploy-plataforma-web-vercel-neon]] para passo-a-passo manual (Vercel + Neon + SQL).

## Links
- [[concepts/design-system-landing]]
- [[concepts/novo-sistema-arquitetura]]
- [[concepts/sistema-legado-componentes]]
- [[workflows/deploy-plataforma-web-vercel-neon]]
