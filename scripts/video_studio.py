#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
video_studio.py  —  Toolkit de edicao de video do BlackHole-Agent / PlantiumAI.

Filosofia (economia de tokens):
  Todo o trabalho pesado de midia e DETERMINISTICO e roda 100% local via
  ffmpeg + Pillow + OpenCV (zero tokens). O LLM so DECIDE (cortes, textos,
  posicoes); nunca move bytes. As decisoes ficam em JSON ("recipe").

Capacidades:
  - Remocao de marca d'agua por INPAINTING content-aware (OpenCV, por frame) ->
    bem melhor que delogo p/ logos semi-transparentes (nao deixa "fantasma").
  - Legendas/lower-thirds como cards (design moderno) com ANIMACAO de entrada
    (slide + fade escalonado) renderizada como sequencia PNG e composta no ffmpeg.
  - Color grade, nitidez, loudnorm, perfis de export (YouTube / web mudo).

Comandos:
  python video_studio.py render  <recipe.json>
  python video_studio.py overlay <spec.json> <out.png>      # card estatico
  python video_studio.py probe   <video>
"""
import json, math, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONTS = {"bold": "C:/Windows/Fonts/arialbd.ttf", "regular": "C:/Windows/Fonts/arial.ttf"}

def font(kind, size):
    return ImageFont.truetype(FONTS[kind], size)

def _wrap(draw, text, fnt, max_w):
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

# ----------------------------------------------------------------- design card
def draw_card(d, c, spec, dx=0):
    """Desenha UM card (lower-third moderno) no ImageDraw `d`, deslocado em x por dx.
    Design: painel escuro opaco + barra de acento a esquerda + tag de categoria
    em caixa-alta (cor do acento) + titulo branco + sublinhado + descricao cinza."""
    x, y, w, h = c["box"]; x += dx
    r = spec.get("radius", 14)
    accent = tuple(c.get("accent", spec.get("accent", [80, 210, 140])))
    fill = tuple(spec.get("card_fill", [16, 20, 27, 255]))

    d.rounded_rectangle([x, y, x + w, y + h], r, fill=fill,
                        outline=(255, 255, 255, 30), width=1)
    # barra de acento vertical
    d.rounded_rectangle([x + 8, y + 12, x + 13, y + h - 12], 2, fill=(*accent, 255))

    pad_l = x + 26
    tag = c.get("tag")
    tf = font("bold", c.get("title_size", 18))
    df = font("regular", c.get("desc_size", 14))
    gf = font("bold", c.get("tag_size", 11))
    max_w = w - (pad_l - x) - 18

    title = c["title"]; ts = c.get("title_size", 18)
    while d.textlength(title, font=tf) > max_w and ts > 12:
        ts -= 1; tf = font("bold", ts)
    desc_lines = _wrap(d, c["desc"], df, max_w)

    tag_h = (gf.size + 8) if tag else 0
    block_h = tag_h + (tf.size + 6) + 4 + len(desc_lines) * (df.size + 4) - 4
    ty = y + max(14, (h - block_h) // 2)

    if tag:
        d.text((pad_l, ty), tag.upper(), fill=(*accent, 255), font=gf)
        ty += gf.size + 8
    d.text((pad_l, ty), title, fill=(255, 255, 255, 255), font=tf)
    tw = min(d.textlength(title, font=tf), max_w)
    uy = ty + tf.size + 3
    d.line([(pad_l, uy), (pad_l + min(tw, 46), uy)], fill=(*accent, 255), width=2)
    ty = uy + 7
    for line in desc_lines:
        d.text((pad_l, ty), line, fill=(206, 214, 222, 255), font=df)
        ty += df.size + 4

def render_overlay(spec, out_path, side=None):
    """Card(s) estaticos -> PNG RGBA. side='left'/'right' filtra por coluna
    (usado p/ os 'callouts' por fase do pipeline lean, estilo Gemini)."""
    W, H = spec.get("width", 1280), spec.get("height", 720)
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    for c in spec["cards"]:
        cx = c["box"][0] + c["box"][2] / 2
        if side == "left" and cx >= W / 2: continue
        if side == "right" and cx < W / 2: continue
        draw_card(d, c, spec)
    img.save(out_path)
    print(f"[overlay] {out_path} ({W}x{H}) side={side}")
    return out_path

def make_logo_overlay(logo_path, out_path, W, H, center, diam, opacity=0.92):
    """Coloca o badge da marca (circular, transparente) num canvas 1280x720 no
    ponto `center`, pronto p/ overlay 0:0. Usado p/ marcar o lugar da marca d'água."""
    logo = Image.open(logo_path).convert("RGBA").resize((diam, diam), Image.LANCZOS)
    if opacity < 1.0:
        a = logo.split()[3].point(lambda p: int(p * opacity)); logo.putalpha(a)
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    cx, cy = center
    canvas.alpha_composite(logo, (int(cx - diam / 2), int(cy - diam / 2)))
    canvas.save(out_path)
    print(f"[logo] {out_path} diam={diam} @ {center}")
    return out_path

