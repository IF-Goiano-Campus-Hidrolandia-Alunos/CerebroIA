---
tags: [importado, italo]
updated: 2026-06-21
---

A lógica de negócio de uma aplicação ou os recursos disponíveis podem sofrer alterações com o tempo. Isso acaba refletindo na API desta aplicação.

Para garantir que os clientes tratem estas mudanças adequadamente é fundamental controlar os números das versões da API e refletir isso na forma de acesso garantindo o uso correto das funcionalidades disponíveis.

## Especificações comuns

### Via URL

- Domínio: `https://api-v1.servidor.com/recurso`
- Caminho do recurso: `https://api.servidor.com/v1/recurso` (Melhor)
- Parâmetro na query `https://servidor.com/recurso?v=1`

### Via cabeçalho HTTP

- Cabeçalho Accept `Accept: application/json;version=1`
- Cabeçalho Customizado: `Accept-Version: 1`

## Versionamento Semântico 

`version: "{major}.{minor}.{patch}`

