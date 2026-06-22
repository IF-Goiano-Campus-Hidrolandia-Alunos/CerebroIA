---
tags: [importado, italo]
updated: 2026-06-21
---

Com a crescente necessidade de usar aplicações para executar processos, fornecer serviços e colher dados, a observabilidade em sistemas ficou mais complexa. O OpenTelemetry vem justamente atuar no cerne do problema, ao permitir centralizar os processos de observabilidade de diferentes aplicações. Com a evolução da computação distribuída, tem sido exigida dos desenvolvedores e dos responsáveis pela gestão dos sistemas uma maior atenção à observabilidade. A complexidade cada vez maior dos microsserviços e das aplicações torna mais difícil identificar os lógs das aplicações, suas saídas e quando querys e serviços estão com tempo de resposta mais elevado do que o normal.

A criação do OpenTelemetry foi a solução encontrada pelos profissionais de DevOps e gestores para tornar a observabilidade das aplicações agnósticas aos vendors, ou seja, centralizar as ações para "driblar" as voltas que normalmente são dadas para elevar a capacidade de monitoramento. OpenTelemetry combinou os projetos OpenTracing e OpenCensus para aprimorar a observabilidade de sistemas e aplicações em rede.


O OpenTracing foi uma iniciativa de padrão aberto, voltada para a criação de uma aplicação que conseguisse direcionar o desenvolvimento de frameworks e rastrear rapidamente o caminho feito por logs, aberturas de chamadas, etc. Ou seja, seu foco é o tracing distribuído. 

O OpenTelemetry é justamente a combinação das funções do OpenTracing e do OpenCensus em uma só aplicação, elevando a capacidade de observabilidade dos microsserviços. Por isso, vem sendo considerado o futuro da telemetria instrumental. Ainda como aplicação de código aberto, o OpenTelemetry foca em três pilares. 

- Rastreamento distribuído
- Métricas
- Logs

Entre as funções mais importantes do OpenTelemetry, estão:

- Monitoramento de integridade dos microserviços
- Atribuição do uso de recursos a grupos de usuários segmentados.
- Criação de solicitações prioritárias entre recursos compartilhados. 

## Como funciona

- OpenTelemetry permite customizar as ferramentas para trabalhar em diferentes contextos de DevOps, conforme asssidades da equipe. 
- O Collector é a função que permite gerar, coletar processar e exportar para o vendor os dados de telemetria de forma padronizada, logo, ele é o componente principal para execução dos objetivos. Porém, com o OpenTelemetry o Collector não mais dependerá do vendor fornecedor, sendo, portanto, o que chamamos anteriormente de uma aplicação agnóstica. 