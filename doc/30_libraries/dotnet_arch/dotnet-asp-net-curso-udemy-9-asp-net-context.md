---
tags: [importado, dotnet]
updated: 2026-06-21
---

a[[concepts/pagina-inicial-asp-net]]
![[concepts/r-3-png-center|200]]

## Páginas anteriores
- [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-1-asp-net-template]]
- [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-2-asp-net-rest]]
- [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-3-asp-net-model]]
- [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-4-asp-net-services]]
- [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-5-asp-net-controller-template]]
- [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-6-asp-net-controller]]
- [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-7-asp-net-run-project]]
- [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-8-postman]]

```table-of-contents
```

---
## Criando um Context para acesso ao banco de dados
---
Podemos usar vários tipos de banco de dados, mas nesse exemplo irei utilizar o SQLite por ser mais simples de configurar e mais simples de utilizar em projetos de POC (Proof of Concept).
Criei uma explicação bem mais a fundo de como utilizar o SQLite e como usar ele em nosso projeto como explicado em [[concepts/3-sqlite-database]] onde criamos lá como exemplo o banco de dados **restemplate** para nosso objetivo de entender a conexão de forma simples.

### Adicionando uma dependência
---
Dependências (ou Dependencies) são softwares criados na biblioteca do Nuget para podermos utilizar em projetos .NET, __Nuget__ é o gerenciador de pacotes do .NET que nos ajuda de uma maneira fácil de adicionar, remover e atualizar bibliotecas e ferramentas em projetos .NET.
Todas as bibliotecas e ferramentas adicionadas ficam dentro de _Dependencies_ no nosso projeto, para poder adicionar nesse diretório devemos clicar com o botão direito do mouse no nome do diretório _Dependencies_ e escolher a opção __Manage Nuget Packages__ 

![[concepts/aspnet-managenugetpackages1-png]]

Ele vai abrir uma página visual do Nuget para pesquisarmos o pacote que queremos instalar no nosso projeto, de forma simples e fácil.

### Entity Framework Core
---
O __Entity Framework Core__ (EF Core) é uma versão leve, extensível e de código aberto do Entity Framework, que é uma tecnologia de acesso a dados popular no .NET.

O EF Core é um _mapeador objeto-relacional (ORM)_ que permite aos desenvolvedores .NET trabalhar com bancos de dados usando objetos .NET. Ele elimina a necessidade da maior parte do código de acesso a dados que os desenvolvedores geralmente precisam escrever.

Com o EF Core, você pode realizar as seguintes tarefas:

- Modelar um domínio orientado a objetos no .NET e mapeá-lo para um banco de dados relacional.
- Consultar e manipular dados diretamente do código de aplicativo usando LINQ.
- Realizar o rastreamento de alterações, persistência e manipulação de dados de maneira eficiente.
- Migrar seu esquema de banco de dados de maneira segura usando migrações do EF Core.

O EF Core suporta muitos provedores de banco de dados, como SQL Server, SQLite, PostgreSQL, MySQL e muitos outros. Ele também suporta uma variedade de padrões de desenvolvimento de aplicativos, incluindo aplicativos de console, aplicativos de desktop, aplicativos da web ASP.NET Core e muito mais.

### Adicionando o EF Core com SQLite
---
Utilizando o ORM EF Core do SQLite nos ajuda a ter mais controle dos dados que estamos querendo que entre no nosso projeto, por isso quando abre a tela do Nuget para pesquisarmos pelo pacote devemos buscar por __EntityFrameworkCore.SQLite__.

![[concepts/aspnet-managenugetpackages2-png]]

Então clique em __Install__ e aceite os requisitos para o pacote e ele vai instalar para você nas dependências do projeto.
Assim que tiver baixado ele vai mostrar um check em verde no lado do pacote.

![[concepts/aspnet-installedpackage-png]]
Após instalado podemos verificar se ele foi corretamente adicionado clicando duas vezes no nome da API na área de __Solution Explorer__

![[concepts/aspnet-verifypackages-png]]

Devemos adicionar também o Pacote _Microsoft.EntityFrameworkCore.Tools_ junto com esse primeiro.

![[concepts/aspnet-efcorepackagetools-png]]
### Criando uma Classe de contexto de acesso
---
Agora que instalamos o pacote no projeto, vamos criar sua configuração no nosso projeto, onde iremos criar uma pasta dentro de _Models_ chamada __Context__ onde ficam armazenado as conexões com o banco de dados.
No nosso caso que estamos trabalhando com SQLite, vamos criar uma classe dentro do diretório __Context__ chamado __SQLiteContext__ .

Criação do Folder __Context__.

![[concepts/createcontextfolder-gif]]

Criação da classe __SQLiteContext__.

![[concepts/createcontextfile-gif]]

Nessa nova classe, temos que estender a classe do Entity Framework chamada __DbContext__ em nossa classe de conexão ao banco de dados e depois adicionar o _Entity Framework Core_ em nossa lista de pacotes conectados nessa classe.

```csharp
// Antes
namespace RESTTemplate.Model.Context
{
    public class SQLiteContext
    {
    }
}

// Depois
using Microsoft.EntityFrameworkCore;

namespace RESTTemplate.Model.Context
{
    public class SQLiteContext : DbContext
    {
    }
}
```

Agora vamos construir dois construtores para nossa classe, um deles é vazio e o outro recebe por parâmetro opções de acesso.

```csharp
using Microsoft.EntityFrameworkCore;

namespace RESTTemplate.Model.Context
{
    public class SQLiteContext : DbContext
    {
        public SQLiteContext() 
        { 
            
        }

        public SQLiteContext(DbContextOptions<SQLiteContext> options) : base(options)
        {

        }
    }
}
```

Qualquer Context deve ter essa estrutura básica, agora vamos construir os métodos dos modelos que queremos em nosso banco de dados.

### Criando método de acesso ao Model Person
---
Agora vamos colocar em nossa classe Context a conexão ao Model de Person, para isso adicionamos o seguinte atributo:

```csharp
public DbSet<Person> Persons { get; set; }
```

### Atualizando o appsettings.json
---
Agora que criamos o nosso Context para acessar ao Banco de dados, devemos atualizar o arquivo _appsettings.json_ com os dados de conexão.
No nosso caso passamos uma String com o nome do nosso banco de dados utilizando na string o nome __Data Source__.
Deve ser colocado todo o caminho até o banco de dados, onde no nosso caso quando criamos localmente em [[concepts/3-sqlite-database-criando-pelo-console]] ele se encontra no seguinte caminho: _C:\sqlite\db\restemplate.db_ e no _appsettings.json_ sempre que tiver uma barra deve colocar duas, como mostra o exemplo abaixo:

```json
"SQLiteConnection": {
  "SQLiteConnectionString": "Data Source=C:\\sqlite\\db\\restemplate.db"  
}
```
 Podemos colocar essa info antes do _Logging_ no _appsettings.json_

### Conectando o Connection no Program.cs
---
Em .NET 8 é feito essa configuração no _Program.cs_ onde vamos dizer a nossa API qual é a conexão do nosso banco de dados, onde colocamos essas informações depois de _AddControllers()_.
Primeiro criamos uma variável puxando as informações que se encontram no _appsetings.json_ como configuramos:

```csharp
var connection = builder.Configuration["SQLiteConnection:SQLiteConnectionString"];
```

Depois criamos um serviço chamado __AddDbContext<>()__ onde iremos conectar o Context que criamos nos passos anteriores e definimos as opções de acesso. 

```csharp
builder.Services.AddDbContext<SQLiteContext>(options => options.UseSqlite(connection));
```
