# 50 - FWK: Horizontal Structure

## 1. THE HORIZONTAL TOPOLOGY

* **Core Principle:** "Functional Grouping over Feature Slicing."
* **Constraint:** You are strictly forbidden from creating "Feature Folders" (e.g., `/Features/Login/`).
* **Directive:** You must distribute logic across the standard horizontal layers defined in Section 2.

## 2. FOLDER RESPONSIBILITIES

* **Documentation:** Non-compiled knowledge base (ADRs, Diagrams).
* **Internal/Reference:** Concrete "Reference" classes used to validate internal interfaces (Strictly `internal` scope).
* **Models:** Data Shapes only (DTOs, Enums). **Anemic** (No logic).
* **Services:** Logic Core (Orchestrators, Calculators). Stateless inputs -> outputs.
* **State:** Memory Management (Stores, Cache). Must define Scope clearly.
* **Templates:** Reusable Patterns (Base Classes, Abstract Components).
* **UI:** Presentation Layer (`Components`, `Layout`, `Pages`).
* **Utilities:** Cross-Cutting Concerns (Extensions). Must be pure functions.

## 3. TECHNICAL STANDARDS

*(Specific implementation details, syntax preferences, or formatting rules)*
* **Namespace Rule:** Root namespace must mirror the folder structure (e.g., `MyLib.UI.Components`).
* **Dependency Flow:** UI -> State -> Services -> Models.
* **Forbidden dependency:** Models must never reference Services or UI.
