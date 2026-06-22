---
tags: [obsidian, dataview, tutorial]
updated: 2026-06-21
---

## Definição

O Dataview é um plugin do Obsidian que permite consultar, filtrar e listar dados das suas notas dinamicamente, funcionando como um banco de dados local para o seu vault.

## Contexto

À medida que o vault cresce, torna-se difícil encontrar conexões manualmente. O Dataview automatiza a agregação de dados ao ler metadados das notas (como tags, datas e propriedades personalizadas) e renderizá-los em tempo real em tabelas, listas ou tarefas.

## Detalhes

### 1. Metadados e Propriedades (YAML Frontmatter)

Para que o Dataview funcione bem, adicionamos metadados no topo de cada nota.
Isso é feito criando um bloco entre três traços `---` no início do arquivo:

```yaml
---
tags: [projeto, software]
autor: "SkepticMystic"
status: "Em Progresso"
prioridade: 3
---
```

#### Listas em Metadados
Podemos declarar listas de duas formas:
- **Linear (Inline):** `tecnologias: [Java, Spring, SQLite]`
- **Identada (Lista):**
  ```yaml
  tecnologias:
    - Java
    - Spring
    - SQLite
  ```

### 2. Metadados Implícitos (Inerentes)

Toda nota no Obsidian possui metadados automáticos que você pode usar nas suas buscas:
- `file.name`: O título do arquivo.
- `file.path`: O caminho completo da nota.
- `file.link`: Um link clicável para a nota.
- `file.size`: Tamanho em bytes.
- `file.ctime`: Data e hora de criação do arquivo.
- `file.mtime`: Data e hora da última modificação.
- `file.tags`: Lista de todas as tags presentes na nota.
- `file.day`: A data contida no título da nota (se o título for no formato YYYY-MM-DD).

---

### 3. Consultas Básicas com Dataview

As consultas são escritas em blocos de código markdown usando o identificador `` `dataview ``:

#### Consulta tipo LIST
Cria uma lista simples de arquivos baseada em filtros:
```dataview
LIST
FROM #projeto
WHERE status = "Em Progresso"
SORT file.mtime DESC
```

#### Consulta tipo TABLE
Gera uma tabela interativa com colunas customizadas:
```dataview
TABLE status, autor, prioridade
FROM "doc/concepts"
WHERE prioridade >= 2
SORT prioridade DESC
```

#### Consulta tipo TASK
Lista todas as tarefas pendentes (`- [ ]`) encontradas nas notas:
```dataview
TASK
FROM "doc/workflows"
WHERE !completed
```

### 4. Operadores e Cláusulas Úteis
- `FROM`: Limita a busca a uma pasta específica (ex: `FROM "doc/concepts"`) ou a uma tag (ex: `FROM #software`).
- `WHERE`: Filtra resultados por condições lógicas (ex: `WHERE status != "Concluído" AND prioridade > 1`).
- `SORT`: Ordena os resultados por qualquer campo (ex: `SORT file.ctime ASC` para os mais antigos primeiro).

## Links

- [[concepts/vault-system]]
- [[concepts/guia-organizacao-para]]
