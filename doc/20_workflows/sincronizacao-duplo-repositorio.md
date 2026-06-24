---
tags: [workflow, git, sync, multi-repo]
updated: 2026-06-24
author: Colaborador1
---

# Fluxo de Sincronizacao em Duplo Repositorio (URSoftware & IF Goiano)

Este guia explica como versionar e enviar atualizacoes do Vault para dois repositorios remotos distintos de forma isolada, mantendo o repositorio do IF Goiano livre de dados e configuracoes pessoais.

## Remotos Configurados

- **`origin`**: `https://github.com/URSoftware/Brain.git` (Repositorio original compartilhado)
- **`ifgoiano`**: `https://github.com/IF-Goiano-Campus-Hidrolandia-Alunos/CerebroIA.git` (Repositorio academico higienizado)

---

## Passo-a-Passo de Sincronizacao

### 1. Sincronizar com o Repositorio Original (origin)
Esta branch mantem todo o historico, incluindo arquivos de perfis locais e configuracoes.

```bash
# 1. Certifique-se de estar na branch main de desenvolvimento
git checkout main

# 2. Adicione e envie as alteracoes normais
git add .
git commit -m "update: sincronizacao de notas e projetos"
git push origin main
```

---

### 2. Sincronizar com o Repositorio do IF Goiano (ifgoiano)
Usamos a branch `if-goiano` para preparar o envio limpo.

#### Setup Inicial (Executar apenas uma vez)
Se a branch `if-goiano` ainda nao foi criada:
```bash
git checkout -b if-goiano
```

#### Envio Recorrente de Atualizacoes
Toda vez que quiser enviar dados novos para o IF Goiano:
```bash
# 1. Acesse a branch de publicacao academica
git checkout if-goiano

# 2. Puxe as atualizacoes da main (sem comitar imediatamente)
git merge main --no-commit

# 3. Copie o gitignore especial para mascarar perfis pessoais
cp .gitignore_ifgoiano .gitignore

# 4. Remova os arquivos confidenciais do indice do git nesta branch
git rm --cached perfil-colaborador1.bat perfil-colaborador2.bat PERFIL-COMMITS.md IDENTIDADE-LOCAL.md scripts/reorganize_vault.py scripts/sanitize_vault.py .gitignore_ifgoiano

# 5. Adicione o novo gitignore, comite e envie
git add .gitignore
git commit -m "update: sincronizacao academica (IF Goiano)"
git push ifgoiano if-goiano:main

# 6. Volte para a branch main de desenvolvimento local
git checkout main
git checkout .gitignore  # Restaura o gitignore original do desenvolvimento
```

---

## Validacao
- Acessar o site do Github do IF Goiano e confirmar que a pasta raiz nao contem arquivos `.bat`, `PERFIL-COMMITS.md` ou emails pessoais dos colaboradores.
