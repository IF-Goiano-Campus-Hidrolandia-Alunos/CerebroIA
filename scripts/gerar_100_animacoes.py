# -*- coding: utf-8 -*-
import os

# Caminhos base
BASE_DIR = r"c:\Users\thyag\OneDrive\Desktop\Brain-main"
DOC_DIR = os.path.join(BASE_DIR, "doc", "30_libraries", "general")
SKILLS_DIR = os.path.join(BASE_DIR, "skills")

# 5 temas de documentacao
THEMES = [
    "front-strategic-animations",
    "ui-motion-design",
    "web-transition-performance",
    "ux-intentional-movement",
    "css-gsap-orchestration"
]

# 20 aspectos padrão do vault
ASPECTS = [
    "auditing", "auth-flow", "budgeting", "caching", "env-config",
    "error-handling", "latency", "middleware", "monitoring", "payload-limits",
    "pooling", "recovery", "redundancy", "routing", "scaling",
    "setup", "throttling", "tls", "tuning", "validation"
]

# Descricoes detalhadas dos aspectos de animacao
ASPECT_DESCS = {
    "auditing": "Auditoria e revisao de animacoes para garantir o principio do proposito e evitar o excesso visual.",
    "auth-flow": "Fluxo de transicoes visuais durante etapas de autenticacao e carregamento seguro.",
    "budgeting": "Orcamento de performance e limite de frames por segundo (FPS) alocados para a interface.",
    "caching": "Armazenamento em cache e otimizacao de assets de animacao (como arquivos JSON de Lottie).",
    "env-config": "Configuracao de variaveis de ambiente e tempo global de transicao na interface.",
    "error-handling": "Tratamento de erros e fallbacks de renderizacao de transicoes em navegadores antigos.",
    "latency": "Controle de latencia e atraso intencional (delay) para guiar o olhar do usuario de forma fluida.",
    "middleware": "Uso de interceptores de estado para coordenar a sequencia de animacoes reativas.",
    "monitoring": "Monitoramento de performance (jank, drops de frames) das transicoes no cliente.",
    "payload-limits": "Limites de tamanho de payload para bibliotecas de animacao e pacotes SVG complexos.",
    "pooling": "Pooling e reutilizacao de elementos graficos na arvore DOM para otimizar transicoes de listas.",
    "recovery": "Recuperacao e suavizacao do estado da interface apos interrupcoes inesperadas de navegacao.",
    "redundancy": "Redundancia e fallbacks estaticos para acessibilidade em dispositivos de baixo processamento.",
    "routing": "Animacoes de transicao de rotas (page transitions) focadas na coesao e fluidez do fluxo.",
    "scaling": "Dimensionamento responsivo e redimensionamento suave dos arcos estruturais e graficos.",
    "setup": "Configuracao inicial de easings, durations e curvas de velocidade baseadas na marca.",
    "throttling": "Controle de taxa (throttling e debouncing) de eventos de scroll e mousemove para animacoes.",
    "tls": "Seguranca na entrega de scripts e integridade de bibliotecas externas de animacao.",
    "tuning": "Ajuste fino de curvas cubicas de Bezier para expressar a linguagem corporal da marca.",
    "validation": "Validacao de acessibilidade (prefers-reduced-motion) para conformidade com padroes web."
}

# 20 tecnologias de skill de animacao
TECH_SKILLS = [
    "gsap-animations", "framer-motion", "css-keyframes", "svg-morphing", "canvas-rendering",
    "webgl-shaders", "threejs-scenes", "lottie-players", "scroll-trigger", "view-transitions",
    "micro-interactions", "gesture-navigation", "parallaxes", "page-transitions", "will-change-optim",
    "hardware-accel", "reduced-motion-acc", "spring-physics", "glare-effects", "particles-float"
]

# 5 variacoes de skill
SKILL_VARIATIONS = ["setup", "debugging", "optimization", "security", "integration"]

