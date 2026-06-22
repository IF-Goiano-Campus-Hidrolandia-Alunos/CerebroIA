---
tags: [importado, italo]
updated: 2026-06-21
---

Definem os conjuntos de serviços Java EE contextuais, que facilitam o uso de [[concepts/italo-plataforma-java-unidade-1-enterprise-javabeans]], através de um conjunto padrão de anotações para uso em classes injetáveis.

## Dependency Injection
\
É a injeção de dependencias em uma classe, utilizado para criar uma instancia de um objeto ao compilar.

## Inversion of Control

A inversão de controle acontece quando delegamos o controle para outro método, que retorna o resultado esperado. Dessa forma, deixamos o controle em outro lugar ao invés do mesmo que precisa.

## Exemplo

```java
class CarController {
	@Inject
	private CarService carService;

	public List<Car> getAll() {
		return carService.getAll();
	}
}
```

Nesse exemplo do controller é possivel ver a injeção de dependência, quando injetamos a instância da classe CarService, através de uma factory por exemplo