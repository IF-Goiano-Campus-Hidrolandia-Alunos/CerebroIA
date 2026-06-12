---
name: vault-manager
description: Manage project learning, documentation, and workflows using the local vault, and synchronize both the vault and the project changes to their respective git repositories.
---

# Vault Manager Skill

This skill ensures that Antigravity always remembers where the personal Vault is located, how to use it, and how to keep it and the current project synchronized with Git.

## Vault Information

- **Local Vault Path**: `C:\Users\vinic\OneDrive\Desktop\vault`
- **Vault Git Remote Repository**: `https://github.com/URSoftware/Brain.git`
- **Git User Name**: `FeronZerbana`
- **Git User Email**: `ddrive221@gmail.com`

## Core Instructions & Rules

1. **Check Local First (Sempre Leia o Vault Primeiro)**
   - Ao iniciar qualquer tarefa, leia o arquivo principal `C:\Users\vinic\OneDrive\Desktop\vault\doc\00_MOC.md`.
   - Busque notas atômicas em `concepts/`, `workflows/` ou `external_cache/` antes de realizar buscas externas.
   - Consuma apenas arquivos específicos para economizar tokens.

2. **Criação e Edição de Notas (Padrões do Vault)**
   - Crie notas atômicas em `concepts/` (1 assunto/arquivo) usando `TEMPLATE_CONCEPT.md`.
   - Escreva de forma econômica (bullet points, sem prosa, direto ao ponto).
   - Registre datas no frontmatter yaml como `updated: AAAA-MM-DD`.
   - Se criar uma nova nota, atualize o link correspondente no `00_MOC.md`.

3. **Sincronização Automática com o Git (Push de Alterações)**
   - **Sincronização do Vault**: Ao concluir alterações de aprendizado, documentação ou fluxos no Vault, acesse o diretório do vault `C:\Users\vinic\OneDrive\Desktop\vault` e envie as alterações:
     ```powershell
     git config user.name "FeronZerbana"
     git config user.email "ddrive221@gmail.com"
     git add .
     git commit -m "update: [descreva a alteração de forma concisa]"
     git push origin main
     ```
   - **Sincronização do Projeto**: Ao concluir alterações no código, testes ou documentação do projeto atual (como `IgnisEngine`), acesse o diretório raiz do projeto e envie as alterações:
     ```powershell
     git add .
     git commit -m "feat/fix/docs: [descreva a alteração de forma concisa]"
     git push origin [current-branch]
     ```
   - **IMPORTANTE**: Lembre-se sempre de que o repositório git do Vault e o repositório git do projeto são totalmente separados. Cada git deve receber exclusivamente seus respectivos arquivos. Nunca misture arquivos de um repositório no outro.

4. **Usuário Git para Commits/Pushes**
   - Sempre utilize as credenciais configuradas localmente para cada repositório. Para o Vault, use o usuário `FeronZerbana` (`ddrive221@gmail.com`).
