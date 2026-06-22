---
tags: ['pythonpdfgeneration', 'documentacao', 'pdf', 'reportlab', 'weasyprint']
updated: 2026-06-21
---

## Definição

Instruções e padrões de geração de PDF profissional em Python para PDF ReportLab Encryption Password Protection.

## Contexto

Essencial para emitir relatórios de solo, alertas de pragas e resumos executivos formatados e prontos para impressão.

## Detalhes

- Conceito do layout, fluxo de páginas e elementos Platypus/CSS Paged Media.
- Técnicas de estilização de tabelas, fontes customizadas e cabeçalhos dinâmicos.
- Otimização no consumo de memória e velocidade de renderização em lote.

### Exemplo de Implementação Prática

```python
# Geração de PDF profissional com ReportLab Platypus
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def gerar_pdf_relatorio(filename="relatorio.pdf"):
    # Configuração do documento com margens seguras
    doc = SimpleDocTemplate(filename, pagesize=letter,
                            rightMargin=36, leftMargin=36, topMargin=54, bottomMargin=54)
    story = []
    styles = getSampleStyleSheet()
    
    # Estilo customizado com leading correto
    titulo_style = ParagraphStyle(
        'TituloCustom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#16a34a') # Verde PlantiumAI
    )
    
    story.append(Paragraph("Relatório Técnico Agronômico", titulo_style))
    story.append(Spacer(1, 15))
    
    # Tabela com estilos profissionais
    data = [
        ['Indicador', 'Valor Lido', 'Status'],
        ['Umidade do Solo', '42.5%', 'Ideal'],
        ['pH do Solo', '6.2', 'Estável'],
        ['NPK Residual', 'Alto', 'Fértil']
    ]
    t = Table(data, colWidths=[200, 150, 150])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#1e293b')),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,0), 8),
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#f8fafc')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
    ]))
    story.append(t)
    doc.build(story)

gerar_pdf_relatorio()
```

## Links

- [[00_MOC]]
- [[concepts/guia-organizacao-para]]
- [[concepts/guia-dataview-obsidian]]
