---
tags: [dotnet, cqrs, mediatr, padroes-projeto]
updated: 2026-06-25
author: Colaborador1
---

## Definição

CQRS (Command Query Responsibility Segregation) é um padrão arquitetural que separa as operações de leitura (Queries) das operações de escrita (Commands) em modelos de dados diferentes.

## Contexto

Utilizado em APIs .NET modernas em conjunto com a biblioteca MediatR para desacoplar as requisições HTTP da lógica de execução de negócios (use cases).

## Detalhes

- **Commands (Comandos):**
  - Representam intenções de mudança de estado do sistema (ex: `CriarPedidoCommand`).
  - Retornam geralmente apenas status de sucesso, identificadores criados ou dados mínimos.
- **Queries (Consultas):**
  - Representam solicitações de leitura de dados (ex: `ObterPedidoPorIdQuery`).
  - Otimizadas para retornar dados rápidos e DTOs específicos, sem efeitos colaterais.
- **MediatR (Mediator Pattern):**
  - Atua como um intermediador em memória para despachar os comandos e consultas para seus respectivos manipuladores (Handlers).
  - Promove o baixo acoplamento: o controller apenas envia o objeto com `_mediator.Send(command)` sem conhecer qual classe processará a mensagem.
- **Handlers:**
  - Classes específicas que implementam `IRequestHandler<TRequest, TResponse>` e contêm a lógica focada de um único caso de uso.

## Links

- [[dotnet-arquitetura-limpa]]
- [[dotnet-asp-net-curso-udemy-12-asp-net-repository]]
