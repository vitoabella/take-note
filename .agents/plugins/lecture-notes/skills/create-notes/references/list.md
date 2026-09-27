---
list_style: "hybrid"
foldable_callouts: true
---

# List & Taxonomy Module Specification

Use this module to structure bullet points, procedures, taxonomies, and unexpounded enumerations into scannable lists and semantic callout expansions.

---

## 1. Visual Skeleton

```markdown
<!-- MODULE:list section="<section_number>" topic="<topic_description>" depth="<1|2|3>" ... -->
- **<Core Term / Property 1>**: <Precise 1-sentence definition and operational role.>
  - *<Sub-dimension A>*: <Key property, metric, or boundary condition.>
  - *<Sub-dimension B>*: <Key property, metric, or boundary condition.>
- **<Core Term / Property 2>**: <Precise 1-sentence definition and operational role.>
- **<Core Term / Property 3>**: <Precise 1-sentence definition and operational role.>

> [!example]- <Unexpounded Item / Scenario 1>
> <Expanded definition, operational mechanism, and real-world significance.>
<!-- -->
> [!example]- <Unexpounded Item / Scenario 2>
> <Expanded definition, operational mechanism, and real-world significance.>
```

## 2. Depth Matrix

| Depth | Scale / Scope | Components Included | Tone & Rigor | Fold Stance |
| :---: | :--- | :--- | :--- | :--- |
| **`1`** | 3–4 items | Simple flat list; omit sub-bullets and callouts | Concise, accessible | Open bullets |
| **`2`** | 4–6 items | Bulleted taxonomy with short sub-bullets; folded callouts for unexpounded lists | Standard operational | Bullets open, callouts folded (`-`) |
| **`3`** | Comprehensive | Hierarchical taxonomy + sub-bullets detailing invariants + in-depth callouts | Rigorous, exhaustive | Bullets open, callouts folded (`-`) |

## 3. Strict Negative Invariants

- **Tag + Body Content Only**: Output ONLY the module tag and the list/callouts directly below it.
- **No Headings or Quote Callouts**: NEVER generate markdown headings (`##`, `###`) or section intro quote callouts (`> [!quote]`).
- **Bold Lead-In Labels**: Every top-level bullet must begin with a bold headword (`- **Label**: ...`).
- **Nesting Limit**: Nest at most 2–3 indentation levels to prevent visual clutter.
