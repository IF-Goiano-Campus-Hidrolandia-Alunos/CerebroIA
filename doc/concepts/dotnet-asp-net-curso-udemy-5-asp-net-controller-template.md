---
tags: [importado, dotnet]
updated: 2026-06-21
---

[[concepts/pagina-inicial-asp-net]]
![[concepts/r-3-png-center|200]]

```table-of-contents
```

Agora vamos criar e entender as partes do template de um Controller!

## Classe

```csharp
[ApiController]
[Route("[controller]")]
public class CalculatorController : ControllerBase 
{
	// Insert code Here
}
```

Aqui, estamos definindo uma classe chamada `CalculatorController` que herda de `ControllerBase`. As anotações `ApiController` e `Route` são usadas para indicar que esta classe é um controlador de API e para definir a rota base para este controlador, respectivamente.

$\color{yellow}{\sf ControllerBase}$ = É uma classe base do ASP.NET Core que manipula solicitações HTTP, fornecendo um conjunto de propriedades e métodos comuns que Controllers podem usar para manipular solicitações HTTP e gerar respostas HTTP.
Um exemplo de método que o ControllerBase possui que utilizamos muito é o **Ok(object? value)** e **BadRequest(object? value)**

#### Exemplo

```Csharp
[HttpGet("mult/{firstNumber}/{secondNumber}")]
public IActionResult Mult(string firstNumber, string secondNumber)
{
    if (IsNumeric(firstNumber) && IsNumeric(secondNumber))
    {
        var mult = ConvertToDecimal(firstNumber) - ConvertToDecimal(secondNumber);
        return Ok(mult.ToString()); // ControllerBase.Ok
    }

    return BadRequest("Error! Invalid Input"); // ControllerBase.BadRequest
}
```

$\color{yellow}{\sf ApiController}$ = é um atributo do ASP.NET Core que, quando associado a um Controller ajuda a simplificar a codificação e a manter o código mais limpo. Este atributo indica que um tipo e todos os tipos derivados são usados para server a response de HTTP.
ApiController auxilia o ControllerBase a fazer requisições Web com os métodos implementados no ControllerBase.

$\color{yellow}{\sf Route}$ = É um atributo do ASP.NET Core que é usado para definir rotas para métodos de ação de um Controller. Ele descreve como os caminhos da URL são correspondidos ás ações e é usado para gerar URLs para links. O padrão é chamar todas as rotas definidas em cada método de ação ou criar uma rota geral, esse normalmente é o exemplo gerado automático:

```csharp
[Route("[controller]")]
```

Podemos alterar para uma rota desejada:

```csharp
[Route("Home/Index/{name?}")]
public IActionResult Index(string name)
{
    //...
}
```

Em relação ao código limpo, é melhor usar o **HttpGet**, ou **HttpPost** ou **HttpPut** ou **HttpDelete** para colocar a rota no método de ação como mostrado anteriormente:

```csharp
[HttpGet("mult/{firstNumber}/{secondNumber}")]
```
****

## Construtor

```csharp
private readonly ILogger<CalculatorController> _logger;
public CalculatorController(ILogger<CalculatorController> logger)
{
    _logger = logger;
}
```

Este é o construtor da classe `CalculatorController` e está injetando uma dependência de `ILogger<CalculatorController>`. A injeção de dependência é um padrão de design que permite que uma classe receba as dependências de outras classes.
`ILogger` é uma interface no .NET que permite registrar informações sobre a execução, erros e avisos dos sistemas de forma simples e fácil. É uma API ou biblioteca presente no .NET, do qual podemos utilizar para "escrever" alguma mensagem durante a execução do nosso código.
Esse construtor cria uma variável de somente leitura do `ILogger` para recebermos informações do projeto em tempo de execução, 

#### Exemplo:

Criamos um método de soma de dois valores:

```csharp
[HttpGet("sum/{firstNumber}/{secondNumber}")]
public IActionResult Get(string firstNumber, string secondNumber)
{
	var sum = ConvertToDecimal(firstNumber) + ConvertToDecimal(secondNumber);
    return Ok(sum.ToString());
}
```

Se quisermos ver o log da soma no console, devemos chamar a classe `_logger` criado no construtor e usar o método **LogInformation()** passando uma string para mostrar no console:

```csharp
[HttpGet("sum/{firstNumber}/{secondNumber}")]
public IActionResult Get(string firstNumber, string secondNumber)
{
	var sum = ConvertToDecimal(firstNumber) + ConvertToDecimal(secondNumber);
    _logger.LogInformation($"Resultado da soma: {sum}");
    return Ok(sum.ToString());
}
```

