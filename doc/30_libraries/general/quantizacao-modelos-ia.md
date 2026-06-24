---
tags: [ia, llm, quantizacao, otimizacao]
updated: 2026-06-21
---

## Definição

Quantização de Modelos de IA é uma técnica de otimização que reduz a precisão dos pesos e das ativações dos tensores (por exemplo, de Float32/FP16 para INT8, INT4 ou sub-1-bit), tornando os modelos significativamente mais leves e rápidos sem perda substancial de qualidade.

## Contexto

Modelos de linguagem grandes (LLMs) exigem gigabytes de memória RAM/VRAM para execução. A quantização permite rodar esses modelos localmente em dispositivos com recursos limitados (como CPUs comuns e GPUs integradas), aproximando a computação de borda de cenários reais de desenvolvimento.

## Detalhes

### Principais Técnicas de Quantização

1.  **Quantização Dinâmica (Dynamic Quantization - PyTorch INT8):**
    *   Converte pesos de camadas lineares (`torch.nn.Linear`) de ponto flutuante de 32 bits (Float32) para inteiros de 8 bits (INT8).
    *   As ativações são quantizadas dinamicamente durante a inferência.
    *   **Benefício:** Reduz o tamanho do modelo em ~3x a 4x em memória e acelera a execução em CPUs que possuem instruções otimizadas para inteiros.

2.  **TurboQuant (Google):**
    *   Desenvolvido pela equipe do Google Research, foca em comprimir o cache de chaves-valores (KV Cache) em até **6x** com perda zero de precisão.
    *   Resolve o gargalo de memória de contexto em conversas longas através de duas etapas: *PolarQuant* (coordenadas polares dos vetores de dados) e *QJL* (Johnson-Lindenstrauss quantizado) para autocorreção estatística dos erros.

3.  **NanoQuant (Samsung Labs):**
    *   Técnica de pós-treinamento (PTQ) que realiza compressão a nível de sub-1-bit (pesos representados por matrizes binárias de baixa classificação).
    *   Permite que modelos gigantescos (ex: Llama-2-70B) rodem em GPUs comerciais com apenas 8 GB de VRAM.

---

### Implementação Local no Agente de Pesquisa

No nosso script local `brain_researcher.py`, aplicamos a **Quantização Dinâmica INT8** do PyTorch no modelo `Qwen2.5-0.5B-Instruct` quando executado em CPU. 

#### Trecho do Código de Implementação:
```python
import torch
from transformers import AutoModelForCausalLM

# Carrega o modelo com precisão Float32 padrão
raw_model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen2.5-0.5B-Instruct",
    torch_dtype=torch.float32
)

# Aplica a quantização dinâmica para as camadas Lineares
model = torch.quantization.quantize_dynamic(
    raw_model,
    {torch.nn.Linear},
    dtype=torch.qint8
)
```

**Resultado Prático:**
- **Tamanho original em memória (FP16/FP32):** ~900 MB a 1.2 GB de RAM.
- **Tamanho pós-quantização (INT8):** ~350 MB a 400 MB de RAM (cerca de 3x a 4x mais leve).
- **Tempo de Resposta:** Inferência local na CPU concluída com sucesso em poucos segundos.

## Links

- [[30_libraries/general/llm-context-token-optimization]]
- [[00_rules/vault-system]]
- [[30_libraries/dotnet_arch/guia-dataview-obsidian]]
