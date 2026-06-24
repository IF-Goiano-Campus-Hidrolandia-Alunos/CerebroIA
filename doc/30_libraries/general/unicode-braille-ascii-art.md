---
tags: [ascii-art, unicode, braille, design, cli]
updated: 2026-06-21
---

## Definição

A arte em Braille Unicode (Braille Art) é uma técnica de renderização gráfica em modo texto que utiliza caracteres da faixa de blocos Braille do padrão Unicode (`U+2800` a `U+28FF`) para simular imagens com alta resolução espacial em terminais de console clássicos.

## Contexto

Aplicável no desenvolvimento de interfaces gráficas em linha de comando (CLI) premium (como loaders, banners de boas-vindas e painéis interativos de ferramentas como o Hermes Agent ou Claude Code) para exibir logotipos ou imagens complexas com uma densidade visual muito superior aos caracteres ASCII convencionais.

## Detalhes

### 1. Resolução Espacial Aumentada (2x4 Pixels)
Diferente do caractere de texto padrão (que renderiza apenas uma letra ou bloco sólido por célula), o caractere Braille divide a célula do terminal em uma matriz interna de **2 colunas por 4 linhas** de pontos (sub-pixels). Isso oferece uma resolução até **8 vezes maior** para desenhos de curvas e gradientes detalhados.

### 2. Mapeamento de Bits Unicode
A faixa Braille no padrão Unicode reserva 256 caracteres baseados em uma máscara de bits de 8 bits. Cada um dos 8 pontos em uma matriz 2x4 corresponde a um bit ativado no deslocamento a partir do ponto base `0x2800`:

```text
Esquema de Posicionamento e Bitmasks:
Ponto 1 (Linha 1, Col 1) -> bit 0 (Valor: 1)      | Ponto 4 (Linha 1, Col 2) -> bit 3 (Valor: 8)
Ponto 2 (Linha 2, Col 1) -> bit 1 (Valor: 2)      | Ponto 5 (Linha 2, Col 2) -> bit 4 (Valor: 16)
Ponto 3 (Linha 3, Col 1) -> bit 2 (Valor: 4)      | Ponto 6 (Linha 3, Col 2) -> bit 5 (Valor: 32)
Ponto 7 (Linha 4, Col 1) -> bit 6 (Valor: 64)     | Ponto 8 (Linha 4, Col 2) -> bit 7 (Valor: 128)
```

Por exemplo, para exibir uma linha diagonal inferior ativando os pontos 1, 5, 6 e 8:
$$\text{Valor total} = 1\ (\text{bit 0}) + 16\ (\text{bit 4}) + 32\ (\text{bit 5}) + 128\ (\text{bit 7}) = 177 \implies \text{Hex: } 0\text{xB1}$$
O caractere Unicode correspondente será `chr(0x2800 + 0xB1)` $\approx$ `⢱`.

### 3. Gradientes de Cor com ANSI
Como os terminais modernos aceitam códigos ANSI de 16 ou 256 cores, calcula-se a cor média (RGB) dos pixels ativos dentro da célula 2x4 para aplicar um escape ANSI de cor (ex: `\033[33m` para laranja do disco de acreção de Gargantua) antes de imprimir o caractere Braille.

### 4. Implementação no Agente Cérebro
A imagem original do buraco negro Gargantua de *Interstellar* foi processada via script Python para:
- Redimensionar proporcionalmente a largura em sub-pixels (144x88 pixels, resultando em 72x22 caracteres).
- Analisar a luminosidade de cada pixel em relação a um limiar dinâmico.
- Gerar o código de caractere e a cor ANSI correspondente, resultando na arte estática inserida no loop de boas-vindas do terminal.

## Links

- [[00_MOC]]
- [[agent-cerebro-otimizacao-memoria]]
