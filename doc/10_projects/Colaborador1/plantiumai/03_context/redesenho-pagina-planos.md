# Redesenho da Pagina de Planos - PlantiumAI

Este documento registra as alteracoes visuais, interativas e de backend na rota `/planos` do PlantiumAI.

## 1. Motivacao e Inspiracao
O objetivo foi reformular a pagina de planos de assinatura para criar uma interface de alta fidelidade e apelo estetico premium, inspirada no design minimalista escuro de `dreamcut.ai/pricing`. O tema de cores (verde-folha e slate) e a identidade de marca do PlantiumAI foram integralmente mantidos.

## 2. Tecnologias e Efeitos Implementados

### 2.1 Efeito 3D Hover Tilt (Inclinacao Baseada em Peso)
Para simular a sensacao de que a caixa do plano se inclina na direcao do cursor do mouse, foi implementada uma solucao em React puro utilizando eventos do cursor:
- **Eventos**: `onMouseMove` e `onMouseLeave`.
- **Calculo**: Obtem-se o bounding box do card (`getBoundingClientRect()`) e as coordenadas relativas do mouse (`clientX - rect.left` e `clientY - rect.top`).
- **Rotacao**: Calcula-se o desvio em relacao ao centro em porcentagem e aplica-se transformacoes de perspectiva e rotacao CSS:
  `transform: perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`
- **Efeito Glare (Brilho)**: Um gradiente radial absolute acompanha a posicao do mouse, simulando reflexo de luz.
- **Destaque do Badge**: O wrapper principal do card teve seu `overflow-hidden` removido, e a propriedade foi movida apenas para o container do efeito de brilho interno. Isso resolveu o problema de corte visual no selo absolute `RECOMENDADO` que fica posicionado acima da borda superior.

### 2.2 Seletor de Faturamento Deslizante
- Estruturado como um container de largura fixa (`w-[296px]`) e padding interno.
- Botoes de toggle com largura fixa (`w-[144px]`).
- Um indicador absolute (sliding pill) que se move horizontalmente atraves de transicoes CSS de acordo com o estado do faturamento:
  - Mensal: `left: 4px`
  - Anual: `left: 148px`
- O indicador possui `pointer-events-none` e `z-0` para garantir que nao intercepte eventos de clique, mantendo os botoes totalmente clicaveis.

### 2.3 Video e Fundo da Estufa
- **Video de Fundo**: O arquivo de video da estufa (`/EstufaEditSite.mp4`) foi copiado para a pasta `/public` do projeto e e executado de forma automatica, silenciosa e em loop (`autoPlay loop muted playsInline`). Ele esta configurado com opacidade de 28% (`opacity-[0.28]`) e escala reduzida (`scale-[0.95]`) para diminuir o zoom e se integrar perfeitamente com as bordas e o gradiente escuro (`#070d0a`), mantendo uma visibilidade clara e esteticamente agradavel da estufa no fundo.
- **Grade de Painel**: Mantida em overlay sobre o video.
- **Particulas de Clorofila/Telemetria**: Geracao dinamica de 25 particulas (divs) com tamanhos, delays e duracoes aleatorios calculados pelo React, mantendo a animacao de flutuacao vertical.

### 2.4 Porcentagem de Desconto (17%)
- Atualizado o desconto de faturamento anual de "2 meses gratis" para a proporcao de **17% de desconto** (economia exata referente a faturar 10 meses e usar 12).
- Na secao de FAQ, a duvida de fidelidade e faturamento foi reescrita para detalhar a relacao matematica de economia (17% de desconto equivale a economizar exatamente 2 meses de uso anualizado).

### 2.5 Tabela de Comparacao de Recursos
- Para customizar a tabela comparativa de acordo com os requisitos e manter a convencao semantica de cores:
  - As indicacoes de **Sim** (e **Incluso**) foram associadas ao checkmark `✓` e estilizadas em verde (`text-emerald-400`).
  - As indicacoes de **Não** foram associadas ao traco `-` e estilizadas em vermelho (`text-red-500 font-semibold`).
  - A observacao sobre o custo do hardware IoT posicionada abaixo da tabela foi estilizada na cor verde chamativa da marca (`text-[#34d977]`) com fonte em negrito suave (`font-semibold`) para chamar a atencao do usuario.

### 2.6 Navbar Fixa e Unificada
- **Acompanhamento do Scroll (Position Fixed)**: A navbar principal do site foi configurada com `position: fixed` tanto na Home Page quanto na pagina de Planos (`/planos`), garantindo que o usuario consiga alternar de sessao a qualquer momento.
- **Navegacao Integrada a partir de Planos**: Na pagina de planos, a navbar foi redesenhada de forma identica à da Home Page, incluindo links ancorados que apontam diretamente para as secoes da Home (como `/#solucao`, `/#tecnologia`, etc.), alem de um link para `/planos`. O padding-top do `<main>` em `/planos` foi aumentado para `pt-32` para acomodar o espaco ocupado pela barra fixa.
- **Mobile Responsivo com Scroll Horizontal**: Em telas com largura inferior a 960px, as abas (`.plf-tabs`) passam a se organizar em um carrossel flexivel com scroll horizontal suave e barra invisivel, prevenindo colapso do layout.
- **Ocultacao Inteligente de Titulo (abaixo de 768px)**: A marca textual `plf-nav-title` ("PlantiumAI") e ocultada via media query em telas pequenas, preservando apenas o icone circular e o botao de Login na navbar mobile para otimizacao de espaco.

## 3. Resolucao de Cache do Next.js
Durante o processo de testes locais, identificou-se que alternar comandos de producao (`npm run build`) com comandos de desenvolvimento (`npm run dev`) gera colisoes de cache (gerando erros como `MODULE_NOT_FOUND` para chunks como `331.js`). 
- **Solucao padrao**: Terminar a tarefa do servidor, deletar a pasta `.next/` completamente (`Remove-Item -Recurse -Force .next`) e reiniciar o servidor.
