---
tags: [plantiumai, economia, precos, assinatura, trabalho-cientifico, saas]
updated: 2026-06-26
---

# PlantiumAI — Modelo de preços e fontes de receita

Adicionado ao Trabalho Científico como **Seções 6.5 e 6.6** (Tabelas 5–8), no padrão acadêmico
(linguagem moderada, memória de cálculo, siglas expandidas) — ver [[editar-trabalho-cientifico]].
Arquivo de trabalho: `Downloads/PlantiumAI_TrabalhoCientifico.docx` (não evoluir os docs de referência
do repo). Espelhado em `tabelaprecos.md` e `lucro_rentavel.md` na raiz do repo.

## Três fontes de receita (separadas)
1. **Equipamento** (única): custo Anexo A + ~28% → kit básico R$ 1.290 (custo 1.010,08); kit completo R$ 2.190 (custo 1.705,22).
2. **Instalação** (única): 8 h × R$ 55,00/h (mesma taxa de dev do Anexo C) = custo R$ 440 → preço R$ 590 (margem R$ 150). Vale Goiânia e RM.
   - **Adendo deslocamento (fora de Goiânia):** `D = 2 × d × c + p` — d = km Goiânia→destino; c = R$ 1,30/km (combustível+desgaste+tempo); p = diária R$ 180 (só com pernoite). Ex.: 120 km → +R$ 312; 250 km c/ pernoite → +R$ 830.
3. **Assinatura** (recorrente, **principal fonte de renda**): planos Semente R$ 89 / Cultivo R$ 179 / Estufa+ R$ 349, com margem de contribuição R$ 64 / 119 / 169.

## Rentabilidade (memória de cálculo)
- OpEx Anexo B (R$ 460/mês) decomposto em fixo ~R$ 350 (servidor + IA) + marginal por plano (R$ 25–180).
- Mix 50/35/15 → ARPU R$ 159,50; margem média R$ 95,75; break-even ~4 assinantes.
- Projeção (Tabela 8): 30 assinantes → R$ 30,3 mil/ano; 50 → R$ 53,2 mil; 100 → R$ 107,7 mil.
- Payback do CapEx (R$ 43.048,74, Anexo C): ~17 meses (30) / ~10 meses (50), sem contar a receita única (equip.+instalação: R$ 1.880 a R$ 2.780/cliente), que antecipa o retorno.

## Reflexo no site
- `/planos` ganhou a seção **"Equipamento e instalação"** (cards: kit básico R$ 1.290, kit completo R$ 2.190, instalação R$ 590 com mão de obra 8h × R$ 55/h) + adendo de deslocamento (fórmula e exemplos). FAQ alinhado aos preços ao cliente.
- Nova página **`/documentos`** (botão na navbar após Planos, nas 3 navbars): visualizador de PDF embutido (`<iframe>`) + baixar + abrir em nova aba. PDF em `web/public/docs/trabalho-cientifico-plantiumai.pdf`. Exigiu trocar `X-Frame-Options: DENY → SAMEORIGIN` e CSP `frame-ancestors 'none' → 'self'` no `next.config.mjs` (mantém proteção contra clickjacking de terceiros; permite o site exibir o próprio PDF).

## Links
- [[plantiumai-responsividade-mobile]]
- [[narrativa-oficial-plantiumai]]
- [[editar-trabalho-cientifico]]
