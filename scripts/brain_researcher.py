#!/usr/bin/env python3
import os
import sys
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
os.environ["TRANSFORMERS_NO_ADVISORY_WARNINGS"] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import json
import re
import datetime
import subprocess
import time
import threading
import gc

# Dynamic resolution of vault path (makes it portable for sharing)
SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_DIR = os.path.dirname(SCRIPTS_DIR)
DOC_DIR = os.path.join(VAULT_DIR, "doc")
CONCEPTS_DIR = os.path.join(DOC_DIR, "concepts")
CACHE_DIR = os.path.join(DOC_DIR, "external_cache")
MOC_PATH = os.path.join(DOC_DIR, "00_MOC.md")
MEMORY_PATH = os.path.join(SCRIPTS_DIR, "agent_memory.json")

# 1. Auto-install dependencies on startup
def install_dependencies():
    deps = ["duckduckgo-search", "torch", "transformers", "huggingface_hub", "prompt-toolkit"]
    for dep in deps:
        try:
            import_name = dep.replace("-", "_")
            __import__(import_name)
        except ImportError:
            print(f"\033[93m[SISTEMA] Instalando biblioteca '{dep}'...\033[0m", flush=True)
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
            except Exception as e:
                print(f"\033[91m[Aviso] Falha ao instalar {dep}: {e}. Continuando...\033[0m", flush=True)

install_dependencies()

# Imports after auto-installation
try:
    from duckduckgo_search import DDGS
    HAS_SEARCH = True
except ImportError:
    HAS_SEARCH = False

try:
    import torch
    HAS_TORCH = True
except ImportError:
    HAS_TORCH = False
    print("[Erro] PyTorch não pôde ser carregado.", flush=True)
    sys.exit(1)

try:
    from prompt_toolkit import PromptSession
    from prompt_toolkit.completion import Completer, Completion
    from prompt_toolkit.auto_suggest import AutoSuggest, AutoSuggestFromHistory, Suggestion
    from prompt_toolkit.styles import Style
    HAS_PROMPT_TOOLKIT = True

    class SlashCommandCompleter(Completer):
        def get_completions(self, document, complete_event):
            text = document.text_before_cursor
            if text.startswith("/"):
                if " " in text:
                    return
                cmds = ["/help", "/model", "/clear", "/status", "/vault", "/read", "/search", "/write", "/run", "/video", "/sair", "/exit"]
                for cmd in cmds:
                    if cmd.startswith(text):
                        yield Completion(cmd, start_position=-len(text))

    class CommandAutoSuggest(AutoSuggest):
        def __init__(self, history_suggest=None):
            self.history_suggest = history_suggest

        def get_suggestion(self, buffer, document):
            text = document.text
            if text.startswith("/"):
                cmds = ["/help", "/model", "/clear", "/status", "/vault", "/read", "/search", "/write", "/run", "/video", "/sair", "/exit"]
                for cmd in cmds:
                    if cmd.startswith(text) and cmd != text:
                        return Suggestion(cmd[len(text):])
            if self.history_suggest:
                return self.history_suggest.get_suggestion(buffer, document)
            return None
except ImportError:
    HAS_PROMPT_TOOLKIT = False


# 2. Beautiful Terminal Spinner Class (runs in background thread)
class Spinner:
    def __init__(self, message="Processando..."):
        self.message = message
        self.running = False
        self.thread = None

    def spin(self):
        chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        i = 0
        while self.running:
            sys.stdout.write(f"\r\033[95m{chars[i]} {self.message}\033[0m")
            sys.stdout.flush()
            time.sleep(0.08)
            i = (i + 1) % len(chars)

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.spin)
        self.thread.daemon = True
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()
        sys.stdout.write("\r" + " " * (len(self.message) + 15) + "\r")
        sys.stdout.flush()

# 3. Vault Files Manager Class
class VaultManager:
    @staticmethod
    def read_note(filename):
        paths_to_check = [
            os.path.join(DOC_DIR, filename),
            os.path.join(CONCEPTS_DIR, filename),
            os.path.join(CACHE_DIR, filename),
            os.path.join(DOC_DIR, "workflows", filename)
        ]
        
        # If the filename does not end with .md, also check with .md appended
        if not filename.endswith(".md"):
            filename_md = filename + ".md"
            paths_to_check += [
                os.path.join(DOC_DIR, filename_md),
                os.path.join(CONCEPTS_DIR, filename_md),
                os.path.join(CACHE_DIR, filename_md),
                os.path.join(DOC_DIR, "workflows", filename_md)
            ]
            
        for path in paths_to_check:
            if os.path.exists(path):
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        return f.read()
                except Exception:
                    pass
        return None

    @staticmethod
    def update_moc(concept_file, cache_file):
        concept_name = os.path.splitext(concept_file)[0]
        cache_name = os.path.splitext(cache_file)[0]

        if not os.path.exists(MOC_PATH):
            return

        with open(MOC_PATH, "r", encoding="utf-8") as f:
            content = f.read()

        # Add to Conceitos & Tecnologias
        concept_link = f"- [[concepts/{concept_name}]]"
        if concept_link not in content:
            pattern = "## Workflows & Processos"
            if pattern in content:
                parts = content.split(pattern)
                content = parts[0].rstrip() + f"\n{concept_link}\n\n" + pattern + parts[1]

        # Add to Cache Externo
        cache_link = f"- [[external_cache/{cache_name}]]"
        if cache_link not in content:
            pattern = "## Archive"
            if pattern in content:
                parts = content.split(pattern)
                content = parts[0].rstrip() + f"\n{cache_link}\n\n" + pattern + parts[1]

        with open(MOC_PATH, "w", encoding="utf-8") as f:
            f.write(content)

# 4. Persistent Memory Manager Class
class MemoryManager:
    def __init__(self):
        self.data = {
            "history": [],
            "user_profile": {"name": "Desenvolvedor"},
            "facts": []
        }
        self.load_memory()

    def load_memory(self):
        if os.path.exists(MEMORY_PATH):
            try:
                with open(MEMORY_PATH, "r", encoding="utf-8") as f:
                    self.data = json.load(f)
            except Exception as e:
                print(f"\033[93m[Aviso] Falha ao carregar memoria.json: {e}\033[0m", flush=True)

    def save_memory(self):
        try:
            with open(MEMORY_PATH, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"\033[91m[Erro] Falha ao salvar memoria.json: {e}\033[0m", flush=True)

    def get_history(self):
        return self.data.get("history", [])

    def save_history(self, history):
        self.data["history"] = history
        self.save_memory()

