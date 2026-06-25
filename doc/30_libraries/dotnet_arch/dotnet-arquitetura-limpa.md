---
tags: [dotnet, arquitetura, clean-architecture, design-pattern]
updated: 2026-06-25
author: Colaborador1
---

## Definição

Arquitetura Limpa (Clean Architecture) é um padrão de design de software que promove a separação de preocupações por meio de camadas concêntricas, onde a dependência aponta sempre de fora para dentro.

## Contexto

Aplicável em projetos .NET modernos (ASP.NET Core Web API, Worker Services) para garantir testabilidade, independência de frameworks e facilidade de manutenção a longo prazo.

## Detalhes

- **Camada de Domínio (Domain):**
  - Fica no núcleo da aplicação.
  - Contém entidades, value objects, exceções do domínio e interfaces de repositórios.
  - Não possui dependências externas (sem referências a Entity Framework ou outras bibliotecas).
- **Camada de Aplicação (Application):**
  - Contém as regras de negócio da aplicação (use cases).
  - Define DTOs, validadores e comandos/consultas (CQRS).
  - Depende apenas da camada de Domínio.
- **Camada de Infraestrutura (Infrastructure):**
  - Contém as implementações de acesso a banco de dados (EF Core Core/Dapper), serviços de email, mensageria e integrações de API.
  - Depende das camadas de Aplicação e Domínio.
- **Camada de Apresentação (Presentation / WebAPI):**
  - Ponto de entrada da aplicação (Controllers, Minimal APIs).
  - Responsável pela autenticação, serialização JSON e tratamento global de erros.

## Links

- [[dotnet-asp-net-curso-udemy-9-asp-net-context]]
- [[dotnet-domain-driven-design]]
