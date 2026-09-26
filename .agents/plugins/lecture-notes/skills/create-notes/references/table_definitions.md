---
name: table_definitions
description: >-
  Compiles a comprehensive glossary of technical terms in the Appendix,
  sorted by importance to the main topic, with internal wikilinks pointing back
  to where each term was first introduced in the document.
# Inherits: target_audience, use_wikilinks from create-notes/SKILL.md
sort_order: "importance"
tone: "rigorous"
detail_level: "exhaustive"
---

# Technical Terms Glossary Skill (`/table_definitions`)

Use this skill to compile the master glossary table (`<!-- MODULE:table_definitions ... -->`) in the appendix of the lecture note.

---

## Core Guidelines & Format Reference

### 1. Section Header & Placement
- Place the glossary in the Appendix under:
  ```markdown
  ## Definition of Terms
  ```

### 2. Table Structure & Columns
- Exactly two columns:
  ```markdown
  | Term | Definition |
  | :--- | :--- |
  | **[[#Section Heading|Term]]** | Precise, technically rigorous definition explaining the concept in domain context. |
  ```

### 3. Bidirectional In-Note Wikilinking Rule

> [!IMPORTANT]
> **Wikilink Back to Source Section**:
> Every term in the glossary MUST include an internal Obsidian wikilink referencing the exact section heading in the document where the concept was first introduced:
> - Format: `**[[#Exact Section Heading|Term Display Name]]**`
> - **Example**: `**[[#1.2 Fundamental Terminology & Quantitative Risk|Vulnerability]]**`
> - **Example**: `**[[#4.2 The STRIDE Methodology & Data Flow Diagrams|STRIDE]]**`
> This enables immediate bidirectional navigation between the appendix glossary and the explanatory narrative.

### 4. Sorting & Completeness Rules
- **Sort by Importance**: Sort terms strictly by importance to the main lecture topic, most important first.
- **Full Coverage**: Cover all primary domain terminology introduced throughout the entire note.
- **No Empty Tables**: Never emit empty placeholder tables or incomplete rows.

---

## Reference Template

```markdown
## Definition of Terms

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
