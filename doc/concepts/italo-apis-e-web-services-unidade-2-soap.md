---
tags: [importado, italo]
updated: 2026-06-21
---

Simple Object Access Protocol (SOAP)

O SOAP é uma proposta robusta para contrução de APIs que mescla complexidade e potência. Utiliza XML para definir comunicações estruturadas e se baseia em um par de cliente e servidor SOAP.

![[concepts/pasted-image-20240611205140-png]]

## Arquitetura 

- SOAP - Protocolo de troca de dados baseado em XML
- XML - Linguagem de marcação para descrição dos dados
- WSDL - Descritor de serviços baseados em XML
- UDDI - Registro e descoberta de serviços

## Estrutura da Mensagem

- Envelope
	- Define o início e o final da mensagem
	- É obrigatório
- Header
	- Traz atributos opcionais da mensagem utilizada para o seu processamento
	- É opcional
- Body 
	- Possui o conteúdo da mensagem em formato XML
	- É obrigatorio

## WSDL

- Web Serverces Description (WSDL)
- Linguagem de descrição de um web service baseada em XML
- Define os seguintes objetos:
	- Tipos de dados suportados pelo serviço
	- Padrão de mensagens de entrada e saída'
	- Protocolos de comunicação permitidos pelo Web Sevice (biding)
	- Serviços e portas de comunicação onde operações são disponibilizadas pelo web serbice
	- Definições sobre schemas e namespaces utilizados no contexto do web service.
	
![[concepts/pasted-image-20240613220904-png]]

## UDDI

- Universal Description and Discovery Interface (UDDI)
- Serviço de diretório que mantem referência para os Web Services refistrados
- Funcionam como páginas amarelas para localização dos Web Services
- Reúne informações como:
	- Nomes endereços e números de telefones dos fornecedores de serviços
	- Serviços oferecidos por cada fornecedor, bem como informações técnicas sobre a interface de cada um.

[[concepts/arquitetura-orientada-a-servicos-soa]]
## Casos de uso | Exemplos

- Integrações de sistemas empresariais, como sistemas de gerenciamento de pedidos e contabilidade.
- Serviços de pagamento online
	- Ex: Nota Fiscal Eletronica (NFe) do governo brasileiro.

