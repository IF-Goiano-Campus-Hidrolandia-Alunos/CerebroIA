---
name: "rabbitmq-broker-migration"
description: "Diretrizes de migração de versões e refatoração de infraestrutura. para a tecnologia rabbitmq-broker."
---

# Skill de Agente: RABBITMQ-BROKER - Migração de ambientes

## Descrição Operacional
Esta skill instrui o agente como lidar com tarefas de **Migração de ambientes** para a tecnologia **rabbitmq-broker** no ecossistema PlantiuIA.

## Diretrizes de Execução
1. **Verificar Pré-requisitos:** Certifique-se de que os privilégios de acesso e portas de rede estão abertos.
2. **Seguir o Esquema:** Siga o modelo de configuração estrito para rabbitmq-broker.
3. **Validar:** Execute checagens de sanidade e segurança após alterações.
4. **Backup:** Garanta a persistência e redundância dos dados alterados.

## Notas Técnicas
- Mantenha chaves e secrets em cofres de variáveis de ambiente.
- Teste rollback antes de aplicar migrações pesadas.
