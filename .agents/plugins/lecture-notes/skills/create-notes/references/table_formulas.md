---
name: table_formulas
description: >-
  Compiles a standardized Appendix formula table with exact columns
  (Formula, Name, Usage, Answers what).
# Inherits: target_audience, math_delimiter from create-notes/SKILL.md
sort_order: "appearance"
tone: "rigorous"
detail_level: "exhaustive"
---

# Appendix Formulas Skill (`/table_formulas`)

Use this skill to compile the master mathematical formula reference table (`<!-- MODULE:table_formulas ... -->`) in the appendix of the lecture note.

---

## Core Guidelines & Format Reference

### 1. Section Header & Placement
- Place the formula table in the Appendix under:
  ```markdown
  ## Formulas
  ```

### 2. Omission Rule
- **Omit If Empty**: If the lecture note contains no mathematical, probabilistic, or cryptographic formulas, omit the entire `## Formulas` subsection completely. Never emit an empty table or template stub.

### 3. Exact 4-Column Table Structure
The table MUST strictly use these four columns:
```markdown
| Formula | Name | Usage | Answers what |
| :---: | :--- | :--- | :--- |
| $...$ | **[Name]** | [When and where to apply this formula] | [What question or metric it resolves] |
```
- Format equations cleanly in KaTeX math syntax (`$...$`).
- Sort formulas chronologically by their order of appearance in the lecture.

---

## Reference Template

```markdown
## Formulas

| Formula | Name | Usage | Answers what |
| :---: | :--- | :--- | :--- |
| $\text{Risk} = P(\text{Attack}) \times \text{Damage}$ | **Quantitative Risk** | Calculating expected annualized financial loss during asset risk assessment. | How much monetary loss should we expect from a specific threat scenario? |
| $\text{Risk} \in \{L, M, H\} \times \{L, M, H\}$ | **Qualitative Risk Matrix** | Categorizing risks into ordinal severity buckets when precise probabilities are unavailable. | What is the relative priority of remediating this threat compared to others? |
| $DREAD = \frac{D + R + E + A + D}{5}$ | **DREAD Scoring Index** | Multi-attribute scoring heuristic across damage, reproducibility, exploitability, affected users, and discoverability. | How do competing threats rank across multi-dimensional impact metrics? |
```
