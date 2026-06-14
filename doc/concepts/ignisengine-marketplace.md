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

## Pendências

- Push do repo do marketplace exige conta GitHub ThyagoToledo (GCM em cache estava como FeronZerbana); resolver via colaborador/PAT.
- Ajustar `DEFAULT_BASE_URL` em MarketplaceClient para a URL real apos deploy.

## Links

- [[concepts/ignisengine-roadmap]]
- [[concepts/ignisengine-javafx-migracao]]
