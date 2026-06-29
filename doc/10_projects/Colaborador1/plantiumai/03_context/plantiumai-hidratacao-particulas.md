---
tags: [plantiumai, frontend, react, nextjs, ssr, bugfix]
updated: 2026-06-29
---

# PlantiumAI — Correção do Erro de Hidratação das Partículas (SSR)

Documentação do bugfix estrutural implementado na página de planos para resolver inconsistências de renderização entre o servidor (SSR) e o cliente.

## O Problema Encontrado

No console de desenvolvimento do navegador, o seguinte aviso era gerado repetidamente ao acessar a página `/planos`:

> "A tree hydrated but some attributes of the server rendered HTML didn't match the client properties..."

### Causa Raiz
No componente `<GreenhouseBackground>` da página `/planos/page.tsx`, as partículas de fundo eram geradas dinamicamente usando a função `Math.random()` para definir:
- `left` (posição horizontal)
- `width` e `height` (dimensões da partícula)
- `--delay` e `--duration` (variáveis CSS de animação)

Como esses valores eram sorteados no servidor durante o pré-render (SSR) e sorteados novamente no navegador do cliente durante a montagem inicial (hydration), ocorria uma divergência no HTML gerado, impedindo a hidratação limpa do React.

## A Solução Implementada

Para resolver a inconsistência, o componente foi refatorado utilizando os hooks `useState` e `useEffect`:

1. **Estado de Montagem (`mounted`)**:
   Introduzimos um estado booleano `mounted` (inicializado como `false`) controlado pelo hook `useEffect`.

2. **Criação tardia das partículas**:
   A lista de partículas com suas propriedades aleatórias passa a ser gerada apenas no cliente após a montagem do componente (`useEffect` disparando após a renderização inicial do DOM):

```typescript
const [particles, setParticles] = useState<Particle[]>([]);
const [mounted, setMounted] = useState(false);

useEffect(() => {
  setMounted(true);
  const items = Array.from({ length: 15 }).map((_, i) => ({
    id: i,
    left: `${Math.random() * 100}%`,
    size: `${Math.random() * 8 + 4}px`,
    delay: `${Math.random() * 10}s`,
    duration: `${Math.random() * 15 + 10}s`,
  }));
  setParticles(items);
}, []);
```

3. **Renderização Condicional**:
   Se `mounted` for falso, renderiza-se apenas o contêiner vazio. As partículas só são injetadas no DOM após a hidratação, evitando qualquer incompatibilidade entre o HTML do servidor e as propriedades do cliente.

## Resultados
A página `/planos` compila e hidrata de forma limpa, eliminando 100% dos erros de hydration no console e otimizando a velocidade de renderização inicial.