def radial_patch_mask(out_path, size=80, core=25, fade_end=40):
    """Mascara circular (cinza): miolo opaco (raio core) + fade quadratico ate 0.
    Usada no 'remendo de folha' (clone) p/ remover marca d'agua via ffmpeg."""
    import numpy as np
    yy, xx = np.mgrid[0:size, 0:size]
    cx = cy = size / 2.0
    dist = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
    a = np.ones_like(dist)
    fade = (dist - core) / (fade_end - core)
    a = np.where(dist <= core, 1.0, np.clip(1.0 - fade, 0.0, 1.0) ** 2)
    Image.fromarray((a * 255).astype("uint8"), "L").save(out_path)
    print(f"[mask] {out_path} {size}x{size} core={core} fade={fade_end}")
    return out_path

# ------------------------------------------------------------------- animacao
def _ease_out_cubic(p):
    return 1 - (1 - p) ** 3

def _card_state(k, t, anim, c, spec):
    """Retorna (alpha 0..1, dx) do card k no tempo absoluto t."""
    W = spec.get("width", 1280)
    cx = c["box"][0] + c["box"][2] / 2
    slide = anim.get("slide", 46)
    sgn = -1 if cx < W / 2 else 1            # left entra da esq, right da dir
    t_in = anim["start"] + anim["in_start"] + k * anim.get("stagger", 0.05)
    in_dur = anim.get("in_dur", 0.32)
    a, dx = 1.0, 0.0
    if t < t_in:
        return 0.0, sgn * slide
    if t < t_in + in_dur:
        p = _ease_out_cubic((t - t_in) / in_dur)
        a, dx = p, sgn * slide * (1 - p)
    # fade-out (sem slide) sincronizado com o escurecimento da cena
    t_out = anim["start"] + anim["out_start"]
    if t >= t_out:
        p = min(1.0, (t - t_out) / anim.get("out_dur", 0.18))
        a = min(a, 1 - p)
    return max(0.0, a), dx

def render_sequence(spec, anim, fps, outdir):
    """Gera a sequencia PNG animada que cobre a janela [start,end]."""
    if os.path.isdir(outdir):
        for f in os.listdir(outdir):
            os.remove(os.path.join(outdir, f))
    else:
        os.makedirs(outdir)
    W, H = spec.get("width", 1280), spec.get("height", 720)
    start, end = anim["start"], anim["end"]
    n = int(round((end - start) * fps))
    for fi in range(n + 1):
        t = start + fi / fps
        canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        for k, c in enumerate(spec["cards"]):
            a, dx = _card_state(k, t, anim, c, spec)
            if a <= 0.001:
                continue
            layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            draw_card(ImageDraw.Draw(layer), c, spec, dx=int(round(dx)))
            if a < 0.999:
                alpha = layer.split()[3].point(lambda p, a=a: int(p * a))
                layer.putalpha(alpha)
            canvas = Image.alpha_composite(canvas, layer)
        canvas.save(os.path.join(outdir, f"cap_{fi:04d}.png"))
    print(f"[seq] {outdir}: {n + 1} frames ({start}->{end}s @ {fps}fps)")
    return n + 1

# ----------------------------------------------------------------- watermark
def _star4_mask(W, H, wm):
    cx, cy = wm["center"]; R = wm.get("outer", 44); r = wm.get("inner", 15)
    ang = [(-90, R), (-45, r), (0, R), (45, r), (90, R), (135, r), (180, R), (225, r)]
    pts = [(cx + rr * math.cos(math.radians(a)), cy + rr * math.sin(math.radians(a)))
           for a, rr in ang]
    m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).polygon(pts, fill=255)
    k = wm.get("dilate", 6) * 2 + 1
    return m.filter(ImageFilter.MaxFilter(k if k % 2 else k + 1))

