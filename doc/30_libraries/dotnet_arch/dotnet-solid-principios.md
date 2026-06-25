---
tags: [dotnet, csharp, solid, boas-praticas]
updated: 2026-06-25
author: Colaborador1
---

## Definição

SOLID são cinco princípios de design de software orientado a objetos compilados por Robert C. Martin para tornar sistemas mais compreensíveis, flexíveis e fáceis de manter.

## Contexto

Aplicável na escrita de qualquer código C# em projetos .NET para evitar classes infladas, alto acoplamento e rigidez arquitetural.

## Detalhes

- **Single Responsibility Principle (SRP):**
  - Uma classe deve ter um, e apenas um, motivo para mudar.
  - Evitar classes que realizam lógica de banco, tratamento de HTTP e formatação simultaneamente.
- **Open/Closed Principle (OCP):**
  - Entidades de software devem ser abertas para extensão, mas fechadas para modificação.
  - Utilizar interfaces e polimorfismo em C# para adicionar novos comportamentos sem alterar o código existente.
- **Liskov Substitution Principle (LSP):**
  - Classes derivadas devem ser capazes de substituir suas classes base sem alterar o comportamento correto do programa.
  - Evitar lançar `NotImplementedException` ao herdar de interfaces ou classes abstratas.
- **Interface Segregation Principle (ISP):**
  - Muitas interfaces específicas são melhores do que uma interface única de propósito geral.
  - Clientes não devem ser forçados a depender de métodos que não utilizam.
- **Dependency Inversion Principle (DIP):**
  - Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.
  - Injetar interfaces (abstrações) no construtor das classes em C#, nunca instanciar diretamente classes de infraestrutura.

## Links

- [[dotnet-arquitetura-limpa]]
- [[dotnet-domain-driven-design]]