# Cria diretorios se nao existirem
os.makedirs(DOC_DIR, exist_ok=True)
os.makedirs(SKILLS_DIR, exist_ok=True)

print("Gerando 100 arquivos de documentacao...")
# 1. Gerar 100 arquivos de documentacao (5 temas * 20 aspectos)
doc_count = 0
for theme in THEMES:
    for aspect in ASPECTS:
        filename = f"{theme}-{aspect}.md"
        filepath = os.path.join(DOC_DIR, filename)
        
        # Conteudo customizado por aspecto
        desc = ASPECT_DESCS[aspect]
        content = f"""---
tags: ['design', 'animacoes', 'ux', '{theme}', '{aspect}']
updated: 2026-06-26
---

## Definicao

{desc} Aplicacao pratica da filosofia de animacao estrategica, focando na restricao e proposito.

## Contexto

As animacoes em sites devem ser vistas como diferenciais artesanais que elevam o valor do projeto. O segredo e aplicar restricao: evitar o excesso decorativo e garantir que cada movimento cumpra uma funcao de negocio clara.

## Detalhes

### Principios Fundamentais Aplicados a {aspect.upper()}
- **Engajamento e Proposito**: Cada animacao configurada nesta etapa deve responder a uma necessidade real do usuario (como guiar a navegacao ou suavizar o feedback).
- **Expressao da Marca**: O comportamento de {aspect} deve estar perfeitamente alinhado com a identidade visual da marca (movimentos precisos para tecnologia, organicos para biologia).
- **Coesao Visual**: Garantir tempos consistentes e transicoes integradas.
- **Evitar o Excesso**: Animacoes inuteis prejudicam a performance e distraem o leitor. Se puder ser removida sem perda de valor, ela nao deve existir.

### Diretrizes Especificas
- Otimizar recursos graficos no cliente.
- Respeitar a acessibilidade (remover animacoes sob `prefers-reduced-motion`).
- Manter transicoes abaixo de 300ms para evitar sensacao de lentidao.

## Links

- [[00_MOC]]
- [[30_libraries/general/design-strategic-animations]]
"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        doc_count += 1

print(f"Total de documentos gerados: {doc_count}")

print("Gerando 100 diretorios de skills com SKILL.md...")
# 2. Gerar 100 skills (20 tecnologias * 5 variacoes)
skill_count = 0
for tech in TECH_SKILLS:
    for var in SKILL_VARIATIONS:
        folder_name = f"{tech}-{var}"
        folder_path = os.path.join(SKILLS_DIR, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        
        skill_file = os.path.join(folder_path, "SKILL.md")
        
        # Conteudo da skill
        content = f"""---
name: {tech.replace('-', ' ').title()} {var.title()}
description: Habilidade tecnica para {var} utilizando {tech.replace('-', ' ')} com foco em animacao estrategica e intencional.
---

# {tech.replace('-', ' ').title()} - {var.title()}

Esta skill descreve as diretrizes praticas e operacionais para a execucao de {var} usando {tech}.

## Diretrizes de Execucao

1. **Restricao e Proposito**: Nao crie animacoes em excesso. Use {tech} de forma pontual para resolver necessidades especificas de comunicacao, engajamento ou guia visual.
2. **Coesao**: Alinhe o setup de {tech} com o design system global, respeitando curvas de duracao coesas.
3. **Performance**: Implemente {var} garantindo que a renderizacao ocorra por hardware (GPU) e respeite a acessibilidade de movimento.
4. **Otimizacao**: Evite redesenhos desnecessarios no DOM (evitar Reflows e Repaints repetitivos).

## Como Aplicar
- Setup: Inicie configuracoes limpas no monorepo.
- Debugging: Inspecione com ferramentas de perfil de frames do navegador.
- Integration: Combine de forma fluida com componentes reativos.
"""
        with open(skill_file, "w", encoding="utf-8") as f:
            f.write(content)
        skill_count += 1

print(f"Total de skills geradas: {skill_count}")
print("Finalizado com sucesso!")
