import os
import re
import datetime
import sys

# --- CONFIGURATION (Common Ignores) ---

# Directories to STRICTLY IGNORE (These are universal for Git/Build Systems)
IGNORE_DIRS = {
    'bin', 'obj', '.git', '.github', '.vs', '.vscode', 'node_modules',
    'releases', 'context', 'brains', '__pycache__', 'TestResults',
}

# Files to ignore
IGNORE_FILES = {
    'package-lock.json', '.DS_Store', 'README.md', 'changelog.md',
    'license.txt', '.gitignore', '.gitkeep', 'pack_context.py' # Added self-reference
}

# Extensions to include (Add/Remove as needed)
ALLOWED_EXTENSIONS = {'.cs', '.razor', '.css', '.js', '.json', '.sql', '.md', '.py', '.yml'}


def generate_markdown_snapshot(project_root, output_filename):
    """Generates a single Markdown file containing all relevant source code."""

    output_path = os.path.join(os.getcwd(), output_filename)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if os.path.abspath(output_path) == os.path.abspath(project_root):
        print("Error: Output file path matches project root. Aborting.")
        sys.exit(1)

    print(f"📦 Packing context from: {project_root}")
    print(f"➡️ Output file: {output_filename}")

    with open(output_path, 'w', encoding='utf-8') as outfile:
        # Century Protocol Header
        outfile.write(f"# {output_filename}\n")
        outfile.write(f"**Generated:** {timestamp}\n\n")
        outfile.write("## 1. Static Library Context\n")
        outfile.write("This file contains the stable source code for a shared library. Treat this as foundational logic.\n\n")

        for root, dirs, files in os.walk(project_root):
            dirs[:] = [d for d in dirs if d.lower() not in IGNORE_DIRS]

            for file in files:
                if file.lower() in IGNORE_FILES: continue

                _, ext = os.path.splitext(file)
                if ext.lower() not in ALLOWED_EXTENSIONS: continue

                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, project_root)

                print(f"  + Packing: {rel_path}")

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

    print(f"\n✅ Success! Context packed into: {output_filename}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python pack_context.py <path_to_library_root> <output_filename.md>")
        print("Example: python pack_context.py ../SharedComponents 800-lib-shared-components.md")
        sys.exit(1)

    project_root = sys.argv[1]
    output_filename = sys.argv[2]

    generate_markdown_snapshot(project_root, output_filename)
