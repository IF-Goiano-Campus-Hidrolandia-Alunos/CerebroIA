---
tags: [importado, dotnet]
updated: 2026-06-21
---

# $${\boxed{\sf CRIANDO \space PRIMEIRO \space HELLO \space WORLD}}$$
---

O primeiro hello world é o mais emocionante, mas o que ninguém diz que tem várias formas e boas práticas.

[Padrão do .NET 6](#padrão-do-net-6)

[Básico](#básico)

[Boas práticas](#boas-práticas)

---

## Padrão do .NET 6

Quando criamos um novo programa, o próprio .NET cria um arquivo chamado `Program.cs` onde vem com a seguinte informação

```csharp
// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
```

O .NET após a versão 6 fica criando um Hello World simples sem importar ou utilizar nada, mas essa não é a melhor prática para quem está começando a desenvolver em C#.

---

## Básico

Uma estrutura básica de uma classe em C# é uma forma mais entendível com outras linguages, como Java, onde podemos construir uma classe com um método $\color{magenta}\sf Main$ como no exemplo em Java abaixo:

```java
// em Java
public class Teste {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
```

Uma estrutura que podemos usar no C# é bem parecido, mas o que muda é a classe e o método para imprimir informações no console e `string` a primeira letra é minúscula, como mostra abaixo:

```csharp
// em C#
public class Teste {
    public static void Main(string[] args) {
        System.Console.WriteLine("Hello World!");
    }
}
```

Essa estrutura ajuda a quem está recém começando a desenvolver em C# tenha um padrão com outras linguagens também de alto nível.

---

## Boas práticas

[Utilizando o using](#utilizando-o-using)

[entendendo o namespace](#entendendo-o-namespace)

[Uso de Classes](#uso-de-classes)

[O que é o método Main?](#o-que-é-o-método-main)

[Padrão esperado completo](#padrão-esperado-completo)


### Utilizando o using

- Toda vez que queremos usar algo do sistema devemos fazer a importação dessas bibliotecas, e isso é feito usando o $\color{lightblue}\sf using$.

```csharp
using system;
```

Esta chamada tras toda a biblioteca básica do C# para podermos usar, como por exemplo o $\color{magenta}\sf Console.WriteLine$.

`Console.WriteLine` é utilizado para apresentar no console um output (Saída de informação) do que você colocar dentro dele, no Java por exemplo é o _System.out.println(text)_.

No C# quando queremos apresentar um output usamos a seguinte estrutura com o `using`

```csharp
using System;

//...

Console.WriteLine("Hello World!");
```

### entendendo o namespace

$\color{magenta}\sf namespace$ é um conjunto de programas juntos (podemos dizer que é um diretório que possui um ou mais arquivos C#) e esse namespace é uma boa prática apresentar de onde pertence o arquivo que estamos mexendo, como por exemplo a seguinte estrutura do projeto:

```mermaid
flowchart LR
    A("#128193; HelloWorld") --> B("#128196; Program.cs")
```

$\color{gold}\sf HelloWorld$ é o nome do Diretório onde possui o arquivo `.csproj` e onde possui o arquivo C# chamado `Program` , temos então que no nosso arquivo o namespace dele é `HelloWorld`.

```csharp
namespace HelloWorld {
    public class Program {
        //...
    }
}
```

Se tivermos um caso onde é um diretório interno do diretório principal, como no diagrama abaixo, o nosso namespace é diferente:

```mermaid
flowchart LR
    A("#128193; HelloWorld") --> B("#128193; Services")
    B --> C("#128196; Program.cs")
```

A cada camada que vai entrando para chegar ao nosso arquivo C# deve ser apresentado no nome do namespace.

```csharp
namespace HelloWorld.Services {
    public Class Program {
        //...
    }
}
```

O namespace não é obrigatório, mas como boa prática e organização, nossas classes devem estar dentro de namespaces para ser melhor visto onde que o projeto se encontra.

### Uso de Classes

Classes é explicado melhor na parte de orientação a objetos, mas deixando claro aqui que pelas boas práticas todos os arquivos C# devem ser classes para armazenar os métodos dentro, por isso que dentro do namespace deve possuir a classe $\color{lightgreen}\sf com \space mesmo \space nome \space do \space arquivo$ utilizando o padrão CamelCase (todas as letras iniciais de uma palavra são maiusculas).

Essas classes podem ser colocados se são públicas ou privadas, mas como inicial não é necessário dizer a forma de visualização dela para as outras classes:

```csharp
using system;

namespace HelloWorld {
    class Program {
        //...
    }
}
```

### O que é o método Main?

O método principal que o .NET procura para rodar um programa é o método $\color{magenta}\sf Main$, que é o método que tem as infos que terão no output, onde ele espera uma String com argumentos e é ativada na hora que for compilado o projeto. Abaixo um exemplo desse método.

```csharp
using system;

namespace HelloWorld {
    class Program {
        public static Main(string[] args) {
            //...
        }
    }
}
```

- $\color{orange}\sf public$ determina que esse método é público para ser usado em outras classes.
- $\color{orange}\sf static$ determina que esse método não sofre alterações durante o uso dele no programa.
- $\color{orange}\sf String[] \space args$ significa que esse método espera um vetor de strings (conjunto de caractéres) vindas como atributos para ser utilizado pelo nome de `args` que siginifica argumentos.

### Padrão esperado completo

Tendo toda essa estrutura o esperado é como no código abaixo:

```csharp
using System;

namespace HelloWorld
{
    class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}

```






