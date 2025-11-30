# 306 - TECH: MYSQL DATA STORE

## 1. DRIVER & CONFIGURATION
* **Provider:** Use `Pomelo.EntityFrameworkCore.MySql` (The industry standard for .NET Core).
* **Connection Logic:**
    * You MUST use `ServerVersion.AutoDetect(connectionString)` when configuring the DbContext to ensure the provider generates SQL compatible with your specific server version (MariaDB vs MySQL 8.0).
    * **Resilience:** Always chain `.EnableRetryOnFailure()` within the options builder to handle transient network blips.

## 2. SCHEMA STANDARDS
* **Character Set:** Enforce `CharSetBehavior(CharSetBehavior.AppendToAllColumns)` with `utf8mb4`.
    * *Why:* This ensures full Unicode support (emojis, global languages) by default.
* **GUID Handling:**
    * By default, GUIDs map to `char(36)`. This is acceptable for readability.
    * *Optimization:* If the database is expected to exceed 1 million rows, configure GUIDs to map to `binary(16)` for index performance.

## 3. TYPE MAPPING QUIRKS
* **DateTime vs DateTimeOffset:**
    * MySQL's `DATETIME` does not store timezone offsets.
    * **Rule:** You must convert all dates to `UTC` in C# *before* saving (`DateTime.UtcNow`). Do not rely on the database to handle timezones.
* **Boolean:** Maps to `TINYINT(1)`. Be aware of this when writing raw SQL queries.
* **Strings:** Default string length in MySQL indexes is limited (767 bytes or 3072 bytes depending on version).
    * **Rule:** Explicitly define `MaxLength` for indexed string columns (e.g., Email, Username) in `OnModelCreating` to avoid "Key too long" errors.

## 4. MIGRATION STRATEGY
* **Snapshots:** When generating migrations, the snapshot will be MySQL-specific. Do not try to share the same `Migrations` folder with SQL Server or SQLite providers.
* **Concurrency:** Use a `[Timestamp]` byte array for optimistic concurrency is not natively supported the same way as SQL Server's `RowVersion`. Use a `Guid` Version column or `DateTime` UpdatedAt column managed by EF Core's `IsConcurrencyToken()`.
