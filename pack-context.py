import os
import re
import datetime

# --- CONFIGURATION ---
# Dynamically name the file: 998-context-[folder_name].md
current_folder = os.path.basename(os.getcwd())
safe_project_name = re.sub(r'[^a-z0-9]', '-', current_folder.lower())
OUTPUT_FILENAME = f"998-context-{safe_project_name}.md"

# Extensions to include in the snapshot
ALLOWED_EXTENSIONS = {'.cs', '.razor', '.css', '.js', '.json', '.sql', '.md', '.py', '.yml'}

# Directories to STRICTLY IGNORE
# We ignore 'gem-brains' so we don't accidentally feed instructions back into the context
IGNORE_DIRS = {
    'bin', 'obj', '.git', '.github', '.vs', '.vscode', 'node_modules',
    'gem-brains', 'releases', 'context', '__pycache__'
}

# Files to ignore
IGNORE_FILES = {
    OUTPUT_FILENAME, 'pack_context.py', 'package-lock.json', '.DS_Store', 'README.md'
}

def generate_markdown_snapshot():
    project_root = os.getcwd()
    output_path = os.path.join(project_root, OUTPUT_FILENAME)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"📦 Packing context for project: {safe_project_name}")

    with open(output_path, 'w', encoding='utf-8') as outfile:
        # Century Protocol Header (High Priority Override)
        outfile.write(f"# {OUTPUT_FILENAME}\n")
        outfile.write(f"**Generated:** {timestamp}\n\n")
        outfile.write(f"## 1. Project Context: {safe_project_name}\n")
        outfile.write("This file contains the active source code snapshot. "
                      "It overrides general technical instructions with specific project logic.\n\n")

        # Walk the directory
        for root, dirs, files in os.walk(project_root):
            # Modify dirs in-place to skip ignored directories
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

            for file in files:
                if file in IGNORE_FILES: continue

                _, ext = os.path.splitext(file)
                if ext.lower() not in ALLOWED_EXTENSIONS: continue

                # Relative path calculation
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, project_root)

                print(f"  + {rel_path}")

                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        outfile.write(f"### File: `{rel_path}`\n")
                        outfile.write(f"```{ext.replace('.', '')}\n")
                        outfile.write(content)
                        outfile.write("\n```\n\n")
                        outfile.write("---\n")
                except Exception as e:
                    print(f"  ! Error reading {rel_path}: {e}")

    print(f"\n✅ Generated: {OUTPUT_FILENAME}")

if __name__ == "__main__":
    generate_markdown_snapshot()
