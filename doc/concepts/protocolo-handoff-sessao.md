---
tags: [workflow, handoff, session, ai, project-management]
updated: 2026-06-21
---

## Definição

Protocolo estruturado para encerramento e transição de sessões entre agentes de IA. Garante persistência e evita perda de contexto.

## Contexto

Como as IAs operam em sessões independentes e sem estado, cada nova conversa começa do zero. O protocolo de handoff armazena o "estado mental" do último agente em um arquivo markdown simples que o próximo agente pode ler imediatamente para retomar o trabalho sem re-pesquisar todo o projeto.

---

## Passos do Protocolo (Para a IA executar no final do turno)

### 1. Criar Nota de Handoff
Sempre que finalizar uma tarefa ou sessão de desenvolvimento, crie ou atualize um arquivo chamado `C:\Users\thyag\OneDrive\Desktop\Brain-main\doc\handoff-sessao-atual.md` com a seguinte estrutura:

```markdown
# Handoff de Sessão - [Data]

## 1. Estado Atual
- Breve resumo das últimas modificações realizadas.
- Quais bugs foram identificados e como foram resolvidos (ex: correção do runtime clássico do Babel).

## 2. Estrutura de Arquivos Criados/Modificados
- [Nome do Arquivo](caminho_absoluto) -> Objetivo do arquivo.

## 3. Próximos Passos
- Lista ordenada com as próximas tarefas pendentes.
- Indicação clara de qual arquivo deve ser aberto e modificado a seguir.

## 4. Comandos e Testes Ativos
- Porta em que os servidores locais estão rodando (ex: porta 8080).
- Comando de teste utilizado.
```

### 2. Deixar Instrução de Leitura
Na última resposta ao usuário, indique explicitamente para o próximo agente:
*"Recomendo que o próximo agente leia a nota de handoff em `C:\Users\thyag\OneDrive\Desktop\Brain-main\doc\handoff-sessao-atual.md` para continuar o trabalho imediatamente."*

---

## Links

- [[concepts/vault-system]]
- [[concepts/llm-context-token-optimization]]
