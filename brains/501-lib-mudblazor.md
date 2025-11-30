# 501 - LIB: MUDBLAZOR STRATEGY

## 1. COMPONENT SELECTION PRIORITY
* **MudBlazor First:** You are forbidden from creating a custom component (e.g., a Card, Modal, or Button) if a MudBlazor equivalent exists.
* **Standard:** Always use the `<Mud*>` namespace (e.g., `<MudButton>`, `<MudGrid>`, `<MudTextField>`).
* **Icons:** Use the `@Icons.Material` collection exclusively. Do not import FontAwesome or other icon sets unless strictly required by a specific brand asset.

## 2. LAYOUT & THEMING
* **Root Layout:** The `MainLayout` must utilize `<MudLayout>`, `<MudAppBar>`, and `<MudDrawer>`. Do not write custom HTML sidebar/header structures.
* **Theming:** Styling customization must happen via the `MudTheme` C# object injected in `MainLayout.razor`.
    * **Forbidden:** Do not write custom CSS to override MudBlazor styles (e.g., `.mud-button { ... }`). Use the `Style` or `Class` parameters with MudBlazor utility classes if absolutely necessary.

## 3. INTERACTIVE SERVICES
* **Dialogs:** Never build a custom modal. Use `IDialogService` for all popups, confirmations, and complex forms.
* **Feedback:** Use `ISnackbar` for toast notifications. Use `IMessageBox` for simple alerts.
* **Grid:** Use `<MudDataGrid>` for complex tables (Sorting, Filtering). Use `<MudTable>` only for simple, static data.
