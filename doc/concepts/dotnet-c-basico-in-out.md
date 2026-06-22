---
tags: [importado, dotnet]
updated: 2026-06-21
---

# $$\boxed{\sf Entrada \space e \space Saída}$$

<p align="center">
    <img src="../../imagens/R (3).png" width=200>
</p>

---

## Entrada

Entrada ou `Input` em inglês na programação significa entrada de valores do meio externo para o nosso programa.

Para isso usamos o namespace $\sf \color{orange}System$ com sua classe $\sf \color{orange}Console$ e sua método $\sf \color{orange}ReadLine()$ para pegar valores pelo terminal, onde o usuário tem que escrever algo.

```csharp
using System;

// ...

string valor = Console.ReadLine();
```

O valor de entrada sempre será uma $\sf \color{magenta}string$, por isso tem algumas funções que nos ajudam a converter esses valores para tipos específicos, para isso precisamos da classe $\sf \color{orange}Convert$ também do namespace $\sf \color{orange}System$ para transformar essas Strings, tendo os seguintes tipos de funções:

- **ToInt16(text)**: converte o valor para um número inteiro de 16 bits.
- **ToInt32(text)**: converte o valor para um número inteiro de 32 bits.
- **ToInt64(text)**: converte o valor para um número inteiro de 64 bits.
- **ToSingle(text)**: converte o valor para um número de ponto flutuante de precisão simples.
- **ToDouble(text)**: converte o valor para um número de ponto flutuante de precisão dupla.
- **ToDecimal(text)**: converte o valor para um número decimal.
- **ToBoolean(text)**: converte o valor para um valor booleano.
- **ToChar(text)**: converte o valor para um caractere Unicode.

```csharp
using System;

// ...

string valor = Console.ReadLine();
int convert = Convert.ToInt32(valor); // mais usado para inteiros
```

---

## Saída

Saída ou `Output` em Inglês na programação é uma forma de apresentar ao usuário o resultado de uma compilação do projeto no console, para verificar se os valores criados fazem sentido do que era esperado.

Para enviarmos valores para o console utilizamos o namespace $\sf \color{orange}System$ com a classe $\sf \color{orange}Console$ e a método $\sf \color{orange}Write$ ou $\sf \color{orange}WriteLine$.

* **Write(text)** : imprime no terminal na mesma linha.
* **WriteLine(text)** : imprime no terminal na linha e no fim faz uma linha nova para o próximo texto

```csharp
using System;

//...

Console.Write("Bem ");
Console.Write("Vindo");

// Saída: Bem Vindo
```

```csharp
Console.WriteLine("Bem Vindo");
Console.WriteLine("Ao mundo de Gumball");

/* Saída:
    Bem Vindo
    Ao mundo de Gumball
*/
```

Com a saída de dados podemos ver bem como está funcionando o que queremos no projeto, onde temos alguma formas de apresentar valores.

### Retornando valores de variáveis

Podemos retornar valores de variáveis de duas formas, uma dentro do texto e outra chamando as variáveis dentro do texto.

* Chamando por fora da string:

```csharp
using System;

//...

int valor = 5;
Console.WriteLine("Valor = " + valor);

// Saída: Valor = 5
```

* Chamando dentro de uma string, isso se chama **Interpolação**:

```csharp
using System;

//...

int valor = 5;
Console.WriteLine($"Valor = {valor}");

// Saída: Valor = 5
```

### Ajustando valores

Quando mexemos com valores de ponto flutuante (double) ele irá calcular e retornar valores muito grandes sem necessidade, para isso podemos ajustar os valores transformando em string o retorno e depois dizendo a estrutura que queremos.

Utilizamos o método $\sf \color{orange}ToString()$ para ajustar os valores para saírem com o número de casas após a vírgula, como mostra os exemplos abaixo:

* Exemplo da divisão sem ajuste

```csharp
// Divisão de 8 por 3
using System;

//...

double dividendo = 8.0;
double divisor = 3.0;
double divisao = dividendo / divisor;

Console.WriteLine($"Divisão = {divisao}");

// Saída: Divisão = 2,6666666666666665
```

* Exemplo da divisão com ajuste

```csharp
// Divisão de 8 por 3
using System;

//...

double dividendo = 8.0;
double divisor = 3.0;
double divisao = dividendo / divisor;

Console.WriteLine($"Divisão = {divisao.toString("0.##")}");

// Saída: Divisão = 2,67
```

### Colocando Entrada sem parar a compilação

Podemos adicionar um valor de entrada sem parar o programa, onde somente usando o $\sf \color{orange}ReadLine()$ ele vai parar o sistema até o usuário adicionar um valor, mas podemos usar o método $\sf \color{orange}SetIn()$ com um método chamado $\sf \color{orange}StringReader()$ para definirmos um valor de entradaa automático.

```csharp
using System;
using System.IO;

//...

string valorEntrada = "6";
Console.SetIn(new StringReader(valorEntrada));

string valorLido = Console.ReadLine();
Console.WriteLine($"Valor: {valorLido}");

//Saída: Valor: 6
```

Isso serve somente para não parar o processo do terminal esperando um valor de entrada, expliquei isso para que o CI/CD desenvolvido para esse exemplo não fique esperando eu dar um resultado para ele.


