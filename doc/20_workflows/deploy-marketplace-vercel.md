---
tags: [workflow, marketplace, vercel, neon, oauth, deploy]
updated: 2026-06-14
---

## Objetivo

Subir o Ignis Marketplace (Next.js) na Vercel com Neon (Postgres) e login GitHub OAuth.

## Passos

1. Vercel: New Project -> importar `Colaborador1/IginisMarketePlace` -> Deploy (Next.js auto-detectado).
2. Vercel -> Storage -> Create Database -> Neon (Free) -> Connect to Project (injeta `DATABASE_URL`).
3. Neon -> SQL Editor -> rodar `db/migrations/002_users_security.sql` (idempotente; cria users + items + seed + admins).
4. GitHub -> Settings -> Developers -> OAuth Apps -> New OAuth App:
   - Homepage: `https://SEU-PROJETO.vercel.app`
   - Authorization callback URL: `https://SEU-PROJETO.vercel.app/api/auth/callback/github`
   - gerar Client secret.
5. Vercel -> Settings -> Environment Variables:
   - `AUTH_SECRET` (openssl rand -base64 33)
   - `AUTH_GITHUB_ID`, `AUTH_GITHUB_SECRET`
   - `ADMIN_GITHUB_LOGINS=Colaborador1,Colaborador2`
   - opcional `GITHUB_TOKEN` (escopo public_repo, evita rate limit no gate)
6. Redeploy.

## Validação

- `SUA_URL/api/health` -> `{"status":"ok","db":"connected","items":5}`.
- Login com GitHub no topo do site; Colaborador1/Colaborador2 entram como admin (veem `/admin`).
- Publicar em `/publish` com repo invalido -> reprovado pelo gate (nao sobe).

## Notas

- Callback URL deve bater exatamente com a URL da Vercel.
- Editor Java: setar `IGNIS_MARKETPLACE_URL` ou ajustar `DEFAULT_BASE_URL` em MarketplaceClient.

## Links

- [[10_projects/Colaborador1/ignisengine/03_context/ignisengine-marketplace]]
