---
# Module-specific overrides
sort_order: "importance"
tone: "rigorous"
detail_level: "exhaustive"
---

# Glossary & Definitions Appendix Specification

Use this skill to compile the master glossary table (`<!-- MODULE:table_definitions ... -->`) in the appendix of the lecture note.

---

## Core Guidelines & Format Reference

### 1. Table Structure & Columns
- Exactly two columns:
  ```markdown
  | Term | Definition |
  | :--- | :--- |
  | **[[#Section Heading|Term]]** | Precise, technically rigorous definition explaining the concept in domain context. |
  ```

### 2. Bidirectional In-Note Wikilinking Rule
- Every term in the glossary MUST include an internal Obsidian wikilink referencing the exact section heading in the document where the concept was first introduced:
  - Format: `**[[#Exact Section Heading|Term Display Name]]**`
  - **Example**: `**[[#1.2 Fundamental Terminology & Quantitative Risk|Vulnerability]]**`
  - **Example**: `**[[#4.2 The STRIDE Methodology & Data Flow Diagrams|STRIDE]]**`

### 3. Sorting & Completeness Rules
- **Sort by Importance**: Sort terms strictly by importance to the main lecture topic, most important first.
- **Full Coverage**: Cover all primary domain terminology introduced throughout the entire note.
- **No Empty Tables**: Never emit empty placeholder tables or incomplete rows.

---

## Depth Specification

- **`depth="1"` (Mentioned in Passing)**:
  - Core foundational terms only (5–8 key terms) with concise 1-sentence definitions.
- **`depth="2"` (Discussed, but not fleshed out)**:
  - Standard glossary (10–15 terms) covering major concepts with concise definitions and section wikilinks.
- **`depth="3"` (Explained in-detail in source - Default)**:
  - Exhaustive domain glossary covering all technical terms, threat models, mechanisms, and cryptographic constructs introduced throughout the lecture note, each paired with precise definitions and bidirectional wikilinks.

---

## Expected Output Format

> [!IMPORTANT]
> Worker modules output **ONLY** the body content below. Do not generate section headings (`##`, `###`) or introductory quote callouts (`> [!quote]`).

```markdown
| Term | Definition |
| :--- | :--- |
| **[[#1.2 Fundamental Terminology & Quantitative Risk|Threat]]** | A potential event, actor, or circumstance with the capability to cause harm, loss, or unauthorized state modification to a system asset. |
| **[[#1.2 Fundamental Terminology & Quantitative Risk|Vulnerability]]** | A latent flaw, weakness, or design error in an information system or process that enables an attack to succeed. |
| **[[#1.2 Fundamental Terminology & Quantitative Risk|Attack]]** | An intentional, malicious action executed by an adversary to exploit a vulnerability and compromise a security objective. |
| **[[#1.2 Fundamental Terminology & Quantitative Risk|Exploit]]** | The concrete implementation, technique, or mechanism used to execute an attack against a specific vulnerability. |
| **[[#1.2 Fundamental Terminology & Quantitative Risk|Risk]]** | The quantitative or qualitative expectation of loss, traditionally defined as the product of attack probability and monetary damage. |
| **[[#4.2 The STRIDE Methodology & Data Flow Diagrams|STRIDE]]** | A systematic threat classification model evaluating six threat categories: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege. |
| **[[#4.2 The STRIDE Methodology & Data Flow Diagrams|Data Flow Diagram]]** | A structural schematic modeling system processes, data stores, external interactors, data flows, and trust boundaries. |
| **[[#4.4 Assessment Pitfalls & Security 'Pixie Dust'|Security Pixie Dust]]** | A critical design anti-pattern wherein cryptographic mechanisms are superficially applied to a system without a coherent threat model. |
| **[[#1.4 The Adversary & Threat Actors|Multilateral Security]]** | A security paradigm recognizing multiple participating entities with competing interests and distinct trust boundaries. |
```
