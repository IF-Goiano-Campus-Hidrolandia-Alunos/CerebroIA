import os
import re
import shutil

vault_root = r"c:\Users\thyag\OneDrive\Desktop\Brain-main"
doc_dir = os.path.join(vault_root, "doc")

# Define target dirs
rules_dir = os.path.join(doc_dir, "00_rules")
rules_templates_dir = os.path.join(rules_dir, "templates")
projects_dir = os.path.join(doc_dir, "10_projects")
workflows_dir = os.path.join(doc_dir, "20_workflows")
libraries_dir = os.path.join(doc_dir, "30_libraries")
external_cache_dir = os.path.join(doc_dir, "40_external_cache")

# Specific authors
thyago_projects_dir = os.path.join(projects_dir, "ThyagoToledo")
feron_projects_dir = os.path.join(projects_dir, "FeronZerbana")
shared_projects_dir = os.path.join(projects_dir, "shared")

# Subdirectories for libraries
agronomy_dir = os.path.join(libraries_dir, "agronomy")
ai_agents_dir = os.path.join(libraries_dir, "ai_agents")
dotnet_arch_dir = os.path.join(libraries_dir, "dotnet_arch")
libraries_general_dir = os.path.join(libraries_dir, "general")

def create_dirs():
    dirs = [
        rules_dir, rules_templates_dir,
        projects_dir, thyago_projects_dir, feron_projects_dir, shared_projects_dir,
        os.path.join(thyago_projects_dir, "ignisengine", "00_spec"),
        os.path.join(thyago_projects_dir, "ignisengine", "01_plan"),
        os.path.join(thyago_projects_dir, "ignisengine", "02_tasks"),
        os.path.join(thyago_projects_dir, "ignisengine", "03_context"),
        os.path.join(thyago_projects_dir, "plantiumai", "00_spec"),
        os.path.join(thyago_projects_dir, "plantiumai", "01_plan"),
        os.path.join(thyago_projects_dir, "plantiumai", "02_tasks"),
        os.path.join(thyago_projects_dir, "plantiumai", "03_context"),
        os.path.join(thyago_projects_dir, "blackhole", "00_spec"),
        os.path.join(thyago_projects_dir, "blackhole", "01_plan"),
        os.path.join(thyago_projects_dir, "blackhole", "02_tasks"),
        os.path.join(thyago_projects_dir, "blackhole", "03_context"),
        os.path.join(thyago_projects_dir, "penetrometro", "03_context"),
        os.path.join(thyago_projects_dir, "general"),
        workflows_dir,
        libraries_dir, agronomy_dir, ai_agents_dir, dotnet_arch_dir, libraries_general_dir,
        external_cache_dir
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)

def map_concept_file(filename):
    lower_name = filename.lower()
    
    # 1. Rules
    if (lower_name.startswith("regra") or 
        lower_name.startswith("template-") or 
        lower_name.startswith("vault-") or 
        lower_name == "readme-structure-template.md"):
        return os.path.join("00_rules", filename)
        
    # 2. Projects (ThyagoToledo owns the current ones)
    if "ignisengine" in lower_name:
        if "roadmap" in lower_name or "decisoes" in lower_name:
            return os.path.join("10_projects", "ThyagoToledo", "ignisengine", "00_spec", filename)
        elif "auditoria" in lower_name or "dividas" in lower_name or "inventario" in lower_name:
            return os.path.join("10_projects", "ThyagoToledo", "ignisengine", "03_context", filename)
        else:
            return os.path.join("10_projects", "ThyagoToledo", "ignisengine", "03_context", filename)
            
    if "plantiumai" in lower_name or "reset-senha" in lower_name:
        if "especificacao" in lower_name:
            return os.path.join("10_projects", "ThyagoToledo", "plantiumai", "00_spec", filename)
        else:
            return os.path.join("10_projects", "ThyagoToledo", "plantiumai", "03_context", filename)
            
    if "blackhole" in lower_name:
        return os.path.join("10_projects", "ThyagoToledo", "blackhole", "03_context", filename)
        
    if "penetrometro" in lower_name:
        return os.path.join("10_projects", "ThyagoToledo", "penetrometro", "03_context", filename)
        
    if any(x in lower_name for x in ["sistema-legado", "desafio-ia", "plataforma-web", "novo-sistema", "desktop-app"]):
        return os.path.join("10_projects", "ThyagoToledo", "general", filename)
        
    # 3. Libraries / Concepts
    if lower_name.startswith("agronomy-"):
        return os.path.join("30_libraries", "agronomy", filename)
        
    if lower_name.startswith("ai-") or lower_name.startswith("agent-") or "agent" in lower_name:
        return os.path.join("30_libraries", "ai_agents", filename)
        
    if (lower_name.startswith("dotnet-") or 
        lower_name.startswith("asp-net-") or 
        "dotnet" in lower_name or 
        "csharp" in lower_name or 
        "dataview" in lower_name or 
        "organizacao-para" in lower_name):
        return os.path.join("30_libraries", "dotnet_arch", filename)
        
    return os.path.join("30_libraries", "general", filename)

