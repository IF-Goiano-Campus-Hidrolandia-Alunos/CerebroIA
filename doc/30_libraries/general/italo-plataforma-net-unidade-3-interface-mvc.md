---
tags: [importado, italo]
updated: 2026-06-21
---


## Características

- Da opção de maior liberdade e menor abstração
- Menor acoplamento da interface do restante do Software
  
## Abordagem diferente

- Alinhamento com arquiteturas de mercado
- Regras de roteamento definem qual URL no browser vai acionar qual Controller
- Cada requisição feita cai em m Controller que usa o Model para buscar (ou salvar) dados e escolhe uma View para exibir a página para o usuário

## Aspectos Positivos

- Melhor divisão de interface e demais recursos (devido ao Controller)
- Utilização de padrão e linguagens amplamente difundidos: MVC, HTML, CSS, JS, etc
- Completo domínio sobre renderização
- Mais leve e rápido.