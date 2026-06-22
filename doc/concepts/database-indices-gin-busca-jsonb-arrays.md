---
tags: ['databasesqlneon', 'documentacao', 'postgres', 'sql', 'drizzle']
updated: 2026-06-21
---

## Definição

Padrão de otimização de banco de dados e queries relacionais Postgres/Neon para Database Indices Gin Busca JSONB Arrays.

## Contexto

Garante que o Neon Postgres (serverless) execute leituras e escritas com a menor latência e maior paralelismo.

## Detalhes

- Funcionamento físico das tabelas e índices no Postgres.
- Estruturação de queries eficientes e leitura de planos de execução.
- Esquemas no Drizzle ORM e migrações resilientes sem downtime.

### Exemplo de Implementação Prática

```sql
-- Criação de índice parcial avançado e análise de query
CREATE INDEX idx_pedidos_pendentes 
ON pedidos (data_criacao DESC) 
WHERE status = 'pendente';

-- Analisando o plano de execução para garantir Index Scan
EXPLAIN ANALYZE
SELECT id, valor, data_criacao
FROM pedidos
WHERE status = 'pendente'
ORDER BY data_criacao DESC
LIMIT 10;
```

## Links

- [[00_MOC]]
- [[concepts/guia-organizacao-para]]
- [[concepts/guia-dataview-obsidian]]
