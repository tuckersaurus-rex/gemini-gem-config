# 305 - TECH: MICROSOFT IDENTITY (CORE)

## 1. CONTEXT ARCHITECTURE
* **Inheritance:** Your application's `DbContext` MUST inherit from `IdentityDbContext<ApplicationUser, ApplicationRole, string>`.
    * Do not use the default `IdentityDbContext`. Always explicitly define the User and Role types to allow future extensibility without breaking schema changes.
* **User Model:** Create an `ApplicationUser` class inheriting from `IdentityUser`.
    * Add domain-specific profile data (e.g., `FullName`, `ProfilePictureUrl`) here, not in a separate "UserProfile" table, unless the data is massive and rarely accessed.

## 2. CONFIGURATION STRATEGY (Program.cs)
* **Service Registration:** Use `builder.Services.AddIdentity<ApplicationUser, ApplicationRole>()`.
    * **Stores:** Chain `.AddEntityFrameworkStores<YourDbContext>()`.
    * **Providers:** Chain `.AddDefaultTokenProviders()`.
* **Password Policy:** Enforce strict defaults in the options lambda:
    * `options.Password.RequireDigit = true;`
    * `options.Password.RequiredLength = 12;`
    * `options.Password.RequireNonAlphanumeric = true;`
* **Lockout:** Enable lockout to prevent brute-force attacks (`DefaultLockoutTimeSpan = TimeSpan.FromMinutes(15)`).

## 3. ACCESS & MANAGER USAGE
* **Dependency Injection:**
    * **DO NOT** query the `AspNetUsers` table directly via `DbContext`.
    * **ALWAYS** use `UserManager<ApplicationUser>` for creating users, changing passwords, or updating claims.
    * **ALWAYS** use `SignInManager<ApplicationUser>` for logging in/out (cookie management).
* **Claims Transformation:** If you need to add data to the `User.Identity` (like "Department" or "VIP Status") for use in `@attribute [Authorize]`, implement a custom `IUserClaimsPrincipalFactory`. Do not look up this data in the View/Component.

## 4. BLAZOR INTEGRATION
* **Authentication State:** Ensure the `AuthenticationStateProvider` is configured to use the Identity cookies (typically `RevalidatingIdentityAuthenticationStateProvider`).
* **Security Stamp:** Enable `options.User.RequireUniqueEmail = true` and ensure the Security Stamp is updated on password changes to invalidate old cookies immediately.