# 5. Local AI Model Execution Class (Lazy Loaded)
AVAILABLE_MODELS = {
    "1": ("Qwen/Qwen2.5-Coder-0.5B-Instruct", "Geral/Código - Rápido e ultra leve (500M) - Padrão"),
    "2": ("Qwen/Qwen2.5-Coder-1.5B-Instruct", "Código/Raciocínio Avançado - Recomendado (1.5B)"),
    "3": ("meta-llama/Llama-3.2-1B-Instruct", "Escrita/Conversação Geral - Respostas mais fluídas (1B)")
}

class LocalModel:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.model_name = "Qwen/Qwen2.5-Coder-0.5B-Instruct"
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def set_model_name(self, new_model_name):
        if self.model_name != new_model_name:
            if self.model is not None:
                del self.model
                self.model = None
            if self.tokenizer is not None:
                del self.tokenizer
                self.tokenizer = None
            self.model_name = new_model_name
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            return True
        return False

    def load(self):
        if self.model is not None and self.tokenizer is not None:
            return
        
        # Oculta logs do Transformers e Hugging Face durante o carregamento
        try:
            from transformers.utils import logging as transformers_logging
            transformers_logging.set_verbosity_error()
        except ImportError:
            pass
        
        spinner = Spinner("Inicializando pesos do modelo...")
        spinner.start()
        
        try:
            from transformers import AutoModelForCausalLM, AutoTokenizer
            
            # Carrega tokenizador com suporte offline-first
            try:
                self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, local_files_only=True)
            except Exception:
                self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, local_files_only=False)
                
            if self.device == "cpu":
                # Usamos float32 na CPU por padrão para máxima velocidade e compatibilidade
                # (bfloat16 em CPU sem instruções nativas AVX-512 BF16 causa lentidão extrema/congelamento).
                try:
                    self.model = AutoModelForCausalLM.from_pretrained(
                        self.model_name,
                        torch_dtype=torch.float32,
                        local_files_only=True
                    )
                except Exception:
                    self.model = AutoModelForCausalLM.from_pretrained(
                        self.model_name,
                        torch_dtype=torch.float32,
                        local_files_only=False
                    )
            else:
                try:
                    self.model = AutoModelForCausalLM.from_pretrained(
                        self.model_name,
                        torch_dtype="auto",
                        local_files_only=True
                    ).to(self.device)
                except Exception:
                    self.model = AutoModelForCausalLM.from_pretrained(
                        self.model_name,
                        torch_dtype="auto",
                        local_files_only=False
                    ).to(self.device)
            
            # Força limpeza do coletor de lixo
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
                
            spinner.stop()
            print(f"\033[92m✔ IA carregada com sucesso no dispositivo: {self.device.upper()}\033[0m\n", flush=True)
        except Exception as e:
            spinner.stop()
            print(f"\033[91m✖ Falha ao inicializar modelo: {e}\033[0m", flush=True)
            sys.exit(1)

    def generate(self, messages, max_new_tokens=1024, temperature=0.3):
        self.load()
        try:
            text = self.tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True
            )
            model_inputs = self.tokenizer([text], return_tensors="pt").to(self.device)
            
            do_sample = temperature > 0.0
            
            with torch.no_grad():
                generated_ids = self.model.generate(
                    **model_inputs,
                    max_new_tokens=max_new_tokens,
                    temperature=temperature if do_sample else None,
                    top_p=0.9 if do_sample else None,
                    do_sample=do_sample,
                    repetition_penalty=1.1,
                    pad_token_id=self.tokenizer.eos_token_id
                )
            
            generated_ids = [
                output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
            ]
            
            response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
            return response.strip()
        except Exception as e:
            print(f"\033[91m[Erro] Falha na inferência: {e}\033[0m", flush=True)
            return None

