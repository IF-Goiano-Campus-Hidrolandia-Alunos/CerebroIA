---
tags: [dotnet, ddd, domain-driven-design, padroes]
updated: 2026-06-25
author: Colaborador1
---

## Definição

Domain-Driven Design (DDD) é uma abordagem de modelagem de software complexo focada na estreita colaboração entre especialistas do domínio e engenheiros de software, traduzida em código por meio de padrões táticos.

## Contexto

Utilizado em sistemas corporativos .NET para organizar regras de negócio complexas na camada de Domínio, evitando o modelo anêmico (classes sem comportamento).

## Detalhes

- **Entidades (Entities):**
  - Classes que possuem uma identidade única contínua ao longo de seu ciclo de vida (ex: ID do cliente).
  - Contêm estado e comportamento (métodos que validam e alteram propriedades).
- **Objetos de Valor (Value Objects):**
  - Objetos imutáveis que não possuem identidade própria, definidos inteiramente por suas propriedades (ex: Endereço, CPF).
  - Dois value objects são iguais se todos os seus atributos forem iguais.
- **Raízes de Agregação (Aggregate Roots):**
  - Entidades principais que agrupam entidades menores e objetos de valor relacionados, garantindo a integridade dos dados e das regras de negócio em bloco.
- **Repositórios (Repositories):**
  - Interfaces definidas no domínio para realizar operações de persistência e recuperação das raízes de agregação.
- **Eventos de Domínio (Domain Events):**
  - Mensagens internas que indicam que algo relevante ocorreu no domínio, permitindo o desacoplamento de ações (ex: PedidoCriadoEvent).

## Links

- [[dotnet-arquitetura-limpa]]
- [[dotnet-solid-principios]]
