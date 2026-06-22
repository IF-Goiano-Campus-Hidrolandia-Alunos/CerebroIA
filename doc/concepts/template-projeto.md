---
tags: [template, projeto]
updated: 2026-06-21
---

## Definição

Template padrão para controle de novos projetos e acompanhamento de entregáveis/status.

## Contexto

Utilizado para estruturar o planejamento inicial, objetivos, cronograma, tarefas e referências de cada projeto ativo do método P.A.R.A.

## Estrutura do Template (Copiar Abaixo)

```markdown
---
status: "Não Iniciado" # Opções: Não Iniciado, Em Progresso, Em Pausa, Concluído
data_inicio: {{date}}
prazo: 
lider: 
tags: [projeto]
---

# Projeto - {{title}}

## 📄 Resumo do Projeto
*Breve descrição do objetivo do projeto e por que ele é importante.*

## 🎯 Objetivos & Entregáveis
- [ ] **Entregável 1:** Descrição do resultado esperado (Prazo: )
- [ ] **Entregável 2:** Descrição do resultado esperado (Prazo: )

## ✅ Lista de Tarefas (Checklist)
- [ ] Planejamento inicial
- [ ] Pesquisa e referências
- [ ] Execução das etapas principais
- [ ] Revisão e validação
- [ ] Conclusão e documentação

## 📚 Recursos & Referências Relacionadas
*   [[concepts/guia-organizacao-para]]
*   Links úteis: 

## 📅 Reuniões Relacionadas
*   `=this.file.inlinks` (Uso de Dataview para listar arquivos vinculados)

---
**Notas Relacionadas:** [[00_MOC]] | [[concepts/guia-organizacao-para]]
```

## Links

- [[concepts/guia-organizacao-para]]
- [[concepts/template-reuniao]]