# 6. Beautiful Terminal Graphic Interface Class (Claude Code / Hermes style)
class TerminalUI:
    @staticmethod
    def print_welcome():
        print("\033[90m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[0m \033[90m⣿\033[0m ⢟⣩\033[90m⣟⡾⡁\033[0m     \033[90m⡀\033[0m  \033[90m⣚\033[0m          ")
        print("\033[90m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[0m ⣿⣏⠰⡀ \033[90m⢀⡀\033[0m  \033[90m⠘⠁\033[0m          ")
        print("⣿\033[90m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[33m⣿⣿\033[90m⣿⣿⣿⣿⣿\033[33m⣿⣿⣿\033[90m⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[0m ⣿\033[90m⡿\033[0m ⣟⠳⠦⠂ \033[90m⣀\033[0m \033[90m⠤\033[0m  \033[90m⠠\033[0m    \033[90m⠐\033[0m    ")
        print("⣿⠟\033[90m⠻⣻⣿⣿⡻⢿\033[0m ⣿⣿⣿⣿⣿⣿\033[90m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[97m⣿⣿⣿⣿\033[90m⣿⣿⣿\033[33m⣿⣿⣿\033[0m \033[90m⣿⣿⣿⣿⣿⣿\033[0m ⣷⣯⠖   \033[90m⢩\033[0m    \033[90m⡤\033[0m         ")
        print("\033[90m⠁\033[0m  ⠟⠻\033[90m⣾⣿\033[0m ⣿⣿⣿⣿⣿\033[90m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[33m⣿⣿\033[97m⣿⣿\033[95m⣿\033[97m⣿⣿⣿⣿⣿⣿⣿\033[37m⣿\033[95m⣿\033[97m⣿⣿\033[90m⣿\033[33m⣿⣿\033[0m \033[90m⣿⣿⣿⣿⣿⣿\033[0m     \033[90m⠘⠃\033[0m        \033[90m⠐\033[0m    ")
        print("\033[90m⣄⣀⣀⣀⣀⣒⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[33m⣿⣿⣿⣿\033[90m⣿\033[97m⣿⣿⣿\033[37m⣿⣿⣿\033[90m⣿⣿⣿⣿⣿\033[37m⣿⣿⣿\033[97m⣿⣿⣿⣿⣿\033[33m⣿⣿\033[90m⣿⣿⣿⣿⣿⣿\033[0m  \033[90m⠰⠆⠈⠁\033[0m             ")
        print("\033[33m⣿⣿⣿⣿⣿\033[90m⣿⣿⣿⣿\033[95m⣿⣿⣿⣿⣿⣿⣿⣿\033[97m⣿⣿⣿⣿⣿⣿\033[95m⣿\033[97m⣿⣿⣿\033[37m⣿⣿\033[90m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[37m⣿⣿\033[97m⣿⣿⣿⣿\033[33m⣿⣿⣿\033[90m⣿⣿⣿⣿⣿⡰⢆\033[0m ⢀⣤\033[90m⡽⠳⠆\033[0m          ")
        print("\033[33m⠿⠿⢿⣿⣿⣿⣿⣿⣿\033[93m⣿\033[97m⣿⣿⣿⣿\033[95m⣿⣿\033[97m⣿⣿⣿⣿⣿⣿⣿⣿\033[37m⣿⣿⣿⣿\033[90m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[37m⣿\033[97m⣿⣿⣿⣿⣿\033[90m⣿⣿⣿⣿⣿⣿⣿\033[0m ⡄\033[90m⡶\033[0m      ⠃⠂   ⠂  ")
        print("    \033[33m⠉⠙⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[97m⣿⣿⣿\033[95m⣿⣿⣿\033[37m⣿\033[95m⣿⣿\033[37m⣿\033[90m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[37m⣿\033[97m⣿⣿⣿⣿\033[95m⣿\033[97m⣿⣿\033[90m⣿⣿⣿⣿⣿⣿⣷⡍\033[0m    \033[90m⢠\033[0m     \033[90m⠘\033[0m   ")
        print("        \033[90m⠤⠄\033[0m \033[90m⣉⡙⠛⠻\033[33m⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[90m⣿⣿\033[95m⣿\033[37m⣿\033[95m⣿\033[37m⣿⣿\033[97m⣿⣿⣿\033[95m⣿⣿\033[97m⣿⣿⣿⣿\033[33m⣿⣿⣿⣿⣿⣷\033[90m⣦⣄⣀\033[0m          ")
        print("            \033[90m⠉⠉⠙\033[0m ⠲\033[90m⠶⢾⣯⣿⣿⣿\033[0m ⣿⣿\033[33m⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[93m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[33m⣿⣿⣿⣿⣿⣿⣿\033[90m⣿⣶⣤⣀\033[0m    \033[90m⠤\033[0m")
        print("         ⢀\033[90m⡀\033[0m       ⠈⠛\033[90m⠛⠋⠛⠉⣉⣿\033[33m⣶⣿⣿\033[90m⣶⣬⡛\033[0m ⣩\033[90m⣽⣿⣻⣿\033[33m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[90m⣶⣶⣤⣄\033[0m")
        print("          \033[90m⠷\033[0m   ⣀⡀     \033[90m⢀\033[0m \033[90m⣛⢻\033[0m \033[33m⣿⣿\033[90m⣿⣿⣿⣿⣿⣶⣶⣿⣷⣿⣿⣿\033[33m⣿⣿⣿⣿\033[90m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣛⣛⠛⠿⠿⠿⠿\033[0m \033[33m⣟⣻⠿⠿\033[90m⠿⠿⢿⣿⣿\033[0m")
        print("              ⠙⡋\033[90m⠶\033[0m ⠢⡤\033[90m⢂\033[0m ⢠⣤\033[90m⣤⣭⣿\033[33m⣿⣿⣿⣿⣿⣿⣿⣿\033[90m⣿⣿⣿⣿⣿⣿⣿⣿\033[33m⣿\033[90m⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠋⠋⠉\033[0m \033[90m⠛\033[0m \033[90m⠒⠒⠒⠉⠉⠒\033[0m      ")
        print("                  \033[90m⣤\033[0m ⠠⠻⠚⠿\033[90m⠿⣿⣿⣿\033[33m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[90m⣿⠿\033[0m \033[90m⠿⠿⠏\033[0m  ⠉⠁⠉⠉⠉                     ")
        print("                 ⢀ ⠦\033[90m⠛\033[0m    ⢮\033[90m⣛⠿⣿⣿\033[0m \033[33m⣿⣿⣿⣿⣿⣿⣿\033[90m⣿⣿⣿⣶⣶\033[0m \033[90m⠄\033[0m                           ")
        print("          \033[90m⠚⠁\033[0m    \033[90m⠰\033[0m ⠿   ⢤\033[90m⣤⣤⣴\033[0m ⣴⣦⡉\033[90m⠉⠛⠻⠿⠿⠿⠿⠟⠛⠋⠉\033[0m ⠁                             ")
        print("  \033[90m⡀\033[0m    \033[90m⠰⠆\033[0m \033[90m⠴⠂\033[0m  \033[90m⣀\033[0m   ⠃     \033[90m⣌⣙\033[0m \033[90m⠿\033[0m ⣟⠛\033[90m⣿⡷\033[0m                    ⡀   \033[90m⠒\033[0m \033[90m⣀\033[0m            ")
        print("\033[96m╭──────────────────────────────────────────────────────────╮\033[0m")
        print("\033[96m│                 🌌 BLACKHOLE-AGENT v2.2                  │\033[0m")
        print("\033[96m│  \"No centro da singularidade do conhecimento —           │\033[0m")
        print("\033[96m│   Conectando ideias no seu Vault.\"                       │\033[0m")
        print("\033[96m├──────────────────────────────────────────────────────────┤\033[0m")
        print("\033[96m│ * Conversação offline-first (carregamento instantâneo).  │\033[0m")
        print("\033[96m│ * Memória persistente ativada entre sessões.             │\033[0m")
        print("\033[96m│ * Ferramenta [LISTAR_VAULT] integrada.                   │\033[0m")
        print("\033[96m│ * Digite /help para ver os comandos de atalho.           │\033[0m")
        print("\033[96m│ * Digite 'sair' para encerrar a conversa.                │\033[0m")
        print("\033[96m╰──────────────────────────────────────────────────────────╯\033[0m", flush=True)

    @staticmethod
    def ask_user(session=None):
        print(f"\033[94m╭─ Você\033[0m")
        try:
            if HAS_PROMPT_TOOLKIT and session is not None:
                completer = SlashCommandCompleter()
                
                style = Style.from_dict({
                    'completion-menu.completion': 'bg:#1e1e2e fg:#cdd6f4',
                    'completion-menu.completion.current': 'bg:#89b4fa fg:#11111b bold',
                    'scrollbar.background': 'bg:#313244',
                    'scrollbar.button': 'bg:#f5c2e7',
                })
                
                val = session.prompt(
                    "╰─> ",
                    completer=completer,
                    complete_while_typing=True,
                    style=style,
                    auto_suggest=CommandAutoSuggest(AutoSuggestFromHistory())
                ).strip()
                return val
            else:
                val = input("\033[94m╰─> \033[0m").strip()
                return val
        except (KeyboardInterrupt, EOFError):
            return "sair"

    @staticmethod
    def print_ai_box(content):
        print("\033[92m╭─ BlackHole-Agent\033[0m")
        for line in content.split("\n"):
            print(f"\033[92m│\033[0m {line}")
        print("\033[92m╰──────────────────────────────────────────────────────────\033[0m", flush=True)

    @staticmethod
    def ask_approval(tool_name, tool_arg):
        print("\033[93m╭─ ⚙️  AÇÃO REQUERIDA (Human-in-the-Loop)\033[0m")
        print(f"\033[93m│\033[0m A IA deseja acionar: \033[1m{tool_name}\033[0m")
        if tool_arg:
            print(f"\033[93m│\033[0m Parâmetro: '{tool_arg}'")
        try:
            choice = input("\033[93m│\033[0m Aprovar execução? (s/n): ").strip().lower()
            approved = choice in ["s", "sim", "y", "yes"]
        except (KeyboardInterrupt, EOFError):
            approved = False
        print("\033[93m╰──────────────────────────────────────────────────────────\033[0m", flush=True)
        return approved

