---
tags: [importado, italo]
updated: 2026-06-21
---

Simular desenvolvimento mais próximo de Desktop: Estado dos componentes, Eventos, Ciclos de vida da página e etc.

Abstrair complexidades do desenvolvimento web.

## Características

- Possui ciclo de vida
- Controi toda a página novamente a cada atualização do estado
- Armazena o estado da página em um campo hidden no html
- Custo alto de tráfego
- Cada arquivo é uma página
	- Arquivos ASPX são páginas da sua interface web
	- Automaticamente cria-se a classe relacionada a página ASPX.cs e ASPX.designer.cs
	- A URL referencia diretamente a página física (arquivo com extensão ASPX)

## Ciclo de vida
![[concepts/pasted-image-20240708220702-png]]

## ASCX e Master Page

- MasterPage é uma página especial que pode conter funcionalidades comuns entre as páginas que implementam: Cabeçalho, rodapé, Autenticação, Carrinho de compras e etc

- User Controls (ASCX) é uma subpagina, funcionalidade padrão que pode ser repetir em mais de uma página

## Vantagens

- Facilidade de entendimento
- Velocidade de produção
- Menor preocupação com renderização
- Abstração de pontos mais complexos
	- Manter status dos componentes de forma automática
	- Gestão de eventos simples: ao mudar o texto, ao clicar, ao selecionar
	- Chamadas e requisições simplificadas: Ajax ou PostBack
