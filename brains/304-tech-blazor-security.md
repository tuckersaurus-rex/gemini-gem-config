# 304 - TECH: BLAZOR SECURITY

## 1. XSS PREVENTION
* **MarkupString:** Use `MarkupString` ONLY when absolutely necessary and NEVER with un-sanitized user input.
* **Encoding:** Trust Razor's default HTML encoding for all `@Variable` rendering.

## 2. AUTHORIZATION
* **Route Guards:** All Pages must have `@attribute [Authorize]` unless explicitly public.
* **State Security:** Never trust client-side validation alone. The Scoped Service must re-validate actions against the `AuthenticationStateProvider`.

## 3. CIRCUIT DATA LEAKS
* **User Isolation:** Ensure Scoped Services are strictly scoped. Never use `static` fields to hold user data (this shares data across all users on the server).
