---
foldable_callouts: true
---

# 2-Way Comparison Module Specification

Use this module to construct side-by-side comparative analyses between exactly two competing paradigms, technologies, architectures, or concepts.

---

## 1. Visual Skeleton

```markdown
<!-- MODULE:vs_comparison section="<section_number>" topic="<topic_description>" depth="<1|2|3>" ... -->

| Dimension / Attribute | <Option A> | <Option B> |
| :--- | :--- | :--- |
| **<Primary Paradigm / Model>** | <Direct comparative analysis> | <Direct comparative analysis> |
| **<Operational Mechanism>** | <Direct comparative analysis> | <Direct comparative analysis> |
| **<Resource Overhead / Cost>** | <Direct comparative analysis> | <Direct comparative analysis> |
| **<Failure Mode / Vulnerability>** | <Direct comparative analysis> | <Direct comparative analysis> |

> [!tip]- Selection Heuristic & Key Trade-Off
> - **Choose / Rely on <Option A> when**: <Specific operational constraints, workload profiles, or environment.>
> - **Choose / Rely on <Option B> when**: <Specific operational constraints, workload profiles, or environment.>
```

## 2. Depth Matrix

| Depth | Scale / Scope | Components Included | Tone & Rigor | Fold Stance |
| :---: | :--- | :--- | :--- | :--- |
| **`1`** | 2–3 rows | High-level contrast table; omit selection heuristic callout | Simple, accessible | Open table |
| **`2`** | 4–5 rows | Operational comparison table + folded selection heuristic callout | Standard technical | Table open, callout folded (`-`) |
| **`3`** | 6+ rows | Invariant & edge-case comparison table + folded comprehensive trade-off insight | Rigorous, edge-case | Table open, callout folded (`-`) |

## 3. Strict Negative Invariants

- **Tag + Body Content Only**: Output ONLY the module tag and the table/callout directly below it.
- **No Headings or Quote Callouts**: NEVER generate markdown headings (`##`, `###`) or section intro quote callouts (`> [!quote]`).
- **Never Leave Empty Cells**: Every row must provide substantive, contrasting detail for both options.
- **Exactly Two Entities**: If comparing 3 or more entities, use `multi_comparison` instead.