def _probe_dims(src):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
         "stream=width,height,r_frame_rate", "-of", "csv=p=0", src],
        stdout=subprocess.PIPE, text=True).stdout.strip().split(",")
    w, h, rate = int(out[0]), int(out[1]), out[2]
    num, den = rate.split("/"); fps = float(num) / float(den)
    return w, h, fps

def _grab_frame(src, t):
    import numpy as np, cv2, io
    p = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", src,
                        "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"],
                       stdout=subprocess.PIPE)
    arr = np.array(Image.open(io.BytesIO(p.stdout)).convert("RGB"))
    return cv2.cvtColor(arr, cv2.COLOR_RGB2BGR)

def unblend_watermark(src, out, wm):
    """Remove marca d'agua SEMI-TRANSPARENTE preservando o que esta por baixo
    (texto!). Estima o alfa da estrela num frame escuro do outro e subtrai so a
    contribuicao dela: recuperado = (obs - alfa*255)/(1-alfa). Use quando a marca
    cobre legendas (inpaint borraria as letras)."""
    import numpy as np, cv2
    W, H, fps = _probe_dims(src)
    mask = np.array(_star4_mask(W, H, wm))
    D = _grab_frame(src, wm.get("dark_t", 8.0))
    bgD = cv2.inpaint(D, mask, wm.get("radius", 5), cv2.INPAINT_TELEA).astype(np.float32)
    Df = D.astype(np.float32)
    a = np.clip((Df - bgD) / (255.0 - bgD + 1e-3), 0, wm.get("amax", 0.85))
    a = cv2.GaussianBlur(a, (0, 0), 1.0)
    soft = cv2.GaussianBlur(mask.astype(np.float32) / 255.0, (0, 0), 2.0)[..., None]
    a = a * soft                                       # zera fora da estrela
    # strength>1 subtrai um pouco mais -> residuo mais transparente (cuidado: muito
    # alto inverte p/ estrela ESCURA; ~1.1-1.2 e o ponto de residuo minimo)
    a = np.clip(a * wm.get("strength", 1.0), 0, 0.97)
    rd = subprocess.Popen(["ffmpeg", "-v", "error", "-i", src, "-f", "rawvideo",
                           "-pix_fmt", "bgr24", "pipe:1"], stdout=subprocess.PIPE)
    wr = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo",
                           "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", f"{fps}",
                           "-i", "pipe:0", "-i", src, "-map", "0:v", "-map", "1:a?",
                           "-c:v", "libx264", "-crf", "12", "-preset", "fast",
                           "-pix_fmt", "yuv420p", "-c:a", "copy", "-shortest", out],
                          stdin=subprocess.PIPE)
    # hibrido: onde NAO ha texto sob a marca, usa inpaint (residuo zero); onde HA
    # texto, usa unblend (preserva letras). Decide por concordancia inpaint/unblend.
    clean = wm.get("clean_residual", False)
    rad = wm.get("radius", 5); lo = wm.get("lo", 22); hi = wm.get("hi", 55)
    fsz = W * H * 3; n = 0
    while True:
        buf = b""
        while len(buf) < fsz:
            ch = rd.stdout.read(fsz - len(buf))
            if not ch: break
            buf += ch
        if len(buf) < fsz: break
        F8 = np.ascontiguousarray(np.frombuffer(buf, np.uint8).reshape(H, W, 3))
        F = F8.astype(np.float32)
        u = np.clip((F - a * 255.0) / (1.0 - a), 0, 255)
        if clean:
            inp = cv2.inpaint(F8, mask, rad, cv2.INPAINT_TELEA).astype(np.float32)
            diff = cv2.GaussianBlur(np.abs(u - inp).mean(axis=2), (0, 0), 1.5)
            w = np.clip((diff - lo) / (hi - lo), 0, 1)[..., None]
            rec = u * w + inp * (1 - w)
        else:
            rec = u
        wr.stdin.write(np.clip(rec, 0, 255).astype(np.uint8).tobytes()); n += 1
    wr.stdin.close(); rd.stdout.close(); wr.wait(); rd.wait()
    print(f"[unblend] {out}: {n} frames (alfa max {a.max():.2f}, clean={clean})")
    return out

