---
tags: [importado, dotnet]
updated: 2026-06-21
---

[[concepts/pagina-inicial-sql-linguagem]]

## O que é Database
Um database (ou banco de dados) em  SQL é uma coleção organizada de dados que são armazenados e acessados eletronicamente. Os bancos de dados SQL são geralmente usados em sistemas que requerem a manutenção e manipulação de grandes volumes de dados. Eles são baseados no modelo relacional, o que significa que os dados são organizados em tabelas. Cada tabela tem linhas (também chamadas de registros) e colunas (também chamadas de campos).

SQL, que significa Linguagem de Consulta Estruturada (Structured Query Language), é a linguagem padrão usada para interagir com bancos de dados SQL. Ela permite aos usuários criar, manipular e consultar dados em um banco de dados SQL.

Aqui está um exemplo simples de como um banco de dados SQL pode ser usado. Vamos supor que temos uma tabela chamada `Estudantes` com as colunas `ID`, `Nome` e `Curso`.

```sql
CREATE TABLE Estudantes (
    ID int,
    Nome varchar(255),
    Curso varchar(255)
);
```

Podemos inserir dados na tabela `Estudantes` usando o comando `INSERT INTO`:

```sql
INSERT INTO Estudantes (ID, Nome, Curso)
VALUES (1, 'João', 'Matemática');
```

E podemos consultar os dados na tabela `Estudantes` usando o comando `SELECT`:

```sql
SELECT * FROM Estudantes;
```

Este comando retornará todos os registros na tabela `Estudantes`.