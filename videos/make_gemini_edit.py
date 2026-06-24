#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_gemini_edit.py
Pipeline de edição de vídeo premium com Pillow (overlays limpos sem desfoque)
e FFmpeg (render de alto desempenho com delogo e overlays em uma única chamada).
Lê as coordenadas e textos dinamicamente de captions.json e intro.json.
Diferencia os cards por fase (phase) de animação e aplica overlays sequenciais.
Remove marca d'água dinamicamente através de inpainting por folha com máscara circular suave (feathered).
"""
import os
import sys
import json
import subprocess
from PIL import Image, ImageDraw, ImageFont

# Caminhos principais
WORKSPACE_DIR = r"c:\Users\thyag\OneDrive\Desktop\Brain-main\videos"
WORK_DIR = os.path.join(WORKSPACE_DIR, "_work")
OUTPUTS_DIR = os.path.join(WORKSPACE_DIR, "videos editados")

# Resolve o vídeo de entrada de forma dinâmica para evitar erros de encoding de caracteres especiais
import glob
video_files = glob.glob(os.path.join(WORKSPACE_DIR, "videos para editar", "*.mp4"))
if not video_files:
    print("[Erro] Nenhum vídeo MP4 encontrado em 'videos para editar'.")
    sys.exit(1)
INPUT_VIDEO = video_files[0]
print(f"Vídeo de entrada encontrado: {INPUT_VIDEO}")

# Fontes padrão do Windows
FONTS_DIR = "C:\\Windows\\Fonts"
FONT_BOLD_PATH = os.path.join(FONTS_DIR, "segoeuib.ttf")
FONT_REGULAR_PATH = os.path.join(FONTS_DIR, "segoeui.ttf")

if not os.path.exists(FONT_BOLD_PATH):
    FONT_BOLD_PATH = os.path.join(FONTS_DIR, "arialbd.ttf")
if not os.path.exists(FONT_REGULAR_PATH):
    FONT_REGULAR_PATH = os.path.join(FONTS_DIR, "arial.ttf")

def get_font(style, size):
    path = FONT_BOLD_PATH if style == "bold" else FONT_REGULAR_PATH
    return ImageFont.truetype(path, size)

def wrap_text(draw, text, fnt, max_w):
    """Quebra o texto em linhas para caber no box de largura max_w."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def generate_callouts_glass():
    """Cria os overlays transparentes das legendas divididos em duas fases."""
    print("[1/3] Gerando overlays de sensores (fase 1 e fase 2)...")
    captions_spec_path = os.path.join(WORK_DIR, "captions.json")
    
    with open(captions_spec_path, "r", encoding="utf-8") as f:
        spec = json.load(f)
        
    width = spec.get("width", 1280)
    height = spec.get("height", 720)
    radius = spec.get("radius", 12)
    card_fill = tuple(spec.get("card_fill", [40, 45, 42, 255]))
    
    # Criamos telas transparentes para as duas fases de animação
    canvas1 = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    canvas2 = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    
    for c in spec["cards"]:
        x, y, w, h = c["box"]
        accent = tuple(c.get("accent", [30, 210, 170]))
        phase = c.get("phase", 1)
        
        # Desenha o card individual
        card_img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        draw = ImageDraw.Draw(card_img)
        
        # Fundo do card e borda teal brilhante (Design limpo sem accent bar na esquerda e sem dot)
        border = (*accent, 220)
        draw.rounded_rectangle(
            [0, 0, w - 1, h - 1],
            radius=radius,
            fill=card_fill,
            outline=border,
            width=2
        )
        
        # Fontes e alinhamento
        pad = 14
        tx = pad
        title_sz = 14
        desc_sz = 12
        f_title = get_font("bold", title_sz)
        f_body = get_font("regular", desc_sz)
        
        max_w = w - pad * 2
        
        # Ajusta o título se for muito grande
        title = c["title"]
        while draw.textlength(title, font=f_title) > max_w and title_sz > 10:
            title_sz -= 1
            f_title = get_font("bold", title_sz)
            
        desc_lines = wrap_text(draw, c["desc"], f_body, max_w)
        
        # Centraliza o bloco de texto verticalmente
        block_h = (f_title.size + 6) + len(desc_lines) * (f_body.size + 4) - 4
        ty = max(pad, (h - block_h) // 2)
        
        # Título
        draw.text((tx, ty), title, font=f_title, fill=(255, 255, 255, 255))
        
        # Descrição
        curr_y = ty + f_title.size + 6
        for line in desc_lines:
            draw.text((tx, curr_y), line, font=f_body, fill=(215, 225, 220, 255))
            curr_y += f_body.size + 4
        
        # Cola na tela correspondente à fase
        if phase == 1:
            canvas1.paste(card_img, (x, y), card_img)
        else:
            canvas2.paste(card_img, (x, y), card_img)
            
    out_path1 = os.path.join(WORK_DIR, "callouts_phase1.png")
    out_path2 = os.path.join(WORK_DIR, "callouts_phase2.png")
    canvas1.save(out_path1)
    canvas2.save(out_path2)
    print(f"-> Salvo Fase 1: {out_path1}")
    print(f"-> Salvo Fase 2: {out_path2}")

def generate_intro_glass():
    """Cria o overlay transparente de introdução com o design limpo unificado."""
    print("[2/3] Gerando overlay de introdução (intro_glass.png)...")
    intro_spec_path = os.path.join(WORK_DIR, "intro.json")
    
    with open(intro_spec_path, "r", encoding="utf-8") as f:
        spec = json.load(f)
        
    width = spec.get("width", 1280)
    height = spec.get("height", 720)
    radius = spec.get("radius", 14)
    card_fill = tuple(spec.get("card_fill", [40, 45, 42, 255]))
    
    canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    
    for c in spec["cards"]:
        x, y, w, h = c["box"]
        accent = tuple(c.get("accent", [30, 210, 170]))
        
        # Desenha o card
        card_img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        draw = ImageDraw.Draw(card_img)
        
        border = (*accent, 220)
        draw.rounded_rectangle(
            [0, 0, w - 1, h - 1],
            radius=radius,
            fill=card_fill,
            outline=border,
            width=2
        )
        
        title_sz = c.get("title_size", 22)
        desc_sz = c.get("desc_size", 15)
        f_title = get_font("bold", title_sz)
        f_desc = get_font("regular", desc_sz)
        
        pad = 16
        tx = pad
        max_w = w - pad * 2
        
        title = c["title"]
        while draw.textlength(title, font=f_title) > max_w and title_sz > 14:
            title_sz -= 1
            f_title = get_font("bold", title_sz)
            
        desc_lines = wrap_text(draw, c["desc"], f_desc, max_w)
        
        block_h = (f_title.size + 7) + len(desc_lines) * (f_desc.size + 4) - 4
        ty = max(pad, (h - block_h) // 2)
        
        # Título
        draw.text((tx, ty), title, font=f_title, fill=(255, 255, 255, 255))
        # Descrição
        curr_y = ty + f_title.size + 7
        for line in desc_lines:
            draw.text((tx, curr_y), line, font=f_desc, fill=(215, 225, 220, 255))
            curr_y += f_desc.size + 4
        
        canvas.paste(card_img, (x, y), card_img)
        
    out_path = os.path.join(WORK_DIR, "intro_glass.png")
    canvas.save(out_path)
    print(f"-> Salvo: {out_path}")

def generate_watermark_mask():
    """Cria uma máscara de degradê circular suave de 80x80 pixels."""
    print("[3/3] Gerando máscara de marca d'água (watermark_mask.png)...")
    mask = Image.new("L", (80, 80), 0)
    draw = ImageDraw.Draw(mask)
    for r in range(40, -1, -1):
        # Centro até r=25 é 100% opaco (255) para cobrir a estrela.
        # De r=26 a r=40, fazemos um fade suave até 0 (totalmente transparente).
        if r <= 25:
            alpha = 255
        else:
            alpha = int(255 * ((40.0 - r) / 15.0) ** 2)
            
        if r == 0:
            draw.point((40, 40), fill=alpha)
        else:
            draw.ellipse([40 - r, 40 - r, 40 + r - 1, 40 + r - 1], fill=alpha)


    out_path = os.path.join(WORK_DIR, "watermark_mask.png")
    mask.save(out_path)
    print(f"-> Salvo: {out_path}")


def render_ffmpeg():
    """Roda a compilação do vídeo no FFmpeg com as duas fases de legendas sincronizadas."""
    print("\n[Render] Iniciando compilação do vídeo com FFmpeg...")
    
    overlay_intro = os.path.join(WORK_DIR, "intro_glass.png")
    overlay_c1 = os.path.join(WORK_DIR, "callouts_phase1.png")
    overlay_c2 = os.path.join(WORK_DIR, "callouts_phase2.png")
    overlay_mask = os.path.join(WORK_DIR, "watermark_mask.png")
    
    # 1. morango_irrigacao_youtube_gemini.mp4
    out_youtube = os.path.join(OUTPUTS_DIR, "morango_irrigacao_youtube_gemini.mp4")
    
    # Remendo dinâmico de marca d'água:
    # 1. Recorta um pedaço limpo de folha do próprio vídeo em x=1030:y=565:w=80:h=80.
    # 2. Aplica a máscara circular com bordas suaves (feathered) via alphamerge.
    # 3. Sobrepõe este remendo sobre a marca d'água original em x=1120:y=565.
    # Isso acompanha a movimentação natural da câmera e do vento, ficando 100% invisível.
    # Depois, aplica equalização de cor, nitidez, e os cards em duas fases.
    filter_complex = (
        "[0:v]crop=w=80:h=80:x=1030:y=565[patch];"
        "[patch][4:v]alphamerge[masked_patch];"
        "[0:v][masked_patch]overlay=1120:565:shortest=1[v_patched];"
        
        "[v_patched]eq=contrast=1.06:saturation=1.12:brightness=0.01:gamma=1.0,"
        "unsharp=5:5:0.5:5:5:0.0[v_base];"
        
        # 1. Fade in/out da intro (0.4s a 3.3s, fade=0.3s)
        "[1:v]format=rgba,fade=t=in:st=0.4:d=0.3:alpha=1,fade=t=out:st=3.0:d=0.3:alpha=1[o_intro];"
        "[v_base][o_intro]overlay=0:0:shortest=1:enable='between(t,0.4,3.3)'[v_intro];"
        
        # 2. Fade in/out dos callouts fase 1 (3.9s a 6.5s, fade=0.3s)
        "[2:v]format=rgba,fade=t=in:st=3.9:d=0.3:alpha=1,fade=t=out:st=6.15:d=0.35:alpha=1[o_c1];"
        "[v_intro][o_c1]overlay=0:0:shortest=1:enable='between(t,3.9,6.5)'[v_c1];"
        
        # 3. Fade in/out dos callouts fase 2 (4.2s a 6.5s, fade=0.3s)
        "[3:v]format=rgba,fade=t=in:st=4.2:d=0.3:alpha=1,fade=t=out:st=6.15:d=0.35:alpha=1[o_c2];"
        "[v_c1][o_c2]overlay=0:0:shortest=1:enable='between(t,4.2,6.5)'[v_out]"
    )
    
    cmd_youtube = [
        "ffmpeg", "-y",
        "-i", INPUT_VIDEO,
        "-loop", "1", "-r", "24", "-i", overlay_intro,
        "-loop", "1", "-r", "24", "-i", overlay_c1,
        "-loop", "1", "-r", "24", "-i", overlay_c2,
        "-loop", "1", "-r", "24", "-i", overlay_mask,
        "-filter_complex", filter_complex,
        "-map", "[v_out]",
        "-map", "0:a?",
        "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
        "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p",
        "-crf", "18", "-preset", "medium",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        out_youtube
    ]
    
    # 2. morango_irrigacao_web_mudo_gemini.mp4
    out_web_mudo = os.path.join(OUTPUTS_DIR, "morango_irrigacao_web_mudo_gemini.mp4")
    cmd_web_mudo = [
        "ffmpeg", "-y",
        "-i", INPUT_VIDEO,
        "-loop", "1", "-r", "24", "-i", overlay_intro,
        "-loop", "1", "-r", "24", "-i", overlay_c1,
        "-loop", "1", "-r", "24", "-i", overlay_c2,
        "-loop", "1", "-r", "24", "-i", overlay_mask,
        "-filter_complex", filter_complex,
        "-map", "[v_out]",
        "-an",
        "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p",
        "-crf", "20", "-preset", "medium",
        "-movflags", "+faststart",
        out_web_mudo
    ]
    
    try:
        print("\n-> Renderizando morango_irrigacao_youtube_gemini.mp4...")
        subprocess.run(cmd_youtube, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
        print("-> Youtube vídeo pronto!")
        
        print("\n-> Renderizando morango_irrigacao_web_mudo_gemini.mp4...")
        subprocess.run(cmd_web_mudo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
        print("-> Web mudo vídeo pronto!")
        
        print("\n[Render] Vídeos compilados com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n[Erro] Falha no FFmpeg:\n{e.stderr[-1000:]}")
        return False

def main():
    os.makedirs(OUTPUTS_DIR, exist_ok=True)
    generate_callouts_glass()
    generate_intro_glass()
    generate_watermark_mask()
    success = render_ffmpeg()
    if success:
        print("\n[OK] Pipeline concluído com sucesso!")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
