---
# Module-specific overrides
sort_order: "appearance"
tone: "rigorous"
detail_level: "exhaustive"
---

# Formula Table Appendix Specification

Use this skill to compile the master mathematical formula reference table (`<!-- MODULE:table_formulas ... -->`) in the appendix of the lecture note.

---

## Core Guidelines & Format Reference

### 1. Omission Rule
- **Omit If Empty**: If the lecture note contains no mathematical, probabilistic, or cryptographic formulas, emit nothing. Never emit an empty table or template stub.

### 2. Exact 4-Column Table Structure
The table MUST strictly use these four columns:
```markdown
| Formula | Name | Usage | Answers what |
| :---: | :--- | :--- | :--- |
| $...$ | **[Name]** | [When and where to apply this formula] | [What question or metric it resolves] |
```
- Format equations cleanly in KaTeX math syntax (`$...$`).
- Sort formulas chronologically by their order of appearance in the lecture.

---

## Depth Specification

- **`depth="1"` (Mentioned in Passing)**:
  - Primary foundational equations only with concise 1-clause usage notes.
- **`depth="2"` (Discussed, but not fleshed out)**:
  - Standard formulas with short usage summaries and practical questions answered.
- **`depth="3"` (Explained in-detail in source - Default)**:
  - Comprehensive mathematical and cryptographic formula inventory covering all equations, derivations, scoring indices, and bounding constraints from the lecture.

---

## Expected Output Format

> [!IMPORTANT]
> Worker modules output **ONLY** the body content below. Do not generate section headings (`##`, `###`) or introductory quote callouts (`> [!quote]`).

```markdown
| Formula | Name | Usage | Answers what |
| :---: | :--- | :--- | :--- |
| $\text{Risk} = P(\text{Attack}) \times \text{Damage}$ | **Quantitative Risk** | Calculating expected annualized financial loss during asset risk assessment. | How much monetary loss should we expect from a specific threat scenario? |
| $\text{Risk} \in \{L, M, H\} \times \{L, M, H\}$ | **Qualitative Risk Matrix** | Categorizing risks into ordinal severity buckets when precise probabilities are unavailable. | What is the relative priority of remediating this threat compared to others? |
| $DREAD = \frac{D + R + E + A + D}{5}$ | **DREAD Scoring Index** | Multi-attribute scoring heuristic across damage, reproducibility, exploitability, affected users, and discoverability. | How do competing threats rank across multi-dimensional impact metrics? |
```
