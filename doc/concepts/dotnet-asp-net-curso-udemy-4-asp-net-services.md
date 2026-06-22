---
tags: [importado, dotnet]
updated: 2026-06-21
---

[[concepts/pagina-inicial-asp-net]]
![[concepts/r-3-png-center|200]]

Em uma API REST no C#, os “Services” são componentes que encapsulam a lógica de negócios e as operações que podem ser reutilizadas. Eles são responsáveis por realizar tarefas específicas e complexas, como interagir com um banco de dados ou processar dados.

Os Services são usados para manter os [[concepts/dotnet-asp-net-curso-udemy-6-asp-net-controller]] enxutos e o código organizado. Em vez de colocar toda a lógica de negócios em um [[concepts/dotnet-asp-net-curso-udemy-6-asp-net-controller]], você pode criar um Service para lidar com essa lógica e, em seguida, injetar esse serviço no controlador. Isso torna o código mais fácil de manter e testar.

---

```table-of-contents
```

## Criando uma Service

### Criando um folder Services
---
O folder Services não vem como padrão no ASP.NET, por isso devemos criar um novo folder e chamar ele de Services, para isso clicamos com o botão direito no nome do projeto, clicamos em **Add..** e depois **New Folder...**, após isso definimos o nome como **Services**.

![[concepts/aspnet-createfolderservices-png]]

### Criando uma interface
---
Uma interface em C# é um tipo que define um conjunto de métodos e propriedades que uma classe ou struct deve implementar. Ela define um contrato que a classe ou struct deve seguir.

Aqui estão alguns pontos importantes sobre as interfaces em C#:

- Uma interface pode conter declarações (assinaturas sem nenhuma implementação) dos seguintes membros: Métodos, Propriedades, Indexadores e Eventos.
- As interfaces não podem declarar dados de instância, como campos, propriedades implementadas automaticamente ou eventos semelhantes a propriedades.
- A partir do C# 11, uma interface pode declarar membros `static abstract` e `static virtual` para todos os tipos de membro, exceto campos.
- Uma interface não pode conter campos de instância, construtores de instância ou finalizadores.
- Os membros da interface são públicos por padrão.

Para criar uma interface é bem simples, clicamos com o botão direito no folder que queremos criar a interface e selecionamos **Add...** depois **Class...**

![[concepts/aspnet-createinterface1-png]]
Em **Class...** selecionamos a opção **Interface** e colocamos o nome do nosso Model desejado começando com um I para dizer que é uma Interface e depois escrito Service para sabermos que é um Service da API, como no exemplo abaixo:

| Nome do Model | Nome do Service |
| ------------- | --------------- |
| Person        | IPersonService  |
Isso é um padrão para qualquer Service no C#.

![[concepts/aspnet-createinterface2-png]]

Quando criamos uma Interface, ele tem por padrão o seguinte código:

```csharp
namespace RESTTemplate.Services
{
    public interface IPersonService
    {
    }
}
```

$\color{yellow}{\sf namespace}$ = namespace serve para organizar um conjunto de classes pelo seu folder definido, no nosso exemplo acima a nossa classe IPersonService faz parte do folder Services da API RESTTemplate.

$\color{yellow}{\sf public}$ = public significa que nossa classe pode ser lidar e utilizada por todo o projeto, sem ser restrito a alguma lugar.

$\color{yellow}{\sf interface}$ = interface mostra que o nosso arquivo é uma interface do C# que podemos escrever os métodos que iremos usar em Controllers. 

### Definindo métodos na Interface
---
Agora iremos construir a estrutura base dos métodos que iremos utilizar em nossos Controllers, utilizando o sistema do CRUD explicado em [[concepts/dotnet-asp-net-curso-udemy-2-asp-net-rest]] onde temos os seguintes tipos:

$\color{yellow}{\sf Create}$ = utilizamos a requisição HTTP $\color{orange}{\sf POST}$ para criar um objeto no banco de dados, mas na nossa Interface usamos o método $\color{lightblue}{\sf Create(Object \space object)}$ para criarmos um objeto novo no banco de dados.
$\color{yellow}{\sf Read}$ = utilizamos a requisição HTTP $\color{cyan}{\sf GET}$ para buscar um objeto no banco de dados, mas na nossa Interface usamos o método $\color{lightblue}{\sf FindById(long \space id)}$ para procurar por um objeto específico pelo seu ID ou  $\color{lightblue}{\sf FindAll()}$ para procurar por todos os objetos existentes no banco de dados.
$\color{yellow}{\sf Update}$ = utilizamos a requisição HTTP $\color{lightgreen}{\sf PUT}$ para editar um objeto no banco de dados, mas na nossa Interface usamos o método $\color{lightblue}{\sf Update(Object \space object)}$ para atualizarmos um objeto já existente no banco de dados.
$\color{yellow}{\sf Delete}$ = utilizamos a requisição HTTP $\color{red}{\sf DELETE}$ para criar um objeto no banco de dados, mas na nossa Interface usamos o método $\color{lightblue}{\sf Create(Object object)}$ 

