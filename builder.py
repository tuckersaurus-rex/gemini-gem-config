import os
import yaml # pip install pyyaml
import shutil
import re
import zipfile

# ==========================================
# CONFIGURATION
# ==========================================
MANIFEST_FILE = "manifest.yaml"

# Sector Bundling Logic
BUNDLE_MAP = [
    {"range": (0, 19),  "output": "00-system.md"},     # Kernel + Core
    {"range": (20, 39), "output": "20-persona.md"},    # Role + Env
    {"range": (40, 89), "output": "40-competency.md"}, # Skill, Fwk, UI, Lib, Custom
    {"range": (90, 99), "output": "90-project.md"}     # Project Context
]

def load_manifest():
    if not os.path.exists(MANIFEST_FILE):
        raise FileNotFoundError(f"Manifest file not found: {MANIFEST_FILE}")
    with open(MANIFEST_FILE, 'r') as f:
        return yaml.safe_load(f)

def get_sector_id(filename):
    match = re.match(r"^(\d{2})-", filename)
    return int(match.group(1)) if match else None

def generate_header(filename):
    module_name = os.path.splitext(filename)[0]
    return f"\n\n=== MODULE: {module_name} ===\n\n"

def clean_dist(dist_path):
    if os.path.exists(dist_path):
        shutil.rmtree(dist_path)
    os.makedirs(dist_path)

def build_artifact(artifact, config):
    name = artifact.get('name')
    gem_id = artifact.get('id')
    version = artifact.get('version')
    description = artifact.get('description')
    modules = artifact.get('modules', [])
    context_files = artifact.get('context', [])

    print(f"🔨 Building: {name} ({gem_id})")

    # 1. Create Artifact Directory
    artifact_dir = os.path.join(config['dist'], gem_id)
    os.makedirs(artifact_dir)

    # 2. GENERATE MARKDOWN BUNDLES
    modules.sort()
    bundle_content = {b["output"]: [] for b in BUNDLE_MAP}
    generated_files = [] # Track files to zip

    for module_file in modules:
        full_path = os.path.join(config['knowledge'], module_file)

        if not os.path.exists(full_path):
            print(f"::error:: Missing module: {full_path}")
            continue

        sector = get_sector_id(module_file)

        # Read & Format
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        formatted_block = generate_header(module_file) + content

        # Assign to Bundle
        assigned = False
        if sector is not None:
            for bundle in BUNDLE_MAP:
                start, end = bundle["range"]
                if start <= sector <= end:
                    bundle_content[bundle["output"]].append(formatted_block)
                    assigned = True
                    break

        if not assigned:
            print(f"::warning:: Unassigned sector for {module_file}, appending to 40-competency.")
            bundle_content["40-competency.md"].append(formatted_block)

    # Write Bundle Files to Disk
    for filename, blocks in bundle_content.items():
        if blocks:
            out_path = os.path.join(artifact_dir, filename)
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write("".join(blocks))
            generated_files.append(filename)
            print(f"   -> Generated {filename}")

    # 3. CREATE ZIP FILE (Containing ONLY bundles)
    zip_name = f"{gem_id}-v{version}.zip"
    zip_path = os.path.join(artifact_dir, zip_name)

    print(f"   📦 Zipping {len(generated_files)} files into {zip_name}...")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in generated_files:
            file_path = os.path.join(artifact_dir, file)
            zipf.write(file_path, arcname=file) # Add to root of zip

    # 4. CLEANUP (Delete the raw markdown files, keep only the zip)
    for file in generated_files:
        os.remove(os.path.join(artifact_dir, file))

    # 5. GENERATE README.md (External Documentation)
    # This now replaces info.txt
    readme_path = os.path.join(artifact_dir, "README.md")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(f"# {name}\n\n")
        f.write(f"**Version:** {version}\n")
        f.write(f"**ID:** {gem_id}\n\n")
        f.write("## Description\n")
        f.write(f"{description}\n")
        f.write("\n## Installation\n")
        f.write(f"1. Upload `{zip_name}` to the Gemini Knowledge base.\n")
        f.write(f"2. Copy the **Name** and **Description** above into the Gem settings.\n")
        f.write(f"3. Paste the System Instructions (Bootloader) into the prompt.\n")
    print("   -> Created README.md")

    # 6. COPY CONTEXT FILES (External - Outside Zip)
    if context_files:
        for ctx_file in context_files:
            src = os.path.join(config['context'], ctx_file)
            filename = os.path.basename(ctx_file)
            dst = os.path.join(artifact_dir, filename)

            if os.path.exists(src):
                shutil.copy(src, dst)
                print(f"   -> Added Context: {filename}")
            else:
                print(f"::warning:: Missing context file: {src}")

def main():
    manifest = load_manifest()

    # Helper to safely get string values, defaulting if key is missing OR value is None
    def get_config(key, default):
        val = manifest.get(key)
        return val if val is not None else default

    config = {
        'kernel': get_config('sys_kernel', 'system-instructions.md'),
        'knowledge': get_config('sys_knowledge', 'brains/').rstrip('/'),
        'context': get_config('sys_context', 'context/').rstrip('/'),
        'dist': get_config('sys_dist', 'releases/').rstrip('/')
    }

    clean_dist(config['dist'])

    if os.path.exists(config['kernel']):
        shutil.copy(config['kernel'], os.path.join(config['dist'], "system-instructions.md"))
        print(f"📄 Global Bootloader copied to {config['dist']}/system-instructions.md")

    if 'artifacts' in manifest:
        for artifact in manifest['artifacts']:
            build_artifact(artifact, config)

if __name__ == "__main__":
    main()
