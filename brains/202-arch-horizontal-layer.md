# 202 - ARCHITECTURE: HORIZONTAL LAYERS (TECHNICAL TIERS)

## 1. PHILOSOPHY
Organize code by **Technical Responsibility**.
* **Goal:** Separation of Concerns. Replaceable layers.
* **Usage:** Best for Libraries, Frameworks, simple CRUD applications, or strict Client/Server splits.

## 2. PROJECT STRUCTURE
### Presentation Layer (UI/Interface)
* **Responsibility:** Rendering, Input capture, Routing.
* **Constraint:** Contains NO business logic. Delegates immediately to the Logic Layer.

### Logic Layer (Service/Domain)
* **Responsibility:** Validations, Calculations, Workflow orchestration.
* **Constraint:** Pure logic. Should have no knowledge of the Database type or the UI framework.

### Data Layer (Infrastructure/Repository)
* **Responsibility:** Database connections, API calls, File I/O.
* **Constraint:** The only layer allowed to touch the "outside world."

### Shared/Common Layer
* **Responsibility:** DTOs, Enums, Interfaces, Constants.
* **Constraint:** Accessible by all layers.

## 3. DEPENDENCY RULES
1.  **Strict Layering:** Dependencies flow DOWN only.
    * UI $\rightarrow$ Logic $\rightarrow$ Data.
    * Data Layer never knows about the UI.
2.  **Abstraction:** Layers should communicate via Interfaces/Contracts defined in the Shared layer, preventing tight coupling between specific implementations (e.g., swapping SQL for NoSQL shouldn't break the UI).
