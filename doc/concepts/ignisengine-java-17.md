---
tags: [ignisengine, java, build, decision]
updated: 2026-06-12
---

## Definição

Versão oficial de Java do IgnisEngine: 17 (LTS), imposta via `maven.compiler.release` no pom.xml.

## Contexto

Bug 2026-06-12: classes compiladas com JDK 26 (class file 70) falhavam com UnsupportedClassVersionError em runtime Java 21 (max 65). `release` trava bytecode e API visível em 17 independente do JDK instalado.

## Detalhes

- pom.xml: `<maven.compiler.release>17</maven.compiler.release>` (substitui source/target)
- Bytecode gerado: class file 61, roda em qualquer JVM 17+
- Maven Wrapper 3.2.0 completo no repo (mvnw, mvnw.cmd, maven-wrapper.jar versionado com exceção no .gitignore)
- Build sem Maven instalado: `mvnw.cmd clean compile` (Windows) / `./mvnw clean compile` (Linux/macOS)
- Recursos não-Java de src/ (ícones do editor) empacotados via `<resources>` no pom
- Distribuições do Builder exigem Java 17+ na máquina do jogador

## Links

- [[concepts/ignisengine-builder]]