def inpaint_watermark(src, out, wm):
    """Remove marca d'agua estatica via OpenCV inpaint (TELEA), frame a frame.
    Gera intermediario quase sem perdas (CRF 12) com o audio original copiado."""
    import numpy as np, cv2
    W, H, fps = _probe_dims(src)
    mask = np.array(_star4_mask(W, H, wm))
    rad = wm.get("radius", 5)
    rd = subprocess.Popen(
        ["ffmpeg", "-v", "error", "-i", src, "-f", "rawvideo",
         "-pix_fmt", "bgr24", "pipe:1"], stdout=subprocess.PIPE)
    wr = subprocess.Popen(
        ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24",
         "-s", f"{W}x{H}", "-r", f"{fps}", "-i", "pipe:0", "-i", src,
         "-map", "0:v", "-map", "1:a?", "-c:v", "libx264", "-crf", "12",
         "-preset", "fast", "-pix_fmt", "yuv420p", "-c:a", "copy",
         "-shortest", out], stdin=subprocess.PIPE)
    fsz = W * H * 3; n = 0
    while True:
        buf = b""
        while len(buf) < fsz:
            chunk = rd.stdout.read(fsz - len(buf))
            if not chunk: break
            buf += chunk
        if len(buf) < fsz: break
        fr = np.frombuffer(buf, np.uint8).reshape(H, W, 3)
        fr = cv2.inpaint(fr, mask, rad, cv2.INPAINT_TELEA)
        wr.stdin.write(fr.tobytes()); n += 1
    wr.stdin.close(); rd.stdout.close(); wr.wait(); rd.wait()
    print(f"[inpaint] {out}: {n} frames limpos")
    return out

# -------------------------------------------------------------------- render
def _ff(args):
    r = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                       text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        sys.stderr.write(r.stderr[-3000:])
        raise SystemExit(f"[erro] ffmpeg falhou ({r.returncode})")

def build_video_filter(rc):
    f = []
    for wm in rc.get("delogo", []):
        x, y, w, h = wm
        f.append(f"delogo=x={x}:y={y}:w={w}:h={h}:show=0")
    g = rc.get("grade")
    if g:
        f.append("eq=contrast={c}:saturation={s}:brightness={b}:gamma={g}".format(
            c=g.get("contrast", 1.0), s=g.get("saturation", 1.0),
            b=g.get("brightness", 0.0), g=g.get("gamma", 1.0)))
    if rc.get("sharpen"):
        f.append("unsharp=5:5:{a}:5:5:0.0".format(a=rc.get("sharpen", 0.6)))
    if rc.get("vignette"):
        f.append("vignette=PI/5")
    return f

