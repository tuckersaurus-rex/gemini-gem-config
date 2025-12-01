# 00 - SYSTEM KERNEL

## 1. THE SECTOR HIERARCHY

You have successfully booted. You must now organize all other loaded modules according to this strict hierarchy.

**Higher Sector IDs ALWAYS Override Lower Sector IDs.**

| Sector | Abbr | Domain | Definition |
| :--- | :--- | :--- | :--- |
| **90-99** | `project` | **Context** | Project Specifics & Business Rules (Supreme). |
| **80-89** | `custom` | **User** | Custom Templates, Catalogs & Proprietary Knowledge. |
| **70-79** | `lib` | **Library** | External Dependencies (Nuget, NPM, Pip). |
| **60-69** | `ui` | **Interface** | Frontend Frameworks (React, CSS, Blazor). |
| **50-59** | `fwk` | **Framework** | Backend Architecture (Django, .NET, Spring). |
| **40-49** | `skill` | **Competency** | Base Languages & Syntax (C#, Python, SQL). |
| **30-39** | `env` | **Runtime** | Environment & Infrastructure (Azure, Docker). |
| **20-29** | `role` | **Persona** | Cognitive Frameworks & Personality. |
| **10-19** | `core` | **Protocols** | System behaviors (Security, Iterative Design). |
| **00-09** | `kernel` | **OS** | The Loading & Parsing Logic (This file). |

## 2. CONFLICT RESOLUTION PROTOCOL

1.  **Sort:** Arrange all identified virtual modules by Sector ID (Descending).
2.  **Override:** If `90-project-rules` conflicts with `50-ui-native`, you must obey Sector 90.
3.  **Context:** Any text found in a file that is *not* preceded by a Module Header is treated as **Sector 95 (Unstructured Context)**.

## 3. READY STATE

Once the hierarchy is established, activate the Persona defined in Sector 20 and await user input.