# Helper search functions
def search_duckduckgo(query, max_results=6):
    if not HAS_SEARCH:
        return []
    try:
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=max_results)]
        return results
    except Exception as e:
        print(f"[Busca] Erro na busca: {e}", flush=True)
        return []

def extract_json(text):
    text = text.strip()
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        text = match.group(0)
    text = text.strip()
    return json.loads(text)

def perform_research(query, local_model):
    print(f"\n=========================================", flush=True)
    print(f"[PESQUISA] Iniciando: \"{query}\"", flush=True)
    print(f"=========================================", flush=True)

    print("[Passo 1/3] Consultando o DuckDuckGo...", flush=True)
    search_results = search_duckduckgo(query)
    if search_results:
        print(f" -> {len(search_results)} fontes encontradas na web.", flush=True)
    else:
        print(" -> Nenhuma fonte web encontrada. Utilizando conhecimento local.", flush=True)

    current_date = datetime.date.today().strftime("%Y-%m-%d")
    prompt = f"""
Você é um estruturador de vault do Obsidian (Brain Vault).
Seu objetivo é analisar os resultados de busca e gerar duas notas no formato Markdown:
1. Uma nota conceitual (Concept) para `doc/concepts/` contendo a explicação estruturada do conceito/tecnologia.
2. Uma nota de cache externo (External Cache) para `doc/external_cache/` contendo links de fontes e resumo dos resultados de busca.

Tópico de Pesquisa: {query}

Resultados de Busca obtidos:
{json.dumps(search_results, indent=2, ensure_ascii=False)}

Escreva as notas em português (BR) seguindo os templates abaixo.

Estrutura da Nota Conceitual (TEMPLATE_CONCEPT.md):
---
tags: [tags relevantes]
updated: {current_date}
---

## Definição
[Explicação concisa em uma frase]

## Contexto
[Quando e onde aplicável no desenvolvimento]

## Detalhes
- [Tópicos técnicos objetivos, explicações e exemplos de código curtos e úteis se aplicável]

## Links
- [[MOC]] (sempre linkar para o 00_MOC)
- [[outra-nota-relevante]] (se houver)

Estrutura da Nota de Cache Externo (TEMPLATE_EXTERNAL.md):
---
tags: [tags relevantes, cache]
updated: {current_date}
---

## Fonte
- [Nome do site ou link]({{{{link}}}})

## Resumo
- [Resumo técnico objetivo em bullet points das informações úteis para desenvolvimento]

Retorne APENAS um objeto JSON válido contendo a seguinte estrutura:
{{
  "concept_filename": "nome-da-nota-conceitual.md",
  "concept_content": "conteúdo markdown da nota conceitual",
  "cache_filename": "nome-da-nota-de-cache.md",
  "cache_content": "conteúdo markdown da nota de cache"
}}
Não inclua nenhuma introdução, conclusão ou blocos de código além do próprio JSON. Use nomes de arquivo baseados em kebab-case (letras minúsculas e hífens).
"""

    print("[Passo 2/3] Executando inferência com modelo local Qwen...", flush=True)
    messages = [
        {"role": "system", "content": "Você é um estruturador de vault do Obsidian e gera APENAS respostas em formato JSON bruto contendo notas Markdown."},
        {"role": "user", "content": prompt}
    ]
    ai_response = local_model.generate(messages, max_new_tokens=1536, temperature=0.1)
    
    if not ai_response:
        print("[Erro] Falha ao obter resposta do modelo local.", flush=True)
        return False

    print("[Passo 3/3] Gravando arquivos e atualizando MOC...", flush=True)
    try:
        data = extract_json(ai_response)
        concept_filename = data["concept_filename"]
        concept_content = data["concept_content"]
        cache_filename = data["cache_filename"]
        cache_content = data["cache_content"]

        os.makedirs(CONCEPTS_DIR, exist_ok=True)
        os.makedirs(CACHE_DIR, exist_ok=True)

        concept_path = os.path.join(CONCEPTS_DIR, concept_filename)
        with open(concept_path, "w", encoding="utf-8") as f:
            f.write(concept_content)

        cache_path = os.path.join(CACHE_DIR, cache_filename)
        with open(cache_path, "w", encoding="utf-8") as f:
            f.write(cache_content)

        VaultManager.update_moc(concept_filename, cache_filename)
        print(f"[Sucesso] Notas criadas:\n -> Concepts: {concept_filename}\n -> Cache: {cache_filename}", flush=True)
        return True
    except Exception as e:
        print(f"[Erro] Falha ao extrair ou gravar notas: {e}", flush=True)
        print(f"Resposta bruta do modelo local: {ai_response}", flush=True)
        return False

