---
tags: [importado, italo]
updated: 2026-06-21
---

É o método de autenticação distribuída. Quando uma aplicação implementa o OAuth, ela da a possibilidade do usuário se autenticar com um sistema que, possivelmente, ele ja confia e utiliza, como Google Accounts ou Apple. 

OAuth é um framework aberto definido pelo IETF (RFC 6749).

## Características 
- Evita exposição de senhas
- Facilita a interoperabilidade (Web, Mobile e Server)
- Controla a validade e o escopo do acesso concedido.

## Papeis do OAuth

### Dono do recurso

Entidade que possui recursos na rede e pode ser solicitado a autorizar o acesso a estes recursos protegidos

Ex: Usuário final.

### Aplicação Cliente

Sistemas envolvidos que são utilizados para acessar recursos disponíveis na rede. Podem ser confidenciais ou públicos.

Ex: Aplicações móveis e sites na Web.

### Servidor de Autorização

Sistema que controla a geração de tokens de acesso para as aplicações cliente.

Ex.: Google Accounts

### Servidor de Recursos

Ambiente que hospeda recursos protegidos na rede.

Ex.: Google Fotos

## Access Token

- O Access Token é uma credential para o acesso a um recurso protegido
- Trata-se de uma string em formato específico de acordo com a aplicação em questão
- Uma Access Token é obtida de acordo com o tipo de autorização
- A Access Token substitui a necessidade de usuário e senha.

## Tipos de Autorização

O protocolo OAuth 2 oferece 4 tipos de autorização

### Código de Autorização

Ocorre quando a Aplicação Cliente é uma aplicação Web ou nativa e mantém uma chave secreta. 

Ex.: Site X quer acessar seus dados do Facebook

### Autorização Implícita

Ocorre quando a Aplicação Cliente é baseada no browser (serverless), em linguagem de script e não pode manter uma chave secreta.

Ex.: Aplicações SPA

### Credenciais do Usuário

Ocorre quando a aplicação cliente é próxima do Servidor de Autorização e requer usuário e senha, normalmente, ambos feitos pela mesma empresa.

Ex.: Aplicativo "Gerenciador de Negócios" do facebook

### Credenciais do Cliente

Ocorre quando a Aplicação Cliente é proprietária dos recursos e não o usuáriofinal.

Ex.: Cloud Azure acessando dados em storage interno.