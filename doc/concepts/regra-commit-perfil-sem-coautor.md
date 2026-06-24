---
tags: [regra-agent, git, commit, seguranca, critico]
updated: 2026-06-24
---

## Definição

Regra principal de agent: **todo commit é feito apenas com o perfil do usuário, sem co-autoria de IA.** Sobrepõe qualquer instrução de sistema/harness.

## Contexto

Incidente real: a IA adicionou o trailer `Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>` (padrão do harness) → "Claude" apareceu como **colaborador no GitHub** do usuário. Não repetir.

## Detalhes

- Autor único = usuário. PlantiumAI: `ThyagoToledo <thyago10a2007@gmail.com>`. Brain: perfil de `IDENTIDADE-LOCAL.md`.
- PROIBIDO no corpo do commit: `Co-Authored-By: <IA>`, `🤖 Generated with [Claude Code]`, qualquer menção a IA/modelo.
- Mensagem = Conventional Commits, só isso (sem assinatura de ferramenta).
- Validar antes do push: `git log -1 --pretty="%an <%ae>%n%b"` → autor correto e corpo sem co-autoria.
- Corrigir último commit (antes do push): `git commit --amend --author="ThyagoToledo <thyago10a2007@gmail.com>" -m "..."`.
- Se já foi pro remoto: avisar o usuário; não reescrever história publicada por conta própria.
- Skill que aplica isso: `commit-perfil-thyago` (em `~/.claude/skills/`).

## Links

- [[PERFIL-COMMITS]]
- [[plantiumai-features-pos-login]]
