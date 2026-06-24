---
tags: [design, ui, landing, tema, plantiumai]
updated: 2026-06-19
---

## Definição

Design system da PlantiumAI para a **landing institucional** (investidores): tema claro/escuro, glassmorphism, verde-folha funcional. Inspirado na referência AgricAI; oposto estético do Spotify (luz, orgânico, sentence case).

## Contexto

- Fonte de verdade: `design/plantium-design-system.md` (no repo PlantiumAI)
- Prompt pronto p/ gerar a landing: `design/PROMPT.md`
- Evolução do app operacional: `design/melhorias-interface-operacional.md`
- Usar com a imagem de referência AgricAI anexada

## Detalhes

- **Temas** via `data-theme` + CSS variables + `localStorage` (`plantium-theme`); respeita `prefers-color-scheme`
- **Marca**: verde `#22c55e` (= `leaf-500` existente) só funcional (CTA/ativo/saúde)
- **Claro**: fundo `#eef3ee`, vidro `rgba(255,255,255,0.65)` blur 18px, texto `#152a1f`
- **Escuro**: fundo `#0b1410`, vidro `rgba(22,40,30,0.55)`, texto `#eaf3ee`, acento `#34d977`
- **Tipografia**: Sora (display/números) + Inter (corpo); sentence case; line-height 1.5–1.6
- **Geometria**: radius 12–24px, pílulas 999px, círculos; sombras difusas suaves
- **Login**: card de vidro central (e-mail/senha, lembrar-me, esqueci, Google, criar conta, toggle tema)
- Stack alvo: a landing/Interface migrou para **Next.js (App Router) + Tailwind**, reusando `packages/ui` (React). O `desktop/` segue em Tauri/Vite.

## Links

- [[10_projects/Colaborador1/general/desktop-app-estrutura]]
- [[10_projects/Colaborador1/general/novo-sistema-arquitetura]]
- [[10_projects/Colaborador1/general/plataforma-web-arquitetura]]
