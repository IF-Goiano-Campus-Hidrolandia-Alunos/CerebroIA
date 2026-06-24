import os

vault_root = r"c:\Users\thyag\OneDrive\Desktop\Brain-main"
doc_dir = os.path.join(vault_root, "doc")

projects_dir = os.path.join(doc_dir, "10_projects")

old_thyago_path = os.path.join(projects_dir, "ThyagoToledo")
new_thyago_path = os.path.join(projects_dir, "Colaborador1")

old_feron_path = os.path.join(projects_dir, "FeronZerbana")
new_feron_path = os.path.join(projects_dir, "Colaborador2")

def rename_folders():
    # Rename ThyagoToledo folder if it exists
    if os.path.exists(old_thyago_path):
        os.rename(old_thyago_path, new_thyago_path)
        print(f"Renomeado: {old_thyago_path} -> {new_thyago_path}")
        
    # Rename FeronZerbana folder if it exists
    if os.path.exists(old_feron_path):
        os.rename(old_feron_path, new_feron_path)
        print(f"Renomeado: {old_feron_path} -> {new_feron_path}")

def sanitize_content(dry_run=True):
    print(f"Higienizando Vault... Dry-run = {dry_run}")
    
    replacements = {
        "Thyago Toledo": "Colaborador 1",
        "Feron Zerbana": "Colaborador 2",
        "ThyagoToledo": "Colaborador1",
        "FeronZerbana": "Colaborador2",
        "thyago10a2007@gmail.com": "colaborador1@email.com",
        "ddrive221@gmail.com": "colaborador2@email.com",
        "perfil-thyago": "perfil-colaborador1",
        "perfil-feron": "perfil-colaborador2",
        "commit-perfil-thyago": "commit-perfil-colaborador1",
        "thyago": "colaborador1",
        "feron": "colaborador2",
        "Thyago": "Colaborador1",
        "Feron": "Colaborador2"
    }
    
    files_modified = 0
    
    for root, dirs, files in os.walk(doc_dir):
        if ".obsidian" in root or ".git" in root:
            continue
        for f in files:
            if f.endswith(".md"):
                file_path = os.path.join(root, f)
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        content = file.read()
                except UnicodeDecodeError:
                    try:
                        with open(file_path, "r", encoding="latin-1") as file:
                            content = file.read()
                    except Exception as e:
                        print(f"Erro ao ler {file_path}: {e}")
                        continue
                except Exception as e:
                    print(f"Erro ao ler {file_path}: {e}")
                    continue
                
                original_content = content
                for old_val, new_val in replacements.items():
                    content = content.replace(old_val, new_val)
                    
                if content != original_content:
                    files_modified += 1
                    if dry_run:
                        if files_modified < 15:
                            print(f"[DRY-RUN] Modificaria arquivo: {file_path}")
                    else:
                        try:
                            with open(file_path, "w", encoding="utf-8") as file:
                                file.write(content)
                        except Exception as e:
                            print(f"Erro ao salvar {file_path}: {e}")
                            
    print(f"Total de arquivos que contem termos higienizados: {files_modified}")

if __name__ == "__main__":
    import sys
    dry_run = True
    if len(sys.argv) > 1 and sys.argv[1].lower() == "false":
        dry_run = False
        
    if not dry_run:
        rename_folders()
        
    sanitize_content(dry_run=dry_run)
