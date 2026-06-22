---
tags: [plantiumai, deploy, vercel, neon, workflow]
updated: 2026-06-21
---

# Deploy da Plataforma Web — Vercel + Neon

Guia completo (com todos os comandos e SQL) vive no repo: `web/DEPLOY.md`.
Esta nota é o índice rápido.

## Passos
1. **Neon**: criar projeto `plantiumai`; copiar string **pooled** (`DATABASE_URL`) e **unpooled** (`DATABASE_URL_UNPOOLED`), ambas com `sslmode=require`.
2. **Segredos**: `openssl rand -base64 32` ×2 → `AUTH_SECRET` e `DEVICE_TOKEN_PEPPER`.
3. **Schema**: `npm run db:migrate` (usando a string unpooled) ou colar `web/drizzle/0000_init.sql` no SQL Editor do Neon.
4. **Vercel**: importar repo, **Root Directory = `web`**, framework Next.js, env vars (4 acima), Deploy.
5. **Pós**: criar conta na landing → painel; gerar token em /app/tokens.
6. **Firmware**: `POST /api/ingest` com `Authorization: Bearer plt_...` + JSON da leitura.

## Pegadinhas
- Migração exige string **unpooled** (sem `-pooler`).
- `AUTH_SECRET` fixo em todos os ambientes (senão a sessão cai).
- Root Directory `web` (o app não está na raiz do repo).
- Rate limiter em memória → trocar por Upstash Redis se multi-instância.

## Links
- [[concepts/plataforma-web-arquitetura]]
- [[workflows/deploy-marketplace-vercel]]
