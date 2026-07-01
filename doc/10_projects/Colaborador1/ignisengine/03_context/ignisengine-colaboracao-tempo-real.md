---
tags: [ignisengine, context, colaboracao, tempo-real, vpn, codetogether]
updated: 2026-06-30
author: Colaborador1
---

# Colaboração em Tempo Real (tipo CodeTogether Cloud)

Fundação de colaboração já implementada e plano de sincronização completa. Permite
que colaboradores **visualizem e editem** o projeto em tempo real, por **VPN**
(Radmin/Hamachi/Tailscale) ou **IP direto** do host.

---

## 1. Objetivo

Editar código junto, ver objetos se movendo, e **quando o host aperta Play, todos
testam** — sem servidor na nuvem: o "endereço/URL" é o do próprio host (por isso VPN
funciona sem configuração extra).

---

## 2. Transporte (implementado)

Modelo **estrela com relay**: o host é o hub; convidados conectam a ele.

| Classe | Arquivo | Papel |
|--------|---------|-------|
| `CollabSession` | `collab/CollabSession.java` | Fachada singleton (host/join, envio, listeners) |
| `CollabServer` | `collab/CollabServer.java` | Host: `ServerSocket`, presença, broadcast |
| `CollabClient` | `collab/CollabClient.java` | Convidado: conecta, envia/recebe |

**Protocolo:** TCP com **uma linha JSON por mensagem** (`\n`, UTF-8) — agnóstico de
transporte, funciona em IP direto ou qualquer VPN de camada 3.

Tipos: `hello` (nome), `presence` (`participants[]`), `chat` (`from`,`text`),
`event` (`channel`,`from`,`payload`).

Canais de evento: `scene` (GameObjects), `script` (edições de código), `play`
(estado de Play do host), `cursor` (seleção/cursor de cada colaborador).

---

## 3. Interface no editor

`Configurações → Colaboração`:
- **Hospedar:** nome + porta (padrão `8791`) → **Hospedar sessão**; o endereço
  `<IP-LAN/VPN>:porta` aparece e pode ser copiado.
- **Entrar:** endereço do host (ex.: IP `25.x.x.x` da Radmin VPN) + porta → **Entrar**.
- Lista de **Participantes** e status ao vivo. Nome/porta persistidos em
  `~/.ignis/editor-prefs.json`. Encerra ao fechar o editor.

Descoberta de IP: `McpHttpBridge.localLanAddress()` (primeiro IPv4 não-loopback ativo,
normalmente o da VPN quando conectada).

---

## 4. Plano de sincronização (a ligar)

Transporte pronto (presença/chat/canais); falta conectar os subsistemas:

- **Código (`script`):** emitir patches do `FxCodeEditor` (início: conteúdo inteiro
  em debounce; evolução: **OT/CRDT** para edição concorrente). Aplicar no receptor
  com guarda anti-eco.
- **Cena (`scene`):** hooks nas operações do editor (reusar comandos do `UndoManager`
  como eventos); aplicar no `Game`/`Scene` na thread de UI; arrasto contínuo em taxa
  limitada (20–30 Hz) com interpolação. **Snapshot inicial** (`.ignis`) ao entrar.
- **Play (`play`):** host roda o runtime autoritativo; transmite snapshots de
  transform/estado por tick; convidados renderizam como espectadores; fase 2: input
  remoto (host-autoritativo) para testes multiplayer reais.
- **Cursor (`cursor`):** posição/seleção em baixa frequência, desenhando cursores
  coloridos por participante.

---

## 5. Concorrência, permissões e segurança (futuro)

- Locking otimista por arquivo/objeto até OT/CRDT; papéis host/editor/espectador;
  autoridade do host sobre o estado salvo.
- TCP simples na LAN/VPN; para redes não confiáveis: **token de sessão** no `hello` e
  opcionalmente **TLS** (`SSLServerSocket`). Host controla entrada/expulsão.

---

## 6. Estado × pendências

**Pronto:** transporte TCP host/convidado, presença ao vivo, chat, canais genéricos,
UI de hospedar/entrar/copiar endereço, compatível com VPN e IP direto.

**Pendente:** ligar `script`/`scene`/`play`/`cursor` aos subsistemas reais; snapshot
inicial; OT/CRDT; streaming de Play; permissões/papéis, locking, token e TLS.

Relacionados: [[ignisengine-mcp-http-bridge]], [[ignisengine-agentic-ai-plan]].
