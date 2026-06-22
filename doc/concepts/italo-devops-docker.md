---
tags: [importado, italo]
updated: 2026-06-21
---

Docker é uma tecnologia Open Source que aplica o conceito [[concepts/containers]], permitindo criar, executar, testar e implantar aplicações distribuídas dentro de containers de software.

Ele permite empacotar um software de contendo tudo que é necessário para a execução: código, runtime, ferramentas, bibliotecas, etc.

O Docker permite que você manipule aplicações rapidamente, de modo confiável e estável, em muitos ambientes virtuais físicos.

## Hello world 

```Dockerfile
FROM ubuntu:latest

ENV MESSAGE "Hello World!"

CMD echo ${MESSAGE}
```

## Buildando imagem

```shell
docker build -t nome-da-imagem .
```

Onde:
 `-t` : Define a tag da imagem para o build
 `nome-da-imgem`: Nome da tag que será buildado.
 `.`: Diretório onde tá presente o `Dockerfile`

## Executando uma imagem

```Shell
docker run nome-da-imagem -d
```

 Onde:
- `-d`: Diz ao docker para rodar em background
- 