O resultado então é que sempre que chamar a requisição de soma, vai mostrar no console o resultado da variável sum.

![[concepts/aspnet-logger-png]]

---

## Métodos

Construímos dois tipos de métodos, os $\color{orange}{\sf Método \space de \space requisição}$ e $\color{orange}{\sf Métodos \space auxiliares}$.

### Métodos de requisição

###### HttpGet

Temos por exemplo a estrutura de um método de requisição GET:

```csharp
[HttpGet("sum/{firstNumber}/{secondNumber}")]
public IActionResult Get(string firstNumber, string secondNumber)
```

Este é um método de ação que responde a solicitações HTTP GET para a rota `sum/{firstNumber}/{secondNumber}`. Ele recebe dois parâmetros, `firstNumber` e `secondNumber`.

$\color{yellow}{\sf IActionResult}$ é uma interface no ASP.NET Core que especifica como o servidor deve responder à solicitação, como escrever dados na resposta ou retornar um código de status de erro. O tipo de retorno `IActionResult` é apropriado quando vários tipos de retorno `ActionResult` são possíveis em uma ação. Os tipos `ActionResult` representam vários códigos de status HTTP.

Qualquer classe não abstrata derivada de `ActionResult` se qualifica como um tipo de retorno válido. Alguns tipos de retorno comuns nesta categoria são `BadRequestResult` (400), `NotFoundResult` (404) e `OkObjectResult` (200).

Podemos colocar nesse método um conjunto de regras e variáveis como a soma abaixo:

```csharp
if (IsNumeric(firstNumber) && IsNumeric(secondNumber))
{
    var sum = ConvertToDecimal(firstNumber) + ConvertToDecimal(secondNumber);
    return Ok(sum.ToString());
}
```

Aqui, estamos verificando se os dois parâmetros são numéricos. Se forem, convertemos os números para decimal, somamos e retornamos o resultado com um status HTTP 200 (OK).

Caso algum dos valores não seja válido, podemos colocar um status 400 (Bad Request) para sabermos se funcionou a requisição.

```csharp
return BadRequest("Error! Invalid Input");
```

### Métodos auxiliares

Métodos auxiliares são métodos que ajudam a fazer alguma validação antes de criar um método, dessa forma podemos separar as lógicas necessárias

###### Método IsNumeric

Criamos o método `IsNumeric` para validarmos a string de entrada e ver se ele é um número válido para o cálculo.

A estrutura do método é a seguinte:

```csharp
private bool IsNumeric(string strNumber)
```

Este é um método privado que verifica se uma string pode ser convertida em um número.
Para isso, devemos converter a string em um decimal, como o exemplo abaixo:

```csharp
double number;
bool isNumber = double.TryParse(
    strNumber, 
    System.Globalization.NumberStyles.Any, 
    System.Globalization.NumberFormatInfo.InvariantInfo, 
    out number);
return isNumber;
```

$\color{yellow}{\sf System.Globalization.NumberStyles.Any}$ é uma enumeração no .NET que determina os estilos permitidos em argumentos de string numéricos que são passados para os métodos `Parse` e `TryParse` dos tipos numéricos integrais e de ponto flutuante.
Um exemplo de `NumberStyles.Any` permite que a string “1,234.56” seja analisada como o número 1234.56.

$\color{yellow}{\sf System.Globalization.NumberFormatInfo.InvariantInfo}$ é uma propriedade no .NET que obtém um objeto `NumberFormatInfo` somente leitura que é independente da cultura (invariável).
Ele representa as convenções de formatação da cultura invariável, que é uma cultura associada ao idioma inglês, mas não com qualquer país/região

Com toda essa info significa que isNumber é uma variável booleana que pega a string de entrada e verifica se está nos conformes com o estilo numérico de qualquer país, se for ele recebe o valor e entrega `True` ou `False`.

###### Método ConvertToDecimal

Esse método serve para pegarmos o valor de entrada em string e transformar em decimal para podermos calcular.

A estrutura base do método é o seguinte:

```csharp
private decimal ConvertToDecimal(string strNumber)
```

Este é outro método privado que tenta converter uma string em um número decimal. Se a conversão falhar, ele retorna 0.

A lógica do método é a seguinte, criamos uma variável decimal e tentamos fazer um `parse`(conversão) da string para decimal, se retornar True ele vai salvar o valor da conversão na variável criada, se retornar False vai retornar zero, dizendo que não pode converter.

```csharp
decimal decimalValue;
if (decimal.TryParse(strNumber, out decimalValue))
{
    return decimalValue;
}
return 0;
```

---
## Próximo
---
[[concepts/dotnet-asp-net-curso-udemy-6-asp-net-controller]]