---
tags: [importado, italo]
updated: 2026-06-21
---

Inicialmente criado para substituir servidores Web bloqueantes como o Apache, o Node foi além e acabou sendo uma plataforma para criar aplicações distribuídas de diversas naturezas, um __nó__ em uma estrutura maior. 

A plataforma Nodejs é orientada a eventos com modelo não bloqueante. 

![[concepts/pasted-image-20240528223204-png]]

## Blocking vs Non-Blocking

### Abordagem Blocking

```js
import fs from 'fs';

// Bloqueia a execução até que o arquivo seja lido
const data = fs.readFileSync('/file.md');

console.log(data);

moreWork();
```

### Abordagem Non-Blocking

```js
import fs from 'fs';

fs.readFile('/file.md', (err, data) => {
	if (err) throw err;
	console.log(data)
});

// Ira executar na sequencia.
moreWork();
```

## Load Balacing e Proxy Reverso

![[concepts/pasted-image-20240528223844-png]]

# Principais Módulos Nativos do Node.js

| Módulo  | Descrição                                             |
| ------- | ----------------------------------------------------- |
| events  | Permite criar e manipular de eventos                  |
| http    | Permite criar servidores Web                          |
| dns     | Permite resolver nomes da Internet                    |
| path    | Permite manipular caminhos de arquivos                |
| OS      | Provê informações sobre o Sistema Operacional         |
| process | Provê informação sobre o processo Node.js em execução |
| net     | Permite criar servidores e clientes                   |
| url     | Interpreta strings de URLS                            |
| stream  | Manipula dados em fluxos                              |
|         |                                                       |
## Módulo Events - `eventEmitter`

| Método                          | Descrição                                                                                   |
| ------------------------------- | ------------------------------------------------------------------------------------------- |
| addListener (event, listener)   | Inclui um listener na fila para o evento passado como parâmetro                             |
| on (event, listener)            | Inclui um listener na fila para o evento passado como parâmetro                             |
| once (event, listener)          | Inclui um listener de um único disparo na fila para o evento passado como parâmetro         |
| removeListener(event, listener) | removeListener (event, listener) Remove o listener da fila do evento passado como parâmetro |
| removeAllListeners (event)      | Remove todos os listeners para o evento passado                                             |
| listeners(event)                | Retorna um array com os listeners para o evento como parâmetro                              |
| emit(event)                     | Executa os listeners ativos para o evento passado como parâmetro                            |
```js
import { EventEmitter } from "events"

const events = new EventEmitter();

events.addListener('oi', (data) => {
	console.log(`${data}, mandou um oi!`)
})

events.on('ola', (data) => {
	console.log(`${data}, disse olá!`)
})

events.emit('ola', 'italo')
```

## Módulo `process`

```js

// Variáveis de ambiente
process.env 

// Diretório de trabalho
process.cwd() 

// Diretório de execução
__dirname

// Arquivo de execução (entrypoint)
__filename

// Apresenta o processo
process
```

## Módulo `http`

```js
import http from "http";

// Cria um servidor e atribui uma callback de processamento da requisição.
const server = http.createServer((req, res) => {
	res.statusCode = 200
	res.setHeader('Content-type', 'application/json')
	res.end('{"user": "italo", "idade": "22"}')
})

// Define parâmetros (hostname e porta) e inicia o servidor

const hostname = '127.0.0.1'
const port = 3000

server.listen(port, hostname, () => {
	console.log(`Servidor rodando em: http://${hostname}:${port}/`)
})

```

## Modulo DNS

```js
import { Resolver } from "dns";

const resolver = new Resolver();

resolver.setServers(["8.8.8.8"]);

resolver.resolve("www.pucminas.com.br", (err, addr) => {
	if (err) {
		console.log(`Erro: ${err.message}`);
		return;
	}
	console.log(`IP: ${addr}`);
});
```
