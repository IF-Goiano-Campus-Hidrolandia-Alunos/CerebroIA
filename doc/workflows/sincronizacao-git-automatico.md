---
tags: [workflow, git, sync, skill]
updated: 2026-06-11
---

## Objetivo
Garantir que as alterações feitas no Vault local e nos projetos em desenvolvimento sejam salvas e enviadas automaticamente para seus respectivos repositórios Git de forma isolada.

## Passos
1. **Sincronização do Vault**:
   - Acesse a pasta do Vault `C:\Users\vinic\OneDrive\Desktop\vault`.
   - Configure as credenciais do commit:
     ```powershell
     git config user.name "FeronZerbana"
     git config user.email "ddrive221@gmail.com"
     ```
   - Adicione, comite e envie as alterações:
     ```powershell
     git add .
     git commit -m "update: [descrição concisa das alterações]"
     git push origin main
     ```

2. **Sincronização do Projeto**:
   - Acesse o diretório raiz do projeto atual (ex: `IgnisEngine`).
   - Adicione, comite e envie as alterações para a branch correspondente:
     ```powershell
     git add .
     git commit -m "feat/fix/docs: [descrição concisa das alterações]"
     git push origin [current-branch]
     ```

3. **Validação de Isolamento**:
   - Certifique-se de que arquivos do Vault nunca sejam enviados ao repositório do projeto, e vice-versa.

## Validação
- Execute `git status` em ambos os repositórios para confirmar que as árvores de trabalho estão limpas (`nothing to commit, working tree clean`).