def find_closest_note_name(arg):
    if not arg:
        return arg
    clean_arg = arg.strip().lower()
    clean_arg = clean_arg.replace("concepts/", "").replace("workflows/", "")
    base_arg = os.path.splitext(clean_arg)[0]
    
    all_files = []
    for folder in [CONCEPTS_DIR, os.path.join(VAULT_DIR, "doc", "workflows"), DOC_DIR]:
        if os.path.exists(folder):
            try:
                all_files.extend(os.listdir(folder))
            except Exception:
                pass
                
    all_files = list(set([f for f in all_files if f.endswith(".md")]))
    if not all_files:
        return arg
        
    for filename in all_files:
        if filename.lower() == clean_arg or filename.lower() == clean_arg + ".md":
            return filename
            
    best_match = None
    best_score = 0
    for filename in all_files:
        name_without_ext = os.path.splitext(filename)[0].lower()
        score = 0
        if base_arg in name_without_ext:
            score += 10
        elif name_without_ext in base_arg:
            score += 8
        common = set(base_arg) & set(name_without_ext)
        score += len(common)
        
        if score > best_score:
            best_score = score
            best_match = filename
            
    if best_score >= 3:
        return best_match
    return arg

def detect_and_normalize_tool_call(text):
    match = re.search(r"\[([^\]]+)\]", text)
    if not match:
        return None
        
    full_inner = match.group(1).strip()
    parts = full_inner.split(":", 1)
    action_raw = parts[0].strip()
    arg = parts[1].strip() if len(parts) > 1 else ""
    
    action_norm = action_raw.upper()
    replacements = {
        "А": "A", "В": "B", "Е": "E", "К": "K", "М": "M", 
        "Н": "N", "О": "O", "Р": "P", "С": "C", "Т": "T", 
        "Х": "X", "У": "U", "И": "I"
    }
    for cyr, lat in replacements.items():
        action_norm = action_norm.replace(cyr, lat)
        
    detected_tool = None
    if "PESQU" in action_norm or "SEARCH" in action_norm:
        detected_tool = "PESQUISAR_TEMA"
    elif "LER" in action_norm or "READ" in action_norm:
        detected_tool = "LER_NOTA"
    elif "LIST" in action_norm or "VAULT" in action_norm:
        detected_tool = "LISTAR_VAULT"
        
    if detected_tool:
        arg = arg.strip("'\" ")
        if detected_tool == "LER_NOTA" and arg:
            arg = find_closest_note_name(arg)
        return detected_tool, arg
    return None

