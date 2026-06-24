---
tags: [importado, italo]
updated: 2026-06-21
---

É um vocabulário que permite descrever, referenciar e validar documentos JSON.

## Benefícios

- Descreve formatos de dados
- Provê uma documentação legível para seres humanos
- Permite validação de dados

## Aplicações

- Automação de testes
- Garantir qualidade de dados submetidas por clientes

## Exemplo

### JSON

```JSON
{
	"productId": 1,
	"productName": "A green door",
	"price": 12.50,
	"tags": [ "home", "green"]
}
```

### JSON Schema

```JSON

{
	"$schema": "https://json-schema.org/draft/2020-12/schema",
	"$id": "https://example.com/product.schema.json",
	"title": "Produto",
	"description": "Um produto do catálogo",
	"type": "object",
	
	"properties": {
		"productId": {
			"description": "Identificador único",
			"type": "integer"
		},
		"productName": {
			"description": "Nome do produto",
			"type": "string"
		},
		"price": {
			"description": "Preço do produto",
			"type": "number",
			"excluseiveMinimum": 0
		},
		"price": {
			"description": "Rotolos do produto",
			"type": "array",
			"items": {
				"type": "string",
				"minItems": 1,
				"uniqueItems": true
			}
		}
	},
	
	"required": ["productId", "productName" ]
}

```

## Palavras Reservadas

| Palavra Reservada | Significado                                                                                                                         |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `$schema`         | Indica o dialeto (Versão) utilizado para descrever o esquema. Possui uma URI com o endereço do dialeto.                             |
| `$id`             | Indica o base URI para esta definição de esquema na Internet. Possui uma URI sem fragmentos com o endereço da definição do esquema. |
| `$ref`            | Indica um esquema definido em outro local.                                                                                          |
| `$defs`           | Indica um local para definição de esquemas e sub-esquemas JSON reutilizáveis em um esquema mais geral                               |