def main(dry_run=True):
    print(f"Iniciando reorganizacao. Dry-run = {dry_run}")
    
    if not dry_run:
        create_dirs()
        
    # Dict to map old wiki paths to new ones (relative to 'doc')
    # e.g., 'concepts/agronomy-foo' -> '30_libraries/agronomy/agronomy-foo'
    path_mapping = {}
    
    # 1. Map concepts
    concepts_src = os.path.join(doc_dir, "concepts")
    if os.path.exists(concepts_src):
        for f in os.listdir(concepts_src):
            if f.endswith(".md"):
                rel_dest = map_concept_file(f)
                old_rel = f"concepts/{os.path.splitext(f)[0]}"
                new_rel = rel_dest.replace("\\", "/").replace(".md", "")
                path_mapping[old_rel] = new_rel
                
    # 2. Map workflows
    workflows_src = os.path.join(doc_dir, "workflows")
    if os.path.exists(workflows_src):
        for f in os.listdir(workflows_src):
            if f.endswith(".md"):
                old_rel = f"workflows/{os.path.splitext(f)[0]}"
                new_rel = f"20_workflows/{os.path.splitext(f)[0]}"
                path_mapping[old_rel] = new_rel
                
    # 3. Map external cache
    cache_src = os.path.join(doc_dir, "external_cache")
    if os.path.exists(cache_src):
        for f in os.listdir(cache_src):
            if f.endswith(".md"):
                old_rel = f"external_cache/{os.path.splitext(f)[0]}"
                new_rel = f"40_external_cache/{os.path.splitext(f)[0]}"
                path_mapping[old_rel] = new_rel
                
    # 4. Map templates in root doc/
    for f in os.listdir(doc_dir):
        if f.startswith("TEMPLATE_") and f.endswith(".md"):
            old_rel = os.path.splitext(f)[0]
            new_rel = f"00_rules/templates/{os.path.splitext(f)[0]}"
            path_mapping[old_rel] = new_rel

    print(f"Mapeados {len(path_mapping)} arquivos para movimentacao.")
    
    # Perform moves
    files_moved = 0
    
    # Move concepts
    if os.path.exists(concepts_src):
        for f in os.listdir(concepts_src):
            if f.endswith(".md"):
                src_path = os.path.join(concepts_src, f)
                rel_dest = map_concept_file(f)
                dest_path = os.path.join(doc_dir, rel_dest)
                if dry_run:
                    # Print first few maps for validation
                    if files_moved < 10:
                        print(f"[DRY-RUN] Move: {src_path} -> {dest_path}")
                else:
                    shutil.move(src_path, dest_path)
                files_moved += 1
                
    # Move workflows
    if os.path.exists(workflows_src):
        for f in os.listdir(workflows_src):
            if f.endswith(".md"):
                src_path = os.path.join(workflows_src, f)
                dest_path = os.path.join(workflows_dir, f)
                if dry_run:
                    if files_moved < 20:
                        print(f"[DRY-RUN] Move: {src_path} -> {dest_path}")
                else:
                    shutil.move(src_path, dest_path)
                files_moved += 1
                
    # Move external cache
    if os.path.exists(cache_src):
        for f in os.listdir(cache_src):
            if f.endswith(".md"):
                src_path = os.path.join(cache_src, f)
                dest_path = os.path.join(external_cache_dir, f)
                if dry_run:
                    if files_moved < 30:
                        print(f"[DRY-RUN] Move: {src_path} -> {dest_path}")
                else:
                    shutil.move(src_path, dest_path)
                files_moved += 1
                
    # Move templates in root doc/
    for f in os.listdir(doc_dir):
        if f.startswith("TEMPLATE_") and f.endswith(".md"):
            src_path = os.path.join(doc_dir, f)
            dest_path = os.path.join(rules_templates_dir, f)
            if dry_run:
                print(f"[DRY-RUN] Move root template: {src_path} -> {dest_path}")
            else:
                shutil.move(src_path, dest_path)
            files_moved += 1

    print(f"Total de arquivos movidos/simulados: {files_moved}")
    
    # Rewrite links in all .md files under doc/ (recursively)
    print("Atualizando wikilinks nos arquivos...")
    links_updated = 0
    
    # Helper to rewrite content
    def rewrite_links_in_file(file_path):
        nonlocal links_updated
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
        except UnicodeDecodeError:
            try:
                with open(file_path, "r", encoding="latin-1") as file:
                    content = file.read()
            except Exception as e:
                print(f"Erro ao ler {file_path}: {e}")
                return
        except Exception as e:
            print(f"Erro ao ler {file_path}: {e}")
            return
            
        original_content = content
        
        # Sort keys by length descending to prevent partial matches
        sorted_keys = sorted(path_mapping.keys(), key=len, reverse=True)
        
        for old_path in sorted_keys:
            new_path = path_mapping[old_path]
            content = content.replace(f"[[{old_path}]]", f"[[{new_path}]]")
            content = content.replace(f"[[{old_path}|", f"[[{new_path}|")
            content = content.replace(f"[[{old_path}#", f"[[{new_path}#")
            
        if content != original_content:
            links_updated += 1
            if dry_run:
                if links_updated < 15:
                    print(f"[DRY-RUN] Modificaria links em: {file_path}")
            else:
                try:
                    with open(file_path, "w", encoding="utf-8") as file:
                        file.write(content)
                except Exception as e:
                    print(f"Erro ao escrever {file_path}: {e}")

    # Walk through the doc directory
    for root, dirs, files in os.walk(doc_dir):
        if ".obsidian" in root or ".git" in root:
            continue
        for f in files:
            if f.endswith(".md"):
                file_path = os.path.join(root, f)
                rewrite_links_in_file(file_path)
                
    print(f"Total de arquivos com links atualizados/simulados: {links_updated}")
    
    # Cleanup empty source folders if not dry run
    if not dry_run:
        for folder in [concepts_src, workflows_src, cache_src]:
            if os.path.exists(folder) and not os.listdir(folder):
                os.rmdir(folder)
                print(f"Removido diretorio vazio: {folder}")

if __name__ == "__main__":
    # Import sys to allow command line argument to toggle dry run
    import sys
    dry_run = True
    if len(sys.argv) > 1 and sys.argv[1].lower() == "false":
        dry_run = False
    main(dry_run=dry_run)
