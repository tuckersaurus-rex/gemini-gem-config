# 80 - CUSTOM: PROJECT CONFIGURATION TEMPLATE

## 1. TEMPLATE USAGE

This file serves as the **Source of Truth** for generating new Project Configuration files. When creating a `90-project-*.md` file for a user, strict adherence to this structure is required.

## 2. THE TEMPLATE CONTENT

*(Copy the block below exactly when generating output)*

```markdown
# 90 - PROJECT CONFIGURATION

## 1. INSTRUCTION

* **Filename:** Rename this file to `90-project-[project-name].md`.

## 2. PROJECT METADATA

* **Name:** [Insert Project Name]
* **Type:** [e.g., Blazor Server, Python Script]
* **Goal:** [Brief description of objective]

## 3. VIRTUAL PRIORITY PATCH

*(Use this table to resolve conflicts between loaded modules. Higher Virtual IDs override Lower ones.)*

| Module Name | Physical ID | **Virtual ID** | Reason |
| :--- | :--- | :--- | :--- |
| **[Module A]** | [Physical Sector] | **[New ID]** | [Why this module takes precedence] |
| **[Module B]** | [Physical Sector] | **[New ID]** | [Why this module yields] |

## 4. BUSINESS CONTEXT

*(Add specific rules that override general best practices)*
* **Rule 1:** [e.g., "All dates must be UTC."]
* **Environment:** [e.g., "Using Azure AD."]
