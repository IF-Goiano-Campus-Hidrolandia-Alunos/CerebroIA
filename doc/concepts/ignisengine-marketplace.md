---
tags: [ignisengine, marketplace, vercel, neon, nextjs, auth, decision]
updated: 2026-06-14
---

## Definição

Marketplace online de plugins/assets do IgnisEngine (itens 9-10 do roadmap): backend Next.js na Vercel + banco Neon (Postgres), consumido pelo editor via API REST.

## Contexto

Repo dedicado: `https://github.com/ThyagoToledo/IginisMarketePlace` (deploy Vercel). Ligado ao repo do motor (`URSoftware/IgnisEngine`) como git submodule na pasta `marketplace/`. Substitui o `VercelServerMock` antigo do `CommunityFrame`.

## Decisões-Chave

- Backend guarda apenas URLs Git, nunca binarios (regra do roadmap).
- Stack: Next.js 14 (App Router) + @neondatabase/serverless; free tier Vercel + Neon.
- Tabela `items`: type/name/author/description/version/git_url/cover_image_text/dependencies/downloads/created_at. JSON da API em camelCase (gitUrl, coverImageText).
- API: GET/POST /api/items, GET/POST /api/items/:id (POST incrementa downloads), GET /api/health.
- Seed via CSV (`db/seed.csv`) importado no Neon; schema em `db/schema.sql`.
- Cliente Java `com.ignis.marketplace.MarketplaceClient` (java.net.http + org.json) com fallback automatico no mock offline — editor nunca quebra sem internet.
- URL base do editor via `-Dignis.marketplace.url` ou env `IGNIS_MARKETPLACE_URL`.

## Usuarios, Seguranca, Admin (add 2026-06-14)

- Auth.js v5 + GitHub OAuth (sessao JWT). Tabela `users` (github_id unico, flags). Identidade unica por conta GitHub.
- Admins ThyagoToledo/FeronZerbana via env `ADMIN_GITHUB_LOGINS` + coluna `is_admin` (auto-set no login). `/admin` e `/api/admin/*` restritos.
- Pacotes vinculados ao dono (`items.author_id`); usuario legado (github_id 0) segura o seed.
- Gate de seguranca na publicacao (`lib/security.js`): valida campos + repo Git (host permitido, existe/publico/nao arquivado via GitHub API) + blocklist. Reprovado nao sobe. Guarda `security_report` jsonb e `status`.
- Banir usuario (banido nao loga/publica, itens somem do catalogo) e remover item (admin/dono).
- Legal: paginas /terms e /privacy, banner de cookies, aceite obrigatorio antes de publicar (`accepted_terms_at`), isencao de responsabilidade.
- Migracao idempotente: `db/migrations/002_users_security.sql`. Env extra: AUTH_SECRET, AUTH_GITHUB_ID/SECRET, ADMIN_GITHUB_LOGINS, GITHUB_TOKEN(opcional). Callback OAuth: `/api/auth/callback/github`.
- Publicacao pelo editor Java exige token (OAuth desktop) — adiado para passo futuro; catalogo GET segue publico.

## Producao (deploy ativo 2026-06-14)

- URL: `https://iginis-markete-place.vercel.app` (= DEFAULT_BASE_URL do MarketplaceClient; ja bate, sem mudar codigo).
- Verificado live: `/api/health` -> db connected, 5 itens; `/api/items` ok (JOIN users, camelCase).
- GitHub OAuth App: nome "Ignis Marketplace", dono @ThyagoToledo, sem Device Flow.
- Callback: `https://iginis-markete-place.vercel.app/api/auth/callback/github`.
- AUTH_GITHUB_ID (Client ID, nao-secreto): `Ov23liZpQYsIRkk4EWmK`.
- Env vars na Vercel (VALORES sao segredos, NAO ficam no Vault): DATABASE_URL, AUTH_SECRET, AUTH_GITHUB_ID, AUTH_GITHUB_SECRET, ADMIN_GITHUB_LOGINS=ThyagoToledo,FeronZerbana, GITHUB_TOKEN(opcional).
- Banco Neon: regiao sa-east-1 (host ep-misty-cherry-acu4p1xt-pooler). Connection string injetada pela integracao Vercel.

## Pendências

- Setar as env vars de OAuth na Vercel + Redeploy + testar login (apos isso ThyagoToledo/FeronZerbana entram como admin).
- Girar o AUTH_GITHUB_SECRET (foi exposto no chat durante o setup) e atualizar na Vercel.
- Publicacao pelo editor Java: via TOKEN (implementado 2026-06-14). Tabela api_tokens (migration 003, guarda hash SHA-256). lib/apiauth.resolveUser aceita sessao OU `Authorization: Bearer <token>`. Pagina web /account gera/revoga token. Editor: MarketplaceClient guarda token em Preferences; CommunityFrame tem 2 botoes (Publicar no site abre browser; Publicar com token publica via Bearer) + dialogo de token + ajuda.

## Links

- [[concepts/ignisengine-roadmap]]
- [[concepts/ignisengine-javafx-migracao]]
