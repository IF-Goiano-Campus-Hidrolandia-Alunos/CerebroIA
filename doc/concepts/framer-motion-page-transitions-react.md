---
tags: ['designanimacoes3d', 'documentacao', 'design', 'threejs', 'css']
updated: 2026-06-21
---

## Definição

Técnicas avançadas de animação e renderização 3D para Framer Motion Page Transitions React aplicadas a websites interativos.

## Contexto

Gera interfaces visuais premium com efeito WOW utilizando tecnologias de baixo custo de processamento.

## Detalhes

- Configuração de cenas e cálculos de renderização acelerados por GPU.
- Otimizações de performance (redução de polígonos, mesh instancing, controle de fps).
- Criação de micro-animações responsivas e adaptadas para acessibilidade (reduce-motion).

### Exemplo de Implementação Prática

```javascript
// Animação de entrada e hover premium usando Framer Motion no React
import { motion } from 'framer-motion';

export function PremiumCard() {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      whileHover={{ scale: 1.05, boxShadow: "0px 10px 30px rgba(34, 197, 94, 0.3)" }}
      whileTap={{ scale: 0.95 }}
      transition={{ type: "spring", stiffness: 300, damping: 20 }}
      style={{ padding: 24, borderRadius: 12, background: 'rgba(255,255,255,0.1)' }}
    >
      <h3>Título do Card</h3>
    </motion.div>
  );
}
```

## Links

- [[00_MOC]]
- [[concepts/guia-organizacao-para]]
- [[concepts/guia-dataview-obsidian]]
