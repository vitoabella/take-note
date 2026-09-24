---
name: table_definitions
description: >-
  Compiles a comprehensive glossary of technical terms in the Appendix,
  sorted by importance to the main topic.
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
  | **[[Term]]** | Precise, technically rigorous definition explaining the concept in domain context. |
  ```

### 3. Sorting & Completeness Rules
- **Sort by Importance**: Sort terms strictly by importance to the main lecture topic, most important first.
- **Full Coverage**: Cover all primary domain terminology introduced throughout the entire note.
- **No Empty Tables**: Never emit empty placeholder tables or incomplete rows.
- **Wikilinks**: Wrap each defined term in `[[wikilinks]]` for Obsidian graph connectivity.

---

## Reference Template

```markdown
## Definition of Terms

| Term | Definition |
| :--- | :--- |
| **[[Threat]]** | A potential event, actor, or circumstance with the capability to cause harm, loss, or unauthorized state modification to a system asset. |
| **[[Vulnerability]]** | A latent flaw, weakness, or design error in an information system or process that enables an attack to succeed. |
| **[[Attack]]** | An intentional, malicious action executed by an adversary to exploit a vulnerability and compromise a security objective. |
| **[[Exploit]]** | The concrete implementation, technique, or mechanism used to execute an attack against a specific vulnerability. |
| **[[Risk]]** | The quantitative or qualitative expectation of loss, traditionally defined as the product of attack probability and monetary damage. |
| **[[STRIDE]]** | A systematic threat classification model evaluating six threat categories: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege. |
| **[[Data Flow Diagram]]** | A structural schematic modeling system processes, data stores, external interactors, data flows, and trust boundaries. |
| **[[Security Pixie Dust]]** | A critical design anti-pattern wherein cryptographic mechanisms are superficially applied to a system without a coherent threat model. |
| **[[Multilateral Security]]** | A security paradigm recognizing multiple participating entities with competing interests and distinct trust boundaries. |
```
