---
tags: ['visionyolov8edge', 'documentacao', 'visao-computacional', 'yolov8', 'opencv']
updated: 2026-06-21
---

## Definição

Processamento de imagem e algoritmos de visão computacional para Vision Edge Deploy Nvidia Jetson Nano TensorRT com foco em dispositivos de borda.

## Contexto

Permite identificar pragas, analisar o crescimento de folhas e automatizar medições ópticas no campo.

## Detalhes

- Pipelines de captação e filtragem de quadros de vídeo em tempo real.
- Inferência local otimizada do modelo YOLOv8 usando aceleração via GPU/TPU.
- Tratamento geométrico de contornos, formas e cores com o OpenCV.

### Exemplo de Implementação Prática

```python
# RTSP Video Stream frame-by-frame Reader com thread isolada para evitar lag
import cv2
import threading
import queue

class RTSPStreamReader:
    def __init__(self, rtsp_url):
        self.cap = cv2.VideoCapture(rtsp_url)
        self.q = queue.Queue(maxsize=3)
        self.stopped = False
        
        # Inicia thread de captura
        self.t = threading.Thread(target=self._capture, daemon=True)
        self.t.start()
        
    def _capture(self):
        while not self.stopped:
            ret, frame = self.cap.read()
            if not ret:
                break
            if not self.q.full():
                self.q.put(frame)
            else:
                try:
                    self.q.get_nowait() # descarta quadro antigo
                    self.q.put(frame)
                except queue.Empty:
                    pass
                    
    def read(self):
        return self.q.get() if not self.q.empty() else None

    def stop(self):
        self.stopped = True
        self.cap.release()
```

## Links

- [[00_MOC]]
- [[concepts/guia-organizacao-para]]
- [[concepts/guia-dataview-obsidian]]
