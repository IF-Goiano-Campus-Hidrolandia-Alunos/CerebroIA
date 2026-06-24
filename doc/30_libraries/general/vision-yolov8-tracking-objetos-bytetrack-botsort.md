---
tags: ['visionyolov8edge', 'documentacao', 'visao-computacional', 'yolov8', 'opencv']
updated: 2026-06-21
---

## Definição

Processamento de imagem e algoritmos de visão computacional para Vision YOLOv8 Tracking Objetos Bytetrack Botsort com foco em dispositivos de borda.

## Contexto

Permite identificar pragas, analisar o crescimento de folhas e automatizar medições ópticas no campo.

## Detalhes

- Pipelines de captação e filtragem de quadros de vídeo em tempo real.
- Inferência local otimizada do modelo YOLOv8 usando aceleração via GPU/TPU.
- Tratamento geométrico de contornos, formas e cores com o OpenCV.

### Exemplo de Implementação Prática

```python
# Inferência local rápida de imagens/vídeos usando YOLOv8 da Ultralytics
from ultralytics import YOLO
import cv2

# Carrega modelo pré-treinado ou customizado leve (.pt ou exportado para .onnx)
model = YOLO("yolov8n.pt") # Modelo Nano (ultra-leve)

# Executa predição em imagem
results = model("folhas.jpg")

for r in results:
    # Plota detecções visualmente na imagem original
    img_plot = r.plot()
    
    # Extrai coordenadas de caixas delimitadoras e classes
    for box in r.boxes:
        coords = box.xyxy[0].tolist() # [x1, y1, x2, y2]
        confidence = box.conf[0].item()
        cls_id = int(box.cls[0].item())
        print(f"Classe: {cls_id}, Confiança: {confidence:.2f}, Box: {coords}")

cv2.imwrite("resultado_inferencia.jpg", img_plot)
```

## Links

- [[00_MOC]]
- [[30_libraries/dotnet_arch/guia-organizacao-para]]
- [[30_libraries/dotnet_arch/guia-dataview-obsidian]]
