---
tags: [importado, italo]
updated: 2026-06-21
---

Devido ao startup do spring boot se basear na utilização de reflexão, dependendo da quantidade de bindings que for executado, o cold start pode ser prolongado e prejudicar a experiência Serverless.

## GraalVM

Uma máquina virtual universal e poliglota (JS, Python, Ruby, R, Java, Scala, Kotlin). Ela possibilita:
- AOT (Ahead-of-time): Processo que compila o código diretamente para um formato binário, sem passar pelo bytecode.

## Quarkus

Um framework Java open source desenvolvido pela Red Hat lançado no final de 2018. Foi desenvolvido para o GraalVM e OpenJDK HotSpot, com a promessa de ter um startup muito rápido e pouco gasto de memória de footprint, sendo assim um framework ótimo para cloud (k8s), microservices e também serverless.

```java
@RegisterForReflection
```

## Micronault

Um framework java open source, concorrente do quarkus, desenvolvido pela micronault Foundation e lançado no final de 2018

``` java
@Introspect
```

## Sprint Native

Framework java Open Source, concorrente do Quarkus e Micronault, desenvolvido pela Sprint e lançado em 2021.

``` java
@AotProxyHint
```

