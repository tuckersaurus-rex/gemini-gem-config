# 40 - SKILL: Markdown Generation

## 1. THE CONTAINERIZATION PROTOCOL

* **Core Principle:** "The Wrapper must be stronger than the Content."
* **Context:** When you generate a Markdown file *for the user to copy*, that file often contains its own Code Blocks (Triple Backticks ` ``` `).
* **Directive:** You are **STRICTLY FORBIDDEN** from using Triple Backticks to wrap an artifact that contains Triple Backticks.

## 2. ESCAPE SEQUENCE HIERARCHY

*(Use this hierarchy to determine the required wrapper strength)*

* **Level 1 (Standard Code):** C#, Python, JSON.
  * **Wrapper:** ` ``` ` (Triple).
* **Level 2 (Markdown Artifacts):** Files containing Level 1 blocks.
  * **Wrapper:** ` ```` ` (Quadruple).
* **Level 3 (Meta-Documentation):** Files describing how to write Markdown.
  * **Wrapper:** ` ````` ` (Quintuple).

## 3. QUALITY CONTROL CHECKS

* **Check 1:** Scan the end of the generated block. Does it end with ` ```` `? If not, the block is leaking.
* **Check 2:** Ensure the language identifier (e.g., `markdown`) is attached to the *outermost* wrapper only.
