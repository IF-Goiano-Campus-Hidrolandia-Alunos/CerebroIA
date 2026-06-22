---
tags: [plantiumai, web, dashboard, integracao, nextjs, claude]
updated: 2026-06-21
---

## Definição

Roteiro técnico e orientações para portar e integrar a interface rica do dashboard pós-login do PlantiumAI (desenhada originalmente no Claude Design) para dentro da aplicação web Next.js (`web/`).

## Contexto

A plataforma web possui uma página de login (`/login`) e signup (`/signup`) configurada com Auth.js que protege as rotas sob `/app/*`. A interface exibida após o login é um protótipo simplificado. Criamos e validamos localmente uma versão de alta fidelidade e interativa que deve substituir a atual.

### Localização dos Arquivos de Referência

- **Template Original do Claude Design**:
  [Dashboard.dc.html](file:///C:/Users/thyag/OneDrive/Desktop/PlantiumAI-main/PlantiumAI/templates/dashboard/Dashboard.dc.html)
- **Interface Local Transpilada e Validada (React Standalone)**:
  [dashboard-local.html](file:///C:/Users/thyag/OneDrive/Desktop/PlantiumAI-main/PlantiumAI/dashboard-local.html)
  *(Este arquivo roda localmente na porta 8080 e contém 100% da lógica e design system de tokens embutidos)*

---

## Passos para o Claude Realizar a Integration

### 1. Sistema de Estilos e Design System
O template original usa classes exclusivas do PlantiumUI (ex: `.pl-card`, `.pl-btn`, `.pl-root`, `.pl-chip`) e tokens CSS definidos no `:root`.
- **Decisão de Estilo**: Importar o arquivo de estilos globais [_ds_bundle.css](file:///C:/Users/thyag/OneDrive/Desktop/PlantiumAI-main/PlantiumAI/_ds_bundle.css) na aplicação Next.js (no `web/src/app/globals.css`), ou traduzir as regras de vidro e gradiente do PlantiumUI para classes nativas do Tailwind CSS para manter a consistência da stack do Next.js.
- **Tema Light/Dark**: Garantir que as variáveis de tema do CSS (`[data-theme=dark]`) conversem perfeitamente com o seletor de classes escuras do Next.js/Tailwind.

### 2. Substituição do Componente Principal do Dashboard
O arquivo principal que renderiza a tela pós-login é:
- [dashboard-demo.tsx](file:///C:/Users/thyag/OneDrive/Desktop/PlantiumAI-main/web/src/components/dashboard-demo.tsx)
- Claude deve substituir a visualização atual de `GeralView` e `TecnicaView` dentro do `dashboard-demo.tsx` pela lógica estruturada em `dashboard-local.html` (linhas 680 a 877).

### 3. Integração de Gráficos ECharts
O dashboard validado possui 8 gráficos ECharts interativos (Trend, Temp, Hum, CO2, pH, Radar, Compare, Heatmap).
- Instalar a dependência oficial do ECharts para React no Next.js (`npm install echarts echarts-for-react`) ou utilizar o carregamento sob demanda para evitar problemas de Server-Side Rendering (SSR).
- Replicar as opções de configuração (`setOption`) idênticas às funções declaradas no arquivo `dashboard-local.html` (linhas 432 a 497).

### 4. Roteamento e Subpáginas
O Next.js utiliza rotas de diretório para navegação:
- `/app` -> Tela Inicial / Dashboard
- `/app/locais` -> Locais Monitorados (Estufas, Containers)
- `/app/sensores` -> Listagem e status em tempo real
- `/app/alertas` -> Histórico e Timeline de avisos
- `/app/configuracoes` -> Configurações de Perfil, Limiares e Notificações

**Ação**: Distribuir o HTML e lógica das seções correspondentes de `dashboard-local.html` para suas respectivas páginas dentro de `web/src/app/app/`:
- `locais/page.tsx` (linhas 880 a 915)
- `sensores/page.tsx` (linhas 918 a 953)
- `alertas/page.tsx` (linhas 956 a 986)
- `configuracoes/page.tsx` (linhas 989 a 1048)

---

## Links

- [[concepts/plataforma-web-arquitetura]]
- [[concepts/design-system-landing]]
- [[concepts/narrativa-oficial-plantiumai]]
