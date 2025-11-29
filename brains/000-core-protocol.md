# 000-core-boilerplate

## 1. System Identity

This file provides the granular operational structure, defining the purpose of each number band within the Century Protocol.

## 2. Century Protocol Band Definition

| Range | Category | Purpose |
| :--- | :--- | :--- |
| **000-099** | **Core/Kernel** | Universal foundational rules (Naming, Protocol, Structure definition). |
| **100-199** | **Domain/Role** | Job title and specific persona rules. |
| **200-299** | **Standards** | Formatting, style guides, and documentation rules. |
| **300-799** | **Tech/Skills** | Specific languages, frameworks, and APIs. |
| **800-899** | **Custom Libraries** | Stable, shared internal code context (as permanent knowledge). |
| **900-999** | **Project Context** | Specific project overrides, business logic, and style exceptions. |

## 3. Conflict and Naming Enforcement

1.  All knowledge files must adhere to **Kebab-Case** naming convention.
2.  All conflicts are resolved by the highest number (CRITICAL OVERRIDE RULE).
3.  Any file uploaded outside of the 000-999 range (e.g., a file without a numeric prefix) is treated as unparsed, lower-priority context.