def run_chat_loop():
    TerminalUI.print_welcome()
    
    memory_manager = MemoryManager()
    local_model = LocalModel()
    
    session = None
    if HAS_PROMPT_TOOLKIT:
        session = PromptSession()
    
    system_prompt = (
        "Você é o BlackHole-Agent, assistente local do PlantiuIA com ACESSO REAL ao sistema de arquivos do vault do usuário.\n"
        "NÃO responda que é um modelo de texto e não tem acesso a arquivos locais, pois você tem ferramentas de sistema para lê-los. Use-as sempre!\n\n"
        "Comandos de ferramentas que você pode emitir (escreva APENAS o comando especial em sua resposta):\n"
        "1. Pesquisar na Web e criar notas: [PESQUISAR_TEMA: termo]\n"
        "2. Ler o conteúdo de uma nota existente: [LER_NOTA: nome_da_nota.md] (Use para ler '00_MOC.md' se precisar listar/buscar arquivos importantes)\n"
        "3. Listar arquivos de notas do vault: [LISTAR_VAULT]\n\n"
        "Exemplos de chamadas corretas:\n"
        "- Se o usuário perguntar: 'quais notas ou readmes temos no vault?' -> Responda APENAS: [LER_NOTA: 00_MOC.md]\n"
        "- Se o usuário perguntar: 'quais são os 5 readmes mais importantes do nosso vault?' -> Responda APENAS: [LER_NOTA: 00_MOC.md]\n"
        "- Se o usuário perguntar: 'o que tem na nota de testes do vault?' -> Responda APENAS: [LER_NOTA: TESTE_DO_Vault.md]\n"
        "- Se o usuário pedir: 'liste os arquivos do vault' -> Responda APENAS: [LISTAR_VAULT]\n\n"
        "Se o usuário pedir algo que você já tem no contexto ou não exigir ferramentas, responda diretamente em português brasileiro de forma objetiva."
    )

    raw_history = memory_manager.get_history()
    history = []
    # Filtra mensagens de recusa da IA anteriores para evitar bloqueio de contexto (context locking)
    for msg in raw_history:
        if msg.get("role") == "assistant":
            content_lower = msg.get("content", "").lower()
            if "não tenho acesso" in content_lower or "incapaz de acessar" in content_lower or "como assistente de" in content_lower or "como um modelo de" in content_lower:
                continue # Descarta a recusa antiga
        history.append(msg)

    # Ensure system prompt is first message
    if not history or history[0].get("role") != "system":
        history = [{"role": "system", "content": system_prompt}] + [m for m in history if m.get("role") != "system"]
    else:
        # Atualiza o system prompt se ele mudou
        history[0]["content"] = system_prompt

    # History cleaning to prevent context window explosion
    if len(history) > 13:
        history = [history[0]] + history[-12:]

    while True:
        user_input = TerminalUI.ask_user(session=session)
        if not user_input:
            continue

        # Intercept slash commands
        if user_input.startswith("/"):
            parts = user_input.split(" ", 1)
            cmd = parts[0].lower()
            arg = parts[1].strip() if len(parts) > 1 else ""

            if cmd in ["/sair", "/exit", "/quit"]:
                print("\033[96m[Chat] Salvando memória de diálogos. Até logo!\033[0m", flush=True)
                memory_manager.save_history(history)
                break

            elif cmd in ["/help", "/?"]:
                print("\033[95m╭─ 💡 COMANDOS DISPONÍVEIS\033[0m")
                print("\033[95m│\033[0m  \033[1m/help\033[0m ou \033[1m/?\033[0m      - Exibe esta tela de ajuda.")
                print("\033[95m│\033[0m  \033[1m/model\033[0m           - Lista os modelos locais e exibe o ativo.")
                print("\033[95m│\033[0m  \033[1m/model [ID]\033[0m      - Altera o modelo de IA ativo.")
                print("\033[95m│\033[0m  \033[1m/clear\033[0m           - Limpa todo o histórico de conversas.")
                print("\033[95m│\033[0m  \033[1m/status\033[0m          - Exibe detalhes do modelo carregado, hardware e memória.")
                print("\033[95m│\033[0m  \033[1m/vault\033[0m           - Lista todos os arquivos catalogados no vault.")
                print("\033[95m│\033[0m  \033[1m/read [nota]\033[0m     - Exibe o conteúdo de uma nota do vault diretamente.")
                print("\033[95m│\033[0m  \033[1m/search [termo]\033[0m   - Dispara imediatamente o fluxo de pesquisa e documentação web.")
                print("\033[95m│\033[0m  \033[1m/write [arq]\033[0m     - Cria/grava um arquivo de script diretamente no terminal.")
                print("\033[95m│\033[0m  \033[1m/run [cmd]\033[0m       - Executa um comando do sistema operacional (testes/compilação).")
                print("\033[95m│\033[0m  \033[1m/video [arg]\033[0m     - Automatiza corte de silêncio e insere legendas via FFmpeg.")
                print("\033[95m│\033[0m  \033[1m/sair\033[0m ou \033[1m/exit\033[0m   - Salva a memória e encerra o assistente.")
                print("\033[95m╰──────────────────────────────────────────────────────────\033[0m\n", flush=True)
                continue

            elif cmd == "/clear":
                # Clear chat history except the system prompt
                history = [history[0]]
                print("\033[92m✔ Histórico de diálogos limpo com sucesso!\033[0m\n", flush=True)
                continue

            elif cmd == "/model":
                if not arg:
                    print("\033[95m╭─ 🧠 CATÁLOGO DE MODELOS LOCAIS\033[0m")
                    for m_id, (m_name, m_hint) in AVAILABLE_MODELS.items():
                        is_active = (local_model.model_name == m_name)
                        marker = "\033[92m[Ativo] \033[0m" if is_active else "        "
                        print(f"\033[95m│\033[0m {marker}\033[1m[{m_id}]\033[0m {m_name}")
                        print(f"\033[95m│\033[0m        └─ Dica: \033[90m{m_hint}\033[0m")
                    print("\033[95m│\033[0m")
                    print("\033[95m│\033[0m Para alternar, digite: \033[1m/model <número>\033[0m")
                    print("\033[95m╰──────────────────────────────────────────────────────────\033[0m\n", flush=True)
                else:
                    if arg in AVAILABLE_MODELS:
                        new_name, new_hint = AVAILABLE_MODELS[arg]
                        changed = local_model.set_model_name(new_name)
                        if changed:
                            print(f"\033[92m✔ Modelo alterado com sucesso para:\033[0m \033[1m{new_name}\033[0m")
                            print(f"\033[93m[Aviso] O modelo será carregado na memória no próximo envio de mensagem.\033[0m\n", flush=True)
                        else:
                            print(f"\033[93m[Aviso] O modelo {new_name} já é o modelo ativo atual.\033[0m\n", flush=True)
                    else:
                        print(f"\033[91m✖ ID de modelo inválido. Digite '/model' sem parâmetros para ver as opções.\033[0m\n", flush=True)
                continue

            elif cmd == "/status":
                print("\033[95m╭─ 📊 STATUS DO SISTEMA\033[0m")
                print(f"\033[95m│\033[0m  Agente:         \033[1mBlackHole-Agent\033[0m")
                print(f"\033[95m│\033[0m  Modelo Ativo:   \033[1m{local_model.model_name}\033[0m")
                print(f"\033[95m│\033[0m  Dispositivo:    \033[1m{local_model.device.upper()}\033[0m")
                msg_count = len(history) - 1 # Desconsidera o prompt de sistema
                print(f"\033[95m│\033[0m  Mensagens:      \033[1m{max(0, msg_count)} mensagens no contexto atual\033[0m")
                mem_est = "N/A"
                if local_model.model_name == AVAILABLE_MODELS["1"][0]:
                    mem_est = "~2.3 GB RAM"
                elif local_model.model_name == AVAILABLE_MODELS["2"][0]:
                    mem_est = "~4.5 GB RAM"
                elif local_model.model_name == AVAILABLE_MODELS["3"][0]:
                    mem_est = "~3.8 GB RAM"
                print(f"\033[95m│\033[0m  Uso de RAM Est: \033[1m{mem_est}\033[0m")
                print("\033[95m╰──────────────────────────────────────────────────────────\033[0m\n", flush=True)
                continue

            elif cmd == "/vault":
                print("\033[95m[Atalho] Acessando estrutura do vault...\033[0m", flush=True)
                try:
                    concepts = os.listdir(CONCEPTS_DIR) if os.path.exists(CONCEPTS_DIR) else []
                    workflows_dir = os.path.join(VAULT_DIR, "doc", "workflows")
                    workflows = os.listdir(workflows_dir) if os.path.exists(workflows_dir) else []
                    
                    print("\033[92m╭─ Arquivos principais no Vault:\033[0m")
                    print("\033[92m│\033[0m Conceitos (doc/concepts/):")
                    concepts_md = [c for c in concepts if c.endswith(".md")]
                    for c in concepts_md[:20]:
                        print(f"\033[92m│\033[0m   - {c}")
                    if len(concepts_md) > 20:
                        print(f"\033[92m│\033[0m   ... e mais {len(concepts_md) - 20} conceitos.")
                        
                    print("\033[92m│\033[0m Workflows (doc/workflows/):")
                    workflows_md = [w for w in workflows if w.endswith(".md")]
                    for w in workflows_md:
                        print(f"\033[92m│\033[0m   - {w}")
                    print("\033[92m╰──────────────────────────────────────────────────────────\033[0m\n", flush=True)
                except Exception as e:
                    print(f"\033[91m✖ Erro ao listar arquivos do vault: {e}\033[0m\n", flush=True)
                continue

            elif cmd == "/read":
                if not arg:
                    print("\033[91m✖ Por favor, informe o nome do arquivo a ser lido. Ex: /read 00_MOC.md\033[0m\n", flush=True)
                else:
                    print(f"\033[95m[Atalho] Acessando nota do vault '{arg}'...\033[0m", flush=True)
                    content = VaultManager.read_note(arg)
                    if content:
                        print(f"\033[92m╭─ Conteúdo do arquivo '{arg}':\033[0m")
                        for line in content.splitlines()[:100]:
                            print(f"\033[92m│\033[0m {line}")
                        if len(content.splitlines()) > 100:
                            print(f"\033[92m│\033[0m ... [Exibição truncada, total de {len(content.splitlines())} linhas]")
                        print("\033[92m╰──────────────────────────────────────────────────────────\033[0m\n", flush=True)
                    else:
                        print(f"\033[91m✖ Não foi possível encontrar ou abrir a nota '{arg}' no vault.\033[0m\n", flush=True)
                continue

            elif cmd == "/search":
                if not arg:
                    print("\033[91m✖ Por favor, informe o tema de pesquisa. Ex: /search python threads\033[0m\n", flush=True)
                else:
                    success = perform_research(arg, local_model)
                    if success:
                        print(f"\033[92m✔ Pesquisa concluída com sucesso e notas geradas no vault!\033[0m\n", flush=True)
                    else:
                        print(f"\033[91m✖ Houve uma falha ao pesquisar ou criar notas para '{arg}'.\033[0m\n", flush=True)
                continue

            elif cmd == "/write":
                if not arg:
                    print("\033[91m✖ Por favor, especifique o nome do arquivo. Ex: /write teste.py\033[0m\n", flush=True)
                else:
                    file_path = os.path.join(VAULT_DIR, arg)
                    print(f"\033[95m[Arquivo] Escrevendo em '{arg}' (Digite seu código. Digite 'SALVAR' em uma linha vazia para concluir e salvar):\033[0m", flush=True)
                    lines = []
                    while True:
                        try:
                            line = input()
                            if line.strip() == "SALVAR":
                                break
                            lines.append(line)
                        except (KeyboardInterrupt, EOFError):
                            break
                    try:
                        dir_name = os.path.dirname(file_path)
                        if dir_name:
                            os.makedirs(dir_name, exist_ok=True)
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write("\n".join(lines))
                        print(f"\033[92m✔ Arquivo '{arg}' gravado com sucesso!\033[0m\n", flush=True)
                    except Exception as e:
                        print(f"\033[91m✖ Erro ao gravar arquivo: {e}\033[0m\n", flush=True)
                continue

            elif cmd == "/run":
                if not arg:
                    print("\033[91m✖ Por favor, especifique o comando a ser executado. Ex: /run python script.py\033[0m\n", flush=True)
                else:
                    print(f"\033[95m[Execução] Rodando comando: '{arg}'...\033[0m", flush=True)
                    try:
                        import threading
                        
                        def stream_reader(pipe, color):
                            for line in iter(pipe.readline, ''):
                                print(f"{color}│\033[0m {line.rstrip()}", flush=True)
                            pipe.close()

                        process = subprocess.Popen(
                            arg,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True,
                            encoding='utf-8',
                            errors='replace'
                        )
                        
                        print("\033[92m╭─ Saída do Comando (Streaming):\033[0m", flush=True)
                        
                        t_out = threading.Thread(target=stream_reader, args=(process.stdout, "\033[92m"))
                        t_err = threading.Thread(target=stream_reader, args=(process.stderr, "\033[91m"))
                        
                        t_out.start()
                        t_err.start()
                        
                        process.wait()
                        t_out.join()
                        t_err.join()
                        
                        print("\033[92m╰──────────────────────────────────────────────────────────\033[0m\n", flush=True)
                    except Exception as e:
                        print(f"\033[91m✖ Falha ao executar comando: {e}\033[0m\n", flush=True)
                continue

            elif cmd == "/video":
                if not arg:
                    print("\033[91m✖ Uso correto: /video [silences|subtitle] [args...]\033[0m")
                    print("\033[90m  - Exemplo 1: /video silences video_bruto.mp4\033[0m")
                    print("\033[90m  - Exemplo 2: /video subtitle video.mp4 'Texto da Legenda' 1.5 3.0\033[0m\n")
                else:
                    parts = arg.split(" ", 1)
                    subcmd = parts[0].lower()
                    subarg = parts[1].strip() if len(parts) > 1 else ""
                    
                    para_editar_dir = os.path.join(VAULT_DIR, "videos", "videos para editar")
                    editados_dir = os.path.join(VAULT_DIR, "videos", "videos editados")
                    os.makedirs(para_editar_dir, exist_ok=True)
                    os.makedirs(editados_dir, exist_ok=True)
                    
                    try:
                        from scripts.video_editor import cut_silences, add_subtitle
                    except ImportError:
                        import sys
                        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
                        from video_editor import cut_silences, add_subtitle

                    if subcmd == "silences":
                        if not subarg:
                            print("\033[91m✖ Especifique o nome do arquivo bruto em videos/videos para editar/. Ex: /video silences input.mp4\033[0m\n", flush=True)
                        else:
                            in_file = os.path.join(para_editar_dir, subarg)
                            out_name = os.path.splitext(subarg)[0] + "_cut" + os.path.splitext(subarg)[1]
                            out_file = os.path.join(editados_dir, out_name)
                            
                            if not os.path.exists(in_file):
                                print(f"\033[91m✖ Arquivo '{subarg}' não encontrado em '{para_editar_dir}'.\033[0m\n", flush=True)
                            else:
                                print(f"\033[95m[Video] Processando corte de silêncio de '{subarg}'...\033[0m", flush=True)
                                success = cut_silences(in_file, out_file)
                                if success:
                                    print(f"\033[92m✔ Sucesso! Vídeo editado gravado em 'videos/videos editados/{out_name}'.\033[0m\n", flush=True)
                                else:
                                    print("\033[91m✖ Falha ao cortar silêncios do vídeo.\033[0m\n", flush=True)
                                    
                    elif subcmd == "subtitle":
                        subparts = re.findall(r'(?:[^\s\"\']|\"(?:\\\\.|[^\"])*\"|\'(?:\\\\.|[^\'])*\')+', subarg)
                        if len(subparts) < 4:
                            print("\033[91m✖ Parâmetros insuficientes. Uso: /video subtitle [video.mp4] '[texto]' [inicio_seg] [duracao_seg]\033[0m\n", flush=True)
                        else:
                            video_name = subparts[0]
                            text_val = subparts[1].strip("'\"")
                            try:
                                start_val = float(subparts[2])
                                dur_val = float(subparts[3])
                            except ValueError:
                                print("\033[91m✖ Tempos de início e duração devem ser números decimais.\033[0m\n", flush=True)
                                continue
                                
                            in_file = os.path.join(para_editar_dir, video_name)
                            if not os.path.exists(in_file):
                                in_file = os.path.join(editados_dir, video_name)
                                
                            if not os.path.exists(in_file):
                                print(f"\033[91m✖ Vídeo '{video_name}' não encontrado nas pastas do vault.\033[0m\n", flush=True)
                            else:
                                out_name = os.path.splitext(video_name)[0] + "_subed" + os.path.splitext(video_name)[1]
                                out_file = os.path.join(editados_dir, out_name)
                                
                                print(f"\033[95m[Video] Adicionando legenda a '{video_name}'...\033[0m", flush=True)
                                success = add_subtitle(in_file, out_file, text_val, start_val, dur_val)
                                if success:
                                    print(f"\033[92m✔ Sucesso! Vídeo legendado gravado em 'videos/videos editados/{out_name}'.\033[0m\n", flush=True)
                                else:
                                    print("\033[91m✖ Falha ao legendar vídeo.\033[0m\n", flush=True)
                    else:
                        print(f"\033[91m✖ Subcomando '/video {subcmd}' não reconhecido. Use '/video' sem argumentos para ajuda.\033[0m\n", flush=True)
                continue

            else:
                print(f"\033[91m✖ Comando '{cmd}' não reconhecido. Digite /help para ver a lista de comandos.\033[0m\n", flush=True)
                continue

        # Fluxo de conversa padrão
        if user_input.lower() in ["sair", "exit", "quit"]:
            print("\033[96m[Chat] Salvando memória de diálogos. Até logo!\033[0m", flush=True)
            memory_manager.save_history(history)
            break

        # RAG / Context Injection: when the user asks about the vault content/readmes,
        # prepare the vault file list as a temporary system grounding block to help the model prevent safety refusals.
        input_lower = user_input.lower()
        vault_files_context = None
        if any(keyword in input_lower for keyword in ["vault", "readme", "moc", "arquivo", "nota", "listar", "pasta"]):
            try:
                concepts = os.listdir(CONCEPTS_DIR) if os.path.exists(CONCEPTS_DIR) else []
                concepts_md = [c for c in concepts if c.endswith(".md")]
                
                workflows_dir = os.path.join(VAULT_DIR, "doc", "workflows")
                workflows = os.listdir(workflows_dir) if os.path.exists(workflows_dir) else []
                workflows_md = [w for w in workflows if w.endswith(".md")]
                
                vault_files_context = (
                    "Contexto de Arquivos Locais do Vault (Injeção de Sistema):\n"
                    "Esta é a lista real de arquivos de notas markdown (.md) disponíveis no vault do Obsidian do usuário:\n"
                    f"- Conceitos (doc/concepts/): {', '.join(concepts_md[:30])}\n"
                    f"- Workflows (doc/workflows/): {', '.join(workflows_md)}\n"
                    "DICA DE CONTEXTO: Use essas informações para responder diretamente ou invocar a ação [LER_NOTA: nome_da_nota.md] se o usuário pedir para ver o conteúdo de alguma nota específica. Não afirme que não tem acesso a arquivos locais, pois você tem."
                )
            except Exception:
                pass

        history.append({"role": "user", "content": user_input})

        consecutive_tool_calls = 0
        while consecutive_tool_calls < 3:
            # Prepare messages with temporary context inserted right before the user's latest query
            messages_to_send = list(history)
            if vault_files_context:
                messages_to_send.insert(-1, {"role": "system", "content": vault_files_context})

            spinner = Spinner("BlackHole-Agent está processando...")
            spinner.start()
            
            response = local_model.generate(messages_to_send)
            spinner.stop()

            if not response:
                TerminalUI.print_ai_box("Desculpe, ocorreu um erro na geração da resposta do modelo local.")
                break

            response = response.strip()

            # Check for tool call using advanced fuzzy normalization
            tool_data = detect_and_normalize_tool_call(response)
            if tool_data:
                tool_name, tool_arg = tool_data
                approved = TerminalUI.ask_approval(tool_name, tool_arg)
                
                observation = ""
                if approved:
                    if tool_name == "PESQUISAR_TEMA":
                        print(f"\033[95m[Ação] Iniciando fluxo de pesquisa para '{tool_arg}'...\033[0m", flush=True)
                        success = perform_research(tool_arg, local_model)
                        if success:
                            observation = f"Sucesso: O tema '{tool_arg}' foi pesquisado com sucesso na web. A nota conceitual e a nota de cache foram criadas sob doc/concepts/ e doc/external_cache/ respectivamente, e o MOC foi devidamente atualizado."
                        else:
                            observation = f"Erro: Houve uma falha interna ao pesquisar e compilar o tema '{tool_arg}'."
                    elif tool_name == "LER_NOTA":
                        print(f"\033[95m[Ação] Acessando nota do vault '{tool_arg}'...\033[0m", flush=True)
                        content = VaultManager.read_note(tool_arg)
                        if content:
                            observation = f"Conteúdo do arquivo '{tool_arg}':\n\n{content}"
                        else:
                            observation = f"Erro: Não foi possível encontrar ou abrir a nota '{tool_arg}' no vault."
                    elif tool_name == "LISTAR_VAULT":
                        print(f"\033[95m[Ação] Acessando estrutura do vault...\033[0m", flush=True)
                        try:
                            concepts = os.listdir(CONCEPTS_DIR) if os.path.exists(CONCEPTS_DIR) else []
                            workflows_dir = os.path.join(VAULT_DIR, "doc", "workflows")
                            workflows = os.listdir(workflows_dir) if os.path.exists(workflows_dir) else []
                            
                            observation = "Arquivos principais no Vault:\n\n"
                            observation += "Conceitos (doc/concepts/):\n"
                            concepts_md = [c for c in concepts if c.endswith(".md")]
                            for c in concepts_md[:40]:
                                observation += f"- {c}\n"
                            if len(concepts_md) > 40:
                                observation += f"... e mais {len(concepts_md) - 40} conceitos.\n"
                                
                            observation += "\nWorkflows (doc/workflows/):\n"
                            workflows_md = [w for w in workflows if w.endswith(".md")]
                            for w in workflows_md:
                                observation += f"- {w}\n"
                        except Exception as e:
                            observation = f"Erro ao listar arquivos do vault: {e}"
                else:
                    print("\033[91m[Ação] Ação recusada pelo usuário.\033[0m", flush=True)
                    observation = "Erro: O usuário recusou a execução desta ação. Responda ao usuário informando que a ação foi recusada e pergunte como proceder ou use seu próprio conhecimento de pesos."

                history.append({"role": "assistant", "content": response})
                history.append({"role": "user", "content": f"Observação da Ferramenta: {observation}"})
                consecutive_tool_calls += 1
            else:
                TerminalUI.print_ai_box(response)
                history.append({"role": "assistant", "content": response})
                memory_manager.save_history(history)
                break
        else:
            print("\n\033[93m[Aviso] Limite de chamadas consecutivas de ferramentas atingido.\033[0m", flush=True)
            break

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--chat":
            run_chat_loop()
        else:
            query = sys.argv[1]
            local_model = LocalModel()
            perform_research(query, local_model)
    else:
        run_chat_loop()

if __name__ == "__main__":
    main()
