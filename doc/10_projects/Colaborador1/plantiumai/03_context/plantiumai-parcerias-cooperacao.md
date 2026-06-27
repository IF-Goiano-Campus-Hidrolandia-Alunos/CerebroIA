---
tags: [plantiumai, parcerias, fpm, varejoin, sirineo, cooperacao-tecnica]
updated: 2026-06-27
<!-- ultima alteracao: Cirineu badge=Mestrando ITA, role=CEO; Juliana badge=Gestao de Recursos -->
---

# Parcerias e Cooperacao Tecnica - PlantiumAI

Este documento registra as parcerias estrategicas e academicas estruturadas para apoiar o desenvolvimento do ecossistema PlantiumAI, englobando mentores, instituicoes de ensino e empresas de base tecnologica.

## 1. Integrantes Parceiros e Mentoria

### 1.1 Cirineu C. Fernandes & Juliana C. V. Fernandes
- **Perfil**: Cirineu C. Fernandes é Engenheiro Mecatrônico, Especialista em Telecomunicações e Segurança Pública, Mestrando no PPGAO pelo ITA no Departamento de Guerra Eletrônica e Sensoriamento Remoto, e CEO da SiriNEO Technologies. Juliana C. V. Fernandes é Fisioterapeuta e Administradora, atuando na Gestão de Recursos da SiriNEO Technologies.
- **Papel no Projeto**: Apoio na cooperacao tecnologica de hardware e integracao de sistemas de telemetria complexos. Atuam como conselheiros tecnicos para o design robusto do firmware ESP32 e dos componentes de instrumentacao eletronica das micro estufas.

### 1.2 Prof. Renato Ribeiro dos Santos
- **Perfil**: Diretor da Faculdade de Principios Militares (FPM) e fundador da empresa de tecnologia comercial VarejoIN.
- **Papel no Projeto**: Orientador cientifico e academico do Trabalho Cientifico de Engenharia de Software (Faculdade SENAI FATESG). Oferece mentoria de gestao de negocios e modelagem comercial para a insercao da solucao IoT no varejo de horticultura.

---

## 2. Empresas e Instituicoes Parceiras

### 2.1 SiriNEO Technologies (https://sirineotechnologies.com/)
- **Perfil**: Startup focada em desenvolvimento de hardware proprietario robusto, sensores avancados e sistemas eletronicos embarcados de alta integridade.
- **Contribuicao**: Servicos de mentoria tecnica e transferencia de conhecimento sobre barramento de dados e otimizacao de consumo energetico para os nos ESP32 do prototipo.

### 2.2 FPM · Faculdade de Principios Militares
- **Perfil**: Instituicao de ensino superior dedicada à formacao de lideres com foco em disciplina, gestao estrategica e rigor cientifico.
- **Contribuicao**: Apoiadora institucional academica do projeto, integrando o estudo de modelagem e sustentabilidade economica do hardware IoT e planos SaaS aos seus laboratorios de pesquisa.

### 2.3 VarejoIN
- **Perfil**: Empresa especializada em tecnologia de dados, business intelligence e automacao comercial para cadeias de distribuicao.
- **Contribuicao**: Apoio de modelagem comercial, definindo o perfil dos canais de venda e auxiliando na integracao do software a paineis corporativos de decisao (SaaS).

---

## 3. Integracao na HomePage (Landing Page)
Os parceiros e suas respectivas logos reais fornecidas foram organizados em uma secao exclusiva denominada **Parceiros e Apoiadores** logo abaixo de **Quem constroi a PlantiumAI**:
- Retratos profissionais reais: `web/public/landing/cirineu.jpg` (origem: SiriNEO), `web/public/landing/juliana.jpg` (origem: SiriNEO) e `web/public/landing/renato.png` (origem: FPM).
- Logotipos reais fornecidos: `web/public/landing/logo-sirineo.png` (linkado para https://sirineotechnologies.com/), `web/public/landing/logo-fpm.png` e `web/public/landing/logo-varejoin.png`.
- O layout utiliza grids CSS responsivos (`class="plf-team"` e `class="plf-pillars"`) com 3 colunas para integrantes e 3 colunas para logotipos das organizacoes parceiras.
- **Aba de Navegacao (Navbar)**: Foi adicionada a aba "Parceiros" na barra de navegacao principal das duas paginas:
  - Na Home Page (`web/src/components/landing.tsx`), aponta diretamente para a ancora local `#parceiros`.
  - Na Pagina de Planos (`web/src/app/planos/page.tsx`), aponta de forma absoluta para a ancora `/#parceiros`, permitindo o retorno direto à secao a partir de outra pagina.

