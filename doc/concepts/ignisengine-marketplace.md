---
tags: [ignisengine, marketplace, vercel, neon, nextjs, decision]
updated: 2026-06-13
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

## Pendências

- Push do repo do marketplace exige conta GitHub ThyagoToledo (GCM em cache estava como FeronZerbana); resolver via colaborador/PAT.
- Ajustar `DEFAULT_BASE_URL` em MarketplaceClient para a URL real apos deploy.

## Links

- [[concepts/ignisengine-roadmap]]
- [[concepts/ignisengine-javafx-migracao]]
