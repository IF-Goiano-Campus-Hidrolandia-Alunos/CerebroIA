---
tags: [importado, dotnet]
updated: 2026-06-21
---

a[[concepts/pagina-inicial-asp-net]]
![[concepts/r-3-png-center|200]]

```table-of-contents
```

## Rodando o projeto
---
É bem simples rodar o projeto no Visual Studio, onde após configurado o $\color{lightgreen}{\sf launchSettings.json}$ com as rotas definidas no [[30_libraries/dotnet_arch/dotnet-asp-net-curso-udemy-6-asp-net-controller]] somente precisamos clicar no Runner desejado, possuindo 3 principais:

![[concepts/aspnet-runningoptions-png]]
 Podemos selecionar a opção que quiser e clique em **Run...** que é onde tem o nome da opção escrita:
 ![[concepts/visualstudiorun-gif]]
 Vai abrir uma página Web, onde vai iniciar na URL definida em `launchUrl` que deve ser o código da API ou de um Controller específico como mostrado a nossa URL vai ser `api/person` que vai iniciar o GET geral, como mostrado abaixo:
 ![[concepts/visualstudiorun2-gif]]
 Com isso podemos testar as requisições diretamente no Browser ou podemos testar no Postman enquanto estiver rodando o projeto no Visual Studio.