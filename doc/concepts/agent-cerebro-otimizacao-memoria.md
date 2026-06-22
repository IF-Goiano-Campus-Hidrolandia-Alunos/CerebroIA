---
tags: [ia-local, otimizacao, torch, qwen, obsidian]
updated: 2026-06-21
---

## Definição

A otimização de memória RAM e de precisão numérica do Agente Cérebro consiste em remover a quantização pós-treinamento dinâmica e carregar pesos nativos em `bfloat16`/`float32` para restaurar a integridade linguística do modelo local e reduzir picos de consumo de memória.

## Contexto

Aplicável na implantação offline e portable do modelo `Qwen2.5-0.5B-Instruct` no ambiente local do usuário. É recomendada sempre que modelos de parâmetros reduzidos (abaixo de 1.5B) demonstrarem degradação cognitiva acentuada ou loops repetitivos (ex: "como assim") causados por perdas de precisão nos blocos de atenção do transformador.

## Detalhes

- **Degradação de Quantização Pós-Treinamento (PTQ)**: A quantização dinâmica convencional (INT8) mapeia pesos lineares de ponto flutuante para inteiros de 8 bits sem recalibração fina. Em modelos pequenos como o Qwen de 500M de parâmetros, isso destrói as representações semânticas e causa inferências com ruído severo (como palavras repetidas ou travessões aleatórios).
- **Consumo de Memória de Modelos Pequenos**:
  - Em `float32` (4 bytes/peso): $0.49 \times 10^9 \text{ params} \times 4 \approx 1.96 \text{ GB}$ de RAM.
  - Em `bfloat16`/`float16` (2 bytes/peso): $0.49 \times 10^9 \text{ params} \times 2 \approx 0.98 \text{ GB}$ (980 MB) de RAM.
- **Resolução de Lentidão na CPU (Emulação de bfloat16)**:
  - Embora o `bfloat16` reduza o consumo de RAM em 50%, o PyTorch em CPU utiliza **emulação de software** para operações em `bfloat16` caso o processador não suporte nativamente o conjunto de instruções AVX-512 BF16.
  - Essa emulação gera uma lentidão extrema (travamento do cálculo de atenção `scaled_dot_product_attention`).
  - **Solução**: Forçar o uso de `torch.float32` por padrão no dispositivo CPU. A inferência passa a rodar nativamente nos vetores AVX2/AVX-512 do processador, resultando em respostas quase instantâneas com um consumo estável e controlado de **~2.3 GB** de RAM, eliminando congelamentos.
- **Configurações Anti-Loop de Inferência**:
  - `repetition_penalty=1.1`: Aplica uma penalidade logarítmica à probabilidade de palavras que já apareceram no contexto, prevenindo loops de feedback ("como assim").
  - `no_repeat_ngram_size=3`: Bloqueia o modelo de repetir qualquer sequência exata de 3 palavras no texto gerado.

```python
# Trecho da implementação otimizada para CPU
if self.device == "cpu":
    # Força float32 para rodar nativamente nos vetores AVX da CPU
    self.model = AutoModelForCausalLM.from_pretrained(
        self.model_name,
        torch_dtype=torch.float32
    )
```

## Links

- [[00_MOC]]
- [[llm-context-token-optimization]]
- [[cheat-sheet-comandos-tecnologias]]
