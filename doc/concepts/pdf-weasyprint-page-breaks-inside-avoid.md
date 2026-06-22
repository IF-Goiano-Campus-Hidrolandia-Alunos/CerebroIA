---
tags: ['pythonpdfgeneration', 'documentacao', 'pdf', 'reportlab', 'weasyprint']
updated: 2026-06-21
---

## Definição

Instruções e padrões de geração de PDF profissional em Python para PDF WeasyPrint Page Breaks Inside Avoid.

## Contexto

Essencial para emitir relatórios de solo, alertas de pragas e resumos executivos formatados e prontos para impressão.

## Detalhes

- Conceito do layout, fluxo de páginas e elementos Platypus/CSS Paged Media.
- Técnicas de estilização de tabelas, fontes customizadas e cabeçalhos dinâmicos.
- Otimização no consumo de memória e velocidade de renderização em lote.

### Exemplo de Implementação Prática

```python
# Renderização de HTML/CSS para PDF usando WeasyPrint e Jinja2
from weasyprint import HTML
from jinja2 import Template

html_template = """
<html>
<head>
<style>
  @page {
    size: A4;
    margin: 20mm;
    @bottom-right {
      content: "Página " counter(page) " de " counter(pages);
      font-family: 'Helvetica', sans-serif;
      font-size: 9pt;
    }
  }
  body { font-family: sans-serif; color: #333; }
  h1 { color: #16a34a; }
  table { width: 100%; border-collapse: collapse; margin-top: 20px; }
  th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
  th { background-color: #f2f2f2; }
</style>
</head>
<body>
  <h1>Relatório de Campo - {{ local }}</h1>
  <p>Data: {{ data }}</p>
  <table>
    <tr><th>Sensor</th><th>Média</th></tr>
    {% for s in sensores %}
    <tr><td>{{ s.nome }}</td><td>{{ s.media }}</td></tr>
    {% endfor %}
  </table>
</body>
</html>
"""

template = Template(html_template)
rendered_html = template.render(local="Setor Norte", data="21/06/2026", 
                                sensores=[{"nome": "Solo 1", "media": "45%"}, {"nome": "Solo 2", "media": "38%"}])

# Gera o PDF
HTML(string=rendered_html).write_pdf("relatorio_weasy.pdf")
```

## Links

- [[00_MOC]]
- [[concepts/guia-organizacao-para]]
- [[concepts/guia-dataview-obsidian]]
