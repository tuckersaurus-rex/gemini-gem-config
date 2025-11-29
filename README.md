# Gemini Gem Configuration

## Overview

This repository manages the source code for Gemini Gem "Knowledge Files." It utilizes a modular architecture known as the **Century Protocol**, which enforces a strict 3-digit numeric hierarchy to manage instruction priority.

## The Century Protocol Structure

- **000-099 (Core):** Kernel instructions and safety protocols.
- **100-199 (Role):** Persona definitions (e.g., Architect, Developer).
- **200-299 (Standards):** Operational standards (e.g., Module writing rules).
- **300-899 (Tech):** Hard skills and frameworks (C#, Blazor, Python).
- **900-999 (Project):** Business logic and specific project constraints.

## Usage

All files are maintained in **Kebab-Case** and intended to be uploaded directly to the "Knowledge" section of a Gemini Gem.

## 🏗️ How to Prompt the Architect

When requesting a new Gem configuration from the **Gem Architect**, use the following template to ensure it correctly maps requirements to the 000-999 file structure:

> **I require a new Gem configuration for the following scenario:**
>
> **1. Role (The "Who"):** > [e.g., Senior C# Backend Developer, Technical Writer, SEO Specialist]
>
> **2. Project Context (The "Goal"):** > [Describe the specific project, business goal, or application being built. e.g., "A Blazor Web App for inventory management."]
>
> **3. Tech Stack & Skills (The "What"):** > [List all languages, frameworks, and tools. e.g., .NET 8, EF Core, Docker, Azure DevOps.]
>
> **4. Constraints & Standards:** > [List any specific rules. e.g., "Must use Kebab-Case for files," "Use clean architecture," "No external libraries."]

**Note:** The Architect will automatically check the `999-architect-library-manifest` and reuse existing modules where possible.

## 🚀 Creating & Updating Gems

### Step 1: Build the "Brain" (The OS)

The "Brain" defines _how_ the Gem thinks (Roles, Standards). It rarely changes.

1.  Navigate to the `/gem-brains` folder.
2.  Select the modules you need (Always include `000` and `200`).
3.  **Zip the files.**
    - **Naming Convention:** `gem-brain-[version]-[date].zip`
    - _Example:_ `gem-brain-v1.2-2025-11-28.zip`
4.  Move this Zip file to the `/releases` folder for safekeeping.
5.  **Upload** this Zip to the Gem's "Knowledge" section.

### Step 2: Build the "Context" (The Project Data)

The "Context" defines _what_ the Gem knows (Source Code, Library Manifests). It changes constantly.

1.  **For the Architect Gem:**
    - Edit `/context/999-architect-library-manifest.md`.
    - Upload directly to the Gem (replace the old one).
2.  **For Project Gems:**
    - Run `python pack_context.py` in your project root.
    - This generates `998-context-[project-name].md`.
    - Upload directly to the Gem (replace the old one).

## 🏗️ Contribution Guidelines

1.  **Strict Naming:** All files in `/gem-brains` MUST follow `[000-899]-[category]-[name].md`.
2.  **Kebab-Case:** No spaces or underscores allowed in filenames.
3.  **CI/CD:** The GitHub Action `Century Protocol QA` will block any PR that violates these rules.

## 🔄 Contribution Workflow

This repository follows a strict **Feature Branch** workflow. Direct commits to `main` are discouraged.

1.  **Sync:** Ensure your local main is up to date (`git checkout main && git pull`).
2.  **Branch:** Create a feature branch (`git checkout -b feature/new-module-name`).
3.  **Work:** Add your new `.md` knowledge files.
4.  **Commit:** Stage and commit your changes.
5.  **Push:** Push the branch to GitHub (`git push -u origin feature/new-module-name`).
6.  **PR:** Open a Pull Request on GitHub to merge into `main`.

## 📂 Repository Structure

This repository utilizes the **Two-Slot Architecture** to separate static instructions from dynamic project data.

| Directory         | Purpose                                                            | Protocol                                                    |
| :---------------- | :----------------------------------------------------------------- | :---------------------------------------------------------- |
| **`/gem-brains`** | **Slot 1: The OS.** Contains logic, roles, and formatting rules.   | **Strict.** Enforced by CI/CD. Files must be `000-899`.     |
| **`/context`**    | **Slot 2: The Data.** Contains manifests and snapshots.            | **Flexible.** Contains `999` manifests and `998` snapshots. |
| **`/releases`**   | Archived Zip files of the "Brain" logic.                           | N/A                                                         |
| **Root**          | Contains the `pack_context.py` script and `system-kernel.md` file. | N/A                                                         |
