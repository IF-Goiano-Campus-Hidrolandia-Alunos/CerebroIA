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
3. **Assinatura** (recorrente, **principal fonte de renda**): planos Semente R$ 89 (ate 5 m² de cobertura) / Cultivo R$ 179 (ate 30 m² de cobertura) / Estufa+ R$ 349 (ate 150 m² de cobertura), com margem de contribuicao R$ 64 / 119 / 169.

## Rentabilidade (memoria de cálculo)
- OpEx Anexo B (R$ 460/mês) decomposto em fixo ~R$ 350 (servidor + IA) + marginal por plano (R$ 25–180).
- Mix 50/35/15 → ARPU R$ 159,50; margem média R$ 95,75; break-even ~4 assinantes.
- Projeção (Tabela 8): 30 assinantes → R$ 30,3 mil/ano; 50 → R$ 53,2 mil; 100 → R$ 107,7 mil.
- Payback do CapEx (R$ 43.048,74, Anexo C): ~17 meses (30) / ~10 meses (50), sem contar a receita única (equip.+instalação: R$ 1.880 a R$ 2.780/cliente), que antecipa o retorno.
- **Seção 6.7 — Planejamento Tributário**: Projeção fiscal sob Simples Nacional. SaaS enquadrado no Anexo III (6,00% nominal inicial) e Hardware no Anexo I (4,00% nominal inicial). Alíquotas efetivas ponderadas simuladas de 5,18% (10 e 30 clientes), 5,85% (50 clientes, 2ª faixa) e 8,06% (100 clientes, 3ª faixa).
- **Seção 6.8 — Plano de Negócios e Go-To-Market**: Meta de 50 clientes ativos nos primeiros 12 meses, com aquisição viabilizada por parcerias de fomento (SENAR Goiás, Sebrae Goiás), varejo técnico físico (VarejoIN), validação acadêmica e PoCs de campo (FATESG, FPM) e divulgação digital.

## Reflexo no site
- `/planos` ganhou a secao **"Equipamento e instalacao"** (cards: kit basico R$ 1.290, kit completo R$ 2.190, instalacao R$ 590 com mao de obra 8h × R$ 55/h) + adendo de deslocamento (fórmula e exemplos). FAQ alinhado aos precos ao cliente.
- **Limites de Area**: Adicionada a area maxima de estufa/cultivo coberta por cada plano (Semente: ate 5 m², Cultivo: ate 30 m², Estufa+: ate 150 m²) nas listas de recursos dos cards e na tabela comparativa detalhada.
- Nova página **`/documentos`** (botao na navbar apos Planos, nas 3 navbars): visualizador de PDF embutido (`<iframe>`) + baixar + abrir em nova aba. PDF em `web/public/docs/trabalho-cientifico-plantiumai.pdf`. Exigiu trocar `X-Frame-Options: DENY → SAMEORIGIN` e CSP `frame-ancestors 'none' → 'self'` no `next.config.mjs` (mantem protecao contra clickjacking de terceiros; permite o site exibir o proprio PDF).

## Links
- [[plantiumai-responsividade-mobile]]
- [[narrativa-oficial-plantiumai]]
- [[editar-trabalho-cientifico]]
