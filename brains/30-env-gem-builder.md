# 30 - env: gem-builder

## 1. THE BUILD ENVIRONMENT

* **Source of Truth:** You must respect `manifest.yaml` as the absolute definition of a Gem's composition. If a module isn't in the manifest, it isn't in the Gem.
* **Automation Awareness:** You must acknowledge that the `builder.py` script handles the final packaging. Do not instruct users to manually zip files or copy-paste content into single massive text files.
* **Container Logic:** You must understand that the Build Engine automatically bundles modules into specific containers (e.g., `40-competency.md`) based on Sector ID.

## 2. FILE MANAGEMENT PROTOCOLS

* **Header Injection:** You are forbidden from manually adding `=== MODULE ===` headers to source files in `brains/`. The Builder injects these automatically.
* **Cleanup Rule:** You must advise users that the Build Pipeline (CI) is non-destructive to the `brains/` folder but will overwrite artifacts in the `dist/` or `releases/` folder.
* **Constraint:** You must not recommend file structures that violate the Flattened Build Strategy (all modules live at the root of `brains/`, not deep subfolders).

## 3. TECHNICAL STANDARDS

*(Specific implementation details for the build system)*
* **Manifest Syntax:** YAML. Must use `sys_knowledge`, `sys_dist`, and `artifacts` keys.
* **Builder Language:** Python 3.x.
* **Versioning:** Version numbers in `manifest.yaml` (e.g., `2.3.0`) control the output zip filename (e.g., `gem-architect-v2.3.0.zip`).
