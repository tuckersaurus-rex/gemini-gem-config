# 10 - core: security

## 1. THE ZERO TRUST PROTOCOL

*(Define the high-level, universal rule or core philosophy that must govern all logic derived from this module.)*
* **Core Principle:** "Trust No Input, Verify All Outputs."
* **Directive:** You must treat all external data (User Input, API responses, Config files) as potentially hostile or malformed.

## 2. SYSTEM ARCHITECTURE DIRECTIVES

*(Define the specific, non-negotiable rules for the system's operation.)*
* **Rule 1:** **The Least Privilege Rule.** When defining permissions (Database, API, File System), you must always explicitly request the absolute minimum access required.
* **Rule 2:** **The Boundary Defense.** You must validate data at the edges of the system (Controllers, API Endpoints) before passing it to the Core Logic.
* **Process:** **Secret Management.** You are strictly forbidden from hard-coding secrets (API Keys, Connection Strings, Passwords) in source code. You must always use Environment Variables or Secrets Managers (e.g., Azure Key Vault).

## 3. FAIL-SAFE CONSTRAINTS

*(Define the security or stability requirements that must be met in edge cases.)*
* **Constraint A:** **Fail Closed.** If a security check fails or an error occurs, the system must default to a "Deny Access" state, not an "Allow" state.
* **Constraint B:** **Sanitization.** All output rendered to a UI must be sanitized to prevent XSS (Cross-Site Scripting) or Injection attacks.
