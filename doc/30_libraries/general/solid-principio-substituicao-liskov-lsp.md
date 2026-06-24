---
tags: ['codigolimpoarquitetura', 'documentacao', 'arquitetura', 'solid', 'cleancode']
updated: 2026-06-21
---

## Definição

Princípio de projeto arquitetural e escrita de código limpo para SOLID Principio Substituicao Liskov Lsp.

## Contexto

Garante que o código permaneça legível, fácil de testar, de manter e livre de acoplamento excessivo.

## Detalhes

- Princípio teórico associado e sua justificativa prática.
- Padrões de refatoração para evitar códigos complexos ou acoplamento espaguete.
- Escrevendo testes de unidade isolados para validar a implementação.

### Exemplo de Implementação Prática

```typescript
// Exemplo de Princípio de Inversão de Dependência (DIP) do SOLID
// 1. Definição da interface/contrato
interface DatabaseConnection {
  connect(): void;
  query(sql: string): any;
}

// 2. Implementação concreta
class PostgresDatabase implements DatabaseConnection {
  connect() { console.log('Conectado ao Postgres'); }
  query(sql: string) { return [{ id: 1, name: 'Teste' }]; }
}

// 3. Classe de alto nível que depende da abstração, não da concretização
class UserManager {
  constructor(private db: DatabaseConnection) {}
  
  getUserName(id: number) {
    const res = this.db.query(`SELECT name FROM users WHERE id = ${id}`);
    return res[0].name;
  }
}
```

## Links

- [[00_MOC]]
- [[30_libraries/dotnet_arch/guia-organizacao-para]]
- [[30_libraries/dotnet_arch/guia-dataview-obsidian]]
