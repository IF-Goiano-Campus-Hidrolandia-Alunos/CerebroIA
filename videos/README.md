# Estúdio de Vídeo — BlackHole-Agent / PlantiumAI

Pipeline de edição de vídeo **dirigido por agente (Claude)**, local e determinístico.
Mando um vídeo no chat → o agente edita → saem os arquivos prontos.

## Filosofia: economia de tokens

> Todo trabalho **pesado de mídia é determinístico** e roda 100% local via
> **ffmpeg + Pillow** (zero tokens). O LLM só decide *o quê* (cortes, textos,
> posições) — nunca move bytes.

As decisões ficam em **JSON ("recipe")**. Reeditar = mudar o JSON e rodar de novo,
sem gastar contexto relendo o vídeo. Inspecionar quadros (Read em PNGs) é o único
custo de tokens, e é pontual.

## Ferramentas e por que estas

| Necessidade | Ferramenta | Custo |
|---|---|---|
| Cortes, filtros, cor, áudio, overlay, encode | **FFmpeg 7.x** | local, 0 tokens |
| Cards/legendas/lower-thirds + animação (PNG/sequência RGBA) | **Pillow (PIL)** | local, 0 tokens |
| Remover marca d'água (inpaint content-aware, por frame) | **OpenCV** (`opencv-python-headless`) | local, 0 tokens |
| Cortar silêncios por transcrição | `video_editor.py` (silencedetect) | local |

> **Marca d'água (3 métodos):**
> - `inpaint` (OpenCV TELEA, por frame) — reconstrói o fundo. Ótimo, mas **borra
>   texto** se a marca estiver sobre legenda.
> - `patch` (remendo de folha, nativo ffmpeg) — clona região limpa vizinha. Rápido,
>   orgânico; também borra se houver texto embaixo.
> - `unblend` — **des-mistura** a marca semi-transparente: estima o alfa dela num
>   frame escuro e subtrai só a contribuição (`rec=(obs−α·255)/(1−α)`), **preservando
>   o texto por baixo**. Use quando a marca cobre legenda. (No `recipe`:
>   `"watermark": { "method": "unblend", ... }`.)
> Evite `delogo`: deixa "fantasma" em marcas semi-transparentes.

