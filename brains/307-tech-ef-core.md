# 307 - TECH: ENTITY FRAMEWORK CORE 10

## 1. CONTEXT LIFECYCLE (BLAZOR SPECIFIC)
* **Factory Pattern:** You MUST inject `IDbContextFactory<TContext>`, not `TContext` directly.
    * *Reason:* Blazor Server circuits are long-lived. A standard Scoped `DbContext` is not thread-safe and will crash if the user triggers two async events simultaneously.
* **Usage:** Create short-lived contexts for every operation.
    * *Pattern:* `using var context = await _factory.CreateDbContextAsync();`

## 2. QUERY PERFORMANCE (READS)
* **No Tracking:** By default, all read-only queries must use `.AsNoTracking()`.
    * *Why:* Tracking entities adds significant memory overhead. Only track entities you intend to `Update()` in the same scope.
* **Projections:** Never return raw Entities to the UI. Use `.Select(x => new Dto { ... })` to fetch only the columns needed.
    * *Forbidden:* `return context.Users.ToList();` (Fetches password hashes, blobs, etc.)
* **Split Queries:** For queries with large `.Include()` collections, use `.AsSplitQuery()` to prevent "Cartesian Explosion" (massive data duplication in the SQL result set).

## 3. MUTATION STRATEGY (WRITES)
* **Batch Operations:** Prefer the .NET 10/EF Core `ExecuteUpdateAsync` and `ExecuteDeleteAsync` methods for bulk operations.
    * *Correct:* `await context.Orders.Where(o => o.Old).ExecuteDeleteAsync();`
    * *Incorrect:* Fetching 1000 orders into memory just to `Remove()` them loop-by-loop.
* **Concurrency:** Handle `DbUpdateConcurrencyException`. If a save fails due to a conflict, catch it and either retry or alert the user.

## 4. RELATIONS
* **Eager Loading:** Use `.Include()` explicitly.
* **Lazy Loading:** Strict Prohibition. `Proxies` should be disabled to prevent accidental "N+1" query performance disasters in the UI rendering loop.
