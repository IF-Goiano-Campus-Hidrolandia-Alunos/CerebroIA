---
tags: ['databasesqlneon', 'documentacao', 'postgres', 'sql', 'drizzle']
updated: 2026-06-21
---

## Definição

Padrão de otimização de banco de dados e queries relacionais Postgres/Neon para Database SQL Views Vs Materialized Views.

## Contexto

Garante que o Neon Postgres (serverless) execute leituras e escritas com a menor latência e maior paralelismo.

## Detalhes

- Funcionamento físico das tabelas e índices no Postgres.
- Estruturação de queries eficientes e leitura de planos de execução.
- Esquemas no Drizzle ORM e migrações resilientes sem downtime.

### Exemplo de Implementação Prática

```sql
-- Exemplo de CTE Recurso (Recursive Common Table Expression)
WITH RECURSIVE hierarquia_categorias AS (
  -- Âncora: Seleciona a categoria raiz
  SELECT id, nome, id_pai, 1 AS nivel
  FROM categorias
  WHERE id_pai IS NULL
  
  UNION ALL
  
  -- União recursiva para buscar subcategorias
  SELECT c.id, c.nome, c.id_pai, h.nivel + 1
  FROM categorias c
  INNER JOIN hierarquia_categorias h ON c.id_pai = h.id
)
SELECT * FROM hierarquia_categorias ORDER BY nivel, nome;
```

## Links

- [[00_MOC]]
- [[concepts/guia-organizacao-para]]
- [[concepts/guia-dataview-obsidian]]
