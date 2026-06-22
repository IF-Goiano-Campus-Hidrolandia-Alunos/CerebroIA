---
tags: ['visionyolov8edge', 'documentacao', 'visao-computacional', 'yolov8', 'opencv']
updated: 2026-06-21
---

## Definição

Processamento de imagem e algoritmos de visão computacional para Vision OpenCV Moments Centroid Calculation com foco em dispositivos de borda.

## Contexto

Permite identificar pragas, analisar o crescimento de folhas e automatizar medições ópticas no campo.

## Detalhes

- Pipelines de captação e filtragem de quadros de vídeo em tempo real.
- Inferência local otimizada do modelo YOLOv8 usando aceleração via GPU/TPU.
- Tratamento geométrico de contornos, formas e cores com o OpenCV.

### Exemplo de Implementação Prática

```python
# Filtragem de cor (HSV) e detecção de contornos de folhas com OpenCV
import cv2
import numpy as np

img = cv2.imread("folha.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Intervalo de cor verde (representa folha saudável)
lower_green = np.array([35, 40, 40])
upper_green = np.array([85, 255, 255])

# Criação de máscara binária
mask = cv2.inRange(hsv, lower_green, upper_green)

# Encontra contornos da folha na máscara
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    area = cv2.contourArea(c)
    if area > 500: # Filtra ruídos pequenos
        # Desenha contorno na imagem original
        cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
        
        # Desenha retângulo delimitador
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imwrite("folha_contorno.jpg", img)
```

## Links

- [[00_MOC]]
- [[concepts/guia-organizacao-para]]
- [[concepts/guia-dataview-obsidian]]
