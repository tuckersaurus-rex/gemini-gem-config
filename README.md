# Gemini Gem Factory

## 1. Overview

This repository serves as a **Continuous Integration (CI) Pipeline** for generating modular System Instructions ("Gem Artifacts") for Google Gemini using the **Decimal Patch Protocol v3.0**.

## 2. Usage Guide

### C. How to Install a Gem (User Perspective)

Once the build completes, navigate to the **Releases** folder in Google Drive.

1.  **System Instructions:**
    * Open `system-instructions.md` in the root of the releases folder.
    * Copy/Paste into the **System Instructions** field in Gemini/AI Studio.
2.  **Knowledge Upload:**
    * Navigate to the specific Gem folder (e.g., `gem-architect/`).
    * Upload the **ZIP file** (e.g., `gem-architect-v3.0.0.zip`).
3.  **Configuration:**
    * Open `README.md` in the Gem folder.
    * Copy the **Name** and **Description** into the Gemini settings.

---

## 3. Output Directory Structure (Production)

```text
/releases
│
├── system-instructions.md        <-- UNIVERSAL Bootloader
│
├── gem-architect/
│   ├── README.md                 <-- Name, Desc, Install Guide
│   ├── gem-architect-v3.0.0.zip  <-- Knowledge Cartridge
│   └── spec-sheet.pdf            <-- Context Assets
│
└── python-analyst/
    ├── README.md
    └── python-analyst-v1.0.0.zip