def render(recipe_path):
    rc = json.load(open(recipe_path, encoding="utf-8"))
    base = os.path.dirname(os.path.abspath(recipe_path))
    P = lambda p: p if os.path.isabs(p) else os.path.join(base, p)
    src = P(rc["input"])
    fps = rc.get("fps", 24)

    # pre-passo: remover marca d'agua -> intermediario limpo
    # method "unblend" preserva texto sob a marca; "inpaint" reconstroi (padrao)
    if rc.get("watermark"):
        clean = P(rc.get("watermark_tmp", "_work/_clean.mp4"))
        os.makedirs(os.path.dirname(clean), exist_ok=True)
        if rc["watermark"].get("method") == "unblend":
            unblend_watermark(src, clean, rc["watermark"])
        else:
            inpaint_watermark(src, clean, rc["watermark"])
        src = clean

    # prepara overlays (estaticos -> PNG; animados -> sequencia)
    overlays = list(rc.get("overlays", []))
    for ov in overlays:
        if not ov.get("from_spec"):
            continue  # PNG ja pronto (ex.: logo)
        spec = json.load(open(P(ov["from_spec"]), encoding="utf-8"))
        if ov.get("animate"):
            anim = dict(ov["animate"]); anim["start"] = ov["start"]; anim["end"] = ov["end"]
            ov["_n"] = render_sequence(spec, anim, fps, P(ov["seq"]))
        else:
            render_overlay(spec, P(ov["png"]))

    # logo da marca no lugar da marca d'agua (POR SAIDA: prof["logo"] liga/desliga)
    lg = rc.get("logo"); logo_ov = None
    if lg:
        png = P(lg.get("png", "_work/logo_overlay.png"))
        make_logo_overlay(P(lg["file"]), png, 1280, 720,
                          lg["center"], lg["diam"], lg.get("opacity", 0.92))
        logo_ov = {"png": png, "start": lg.get("start", 0.4),
                   "end": lg.get("end", 6.7), "fade": lg.get("fade", 0.4)}

    for prof in rc["outputs"]:
        out = P(prof["file"]); os.makedirs(os.path.dirname(out), exist_ok=True)
        ov_list = list(overlays)
        if logo_ov and prof.get("logo", True):
            ov_list.append(logo_ov)
        inputs = ["ffmpeg", "-y", "-i", src]
        for ov in ov_list:
            if ov.get("animate"):
                inputs += ["-framerate", str(fps), "-i", os.path.join(P(ov["seq"]), "cap_%04d.png")]
            else:
                inputs += ["-loop", "1", "-r", str(fps), "-i", P(ov["png"])]

        vf = build_video_filter(rc)
        graph = [f"[0:v]{','.join(vf)}[v0]" if vf else "[0:v]null[v0]"]
        last = "v0"
        for i, ov in enumerate(ov_list, start=1):
            st, en = ov["start"], ov["end"]
            lbl = f"o{i}"; nxt = f"v{i}"
            if ov.get("animate"):
                graph.append(f"[{i}:v]format=rgba,setpts=PTS-STARTPTS+{st}/TB[{lbl}]")
                graph.append(f"[{last}][{lbl}]overlay=0:0:eof_action=pass:"
                             f"enable='between(t,{st},{en})'[{nxt}]")
            else:
                fd = ov.get("fade", 0.25)
                graph.append(f"[{i}:v]format=rgba,fade=t=in:st={st}:d={fd}:alpha=1,"
                             f"fade=t=out:st={en-fd}:d={fd}:alpha=1[{lbl}]")
                graph.append(f"[{last}][{lbl}]overlay=0:0:shortest=1:"
                             f"enable='between(t,{st},{en})'[{nxt}]")
            last = nxt
        args = inputs + ["-filter_complex", ";".join(graph), "-map", f"[{last}]"]

        if prof.get("audio", True):
            args += ["-map", "0:a?"]
            if rc.get("audio_filter"):
                args += ["-af", rc["audio_filter"]]
            args += ["-c:a", "aac", "-b:a", prof.get("abr", "192k")]
        else:
            args += ["-an"]
        args += ["-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p",
                 "-crf", str(prof.get("crf", 18)), "-preset", prof.get("preset", "slow"),
                 "-movflags", "+faststart", out]
        _ff(args)
        print(f"[ok] {out}")

