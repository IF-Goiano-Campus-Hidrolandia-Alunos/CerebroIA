---
tags: [importado, dotnet]
updated: 2026-06-21
---

[[concepts/pagina-inicial-asp-net]]
![[concepts/r-3-png-center|200]]

```table-of-contents
```

## Páginas anteriores
---
- [[concepts/dotnet-asp-net-curso-udemy-1-asp-net-template]]
- [[concepts/dotnet-asp-net-curso-udemy-2-asp-net-rest]]
- [[concepts/dotnet-asp-net-curso-udemy-3-asp-net-model]]
- [[concepts/dotnet-asp-net-curso-udemy-4-asp-net-services]]
- [[concepts/dotnet-asp-net-curso-udemy-5-asp-net-controller-template]]
- [[concepts/dotnet-asp-net-curso-udemy-6-asp-net-controller]]
- [[concepts/dotnet-asp-net-curso-udemy-7-asp-net-run-project]]
- [[concepts/dotnet-asp-net-curso-udemy-8-postman]]
- [[concepts/dotnet-asp-net-curso-udemy-9-asp-net-context]]
- [[concepts/dotnet-asp-net-curso-udemy-10-asp-net-ajustando-model]]
- [[concepts/dotnet-asp-net-curso-udemy-11-asp-net-ajustando-implementations]]

## O que é Repository
---
O **padrão Repository** é uma abordagem importante no desenvolvimento de aplicações ASP.NET. Ele se origina do **Domain-Driven Design (DDD)** e propõe a criação de objetos chamados **Repositories**, que gerenciam coleções de dados persistidos. A principal característica dos Repositories é que eles são **agnósticos à tecnologia utilizada**, ou seja, não estão vinculados a um banco de dados específico, cache de memória ou qualquer outra fonte de dados.

Aqui estão alguns pontos essenciais sobre o padrão Repository:

1. **Separação de Responsabilidades**: O padrão Repository ajuda a separar a responsabilidade de acesso a dados das outras camadas da aplicação. Isso melhora a organização do código e facilita a manutenção.
    
2. **Menor Acoplamento**: Ao utilizar o padrão Repository, o acoplamento entre as camadas da aplicação é reduzido. Isso significa que as mudanças no acesso a dados não afetam diretamente outras partes do sistema.
    
3. **Testabilidade Aprimorada**: O uso de interfaces com o padrão Repository permite a criação de testes unitários mais eficientes. Isso ocorre porque podemos criar implementações de teste para os Repositories sem depender de um banco de dados real.
    

Para ilustrar, vejamos um exemplo prático de como implementar o padrão Repository em uma aplicação ASP.NET Core com o Entity Framework (EF) Core:

1. **Interface ICustomerRepository**:
    
    - Primeiro, criamos uma interface chamada `ICustomerRepository`. Essa interface define os métodos básicos de acesso aos dados, como `GetAll`, `GetById` e `Insert`.
2. **Classe CustomerRepository**:
    
    - Em seguida, implementamos a classe `CustomerRepository`, que é responsável por realizar a interação com a entidade “Customer”. Nessa classe, transferimos o código de acesso a dados que estava anteriormente no Controller.

## Criando o Repository
---
Agora que sabemos o que é o Repository em teoria, vamos criar um Repository em nosso projeto, onde vamos criar um diretório novo com o nome Repository e criar a interface para o nosso objeto Person

![[concepts/aspnet-repository-png|400]]

Depois criamos uma interface que chamaremos de __IPersonRepository__

![[concepts/aspnet-repositorypersoninterface-png]]

Essa Interface vai ter os mesmos construtores do Service, onde iremos implementar mais um que é o _Exists_ que utilizamos antes:

![[concepts/aspnet-repositorypersoninterface2-png]]

Depois criamos um diretório chamado _Implementations_ e criamos a classe __PersonRepositoryImplementation__ com os mesmos métodos do __PersonServiceImplementation__ sendo a principal mudança que o método _Exists_ agora será público.

```csharp
using RESTTemplate.Model;
using RESTTemplate.Model.Context;

namespace RESTTemplate.Repository.Implementations
{
    public class PersonRepositoryImplementation : IPersonRepository
    {
        private SQLiteContext _context;

        public PersonRepositoryImplementation(SQLiteContext context) 
        { 
            _context = context; 
        }

        
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

        public List<Person> FindAll()
        {
            return _context.Persons.ToList();
        }

        public Person FindbyID(long id)
        {
            return _context.Persons.SingleOrDefault(p => p.Id.Equals(id));
        }

        public Person Update(Person person)
        {
            if (!Exists(person.Id)) return null;

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

        public bool Exists(long id)
        {
            return _context.Persons.Any(p => p.Id.Equals(id));
        }
    }
}
```

Toda a lógica dos Services agora será modificada!

Foi ajustado também a chamada do método _Exists_ no update onde caso não exista o ID ele deve retornar `null`.
```csharp
if (!Exists(person.Id)) return null;
```

## Adicionando a dependência no Program.cs
---
Assim como fizemos no Service, devemos alterar o _Program.cs_ adicionando a conexão com o Repository que foi recém criado, de uma forma bem simples, adicione o seguinte código abaixo da dependência do Service:

```csharp
builder.Services.AddScoped<IPersonRepository, PersonRepositoryImplementation>();
```


