---
tags: [importado, dotnet]
updated: 2026-06-21
---

a[[concepts/pagina-inicial-asp-net]]
![[concepts/r-3-png-center|200]]

```table-of-contents
```

## Páginas anteriores
---
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
- [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-11-asp-net-ajustando-implementations]]
- [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-12-asp-net-repository]]

## Atualizando nosso Service
---
Agora toda a lógica de conexão ao banco de dados ficou no __Repository__ como explicado em [[concepts/12-asp-net-repository-criando-o-repository]] e agora vamos chamar nosso Repository criado para ser usado no nosso Service, removendo assim o _context_ do Service:

```csharp
// Antes
private SQLiteContext _context;
public PersonServiceImplementation(SQLiteContext context)
{
    _context = context;
}

// Depois
private readonly IPersonRepository _repository;
public PersonServiceImplementation(IPersonRepository personRepository)
{
    _repository = personRepository;
}
```

Agora todos os métodos de conexão com o banco de dados ficarão somente implementados na classe __PersonRepositoryImplementation__ e os métodos na Interface que chamamos no nosso Service, então todos os métodos irão ter mudanças chamando somente do Repository.

### Atualização do Método Create

```csharp
// Antes
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

// Depois
public Person Create(Person person)
{
    return _repository.Create(person);
}
```

### Atualização do Método Update

```csharp
// Antes
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

// Depois
public Person Update(Person person)
{
   return _repository.Update(person);
}
```

### Atualização do Método Delete

```csharp
// Antes
public void Delete(long id)
{
    var result = _context.Persons.SingleOrDefault(p => p.Id.Equals(id));

    if (result != null)
    {
        try
        {
            _context.Persons.Remove(result);
            _context.SaveChanges();
        }
        catch (Exception)
        {
            throw;
        }
    }
}

// Depois
public void Delete(long id)
{
    _repository.Delete(id);
}
```

### Atualização do Método Exists

Ele pode ser removido porque ele somente é utilizado pelo Repository agora.

### Atualização do Método FindAll

```csharp
// Antes
public List<Person> FindAll()
{
   return _context.Persons.ToList();
}

// Depois
public List<Person> FindAll()
{
   return _repository.FindAll();
}
```

### Atualização do Método FindById

```csharp
// Antes
public Person FindbyID(long id)
{
    return _context.Persons.SingleOrDefault(p => p.Id.Equals(id));
}

// Depois
public Person FindbyID(long id)
{
    return _repository.FindbyID(id);
}
```