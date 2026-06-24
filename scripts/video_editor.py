import os
import re
import subprocess
import sys

def get_video_duration(video_path):
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        video_path
    ]
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return float(res.stdout.strip())
    except Exception as e:
        print(f"[Erro] Falha ao obter duração do vídeo: {e}", flush=True)
        return 0.0

def detect_silence(video_path, noise_db=-30, min_duration=0.5):
    print(f"[Silêncio] Detectando pausas no vídeo '{os.path.basename(video_path)}' (ruído < {noise_db}dB, duração > {min_duration}s)...", flush=True)
    cmd = [
        "ffmpeg", "-i", video_path,
        "-af", f"silencedetect=noise={noise_db}dB:d={min_duration}",
        "-f", "null", "-"
    ]
    
    # FFmpeg outputs silencedetect details to stderr
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8', errors='replace')
    _, stderr = process.communicate()
    
    silences = []
    start = None
    for line in stderr.splitlines():
        if "silence_start" in line:
            match = re.search(r"silence_start:\s*([\d\.]+)", line)
            if match:
                start = float(match.group(1))
        elif "silence_end" in line:
            match = re.search(r"silence_end:\s*([\d\.]+)", line)
            if match:
                end = float(match.group(1))
                if start is not None:
                    silences.append((start, end))
                    start = None
    print(f"[Silêncio] {len(silences)} silêncios detectados.", flush=True)
    return silences

def calculate_non_silent_segments(silences, total_duration, padding=0.1):
    segments = []
    current_time = 0.0
    
    for start, end in silences:
        # Apply padding to prevent cutting word boundaries
        non_silent_end = max(0.0, start - padding)
        if non_silent_end > current_time:
            segments.append((current_time, non_silent_end))
        current_time = min(total_duration, end + padding)
        
    if current_time < total_duration:
        segments.append((current_time, total_duration))
        
    return segments

def cut_silences(input_path, output_path, noise_db=-30, min_duration=0.5, padding=0.1):
    total_duration = get_video_duration(input_path)
    if total_duration <= 0:
        print("[Erro] Duração do vídeo inválida.", flush=True)
        return False
        
    silences = detect_silence(input_path, noise_db, min_duration)
    if not silences:
        print("[Silêncio] Nenhum silêncio detectado. Apenas copiando arquivo para o destino...", flush=True)
        try:
            import shutil
            shutil.copy2(input_path, output_path)
            return True
        except Exception as e:
            print(f"[Erro] Falha ao copiar arquivo: {e}", flush=True)
            return False
            
    segments = calculate_non_silent_segments(silences, total_duration, padding)
    if not segments:
        print("[Aviso] O vídeo inteiro foi detectado como silêncio! Nada a cortar.", flush=True)
        return False
        
    print(f"[Corte] Cortando e juntando {len(segments)} segmentos falados...", flush=True)
    
    # Build filter_complex string
    filter_parts = []
    concat_inputs = ""
    for i, (start, end) in enumerate(segments):
        filter_parts.append(
            f"[0:v]trim=start={start:.3f}:end={end:.3f},setpts=PTS-STARTPTS[v{i}];"
            f"[0:a]atrim=start={start:.3f}:end={end:.3f},asetpts=PTS-STARTPTS[a{i}]"
        )
        concat_inputs += f"[v{i}][a{i}]"
        
    filter_parts.append(f"{concat_inputs}concat=n={len(segments)}:v=1:a=1[outv][outa]")
    filter_complex_str = ";".join(filter_parts)
    
    cmd = [
        "ffmpeg", "-y", "-i", input_path,
        "-filter_complex", filter_complex_str,
        "-map", "[outv]", "-map", "[outa]",
        "-c:v", "libx264", "-preset", "superfast",
        "-c:a", "aac", "-b:a", "192k",
        output_path
    ]
    
    print(f"[Corte] Renderizando vídeo sem silêncio em '{os.path.basename(output_path)}'...", flush=True)
    try:
        # Run ffmpeg showing standard outputs
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        print("[Corte] Renderização concluída com sucesso!", flush=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"[Erro] Falha ao renderizar vídeo com FFmpeg:\n{e.stderr}", flush=True)
        return False

def add_subtitle(input_path, output_path, text, start_time, duration):
    print(f"[Legenda] Adicionando legenda '{text}' a partir de {start_time}s por {duration}s...", flush=True)
    
    # Escape single quotes in text for ffmpeg drawtext filter
    escaped_text = text.replace("'", "'\\\\''").replace(":", "\\:")
    
    end_time = start_time + duration
    filter_str = (
        f"drawtext=text='{escaped_text}':fontcolor=white:fontsize=36:"
        f"borderw=3:bordercolor=black:box=1:boxcolor=black@0.4:boxborderw=10:"
        f"x=(w-text_w)/2:y=h-100:enable='between(t,{start_time:.3f},{end_time:.3f})'"
    )
    
    cmd = [
        "ffmpeg", "-y", "-i", input_path,
        "-vf", filter_str,
        "-c:v", "libx264", "-preset", "superfast",
        "-c:a", "copy",
        output_path
    ]
    
    try:
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        print("[Legenda] Legenda adicionada com sucesso!", flush=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"[Erro] Falha ao adicionar legenda com FFmpeg:\n{e.stderr}", flush=True)
        return False
