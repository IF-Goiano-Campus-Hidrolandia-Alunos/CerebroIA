---
tags: [ignisengine, plan, ia, agentic, gemini, nvidia, mcp]
updated: 2026-06-30
author: Colaborador1
---

# Plano de IA Agêntica (Gemini / NVIDIA / IA embarcada)

Plano de evolução para uma **IA agêntica** que opera o editor usando as ferramentas
do MCP. Complementa [[ignisengine-mcp-http-bridge]] e [[ignisengine-ai-integration]].

---

## 1. Objetivo

Agente que entende pedido em linguagem natural ("crie um inimigo que persegue o
player") e **executa** chamando as ferramentas do motor (criar/editar scripts,
compilar, mexer na cena), observando resultados e iterando — laço *pensar → agir →
observar*.

Requisitos: funcionar com **APIs gratuitas do Gemini** (Google AI Studio) e da
**NVIDIA** (build.nvidia.com, OpenAI-compatível), e permitir no futuro uma **IA
local/embarcada** com acesso às **mesmas ferramentas**.

---

## 2. Fundação já implementada

| Peça | Arquivo | Papel |
|------|---------|-------|
| Registry canônico | `mcp/IgnisToolRegistry.java` | Fonte única das ferramentas |
| Bridge HTTP (URL) | `mcp/McpHttpBridge.java` | Expõe ferramentas por URL |
| Fachada MCP | `mcp/McpService.java` | Ciclo de vida + registry compartilhado |
| Provider Gemini | `editor/GeminiProvider.java` | REST `gemini-2.5-flash` |
| Provider NVIDIA | `editor/NvidiaProvider.java` | Endpoint OpenAI-compatível NVIDIA |
| Interface comum | `editor/AIServiceProvider.java` | `callAPI(key, prompt)` |
| Executor | `editor/AgentToolExecutor.java` | Cola resposta do LLM ↔ registry |
| UI | `editor/fx/FxSettingsWindow.java` (aba IA & MCP) | Provedor, chaves, toggle |

### Function-calling atual (baseado em prompt)
`AgentToolExecutor` fornece:
1. `toolManifest()` — descreve as ferramentas no *system prompt*, instruindo o modelo
   a responder com `{"tool":"<nome>","arguments":{...}}`.
2. `tryHandleToolCall(resposta)` — detecta esse JSON, executa via `IgnisToolRegistry`
   e devolve o resultado para realimentar o modelo.

Mesmo registry publicado pelo `McpService` → **paridade** com agentes externos.

---

## 3. Arquitetura-alvo do laço

```
 Usuário → AgentRunner → AIServiceProvider (Gemini|NVIDIA|Local)
                ▲                     │
                │  resultado          ▼ resposta
                └──── AgentToolExecutor (é tool-call? executa no registry : resposta final)
                                      │
                                      ▼  GameObjects/Scripts/Cena (thread de UI)
```

**A criar — `AgentRunner`:** mantém histórico e orçamento de iterações; monta prompt
(persona + `toolManifest()` + histórico); chama o provider ativo
(`EditorPrefs.getAiProvider()`); se a resposta for tool-call, executa, anexa o
resultado e repete; senão, entrega ao painel de chat. Roda em background; efeitos via
`IgnisMcpBridge`.

**Painel de chat:** aba "Assistente IA" com histórico, **log das ferramentas usadas**
(transparência) e modos "aprovar antes de executar" vs. "autônomo".

---

## 4. Providers gratuitos

- **Gemini:** `generativelanguage.googleapis.com/.../gemini-2.5-flash:generateContent`
  (chave em aistudio.google.com). Evolução: **function-calling nativo**
  (`functionDeclarations`) convertendo os schemas do registry.
- **NVIDIA:** `integrate.api.nvidia.com/v1/chat/completions` (chave em
  build.nvidia.com), modelo padrão `meta/llama-3.1-8b-instruct`. Evolução: campo
  `tools`/`tool_calls` (padrão OpenAI) e seleção de modelo na UI.

---

## 5. IA embarcada (local) — futuro

- **Interface:** implementar `AIServiceProvider` para runtime local
  (`LocalLlmProvider`); nada mais muda (AgentRunner/Executor são agnósticos).
- **Runtime de menor esforço:** servidor local OpenAI-compatível (Ollama/LM Studio/
  llama.cpp) — reaproveita o `NvidiaProvider` trocando a URL base para
  `http://localhost:11434/v1/...`.
- **Ferramentas in-process:** chamar `McpService.getRegistry().call(...)`
  diretamente (sem overhead de rede). Paridade por construção.
- **Salvaguardas:** manter "aprovar antes de executar" como padrão para modelos
  locais menores.

---

## 6. Roadmap

1. [feito] Registry + bridge HTTP + providers + UI de chaves + executor.
2. `AgentRunner` + painel de chat com log de ferramentas.
3. Function-calling nativo (Gemini/NVIDIA).
4. Expandir registry (cena, assets, animação, áudio).
5. `LocalLlmProvider` via servidor OpenAI-compatível local.
6. Modo autônomo com salvaguardas (limite de passos, aprovação, undo automático).

---

## 7. Pendências

- `AgentRunner` e painel de chat ainda **não** implementados (há manifesto + executor).
- Function-calling por prompt (frágil com modelos pequenos) até migrar aos formatos
  nativos.
- Falta seleção de modelo por provider na UI.

Relacionados: [[ignisengine-mcp-http-bridge]], [[ignisengine-ai-integration]],
[[ignisengine-colaboracao-tempo-real]].
