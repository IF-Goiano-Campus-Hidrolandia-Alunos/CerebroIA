---
tags: [plantiumai, economia, precos, assinatura, trabalho-cientifico, saas, haas]
updated: 2026-06-29
---

# PlantiumAI — Modelo de preços e fontes de receita

Adicionado ao Trabalho Científico como **Seções 6.5 e 6.6** (Tabelas 5–8), no padrão acadêmico
(linguagem moderada, memória de cálculo, siglas expandidas).
Arquivo de trabalho: `Downloads/PlantiumAI_TrabalhoCientifico.docx` (não evoluir os docs de referência
do repo). Espelhado em `tabelaprecos.md` e `lucro_rentavel.md` na raiz do repo.

## Três fontes de receita (separadas e atualizadas)

1. **Equipamento** (única / aquisição no plano Pro ou aluguel subsididado no plano Premium):
   - **Kit Protótipo IoT**: R$ 1.010,08 (Sem LED) / R$ 1.860,08 (Com LED Grow Light Full Spectrum 100W).
   - **Kit Expansão Pro**: R$ 1.705,22 (Sem LED) / R$ 2.855,22 (Com LED Grow Light Profissional Multicor).
   - **Preço por m² adicional**: +R$ 45,00 (único) em cabeamento/sensores de sinal extra.
2. **Instalação** (única):
   - **Básica (Sem LED)**: R$ 590,00 (8 horas × R$ 55/h).
   - **Completa (Com LED)**: R$ 790,00 (12 horas × R$ 55/h) devido ao cabeamento de potência e fixação do painel grow LED.
   - **Preço por m² adicional**: +R$ 25,00 (cabeamento estruturado físico adicional).
   - **Adendo deslocamento (fora de Goiânia):** `D = 2 × d × c + p` — d = km Goiânia→destino; c = R$ 1,30/km (combustível+desgaste+tempo); p = diária R$ 180 (só com pernoite).
3. **Assinatura** (recorrente, **principal fonte de renda**):
   - **WhatsApp Grátis (Freemium)**: R$ 0,00.
   - **Software Assinatura (Premium - HaaS)**: R$ 299,00/mês (mensal) ou R$ 249,00/mês (anual) - locação de placas e conectividade 4G incluídos. Cobertura de até 15 m² (+ R$ 12,00/mês por m² adicional).
   - **Aquisição Total (Pro)**: R$ 79,00/mês (mensal) ou R$ 59,00/mês (anual) - cliente adquire o hardware upfront. Cobertura de até 30 m² por kit.

## Rentabilidade, Viabilidade do Aluguel (HaaS) e ROI
- **Estudo de Viabilidade HaaS**: O valor do plano Premium (R$ 299,00/mês) foi estruturado para viabilizar a amortização do hardware (CapEx R$ 1.010,08) juntamente com a manutenção da telemetria 4G LTE (OpEx R$ 60,00/mês) e custos de processamento em nuvem. O payback estimado do hardware em locação é de ~10 meses.
- **Métricas de ROI Agrícola**:
  - *Mitigação de Perda*: Até **85%** de redução na quebra total de ciclos produtivos causados por anomalias hídricas/térmicas ou erro humano (Fonte: **EMBRAPA Hortaliças**).
  - *Economia de Recursos*: Até **40%** no consumo de água e insumos minerais por irrigação pulsada de precisão (Fonte: **FAO / EMBRAPA**).
  - *Retorno Financeiro*: Evitar uma única perda de ciclo em estufa de contêiner vertical preserva até **R$ 15.000,00** de receita comercializável, cobrindo o investimento em menos de **6 a 8 meses** (Fonte: **VarejoIN / FPM**).

## Reflexo no site
- `/planos` exibe os cards atualizados de preços (Premium a R$ 299 / R$ 249 e Pro a R$ 79 / R$ 59), a tabela comparativa atualizada com a linha de "Área de Cobertura" e o valor dos adicionais por m² excedente, a seções de custos de hardware discriminados com painéis LED opcionais, a mão de obra variando com e sem iluminação de LED, e a seção de **Estudo de Viabilidade e ROI**.
- Correção do erro de hidratação Next.js/SSR em `<GreenhouseBackground>` compilando 100% de forma limpa.

## Links
- [[plantiumai-responsividade-mobile]]
- [[narrativa-oficial-plantiumai]]
- [[editar-trabalho-cientifico]]
- [[plantiumai-hidratacao-particulas]]
