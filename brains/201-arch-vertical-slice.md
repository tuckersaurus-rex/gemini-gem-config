# 201 - ARCHITECTURE: VERTICAL SLICES (FEATURE DRIVEN)

## 1. PHILOSOPHY
Organize code by **Domain Feature**, not by technical file type.
* **Goal:** High Cohesion. Everything related to a specific user requirement changes together and lives together.
* **Usage:** Best for Applications, Complex UIs, and Domain-Driven Design (DDD).

## 2. PROJECT STRUCTURE
### The Core (The "System")
* Contains logic shared by *all* features.
* **Base Classes:** Abstract types used across the system.
* **Shared UI:** Layouts, Navigation, styling systems.
* **Utilities:** Generic helpers (Date formatting, Math).

### The Features (The "Slices")
* **Format:** `/Features/{FeatureName}/`
* **Contents:**
    * **Entry Point:** The route or public interface for the feature.
    * **UI Components:** Views/Templates specific to this feature.
    * **State/Logic:** The controller, store, or service handling this feature's rules.
    * **Data Models:** DTOs or Types specific to this feature's input/output.

## 3. DEPENDENCY RULES
1.  **One-Way Flow:** Features depend on Core. Core NEVER depends on Features.
2.  **Isolation:** Features should **not** depend on other Features.
    * *Communication:* If Feature A needs data from Feature B, they should communicate via a shared Event Bus, a Core Mediator, or a URL change, not direct imports.
3.  **Refactoring:** If logic is duplicated in 3+ features, promote it to Core.
