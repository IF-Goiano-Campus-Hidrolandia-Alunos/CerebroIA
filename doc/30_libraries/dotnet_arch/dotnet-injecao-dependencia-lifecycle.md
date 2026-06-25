---
tags: [dotnet, injecao-dependencia, ciclo-vida, middleware]
updated: 2026-06-25
author: Colaborador1
---

## Definição

Injeção de Dependência (DI) em .NET Core é um middleware nativo para gerenciar a instanciação de classes e definir seus respectivos ciclos de vida (lifetimes) no container IoC.

## Contexto

Utilizado em todas as aplicações modernas .NET (ASP.NET Core) para registrar serviços, repositórios e contextos de banco de dados, configurando o tempo de vida da instância.

## Detalhes

- **Transient (Transitório):**
  - Registrado com `builder.Services.AddTransient<IService, Service>()`.
  - Uma nova instância do serviço é criada a **cada vez** que ele é solicitado pelo construtor ou resolvido do container.
  - Indicado para serviços leves e sem estado.
- **Scoped (Escopo):**
  - Registrado com `builder.Services.AddScoped<IService, Service>()`.
  - Uma nova instância do serviço é criada **uma única vez por requisição HTTP**.
  - Todos os componentes compartilhando a mesma requisição HTTP receberão a mesma instância.
  - Padrão para repositórios e contextos do Entity Framework (`DbContext`).
- **Singleton (Único):**
  - Registrado com `builder.Services.AddSingleton<IService, Service>()`.
  - Uma única instância do serviço é criada no início da aplicação e compartilhada durante **todo o tempo de execução** por todos os usuários.
  - Indicado para cache em memória ou serviços de configuração estática.

## Links

- [[dotnet-asp-net-curso-udemy-4-asp-net-services]]
- [[dotnet-solid-principios]]