### Os dois repositórios de referência
- **[browser-use/video-use](https://github.com/browser-use/video-use)** — define a
  *metodologia*: um agente edita vídeo por linguagem natural usando ffmpeg + overlays,
  lendo transcrição/timeline em vez de frames crus (economia de tokens). **Nosso
  `video_studio.py` implementa esse padrão localmente.** Para cortes guiados por fala,
  o video-use usa transcrição (ElevenLabs Scribe) — dá pra plugar quando precisarmos.
- **[heygen/hyperframes](https://github.com/heygen-com/hyperframes)** — render de
  animações **HTML/CSS/JS → MP4 com canal alfa** (headless Chrome + GSAP). É o backend
  ideal para **motion graphics complexos** (slide/scale/stagger, Lottie, gráficos
  animados). **Hoje não é necessário**: as legendas deste vídeo são *fade simples*, que
  o ffmpeg replica com fidelidade total. Fica como backend opcional documentado.

**Quando trocar de ferramenta:** se um vídeo pedir animação de overlay rica (não só
fade/posição estática), aí sim instalar o HyperFrames (Node 22+ / Puppeteer) e gerar
o overlay como vídeo alfa, compondo no lugar do PNG do PIL.

## Estrutura

```
videos/
  videos para editar/    # entrada (conteúdo NÃO versionado)
  videos editados/       # saída   (conteúdo NÃO versionado)
  edição de video/       # 100 skills de edição (VERSIONADAS)
  recipe_*.json          # receita de edição (versionada)
  captions_*.json        # spec das legendas (versionada)
  intro_*.json           # spec do lower-third (versionada)
  _work/                 # scratch: frames, PNGs, logs (NÃO versionado)
scripts/
  video_studio.py        # toolkit (overlay + render + probe)
  video_editor.py        # cortes de silêncio
```

## Como editar um vídeo novo

1. Jogue o arquivo em `videos/videos para editar/`.
2. Peça a edição no chat. O agente inspeciona frames e ajusta os JSON.
3. Render:
   ```bash
   python scripts/video_studio.py render videos/recipe_SEU.json
   ```

### Comandos do toolkit
```bash
python scripts/video_studio.py overlay    <captions.json> <out.png>  # gera só o overlay
python scripts/video_studio.py render      <recipe.json>             # pipeline completo (inpaint + sequência animada)
python scripts/video_studio.py renderlean  <recipe.json>             # pipeline LEAN (estilo Gemini, ~12s)
python scripts/video_studio.py probe       <video>                   # metadados
```

## Dois pipelines (escolha por necessidade)

Aprendemos a técnica do **Gemini** (que editou este mesmo vídeo antes) e a otimizamos.
Hoje há duas formas de renderizar, com o mesmo `captions_*.json`:

| | `render` (v2 — qualidade máx.) | `renderlean` (v3 — estilo Gemini) |
|---|---|---|
| **Marca d'água** | inpaint OpenCV (reconstrói, por frame) | **remendo de folha**: clona pixels limpos do próprio frame e cobre a estrela (nativo ffmpeg, 1 passada) |
| **Legenda** | sequência PNG (76 frames) — animação livre | **2 PNGs** (esq/dir) + slide/fade no ffmpeg |
| **Passada** | Python por frame + ffmpeg | **1 chamada ffmpeg** |
| **Velocidade** | ~mais lento | **~9–12 s** |
| **Quando** | controle total de animação, fundo difícil | velocidade, fundo com textura reaproveitável |

> O "remendo de folha" é a sacada do Gemini: em vez de borrar (delogo) ou
> reconstruir (inpaint), **clona uma região limpa vizinha** e a sobrepõe com máscara
> circular suave — orgânico, acompanha a câmera, sem custo de Python por frame.
> Coordenadas e máscara ficam no `recipe_*_v3.json` (bloco `patch`).

### Logo da marca no lugar da marca d'água
Os dois pipelines aceitam um bloco `logo` na recipe: depois de remover a estrela,
sobrepõem o **badge da PlantiumAI** (`videos/assets/logo_badge_circular.png`) no mesmo
ponto, como "bug" de canto. Some no outro (onde o logo grande aparece). Ajuste
`center`, `diam`, `opacity`, `start`/`end` na recipe.

## Caso de referência: `Strawberry_plant_smart_irrigation` (10s, 720p24)

- **Marca d'água** (estrela ✦ semi-transparente, canto inf-dir estático) removida por
  **inpaint do OpenCV** — some por completo em qualquer fundo (sem fantasma do `delogo`).
- **Legendas dos sensores** (texto gerado por IA, embolado e trocado) substituídas por
  cards corretos, **cobrindo 100%** as originais e **ocupando o mesmo espaço**. Design
  novo (lower-third moderno: barra de acento + tag de categoria colorida + título com
  sublinhado + descrição) e **animação** (entrada deslizante escalonada + fade).
  Sincronizado com o vídeo: os cards entram *sobre filmagem limpa* e ficam opacos
  **antes** da legenda original surgir (4,15s), saindo só quando a cena escurece para o
  logo (~6,45s) — zero vazamento do texto antigo, do surgimento ao sumiço.
- **Ajustes:** color grade vibrante (`eq`), leve nitidez (`unsharp`), abertura
  (lower-third "Irrigação Inteligente para Morangos") e normalização de loudness
  (-14 LUFS) na versão YouTube.
- **Saídas:**
  - `morango_irrigacao_youtube.mp4` — com áudio normalizado (postar no YouTube).
  - `morango_irrigacao_web_mudo.mp4` — sem áudio (incorporar no site).

### Mapeamento dos componentes (revisar com o hardware real!)
As legendas foram corrigidas assumindo um sistema padrão de irrigação inteligente.
**Confirme se batem com a sua placa/sensores reais** — é só editar `captions_morango.json`:

| Card | Componente assumido |
|---|---|
| Sensor de luz | BH1750 (lux) |
| Temp. & umidade do ar | DHT22 |
| Temp. do solo | DS18B20 (sonda à prova d'água) |
| Umidade do solo | sensor capacitivo |
| Controlador | Raspberry Pi + ESP32 |
| Atuação | relé 4 canais + válvula solenoide |
