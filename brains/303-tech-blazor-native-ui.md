# 303 - TECH: BLAZOR NATIVE UI

## 1. CSS IMPLEMENTATION
* **Framework:** Use the project's standard framework (Bootstrap 5 or `app.css`) for global utility classes.
* **Isolation:** You MUST use **Blazor CSS Isolation** (`Component.razor.css`) for all component-specific styling. Do not pollute the global stylesheet with component styles.
* **Libraries:** NO third-party component libraries (MudBlazor, Radzen, etc.) are permitted. You are expected to build atomic, native components (Buttons, Inputs) using standard HTML/CSS.

## 2. JAVASCRIPT INTEROP POLICY
* **Blazor-First:** Javascript Interop is forbidden unless there is **zero** C# alternative (e.g., Focus management, Canvas, Geolocation, specialized DOM measurements).
* **Module Isolation:** If JS is absolutely required, you must use **ES Modules** (`export function...`) and import them via `IJSObjectReference`.
* **No Global Scope:** Never attach functions to `window` or `document` directly.

## 3. STATIC ASSETS
* Use **.NET 10 Static Web Assets** conventions.
* Place images/scripts in `wwwroot`.
* Reference them via standard relative paths (e.g., `_content/{PackageId}/...` if inside a library).
