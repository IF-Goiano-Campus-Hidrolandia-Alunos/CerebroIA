---
tags: [importado, italo]
updated: 2026-06-21
---

Padrão que define uma forma compacta e segura de tranferência de informações baseada em tokens no formato JSON (RFC-7519) utilizadas em mecanismos de autenticação e autorixação.

## Estrutura básica do token

### \[header]

Informações sobre o tipo do token e o algoritimo de criptografia utilizado.

```json
base64enc ({
	"alg": "HS256",
	"typ": "JWT"
})
```

### \[payload]

Dados da token, denominados Claims que podem ser reservados, públicos ou privados.

```json
base64enc({
	"id": "HS256",
	"roles": "ADMIN"
})
````

### \[signature]

Assinatura do token que garante a confiabilidade do token evitando alterácões

```
HMACSA256 (
		base64enc(header) + "." + base64enc(payload,
	secretKey
)
```

## Campos reservados (claims)

- `iss` (Issuer): Emissor do token JWT
- `sub` (Subject): Assunto do token
- `aud` (Audience): Identifica o público para o qual o token foi emitido
- `exp`: (Expiration Time) - Horário de expiração do token, a partir do qual não é mais aceita
- `iat` (Issued At): Horário em que o toke. foi emitida.

## Exemplo de JWT em Node

```js
require ('dotenv').config()
const JWT = require('jsonwebtoken')
const express = require("express")
const app = express()

app.get("/", function (req, res){
	JWT.sign(
		{ userID: 'abc123' },
		process.env.SECRET_KEY, 
		{ algorithm: 'HS256' },
		(err, token) => {
			if (err) console.error('Erro: ' + err);
			else console.log (token)
		}
	)
	res.send ('Hello JWT')
});

app.listen(3000);
```
