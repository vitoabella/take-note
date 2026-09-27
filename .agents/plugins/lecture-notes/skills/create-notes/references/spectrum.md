---
diagram_engine: "ascii_or_unicode"
foldable_callouts: true
---

# Spectrum Module Specification

Use this module to visualize continuous trade-off continuums between two opposing architectural poles (e.g. Consistency vs Availability, Performance vs Security).

---

## 1. Visual Skeleton

```markdown
<!-- MODULE:spectrum section="<section_number>" topic="<topic_description>" depth="<1|2|3>" ... -->
```text
[ Pole A: <Opposing Ideal A> ] ────────── [ Balanced / Hybrid ] ────────── [ Pole B: <Opposing Ideal B> ]
(<Core Advantage / Operational Cost>)                                    (<Core Advantage / Operational Cost>)
               │                                      │                                      │
       <System / Model 1>                     <System / Model 2>                     <System / Model 3>
       <Key Trade-Off Stance>                 <Key Trade-Off Stance>                 <Key Trade-Off Stance>
```

| Continuum Position | Architecture / System | Primary Guarantee | Operational Compromise |
| :--- | :--- | :--- | :--- |
| **Left Pole: <Pole A>** | `<System / Approach A>` | `<Maximum property A>` | `<Severe penalty on property B>` |
| **Center: <Balanced>** | `<System / Approach B>` | `<Balanced trade-off>` | `<Moderate compromise on both>` |
| **Right Pole: <Pole B>** | `<System / Approach C>` | `<Maximum property B>` | `<Severe penalty on property A>` |

> [!info]- Decision Rubric: Where to Position Your System
> - **Favor <Pole A> when**: <Specific latency, workload, or operational constraints.>
> - **Favor <Pole B> when**: <Specific consistency, integrity, or compliance requirements.>
```

## 2. Depth Matrix

| Depth | Scale / Scope | Components Included | Tone & Rigor | Fold Stance |
| :---: | :--- | :--- | :--- | :--- |
| **`1`** | 2 poles | Horizontal axis diagram with 2 extreme poles; omit table/callout | High-level, conceptual | Open ASCII diagram |
| **`2`** | 3 points | Axis diagram + position breakdown table | Standard comparative | Diagram and table open |
| **`3`** | Full continuum | Axis diagram + positioning table + folded decision rubric | Rigorous, trade-off | Diagram/table open, rubric folded (`-`) |

## 3. Strict Negative Invariants

- **Tag + Body Content Only**: Output ONLY the module tag and the spectrum diagram/table directly below it.
- **No Headings or Quote Callouts**: NEVER generate markdown headings (`##`, `###`) or section intro quote callouts (`> [!quote]`).
- **Continuous Tension**: The two poles must represent genuine competing design trade-offs, not unrelated orthogonal features.
