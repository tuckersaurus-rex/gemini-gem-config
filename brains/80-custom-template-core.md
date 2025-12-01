# 80 - CUSTOM: CORE/KERNEL TEMPLATE

## 1. TEMPLATE USAGE

This template is for generating **System-Level Logic** only.
* **Sector 00 (Kernel):** Operating System logic, Parsing rules, Hierarchy definitions.
* **Sector 10 (Core):** Universal behaviors (Security, Iterative Design, Thinking Processes).

## 2. THE TEMPLATE CONTENT

*(Copy the block below exactly when generating output)*

```markdown
# [00 or 10] - [kernel OR core]: [TOPIC NAME]

## 1. THE [PROTOCOL/PHILOSOPHY NAME]

*(Define the high-level, universal rule or core philosophy that must govern all logic derived from this module.)*
* **Core Principle:** [e.g., "Zero Trust Philosophy."]
* **Directive:** [e.g., "Treat all input as hostile."]

## 2. SYSTEM ARCHITECTURE DIRECTIVES

*(Define the specific, non-negotiable rules for the system's operation, often dealing with hierarchy, conflict, or lifecycle.)*
* **Rule 1:** [e.g., "Higher Sector IDs ALWAYS Override Lower Sector IDs."]
* **Rule 2:** [e.g., "You are forbidden from generating code immediately." (Measure Twice Rule)]
* **Process:** [Outline a multi-step required process, e.g., the steps in the Calibration Phase.]

## 3. FAIL-SAFE CONSTRAINTS

*(Define the security or stability requirements that must be met in edge cases.)*
* **Constraint A:** [e.g., "Systems should fail closed (deny access), not open."]
* **Constraint B:** [e.g., "Request only the permissions absolutely necessary (Least Privilege)."]
```
