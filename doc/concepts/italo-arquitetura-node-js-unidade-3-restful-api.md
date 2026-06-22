---
tags: [importado, italo]
updated: 2026-06-21
---

[[concepts/rest]] é um estilo arquitetural para construção de serviços Web que significa a Transferência de Estado Representacional (REpresentational State Transfer)

O termo **RESTful** caracteriza serviços Web que seguem <mark class="hltr-yellow">integralmente as recomendações REST,</mark> diferentemente daqueles RESTlike que implementam parcialmente suas recomendações.

## Princípios de Design

- Definições do protocolo HTTP
- ﻿﻿Estrutura uniforme de Endpoint
- ﻿﻿Abordagem stateless (sem estado)
- ﻿﻿Abordagem HATEOAS
- ﻿﻿Controle do versionamento da API
- ﻿﻿Controle adequado do cache
- ﻿﻿Documentação clara e adequada da API


|          |     Não RESTful     |                    |
| :------: | :-----------------: | :----------------: |
|  Verbo   |        href         |        Ação        |
|   POST   |  /bookmarks/create  |   Criar (Create)   |
|   GET    |  /bookmarks/show/1  | Visualizar (Read)  |
|   POST   | /bookmarks/update/1 | Atualizar (Update) |
| POST/GET | /bookmarks/delete/1 |  Apagar (Delete)   |
|          |       RESTful       |                    |
|  Verbo   |        href         |        Ação        |
|   POST   |     /bookmarks      |   Criar (Create)   |
|   GET    |    /bookmarks/1     | Visualizar (Read)  |
|   PUT    |    /bookmarks/1     | Atualizar (Update) |
|  DELETE  |    /bookmarks/1     |  Apagar (Delete)   |

### Abordagem stateless
O Servidor não mantem estado sobre a sessão do usuário/aplicação
Toda requisição deve conter todas informações requeridas (como parte da URI, na query string, no corpo ou no cabeçalho)

#### Benefícios
- Simplifica o servidor
- Maior escalabilidade uma vez que o servidor não mantém informações sobre sessão
- Servidores de balanceamento de carga não precisam se preocupar com dados de sessão
- Maior confiabilidade (recuperação de falhas)

### Abordagem HATEOAS
Hipertexto com mecanismo de estado da aplicação
Retorna o proximo estado possivel da aplicação com base no estado atual.