Com esses métodos temos as seguinte estruturas nas interfaces

```csharp
public interface IPersonService
{
    Person Create(Person person); // Cria uma nova pessoa no banco de dados
    Person FindbyID(long id); // Busca uma pessoa específica pelo seu ID
    List<Person> FindAll(); // Busca todas as pessoas cadastradas
    Person Update(Person person); // Atualiza uma pessoa definida no objeto
    void Delete(long id); // Deleta uma pessoa específica pelo seu ID
}
```

### Implementando os métodos da Interface
---
Agora que temos o nosso template do Service com sua interface, devemos implementar os métodos, por isso iremos criar um folder dentro do nosso folder **Services** chamado de **Implementations** onde iremos criar arquivos implementando os Services.

![[concepts/aspnet-createimplementation1-png]]
![[concepts/aspnet-createimplementation2-png]]
Como estamos criando um Service do Objeto Person, o nome da nossa implementação deve começar com o nome do objeto, dizer que é de um Service e dizer que é uma implementação.

| Nome do Model | Nome do Service | Nome do Implementation |
| ---- | ---- | ---- |
| Person | IPersonService | PersonServiceImplementation |
Para isso iremos criar uma classe com esse nome da seguinte forma: iremos clicar com o botão direito encima do folder **Implementations** e depois no **Add...** e selecione a opção **Class...**
![[concepts/aspnet-createimplementation3-png]]
Dai colocamos o nome da implementation escolhendo a opção **Class**

![[concepts/aspnet-createimplementation4-png]]
Para utilizarmos a nossa interface, devemos chamar ela na nossa classe inicial, a classe inicial é esta abaixo:

```csharp
namespace RESTTemplate.Services.Implementations
{
    public class PersonServiceImplementation
    {

    }
}
```

Para implementar devemos chamar a Interface como mostrado abaixo:

```csharp
namespace RESTTemplate.Services.Implementations
{
    public class PersonServiceImplementation : IPersonService
    {

    }
}
```

Chamar a interface vai mostrar um erro no Visual Studio, porque não foram implementados os métodos construtores definidos na Interface dentro da classe, para isso o Visual Studio mostra como implementar essa funções mais rápido usando o `Quick Fix` como na imagem abaixo:

![[concepts/aspnet-implementinterface-png]]
A estrutura inicial implementada utilizando o Visual Studio ficou assim

```csharp
using RESTTemplate.Model;

namespace RESTTemplate.Services.Implementations
{
    public class PersonServiceImplementation : IPersonService
    {
        public Person Create(Person person)
        {
            throw new NotImplementedException();
        }

        public void Delete(long id)
        {
            throw new NotImplementedException();
        }

        public List<Person> FindAll()
        {
            throw new NotImplementedException();
        }

        public Person FindbyID(long id)
        {
            throw new NotImplementedException();
        }

        public Person Update(Person person)
        {
            throw new NotImplementedException();
        }
    }
}
```

Agora podemos implementar a lógica que quisermos nos métodos do objeto Person.
Vamos implementar esses método após definirmos a conexão com o banco de dados.
#### Criando o método Create
---
#### Criando o método Delete
---
#### Criando o método FindAll
---
#### Criando o método FindById
---
#### Criando o método Update
---

## Ativando o nosso Service na API 
---
Agora que temos criado a nossa Service e seu Implementation, devemos chamar esse Service em nosso arquivo **Program.cs** (depois de .NET 8) ou **Startup.cs** (antes de .NET 8).
Isso que iremos fazer se chama $\color{magenta}{\sf Injeção \space de \space dependências}$ no .NET.
1) Abrimos o nosso arquivo **Program.cs**
2) Vamos até o método **ConfigureServices**
3)  Abaixo de _services.AddControllers();_ iremos adicionar as nossas Services
4) Para isso iremos usar o método _AddScoped<>_ passando como atributos primeiro o nosso Service com sua Interface e depois a nossa Implementation, como mostra abaixo

- Para versões anteriores do .NET 8 (no Startup.cs)
```csharp
services.AddScoped<IPersonService, PersonServiceImplementation>();
```
* Para versões depois do .NET 8 (no Program.cs)
```csharp
builder.Services.AddScoped<IPersonService, PersonServiceImplementation>();
```

5) Para adicionar as dependências podemos clicar em `Alt` + `Enter` para ele importar automaticamente o Service e o Implementation.

---
## Próximo
---
[[concepts/dotnet-asp-net-curso-udemy-5-asp-net-controller-template]]