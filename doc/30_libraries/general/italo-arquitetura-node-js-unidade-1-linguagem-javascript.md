---
tags: [importado, italo]
updated: 2026-06-21
---

## Browsers e ECMAScript engines

| Browser / Ambiente | Web Engine | ECMAScript Engine        |
| ------------------ | ---------- | ------------------------ |
| Mozilla Firefox    | Gecko v    | Spider Monkey            |
| Google Chrome      | Blink      | Google V8                |
| Apple Safari       | WebKit V   | JavaScriptCore           |
| Internet Explorer  | Trident    | Chakra Core              |
| Edge               | EDGE       | Chakra Core \| Google V8 |
## Capacidades do Javascript no navegador

1. Manipulação de objetos da página HTML e tratamento de eventos (DOM Document Object Moddel)
2. Comunicação com o servidor e o uso de APIs via AJAX (XMLHttpRequest | Fetch)
3. Persistência de dados (Indexed DB e Local Storage)
4. Interação com APIs do HTML5: Canvas, Media, File, Drag and Drop, Geolocation, Web Workers, History entre outros.

# Novidades ES6

## Conceito `let` e `const` 

* `var`: define elementos de escopo global ou escopo de função, se for dentro de funções.
* `let` e `const` definem elementos de escopo local.
```js
var z = 'original Z';

{
	let x = 'original X';
	var y = 'original Y''
	
	console.log(`x: #{x} -- y: ${y} -- z: ${2} --`);
	{
		// novo escopo ==> novo x
		const x = "novo-- X";
		console.log(`x: ${x} -- y: $(y} -- z: ${2} -- `);
	}
	// retorno ao escopo anterior ==> original x
	console.log(`x: ${x} -- y: ${y} -- z: ${2} --`);
｝

console.log(`z: ${z} `); // z é global
console.log(`y: ${y} `); // y é global
console.log(`x: $(x} `); // x é local e linha gera erro
 ```

## Template Literals

* Similar a strings, com crases (\`..\`)no lugar de apostrofes ('..') ou aspas ".")
* Permite textos em múltiplas linhas
* Permite a inserção de expressões por meio da construção ${ expr }

## Arrow Function

Arrow Functions são uma sintaxe simplificada para a definição de funções.

```js
// forma tradicional de declaração
let soma = function (a, b) { return a + b }

// Declaração com arrow functions 
let soma = (a, b) => { return a + b }

// ou sem as chaves
let soma = (a, b) => a + b
```

> [!tip] 
> O operador `this` em uma Arrow Function faz referência ao bloco que contém a função, diferente de funções normais.

```js
var bob = {
	_name: "Bob",
	_friends: [],
	
	printFriends() {
		this._fiends.forEach(f => 
			// this._name será 'Bob' pois está no escopo do objeto bob
			console.log(`${this._name} knows ${f}`);
		)
	}
}
```

## Parâmetros default

Funções podem definir valores padrões para parâmetros não enviados

```js
const foo => (num = 0) => {
	console.log(num)
}

foo(); // 0
foo(1); // 1
```

## Destructuring

Permite a associação de elementos utilizando casamento de padrões

```js
const [a, b, c] = [1, 'dois', 3];

console.log({a, b, c}) // {a: 1, b: 'dois', c: 3}

const foo = ({ name }) => console.log(`nome: ${name}`);

foo({name: 'Italo'}) // nome: Italo

// Fail-soft destructuring
var [a] = [];

console. log(`a: ${a)``); // Imprime ==> a: undefined

// Fail-soft destructuring with defaults
var [a, b = 1] = [2];

console.log(`a: ${a} | b: ${b}`); // Imprime ==> a: 2 | b: 1
```

# Arquitetura JavaScript

![[concepts/pasted-image-20240527215925-png]]

### Componentes
- Call Stack: Pilha Single Thread que executa os eventos
- Event Loop: Captura o callback na fila e empilha na Call Stack
- Callback Queue: Fila de callbacks que fica aguardando serem retiradas pelo Event Loop e serem executadas na Call Stack;
- Web APIs: Lado de processamento do Navegador (Podendo ser multi-thread)

> [!tip] Single Thread!
> O javascript executa suas funções em apenas 1 Thread.

## Single Thread Javascript

```js
const log = (...p) => console.log(...p)

setTimeout(() => log('A'), 0);
log('B');
setTimeout(() => log('C'), 100);
setTimeout(() => log('D', 0));

let i = 0;
while (i < 1000000) {
	let ignore = Math.sqrt(i);
	i++;
}

log('E');
```

Nesse código o output de log será a seguinte ordem:
1. B -> Pois é o primeiro log
2. E -> Chamado após o loop while
3. A -> Como iniciou com um `setTimeout` a Call Stack executa a chamada da Web API, que executa o tempo no navegador em uma Thread Separada e após a finalização do tempo e enviado a callback para a  Callback Queue. Porém, a leitura do código ja foi lida e preenchida a fila com as demais linhas de código. Oque faz ele ficar após a finalização da Thread.
4. D
5. C

## `Promises` - Programação Assíncrona

Veio para aprimorar o processamento assíncrono em cadeia, resolvendo problemas como *Callback Hell*, evitando  aninhamento extensivo de callbacks.

### Antes

```js
doSomething((result) => {
	doSomethingElse(result, newResult => {
		doThirdThing(newResult, finalResult => {
			console.log(`Final: ${finalResult}`);
		}, fallback);
	}, fallback)
}, fallback)
```

### Com `Promises`

```js
doSomething()
.then(result => doSomethingElse(result))
.then(newResult => doThirdThing(newResult))
.then(finalResult => console.log(`Final: ${finalResult}`))
.catch(fallback)
```

Uma `Promise` é um mecanismo que recebe uma função que por sua vez apresenta dois callbacks:
1. `resolve`: Função a ser executada caso seja bem sucedido
2. `reject`: Função a ser executada caso haja falha

```js
let p = new Promise((resolve, reject) => {
	// lógica demorada
	
	if (/* condição sucesso */)
		resolve("Valor que foi processado");
	else 
		reject(Error("Operação Falhou"))
})

p().then(...).catch(...)
```


As `Promises` buscam simplificar a programação assíncrona. Recursos similares realizados anteriormente via libs como: jQuery ou deferred.js