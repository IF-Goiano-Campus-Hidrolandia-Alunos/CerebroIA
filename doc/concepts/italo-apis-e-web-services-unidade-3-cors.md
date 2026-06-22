---
tags: [importado, italo]
updated: 2026-06-21
---

CORS é um mecanismo de segurança HTTP que permite páginas de um Site A acessarem recursos de um site B

A política de mesma origem (same-origin) restringe sites de acessarem recursos apenas no servidor em que está hospedado, evitando que códigos maliciosos usem chamadas AJAX para repasse de informações em uma sessão aberta

O CORS define dois tipos de requisições:

![[concepts/pasted-image-20240618222121-png]]

## Simples

![[concepts/pasted-image-20240618222141-png]]

## Preflighted

![[concepts/pasted-image-20240618222218-png]]

## Configuração CORS em Node.js

Utilizando o módulo `cors`, podemos tratar a negociação HTTP para chamadas cross-origin.

Funcionalidades:
- Habilita CORS no servidor todo ou em rotas específica
- Altamente configurável

```js

const express = require ('express');
const cors = require ('cors');
const app = express();

// Configuração do CORS para permitir site específico
const corsOptions = {
	origin: 'https://www.exemplo.com/client', 
	methods: 'GET, PUT, POST, DELETE',
}

// Aplicando as configurações CORS 
app.use(cors(corsOptions));

// Rotas de exemplo para as operações CRUD 
app.get('/recurso', (req, res) => (}); 
app.post('/recursote', (req, res) => {}); 
app.put ('/recursote', (req, res) => 1}); 
app.delete('/recursote', (req, res) » 17);

app.listen (3000, () => { console. log ('Server ok'); });

```
