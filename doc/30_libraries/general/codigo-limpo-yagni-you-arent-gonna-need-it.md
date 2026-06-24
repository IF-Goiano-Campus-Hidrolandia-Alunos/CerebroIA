---
tags: ['codigolimpoarquitetura', 'documentacao', 'arquitetura', 'solid', 'cleancode']
updated: 2026-06-21
---

## Definição

Princípio de projeto arquitetural e escrita de código limpo para Codigo Limpo Yagni You Arent Gonna Need It.

## Contexto

Garante que o código permaneça legível, fácil de testar, de manter e livre de acoplamento excessivo.

## Detalhes

- Princípio teórico associado e sua justificativa prática.
- Padrões de refatoração para evitar códigos complexos ou acoplamento espaguete.
- Escrevendo testes de unidade isolados para validar a implementação.

### Exemplo de Implementação Prática

```typescript
// Código Limpo: Guard Clauses vs Ninhos de Ifs (Deixa o código legível)
// Código Ruim (Ninho de Ifs):
function processUserBad(user) {
  if (user !== null) {
    if (user.isActive) {
      if (user.hasPermission) {
        return "Acesso Concedido";
      }
    }
  }
  return "Acesso Negado";
}

// Código Limpo (Guard Clauses):
function processUserClean(user): string {
  if (!user) return "Acesso Negado";
  if (!user.isActive) return "Acesso Negado";
  if (!user.hasPermission) return "Acesso Negado";
  
  return "Acesso Concedido"; // Fluxo principal livre de identação excessiva
}
```

## Links

- [[00_MOC]]
- [[30_libraries/dotnet_arch/guia-organizacao-para]]
- [[30_libraries/dotnet_arch/guia-dataview-obsidian]]
