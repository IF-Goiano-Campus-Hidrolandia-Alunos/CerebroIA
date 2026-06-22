---
tags: [importado, dotnet]
updated: 2026-06-21
---

a[[concepts/pagina-inicial-asp-net]]
![[concepts/r-3-png-center|200]]

```table-of-contents
```
# Entendendo REST

## Definição
---
$\color{lightgreen}{\sf REST}$ significa $\color{lightgreen}{\sf RE}$presentational $\color{lightgreen}{\sf S}$tate $\color{lightgreen}{\sf T}$ransfer e é um estilo de arquitetura de software para sistemas distribuídos de hipermídia, como a World Wide Web.

É o tipo de arquitetura mais utilizado no mundo da programação hoje em dia.
## Boas práticas
---

1. Paginação dos dados: se forem muitos dados de uma pesquisa é importante poder paginar o número de registros para auxiliar na busca
2. Filtros configurados: ter formas de filtrar os dados para encontrar mais rápido.
3. Separar corretamente os recursos lógicos: cada request deve ser de uma informação específica, não misturando tudo para uma única coisa.
4. Tolerância a falhas: fazer com que a API consiga lidar corretamente com possíveis erros.
5. Cache de informações recorrentes: quando temos alguma info que precisamos buscar sempre, fazemos um sistema de cache que não precise sempre buscar o dado no banco de dados.
6. Conectividade com a API: achar formas que facilite o acesso as suas APIs de fora.
7. Definir Timeouts: para que não fique segurando o servidor permanentemente, dessa forma ele finaliza o processo caso não conclua em um tempo determinado.
8. Documentação da API: ache formas fáceis e práticas de documentar suas APIs para que qualquer um consiga utilizar ela.
9. Utilizar SSL: para melhor segurança ao seu projeto.
10. Versionamento de APIs: para caso algo dê de errado podemos avaliar a versão anterior.
11. Teste e Validação da API: para ver se a API está seguindo o fluxo corretamente.
12. Permitir exportações de infos em diferentes formatos (JSON, CSV, etc...)
13. Notificações: achar uma forma de notificar caso a API tenha tido um problema.
14. Monitore sua API: verificar como anda a utilização da API.

## Framework Swagger
---
Swagger é um framework para documentar APIs REST e mostrar as possíveis rotas disponíveis para serem usados pelos desenvolvedores.

![[concepts/swagger-png]]

## JWT - Jason Web Token
---
JWT é um framework para autenticação onde ele deve receber informações de login e criar um token que deve ser utilizado durante o tempo que estiver ativo.

Os tokens tem um tempo curto de uso, que é o tempo que ele valida sua autenticação, depois é só Logar novamente.

![[concepts/jwt-token-png]]

## HTTP Status Requests
---
Uma API REST utiliza os status HTTP como respostas recebidas de um servidor, onde podemos utilizar vários tipos, onde os principais são os seguintes:

- **Conjunto de Status Codes**

![[concepts/conjunto-de-status-codes-png]]

- **Códigos de Sucesso**

![[concepts/mais-utilizados-de-sucesso-png]]
![[concepts/status-de-ok-png]]

- **Códigos de falha**

![[concepts/mais-utilizado-de-erros-png]]
![[concepts/status-de-erros-png]]
![[concepts/status-de-erro-2-png]]

- **Código de resposta do servidor**

![[concepts/mais-usados-de-server-png]]

## Definição de CRUD
---

**CRUD** significa $\color{yellow}{\sf C}$reate, $\color{lightgreen}{\sf R}$ead, $\color{lightblue}{\sf U}$pdate, $\color{red}{\sf D}$elete.
![[concepts/crud-png]]
### $$\boxed{\color{yellow}\sf Create}$$

- **Create** serve para inserir recursos novos em um servidor ou banco de dados.
- Utilizamos o verbo HTTP chamado $\color{yellow}{\sf POST}$ e ele é o mais frequente usado para criar novos recursos.
- Em uma aplicação REST perfeita quando uma operação é executada com sucesso, retornando o HTTP status code $\color{green}{\sf 200 \space OK}$ ou $\color{green}{\sf 201 \space Created}$

### $$\boxed{\color{lightgreen}\sf Read}$$

- **Read** serve para selecionar ou recuperar um recurso do servidor ou banco de dados.
- Utilizamos o verbo HTTP chamado $\color{lightgreen}{\sf GET}$ e ele é usado para ler ou recuperar uma representação de um recurso. Em um cenário feliz um requisição GET retorna uma representação normalmente em JSON e um HTTP status code $\color{green}{\sf 200 \space OK}$
- Em um cenário de erro o retorno mais comum é $\color{red}{\sf 404 \space NOT \space FOUND}$ ou $\color{red}{\sf 400 \space BAD \space REQUEST}$

### $$\boxed{\color{lightblue}\sf Update}$$

- **Update** serve para modificar um recurso no servidor ou banco de dados.
- Utilizamos o verbo HTTP chamado $\color{lightblue}{\sf PUT}$ e ele é usado para atualizar informações, colocando um recurso conhecido no corpo da requisição (**body**) contendo as novas informações que representam o recurso original.
- Um update bem sucedido retorna o HTTP status code $\color{green}{\sf 200 \space OK}$ ou $\color{green}{\sf 204 \space No \space Content}$ quando não retorna nenhum conteúdo no body.

### $$\boxed{\color{red}\sf Delete}$$

- **Delete** serve para remover um recurso no servidor ou banco de dados
- Utilizamos o verbo HTTP chamado $\color{red}{\sf DELETE}$ e ele remove um recurso identificado por um ID
- Em uma deleção bem sucedida retorna-se o HTTP status $\color{green}{\sf 200 \space OK}$ junto com um corpo de resposta (**response**) com uma representação do item deletado.

---

## Próximo
---
[[concepts/dotnet-asp-net-curso-udemy-3-asp-net-model]]
