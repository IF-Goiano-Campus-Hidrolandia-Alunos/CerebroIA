---
tags: [workflow, pesquisar, automatico, agente, ia, loop, autonomo]
updated: 2026-06-21
---

## Objetivo

Executar pesquisas autônomas sobre tecnologias, bibliotecas ou conceitos de programação e documentá-las automaticamente no vault, estruturando uma nota conceitual em `concepts/`, uma nota de cache em `external_cache/` e atualizando o `00_MOC.md`. Suporta modo de execução autônoma contínua (loop).

## Pré-requisitos

- Python 3 instalado no sistema.
- Acesso à internet para realizar buscas e chamada de API.
- Uma chave de API do Gemini (obtenha gratuitamente em: [Google AI Studio](https://aistudio.google.com/)).

## Modos de Execução

### 1. Modo Manual (Tópico Específico)
Use este modo quando quiser pesquisar e documentar um assunto específico de imediato.
- Abra o terminal na raiz do vault e execute `pesquisar.bat` com o assunto desejado entre aspas:
  ```bash
  .\pesquisar.bat "regras de re-conexao MQTT na ESP32"
  ```

### 2. Modo Autônomo Contínuo (Loop)
Use este modo para deixar o agente trabalhando em segundo plano. Ele analisará o estado atual do vault e os componentes do projeto para pesquisar e documentar automaticamente tópicos relevantes em falta.
- Dê dois cliques em `pesquisar.bat` ou abra o terminal na raiz do vault e execute sem passar nenhum argumento:
  ```bash
  .\pesquisar.bat
  ```
- O terminal exibirá logs em tempo real sobre os tópicos descobertos, pesquisas web efetuadas, compilações da IA e gravações de arquivos.
- Para encerrar o agente autônomo, pressione `Ctrl + C` no terminal.

## Validação

- Verifique se a nota conceitual foi criada em `doc/concepts/`.
- Verifique se a nota de cache foi criada em `doc/external_cache/`.
- Abra o [00_MOC.md](file:///C:/Users/thyag/OneDrive/Desktop/Brain-main/doc/00_MOC.md) e confira se os links foram inseridos nas listas correspondentes automaticamente.

## Troubleshooting

- **Chave de API inválida** -> Delete o arquivo `.env` na raiz do vault e rode o comando novamente para reinserir a chave correta.
- **Python não encontrado** -> Certifique-se de que o executável `python` está adicionado ao `PATH` do Windows.
