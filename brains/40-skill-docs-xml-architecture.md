# 40 - SKILL: Docs Xml Architecture

## 1. THE "WHY OVER HOW" PROTOCOL

* **Core Principle:** "Code explains How; Comments explain Why."
* **Directive:** You are forbidden from writing XML summaries that simply repeat the method name (e.g., "Saves the data" for `SaveData()`).
* **Focus:** Documentation must capture **Design Intent**, **Constraints**, and **Side Effects**.

## 2. XML TAG USAGE

* **Summary Tag:** Defines the High-Level Contract (What problem does this solve?).
* **Remarks Tag:** **THE ARCHITECTURAL CONTEXT.** Mandatory for complex logic. Explain *why* this approach was chosen and *why* others were rejected.
* **Example Tag:** Usage scenarios, strictly required for `public` APIs.
* **Exception Tag:** You must enumerate ALL possible exceptions.

## 3. TECHNICAL STANDARDS

*(Specific implementation details, syntax preferences, or formatting rules)*
* **Format:** Standard C# XML Documentation Comments (`///`).
* **Constraint:** Do not use `include` tags to external files; keep documentation inline for IntelliSense visibility.
* **Example Syntax:**

```csharp
/// <summary>
/// Orchestrates the state transition for the Wizard workflow.
/// </summary>
/// <remarks>
/// <strong>Architectural Note:</strong>
/// We use a pessimistic locking strategy here because the State Container
/// is shared across the Circuit. An optimistic approach was rejected
/// due to the high frequency of user updates in the Wizard steps.
/// </remarks>
public void TransitionState() { ... }
```
