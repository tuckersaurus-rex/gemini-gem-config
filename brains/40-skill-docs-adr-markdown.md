# 40 - SKILL: Docs Adr Markdown

## 1. THE DECISION RECORD PROTOCOL

* **Trigger:** You must generate an Architecture Decision Record (ADR) whenever a significant architectural choice is made.
* **Storage:** You must save these files in `/Documentation/ADR/`.
* **Immutable History:** You must never delete or overwrite an old ADR. If a decision changes, create a new ADR that "Supersedes" the old one.

## 2. RECORD STRUCTURE

* **Status Field:** Must be one of: [Proposed, Accepted, Rejected, Deprecated, Superseded].
* **Context:** You must explain the *forces* at play (technical constraints, business goals) that necessitated the decision.
* **Consequences:** You must list both the positive and negative outcomes (Technical Debt accepted, Complexity added, Performance cost).

## 3. TECHNICAL STANDARDS

*(Specific implementation details, syntax preferences, or formatting rules)*
* **Naming Convention:** `[Index]-[kebab-case-title].md` (e.g., `001-initial-architecture.md`).
* **Template Source:**

  ```markdown
  # [Index] - [Short Title]
  ## Status
  [Proposed | Accepted | Deprecated | Superseded by [Index]]
  ## Context
  ...
  ## Decision
  ...
  ## Consequences
  ...
  ```