def render_lean(recipe_path):
    """Pipeline LEAN (estilo Gemini, otimizado): marca d'agua por 'remendo de folha'
    (clone nativo ffmpeg) + callouts em 2 PNGs (esq/dir) com slide+fade dirigidos
    pelo ffmpeg. UMA passada por saida, sem Python por frame. Rapido (~12s)."""
    rc = json.load(open(recipe_path, encoding="utf-8"))
    base = os.path.dirname(os.path.abspath(recipe_path))
    P = lambda p: p if os.path.isabs(p) else os.path.join(base, p)
    src = P(rc["input"]); fps = rc.get("fps", 24)
    wk = P(rc.get("workdir", "_work")); os.makedirs(wk, exist_ok=True)

    # 1) gera os assets-imagem (callouts esq/dir, intro, mascara do remendo)
    cap = json.load(open(P(rc["captions"]), encoding="utf-8"))
    left = os.path.join(wk, "callouts_left.png");  render_overlay(cap, left, "left")
    right = os.path.join(wk, "callouts_right.png"); render_overlay(cap, right, "right")
    intro = os.path.join(wk, "intro_lean.png")
    render_overlay(json.load(open(P(rc["intro"]), encoding="utf-8")), intro)
    mask = os.path.join(wk, "patch_mask.png")
    pm = rc["patch"]; radial_patch_mask(mask, pm.get("size", 80),
                                        pm.get("core", 25), pm.get("fade", 40))
    lg = rc.get("logo"); logo_png = None
    if lg:
        logo_png = os.path.join(wk, "logo_overlay.png")
        make_logo_overlay(P(lg["file"]), logo_png, 1280, 720,
                          lg["center"], lg["diam"], lg.get("opacity", 0.92))

    cw = rc.get("captions_window", [3.5, 6.62])
    st, en = cw[0], cw[1]
    ind = rc.get("in_dur", 0.30); outd = rc.get("out_dur", 0.18)
    out_st = rc.get("out_start", en - 0.17); sl = rc.get("slide", 46)
    g = rc.get("grade", {}); sx, sy = pm["dst"]; px, py = pm["src"]
    sz = pm.get("size", 80)
    grade = ("eq=contrast={c}:saturation={s}:brightness={b}:gamma={gm},"
             "unsharp=5:5:{sh}:5:5:0".format(
                 c=g.get("contrast", 1.0), s=g.get("saturation", 1.0),
                 b=g.get("brightness", 0.0), gm=g.get("gamma", 1.0),
                 sh=rc.get("sharpen", 0.5)))
    # rampa 0->1 da animacao de entrada
    ramp = "min(1\\,max(0\\,(t-{st})/{d}))".format(st=st, d=ind)
    fades = "fade=t=in:st={st}:d={d}:alpha=1,fade=t=out:st={o}:d={od}:alpha=1".format(
        st=st, d=ind, o=out_st, od=outd)

    intro_st, intro_en = rc.get("intro_window", [0.4, 3.3])

    for prof in rc["outputs"]:
        out = P(prof["file"]); os.makedirs(os.path.dirname(out), exist_ok=True)
        args = ["ffmpeg", "-y", "-i", src, "-i", mask,
                "-loop", "1", "-r", str(fps), "-i", left,
                "-loop", "1", "-r", str(fps), "-i", right,
                "-loop", "1", "-r", str(fps), "-i", intro]
        if logo_png:
            args += ["-loop", "1", "-r", str(fps), "-i", logo_png]
        fc = (
            # remendo de folha: clona patch limpo e cobre a estrela
            f"[0:v]split=2[base][s];"
            f"[s]crop={sz}:{sz}:{px}:{py}[p];"
            f"[p][1:v]alphamerge[pm];"
            f"[base][pm]overlay={sx}:{sy}:shortest=1[wm];"
            f"[wm]{grade}[gr];"
            # callouts esquerda: entra deslizando da esquerda
            f"[2:v]format=rgba,{fades}[L];"
            f"[gr][L]overlay=x='-{sl}+{sl}*{ramp}':y=0:shortest=1:"
            f"enable='between(t,{st},{en})'[a];"
            # callouts direita: entra deslizando da direita
            f"[3:v]format=rgba,{fades}[R];"
            f"[a][R]overlay=x='{sl}-{sl}*{ramp}':y=0:shortest=1:"
            f"enable='between(t,{st},{en})'[b];"
            # intro lower-third
            f"[4:v]format=rgba,fade=t=in:st={intro_st}:d=0.3:alpha=1,"
            f"fade=t=out:st={intro_en-0.3}:d=0.3:alpha=1[I];"
            f"[b][I]overlay=0:0:shortest=1:enable='between(t,{intro_st},{intro_en})'[vi]"
        )
        if logo_png:
            ls, le = lg.get("start", 0.4), lg.get("end", 6.7); lf = lg.get("fade", 0.4)
            fc += (f";[5:v]format=rgba,fade=t=in:st={ls}:d={lf}:alpha=1,"
                   f"fade=t=out:st={le-lf}:d={lf}:alpha=1[LG];"
                   f"[vi][LG]overlay=0:0:shortest=1:enable='between(t,{ls},{le})'[v]")
        else:
            fc += ";[vi]null[v]"
        args += ["-filter_complex", fc, "-map", "[v]"]
        if prof.get("audio", True):
            args += ["-map", "0:a?"]
            if rc.get("audio_filter"): args += ["-af", rc["audio_filter"]]
            args += ["-c:a", "aac", "-b:a", prof.get("abr", "192k")]
        else:
            args += ["-an"]
        args += ["-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p",
                 "-crf", str(prof.get("crf", 18)), "-preset", prof.get("preset", "medium"),
                 "-movflags", "+faststart", out]
        _ff(args)
        print(f"[ok-lean] {out}")

def probe(video):
    subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format", video])

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "overlay":
        render_overlay(json.load(open(sys.argv[2], encoding="utf-8")), sys.argv[3])
    elif cmd == "render":
        render(sys.argv[2])
    elif cmd == "renderlean":
        render_lean(sys.argv[2])
    elif cmd == "probe":
        probe(sys.argv[2])
    else:
        print(__doc__)
