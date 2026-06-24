---
tags: [seguranca, auth, nextjs, plantiumai, password-reset]
updated: 2026-06-22
---

# Fluxo seguro de "esqueci a senha"

Padrão real implementado no PlantiumAI (`web/`), substituindo os stubs vazios do vault.

## Regras de ouro
- **NUNCA enviar a senha por email.** Ela é hash bcrypt (irreversível). Envie **link de redefinição**.
- **Token = 32 bytes CSPRNG** (`crypto.randomBytes(32).hex`) — vai no link (alta entropia).
- **No banco guarda-se só `sha256(token)`** — vazamento do DB não permite forjar link. (SHA-256 basta p/ token de alta entropia; bcrypt é p/ senha humana.)
- **Expiração curta** (30 min) + **uso único** (apaga a linha ao consumir e invalida tokens antigos do mesmo email).
- **Anti-enumeração:** a ação de solicitar SEMPRE responde a mesma mensagem genérica, exista ou não a conta.
- **POST/Server Action** (CSRF nativo do Next) — nunca efetivar troca via GET.
- **Pós-reset:** regravar `passwordHash` (bcrypt), idealmente invalidar sessões + email "sua senha mudou".
- **Rate limit** por IP+email (Upstash/Vercel KV — memória não serve em serverless). *Pendente.*

## Implementação no projeto
- Reusa a tabela `verification_tokens` (Auth.js) com `identifier = "pwreset:" + email`.
- `web/src/lib/password-reset.ts`: `createResetToken(email)` / `consumeResetToken(raw)`.
- `web/src/lib/email.ts`: envio plugável (Resend via HTTP se `RESEND_API_KEY`, senão loga no servidor).
- Rotas: `/recuperar-senha` (solicita) e `/redefinir-senha?token=` (define nova senha).
- Env: `RESEND_API_KEY`, `EMAIL_FROM` (domínio verificado SPF/DKIM), base URL via headers.

## Links
- [[10_projects/Colaborador1/general/plataforma-web-arquitetura]]
- [[10_projects/Colaborador1/plantiumai/03_context/plantiumai-features-pos-login]]
- [[30_libraries/general/hashing-senhas-bcrypt-argon2]]
