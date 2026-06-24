---
tags: [importado, dotnet]
updated: 2026-06-21
---

a[[concepts/pagina-inicial-asp-net]]
![[concepts/r-3-png-center|200]]

```table-of-contents
```

## Páginas anteriores
- [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-1-asp-net-template]]
- [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-2-asp-net-rest]]
- [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-3-asp-net-model]]
- [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-4-asp-net-services]]
- [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-5-asp-net-controller-template]]
- [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-6-asp-net-controller]]
- [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-7-asp-net-run-project]]
- [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-8-postman]]
- [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-9-asp-net-context]]
- [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-10-asp-net-ajustando-model]]

## Arrumando Implementations
---
Quando criamos o Implementation no tópico [[concepts/4-asp-net-services-implementando-os-metodos-da-interface]] criamos somente um exemplo onde não precisava de banco de dados, agora iremos modificar essa classe para implementar as regras de configuração com o banco de dados.

### Invocando o Context e Criando construtor
---
Agora iremos chamar o nosso Context que criamos em [[concepts/9-asp-net-context-criando-um-context-para-acesso-ao-banco-de-dados]] sendo privado e com o nome começando com underline `_`

```csharp
private SQLiteContext _context;
```

Depois criamos o construtor do nosso __PersonServiceImplementation__ chamando o nosso Context nele:

```csharp
public PersonServiceImplementation(SQLiteContext context)
{
	_context = context;
}
```

### Atualizando o método FindAll
---
Agora que temos o Context conectado, alteramos o nosso método de busca de todas as pessoas utilizando o método do Context chamado __ToList()__ onde fica o nosso método assim:

```csharp
public List<Person> FindAll()
{
   return _context.Persons.ToList();
}
```

Vamos criar um exemplo pelo nosso SQLite Studio para termos um dado para verificar, como no INSERT abaixo:

```sql
INSERT INTO persons(first_name,last_name,address,gender)
VALUES ('Gabriel','Fanto','Porto Alegre','Male');
```

Então clicamos em _Run_ no SQLiteStudio e vai criar o dado em nosso banco, depois disso podemos rodar a seguinte Query para vermos os dados:

```sql
SELECT *
FROM persons;
```

Pelos SQLite Studio vai nos mostrar assim:

![[concepts/sqliteinsertselect-png]]

Após criarmos, podemos rodar o nosso projeto no Visual Studio e abrir a página web onde depois que fizemos a alteração do método __FindAll()__ deve aparecer esse registro, se aparecer a nossa conexão com o banco de dados foi um sucesso!

![[concepts/aspnet-findallsqliteconnection-png]]

### Atualizando o Método Create()
---
Para adicionarmos um objeto no banco utilizamos o método __Add(object)__ do Context e para salvar as modificações usamos o método __SaveChanges()__  para registrar nossas modificações.
Isso deve ser feito dentro da estrutura TRY-CATCH para que caso ocorra um erro podemos tratar ele no futuro, além disso no final depois de salvar tudo deve ser retornado o objeto _person_ de entrada para a __response__ do Postman.
Nosso método fica assim:

```csharp
public Person Create(Person person)
{
    try
    {
        _context.Add(person);
        _context.SaveChanges();
    }
    catch (Exception)
    {
        throw;
    }
    return person;
}
```

### Atualizando o método FindById()
---
Utilizamos do nosso Context o método __SingleOrDefault__ para buscar pelo ID um objeto no banco de dados, dessa forma retornando o objeto, como no exemplo:

```csharp
public Person FindbyID(long id)
{
    return _context.Persons.SingleOrDefault(p => p.Id.Equals(id));
}
```
Ele verificar o ID de entrada com os IDs do banco para ver se encontra algum que retorne o valor esperado.

### Atualizando o método Update
---
O método update é um pouco mais complexo, onde devemos verificar se existe o objeto que queremos alterar e caso não exista ele gera um novo objeto para nós, para isso criamos um novo método para verificar sua existência chamado _Exists_ :

```csharp
private bool Exists(long id)
{
	return _context.Persons.Any(p => p.Id.Equals(id));
}
```

Ele vai buscar o ID no banco de dados e se encontrar ele retornar True para esse método.

Após a criação desse método auxiliar, criamos uma validação com ele para verificar sua existência:

```csharp
if (!Exists(person.Id)) return new Person();
```

Caso não exista ele cria uma pessoa nova, senão continua nossa lógica.

Depois nós criamos uma variável buscando o objeto de entrada no banco, como se fez na busca por ID;

```csharp
var result = _context.Persons.SingleOrDefault(p => p.Id.Equals(person.Id));
```

Caso o result tenha dados, ele deve fazer um TRY-CATCH onde deve usar os métodos do Context chamado __Entry()__ para dizer que tem um dado novo entrando e o método __SetValues()__ para alterar os valores que estão salvos na variável _result_ buscando os valores atuais com _CurrentValues_:

```csharp
if (result != null)
{
	_context.Entry(result).CurrentValues.SetValues(person);
	_context.SaveChanges();
}
```

Com esses métodos ele vai mudar os valores salvos no banco de dados com os valores de entrada no Body do Postman.

O método completo fica assim:

```csharp
public Person Update(Person person)
{
    if (!Exists(person.Id)) return new Person();

    var result = _context.Persons.SingleOrDefault(p => p.Id.Equals(person.Id));

    if (result != null)
    {
        try
        {
            _context.Entry(result).CurrentValues.SetValues(person);
            _context.SaveChanges();
        }
        catch (Exception)
        {
            throw;
        }
    }
    return person;
}
```

### Atualizando o método Delete
---
Para deletar um dado iremos usar o método do Context chamado __Remove__ onde iremos buscar pelo objeto com o ID dele como feito no update e depois iremos remover.

```csharp
public void Delete(long id)
{
    var result = _context.Persons.SingleOrDefault(p => p.Id.Equals(id));

    if (result != null)
    {
        try
        {
            _context.Persons.Remove(result); // Aqui que mudou
            _context.SaveChanges();
        }
        catch (Exception)
        {
            throw;
        }
    }
}
```

Com isso ele busca o dado no banco e remove ele pelo ID passado!