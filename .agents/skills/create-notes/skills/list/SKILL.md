---
name: list
description: >-
  Generates structured taxonomies, sequential procedures, characteristic bulleted breakdowns,
  and takeaway checklists.
# Inherits: tone, detail_level, target_audience, foldable_callouts from create-notes/SKILL.md
list_style: "hybrid"
foldable_callouts: true
---

# List Skill (`/list`)

Use this skill to convert slide bullet points, categorizations, operational procedures, and taxonomies (`<!-- MODULE:list ... -->`) into scannable, structured Markdown lists.

---

## Core Guidelines & Format Reference

### 1. Heading Lead-in & Definition Rules
- When introducing a concept with $\ge 3$ sentences of definitional content: Keep a short lead blockquote, followed by bullet characteristics:
  ```markdown
  > [Lead definition sentence under 3 sentences].
  > - **Characteristic 1**: Specific operational property.
  > - **Characteristic 2**: Specific operational property.
  ```
- If each sub-type is a one-line definition: Present as a clean flat bulleted list under the H2/H3 header.

### 2. Formatting Conventions
- **Bold Lead-in Labels**: Every bullet must lead with a bold term or action verb (`- **Term**: Explanation...`).
- **Nesting Limit**: Nest at most 2–3 levels to preserve readability.
- **Voice**: Strong student explaining to a peer — digestible, technically precise.

---

## Reference Templates

### 1. Multi-Dimensional Taxonomy
```markdown
- **Confidentiality**: Protection of sensitive secrets against unauthorized reading or disclosure.
  - *Data at Rest*: Encrypted storage, file-level ACLs, and cryptographic databases.
  - *Data in Transit*: TLS sessions, forward secrecy, and authenticated encryption.
- **Integrity**: Assurance that data and system state are modified only through authorized, audited transactions.
- **Availability**: Guarantee that services remain operational and accessible under legitimate user demand.
- **Access Control**: Enforcement mechanisms verifying authorization before granting resource operations.
- **Privacy**: Policy and technical boundaries allowing individuals to control personal data dissemination.
```

### 2. Sequential Algorithmic Procedure
```markdown
1. **Understand Architecture & Objectives**: Map all system components, data flows, communication protocols, and operational goals.
2. **Catalog Assets & Valuation**: Identify what has tangible value (money, user credentials, transport capacity, server uptime) and how loss impacts solvency.
3. **Enumerate Threat Actors**: Identify all stakeholders, external adversaries, and privileged insiders, profiling their capabilities and motivations.
4. **Iterative Attack Discovery**: Brainstorm vulnerabilities and attack vectors across every interface and trust boundary without structural dogma.
5. **Prioritize & Remediate**: Rank identified threats by empirical risk and implementation cost of countermeasures.
```
