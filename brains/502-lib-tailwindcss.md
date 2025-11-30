# 502 - LIB: TAILWIND CSS STRATEGY

## 1. UTILITY-FIRST PHILOSOPHY
* **No Custom CSS:** Writing custom CSS classes in `.razor.css` or `app.css` is strictly discouraged.
* **Primary Strategy:** Style components exclusively using Tailwind utility classes directly in the HTML.
    * *Correct:* `<div class="flex items-center justify-between p-4 bg-gray-100 rounded-lg">`
    * *Incorrect:* `<div class="user-card-header">` (with a matching CSS file).

## 2. CONSISTENCY & CONFIGURATION
* **Source of Truth:** All colors, spacing, and breakpoints must be defined in `tailwind.config.js`. Do not use "Arbitrary Values" (e.g., `w-[17px]`) if a theme value (e.g., `w-4` or `w-5`) is close enough.
* **Component Abstraction:** If a set of Tailwind classes is repeated 3+ times (e.g., a specific button style), extract it into a small Razor component (e.g., `<PrimaryButton>`) wrapping the classes, rather than using `@apply` in a CSS file. We prefer explicit HTML over hidden CSS abstractions.

## 3. BLAZOR INTEGRATION
* **Class Merging:** When building reusable components, always allow additional classes to be passed in and merged with the default Tailwind classes.
    * *Pattern:* `class="bg-blue-500 text-white @Class"`
