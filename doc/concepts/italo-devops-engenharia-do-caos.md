---
tags: [importado, italo]
updated: 2026-06-21
---

>[!info]
>"Precisamos identificar fragilidade antes que elas se manifestem em comportamentos aberrantes em todo sistema.
>Devemos lidar com fraquezas mais significativas de forma proativa, antes que afetem nossos clientes na produção. Precisamos de uma maneira de gerenciar o caos inerente a esses sistemas, aproveitar o aumento da flexibilidade e velocidade e ter confiança em nossas implantações de produção, apesar da complexidade que eles representam."

É um tipo de prática onde extressamos o sistema para validar se ele se comporta conforme o esperado. Gerando dessa forma, um conhecimento a respeito da infraestrutura e código do software.

## Exemplos de estressores

- Injeção de latência na chamada de APIs
- Aumento da carga de um processador
- Interromper conexões de rede
- Terminar um contêiner
- Remover um ambiente de produção inesperadamente

## Processo de engenharia do caos

1. Comece definindo o "estado estável" como uma saída mensurável de um sistema que indica um comportamento normal
2. A hipótese de que este estado estável continuará tanto no grupo controle quanto no grupo experimental.
3. Introduza variáveis que refletem eventos no mundo real, como servidores que falham, discos rígidos que funcionam mal, conexões de rede que são cortadas e etc.
4. Tente refutar a hipótese procurando uma diferença de estado estável entre o grupo controle e o grupo experimental.

> [!tip]
> Engenharia do caos é uma prática avançada para experimentar um sistema a fim de construir confiança na capacidade do sistema de suportar condições turbulentas na produção


