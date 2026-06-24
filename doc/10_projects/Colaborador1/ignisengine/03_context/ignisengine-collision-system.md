---
tags: [ignisengine, physics, collision]
updated: 2026-06-14
---

## Definição

O sistema de colisão do IgnisEngine é o mecanismo encarregado de detectar interseções geométricas entre entidades e resolver seus posicionamentos físicos ou disparar eventos lógicos (triggers).

## Contexto

Executado como parte do loop de física e atualização do motor, o sistema analisa os `GameObject`s que possuem colliders ativos e calcula as forças de resposta para impedir sobreposição em tempo de execução.

## Detalhes

- **Tipos de Colisores**: Suporta formas geométricas fundamentais:
  - **AABB (Axis-Aligned Bounding Box)**: Retângulos alinhados aos eixos para detecção rápida.
  - **Circle**: Círculos definidos por raio e centro.
  - **Polygon**: Polígonos convexos arbitrários definidos por vértices.
- **Algoritmo de Detecção e Resolução**:
  - **Separating Axis Theorem (SAT)**: Usado para testar se polígonos convexos estão se sobrepondo projetando os eixos ortogonais.
  - **Minimum Translation Vector (MTV)**: Determina a menor distância e direção necessárias para afastar os objetos colididos, resolvendo a penetração física.
- **Otimização de Performance (Broad-phase)**:
  - **SpatialGrid**: Grade bidimensional para indexar objetos espacialmente e evitar testes de colisão redundantes de complexidade \(O(N^2)\).
- **Continuous Collision Detection (CCD)**:
  - Mecanismo para prevenir o efeito de "tunneling" (quando objetos rápidos atravessam paredes entre frames).
- **Acoplamento e Recomendações de Evolução**:
  - Atualmente, o `GameObject` possui uma dependência direta com o estado físico de colisão. A recomendação de evolução arquitetural é separar essa lógica em um componente isolado (`RigidBody` / `ColliderComponent`), desacoplando o modelo de dados de entidade das regras da engine de física.

## Links

- [[ignisengine-gameobject]]
