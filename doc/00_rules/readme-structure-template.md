---
tags: [documentation, template, readme]
updated: 2026-06-10
---

## Definição

Estrutura padrão de README reutilizável em qualquer projeto para documentação clara, visual e bem-organizada.

## Contexto

README é o primeiro contato do usuário com o projeto. Deve ser legível, ter visual atrativo e navegar para documentação detalhada. Essa estrutura garante consistência e profissionalismo.

## Estrutura Recomendada

### 1. Header Visual
- Logo do projeto (centralized, com estilos)
- Badges de tecnologias (shields.io)
- Descrição breve (1-3 linhas)

```markdown
<p align="center">
  <img src="Icons/Logo.png" alt="Project Logo" width="350px" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Tech-Version?style=for-the-badge&logo=..." />
</p>

Uma frase que resume o projeto.
```

### 2. Estrutura do Projeto
- Árvore de diretórios com emojis
- Comentários breves explicando cada pasta
- Máximo 2 níveis de profundidade (legível)

```markdown
## Estrutura do Projeto

projeto/
├── 📁 Icons/          # Imagens
├── 📁 doc/            # Documentação
├── 📁 cmd/            # Entry points
├── 📄 README.md
```

### 3. Hub de Documentação
- Links para documentação modularizada em `doc/`
- Cada link com 1-2 linhas de contexto
- Não incluir conteúdo detalhado no README (deixar em `doc/`)

```markdown
## Hub de Documentação

- **[Funcionalidades](doc/features.md)**: Detalhes de execução
- **[Arquitetura](doc/architecture.md)**: Diagrama e design
- **[Guia Dev](doc/development.md)**: Setup local e deploy
```

### 4. Quick Start
- Instruções mínimas para rodar localmente
- Múltiplos sistemas operacionais (Windows, Linux, macOS)
- Variáveis de ambiente necessárias

```markdown
## Quick Start

### Execução Local
export VAR="value"
command run
```

### 5. Autores (Opcional)
- Tabela com avatares circulares do GitHub (`style="border-radius: 50%;"`)
- Links para os perfis

```markdown
## Autores e Organização

Este projeto é mantido pela organização **URSoftware**.

<table align="center">
  <tr>
    <td align="center">
      <a href="https://github.com/user">
        <img src="https://github.com/user.png?size=100" width="100px;" alt="Name" style="border-radius: 50%;" /><br />
        <sub><b>Name</b></sub>
      </a>
    </td>
  </tr>
</table>
```

### 6. Licença (Rodapé)
- Menção breve com link para arquivo
- Formato: "Sob licença MIT. Veja LICENSE para detalhes."

## Padrões de Estilo e Decorações HTML

Para garantir uma apresentação visual premium e consistente nos READMEs principais:
- **Banner do Projeto:** Deve ser centralizado usando `<p align="center">` e conter cantos arredondados com sombra para profundidade:
  ```html
  <p align="center">
    <img src="Icons/Banner.jpg" alt="Project Banner" width="250px" style="border-radius: 12px; box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);" />
  </p>
  ```
- **Badges:** Alinhados no centro com links estilizados (shields.io).
- **Avatares dos Autores:** Formatados em tabelas centralizadas com bordas arredondadas de `50%` para formar círculos:
  ```html
  <img src="https://github.com/username.png" width="100px" style="border-radius: 50%;" />
  ```
- **Separadores:** Linhas horizontais markdown padrão (`---`) separando cada bloco lógico.
- **Tom de Texto:** Livre de emojis no corpo do texto de documentações para preservar o tom profissional de engenharia (emojis permitidos apenas na árvore de diretórios).

## Diretriz da Estrutura de Documentos

> [!IMPORTANT]
> **Regra do Único README.md:**
> Existe estritamente **apenas um único arquivo README.md** no repositório, posicionado na raiz principal (fora da pasta `doc/`).
> Todos os demais arquivos `.md` devem residir obrigatoriamente dentro da pasta `doc/` e constituem a documentação técnica (Vault de conhecimento). O README.md atua puramente como o portal visual e índice de links.

## Benefícios

- Profissionalismo: Layout visual atraente com sombras e imagens limpas
- Clareza: Estrutura hierárquica óbvia
- Reutilizabilidade: Mesmo padrão em vários projetos
- Manutenibilidade: Documentação modularizada fácil de atualizar
- Navegar fácil: Links para docs detalhadas, não parágrafos longos

## Links

- [[workflows/criar-readme]]
