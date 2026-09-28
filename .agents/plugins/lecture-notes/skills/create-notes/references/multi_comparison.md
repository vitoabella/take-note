---
foldable_callouts: true
---

# Multi-Option Comparison Module Specification

Use this module to evaluate 3 or more candidate systems, algorithms, models, or frameworks across shared technical dimensions.

---

## 1. Visual Skeleton

```markdown
<!-- MODULE:multi_comparison section="<section_number>" topic="<topic_description>" depth="<1|2|3>" ... -->

| Evaluation Dimension | <Candidate A> | <Candidate B> | <Candidate C> |
| :--- | :--- | :--- | :--- |
| **<Primary Objective>** | <Substantive comparison> | <Substantive comparison> | <Substantive comparison> |
| **<Mechanism / Architecture>** | <Substantive comparison> | <Substantive comparison> | <Substantive comparison> |
| **<Complexity / Overhead>** | <Substantive comparison> | <Substantive comparison> | <Substantive comparison> |
| **<Primary Limitation>** | <Substantive comparison> | <Substantive comparison> | <Substantive comparison> |

> [!info]- Architectural Trade-Off & Pareto Synthesis
> - **Optimal for <Workload / Context 1>**: Choose `<Candidate A>` because `<rationale>`.
> - **Optimal for <Workload / Context 2>**: Choose `<Candidate B>` because `<rationale>`.
> - **Pareto Frontier**: No single candidate dominates all dimensions; trade-off centers on `<core tension>`.
```

## 2. Depth Matrix

| Depth | Scale / Scope | Components Included | Tone & Rigor | Fold Stance |
| :---: | :--- | :--- | :--- | :--- |
| **`1`** | 3 dimensions | 3-row matrix across candidates; omit synthesis callout | Concise, high-level | Open table |
| **`2`** | 4–5 dimensions | Standard matrix + folded trade-off synthesis callout | Standard technical | Table open, callout folded (`-`) |
| **`3`** | 6+ dimensions | Multi-attribute matrix evaluating invariants, bounds, failure modes + synthesis | Rigorous, comparative | Table open, callout folded (`-`) |

## 3. Strict Negative Invariants

- **Tag + Body Content Only**: Output ONLY the module tag and the table/callout directly below it.
- **No Headings or Quote Callouts**: NEVER generate markdown headings (`##`, `###`) or section intro quote callouts (`> [!quote]`).
- **Never Leave Empty Cells**: Every cell must contain meaningful comparative analysis; never output bare dashes or blanks.
- **Shared Dimensions Only**: Every row must apply equally to all candidate columns.
