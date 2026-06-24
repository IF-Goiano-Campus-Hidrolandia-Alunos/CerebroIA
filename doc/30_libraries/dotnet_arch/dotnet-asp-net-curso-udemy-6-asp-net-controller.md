---
tags: [importado, dotnet]
updated: 2026-06-21
---

[[concepts/pagina-inicial-asp-net]]
![[concepts/r-3-png-center|200]]

Como criar um Controller para definirmos nossas Requisições a API REST
Entenda o [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-2-asp-net-rest]] neste artigo.
Entenda como criar um template ASP.NET neste artigo: [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-1-asp-net-template]]

---
```table-of-contents
```
## Inicio
---
Primeiro criamos um arquivo dentro do diretório **Controller** no projeto

![[concepts/aspnet-create-controller-png]]
Depois abrimos o arquivo **launchSettings.json** e colocamos uma rota que iremos criar para ajustar do template criado

![[concepts/aspnet-launchsettings-config1-png]]

## Controller da classe Person
---
Antes de mexer aqui deve ser feito os seguintes tutoriais primeiros:

1. [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-3-asp-net-model]]
2. [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-4-asp-net-services]]
---

### Configurando o Service no nosso Controller

Agora que temos o nosso Service, devemos importar ele no nosso Controller, da seguinte forma:
1) Dentro da classe PersonController vamos criar uma nova variável chamado o nosso Service.
```csharp
private IPersonService _personService;
```
O nome com underline no inicio é um padrão do .NET para não ter que chamar o `this` e para usar como uso global, segue o exemplo do clean code.
2) Depois chamamos no construtor a espera de um Service, como mostra abaixo:
```csharp
// ANTES
public PersonController(ILogger<PersonController> logger)
{
    _logger = logger;
}

// DEPOIS
public PersonController(ILogger<PersonController> logger, IPersonService personService)
{
    _logger = logger;
    _personService = personService;
}
```

Com isso já podemos usar o nosso Service no Controller.

### Configurando as rotas HTTP
---
Agora que temos definido os métodos que iremos usar para fazer as requisições que se encontram explicados na Implementation dos [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-4-asp-net-services]] podemos fazer nossos métodos do Controller para interagirmos com as requisições de entrada na API.

Antes no nosso template somente usamos o HTTP request de GET, mas agora iremos poder usar todas.

#### HttpGet
---
Possuímos duas rotas para o GET, uma é do ID e a outra é de todos os dados, temos como exemplo os dois métodos:
```csharp
/*
 * -------------------------
 * HTTP GET (READ) ALL DATA
 * -------------------------
*/

[HttpGet]
public IActionResult Get()
{
    return Ok(_personService.FindAll());
}

/*
 * ---------------------
 * HTTP GET (READ) BY ID
 * ---------------------
*/
[HttpGet("{id}")]
public IActionResult Get(long id)
{
    var person = _personService.FindbyID(id);
    if (person == null) return NotFound(); 
    return Ok(person);
}
```

- No primeiro método iremos retornar $\color{lightgreen}{\sf 200 \space OK}$ e entregando na Response do Postman todos os registros criados, sendo chamados pelo Service no método $\color{lightblue}{\sf FindAll()}$ que irá interagir com o banco de dados e trazer os objetos.
- No segundo método temos uma rota diferente do HttpGet inicial, onde ele recebe um valor pela requisição definidos por `{}` na rota (no caso ele vai receber um ID). É utilizado o método do Service chamado $\color{lightblue}{\sf FindbyId(id)}$ que busca no banco de dados um registro pelo ID definido. Caso ele não encontre o Registro retorna para o response $\color{red}{\sf 404 \space NOT \space FOUND}$ e caso encontre o registro ele retorna $\color{lightgreen}{\sf 200 \space OK}$ junto com o objeto encontrado no response do Postman.

#### HttpPost
---
Para o POST (Create) temos o seguinte código de exemplo:
```csharp
/*
 * -------------------
 * HTTP POST (CREATE)
 * -------------------
*/

[HttpPost]
public IActionResult Post([FromBody] Person person)
{
    if (person == null) return BadRequest();
    return Ok(_personService.Create(person));
}
```

- Neste exemplo temos que o nosso método possui o $\color{yellow}{[FromBody]}$  que significa que ele vai pegar o Body da requisição e transformar no objeto Person definido, então tudo que colocarmos no Postman na aba **Body** ele vai transformar em nossa API em um objeto Person. Caso o Body esteja vazio, ele vai retornar $\color{red}{\sf 400 \space BAD \space REQUEST}$, caso tenha um valor, ele vai utilizar o método do Service $\color{lightblue}{\sf Create(Person \space person)}$ para criar o objeto Person no nosso banco de dados e retornar ele no nosso Response do Postman.

#### HttpPut
---
O PUT (Update) é a mesma estrutura do POST, a única coisa que muda é que iremos usar o método $\color{lightblue}{\sf Update(Person \space person)}$ para atualizarmos no banco de dados nosso objeto passado.

```csharp
/*
 * ------------------
 * HTTP PUT (UPDATE)
 * ------------------
*/

[HttpPut]
public IActionResult Put([FromBody] Person person)
{
    if (person == null) return BadRequest();
    return Ok(_personService.Update(person));
}
```

#### HttpDelete
---
O DELETE serve para chamarmos o método do Service $\color{lightblue}{\sf Delete(id)}$ para remover o dado do banco de dados e não retorna nada para o response

```csharp
/*
 * ---------------------
 * HTTP DELETE (DELETE)
 * ---------------------
*/

[HttpDelete("{id}")]
public IActionResult Delete(long id)
{
   _personService.Delete(id);
    return NoContent();
}
```

É bem simples, ele remove o dado e entrega o resultado $\color{lightgreen}{\sf 204 \space NO \space CONTENT}$.

---

## Alterando o launchSettings.json
---
Após configurado os métodos, devemos alterar o launchSettings.json para iniciar o nosso projeto em uma rota específica.

Primeiro devemos alterar a Rota do nosso Controller para iniciar com o prefixo `api` dai ele vai pegar esse prefixo e depois o nome do Controller projetado, como mostrado abaixo:
```csharp
// ANTES

[ApiController]
[Route("[controller]")]
public class PersonController : ControllerBase
{}

// DEPOIS

[ApiController]
[Route("api/[controller]")]
public class PersonController : ControllerBase
{}
```

Depois disso abrimos o nosso launchSettings.json e chamamos o Controller do Person definido nesse exemplo:

![[concepts/aspnet-changelaunchsettings-png]]
E pronto! toda vez que iniciarmos o projeto, ele vai iniciar na rota $\color{lightgreen}{\sf GET}$ padrão com todos os dados salvos e assim podemos ver os exemplos mockados. 

---
## Próximo
---
[[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-7-asp-net-run-project]]