---
tags: [importado, dotnet]
updated: 2026-06-21
---

[[concepts/pagina-inicial-asp-net]]
![[concepts/r-3-png-center|200]]

```table-of-contents
```

## Páginas anteriores
- [[concepts/dotnet-asp-net-curso-udemy-1-asp-net-template]]
- [[concepts/dotnet-asp-net-curso-udemy-2-asp-net-rest]]
- [[concepts/dotnet-asp-net-curso-udemy-3-asp-net-model]]
- [[concepts/dotnet-asp-net-curso-udemy-4-asp-net-services]]
- [[concepts/dotnet-asp-net-curso-udemy-5-asp-net-controller-template]]
- [[concepts/dotnet-asp-net-curso-udemy-6-asp-net-controller]]
- [[concepts/dotnet-asp-net-curso-udemy-7-asp-net-run-project]]
- [[concepts/dotnet-asp-net-curso-udemy-8-postman]]
- [[concepts/dotnet-asp-net-curso-udemy-9-asp-net-context]]

## Ajustando o Model
---
Agora que fizemos toda a criação do Context e sua configuração com o projeto, vamos ajustar o Model para se entender com os dados no banco de dados.
Os nomes que se encontram no banco de dados são diferentes aos nomes que se encontra na classe Model, por isso podemos fazer as modificações necessárias para que o Model reconheça esses valores.

### Anotação Table
Como vimos no estudo [[concepts/4-sqlite-tables]] vimos que o nome da nossa tabela de pessoas se chama _persons_ e o nome do nosso Model é _Person_ por isso podemos usar a anotação __Table__ para dissermos exatamente qual o nome que é esperado para enviar ao banco de dados.

```csharp
[Table("persons")]
public class Person {}
```

### Anotação Column

Para as colunas do banco de dados deve ser feito o mesmo, mas utilizando a anotação __Column__ onde iremos colocar os nomes como foram identificados na criação da tabela no tópico [[concepts/4-sqlite-tables-exemplo-de-tabela]] :

```sql
CREATE TABLE IF NOT EXISTS persons (
	person_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	address TEXT,
	gender TEXT
);
```

No ASP.NET ficam com os seguintes nomes ajustando:

```csharp

[Column("person_id")]
public long Id { get; set; }

[Column("first_name")]
public string FirstName { get; set; }

[Column("last_name")]
public string LastName { get; set; }

[Column("address")]
public string Address { get; set; }

[Column("gender")]
public string Gender { get; set; }
```

