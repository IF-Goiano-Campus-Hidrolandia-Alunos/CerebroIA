---
tags: [plantiumai, git, repo, limpeza, organizacao]
updated: 2026-06-26
---

# PlantiumAI — Limpeza do repositório

Faxina do repo `PlantiumAI` (commit `561cbb6`, push para `PlantiumAI/PlantiumAI` e `ThyagoToledo/PlantiumAI`).

## Removido (era lixo / não usado)
- **`packages/ui`** — design system `@plantium/ui` (Button, Card, LoginCard, Navbar, ThemeToggle, KpiCard, HealthGauge…). **Não importado por `web/` nem `desktop/`**: não há `package.json` na raiz (não é monorepo/workspace) e zero `import ... from "@plantium/ui"` no código real. A `web/` tem suas próprias versões (`theme-toggle.tsx`, `login/page.tsx`, `landing.tsx`, `kpi-card.tsx`). Interface duplicada e morta.
- **`.design-sync`** — tooling do Claude Design que só existia para sincronizar/preview do `packages/ui` (`config.json` aponta `"pkg": "@plantium/ui"`; `previews/` importam dele). Órfão após remover o pacote. Passou a ser ignorado por inteiro no `.gitignore`.

## Tirado do versionamento (mantido só local)
- `tabelaprecos.md` e `lucro_rentavel.md` (docs de preços/negócio) **removidos do git** (`git rm --cached`, continuam no disco) e **gitignorados** via `/*.md` + `!/README.md`. Só o `README.md` permanece versionado entre os `.md` da raiz.

## Mantido (decisão do usuário)
- `HomePage/` (export original da landing — referência), `design/` (prompts de UI), `documentos de referencia do projeto/`.

## Docs corrigidos
- `README.md`: removida a linha do `packages/ui` da árvore de estrutura.
- O `CLAUDE.md` (global, fora do repo) ainda descreve `packages/ui` como "reusado por web" — desatualizado; corrigir lá se incomodar.

## Links
- [[plantiumai-modelo-precos]]
- [[plantiumai-responsividade-mobile]]
