---
diagram_engine: "ascii_or_unicode"
foldable_callouts: true
---

# Causal Chain Module Specification

Use this module to model root-cause-to-failure cascades, security exploit progressions, performance bottlenecks, or cascading domino effects where one event directly triggers the next.

---

## 1. Visual Skeleton

```markdown
<!-- MODULE:causal_chain section="<section_number>" topic="<topic_description>" depth="<1|2|3>" ... -->
```text
[ 1. <Root Cause / Initial Trigger> ]
       │
       ▼  (<Direct Consequence / Mechanism>)
[ 2. <Intermediate Vulnerable / Degraded State> ]
       │
       ▼  (<Compounding Factor / Escalation>)
[ 3. <Exploitation / Cascade Propagation> ]
       │
       ▼  (<Systemic Failure Boundary>)
[ 4. <Terminal Outcome / System Impact> ]
```

> [!danger]- Domino Progression & Side Effects
> - **Stage 1 -> Stage 2**: <How initial trigger breaches primary invariant.>
> - **Stage 2 -> Stage 3**: <How vulnerability propagates to adjacent components.>
> - **Stage 3 -> Stage 4**: <Ultimate system compromise, outage, or data corruption.>
> - **Lateral Side Effects**: <Collateral damage or secondary invariants affected.>
```

## 2. Depth Matrix

| Depth | Scale / Scope | Components Included | Tone & Rigor | Fold Stance |
| :---: | :--- | :--- | :--- | :--- |
| **`1`** | 2–3 stages | High-level chain diagram only; omit side effects callout | High-level, accessible | Open diagram |
| **`2`** | 3–4 stages | Chain diagram + folded progression walkthrough | Standard operational | Diagram open, callout folded (`-`) |
| **`3`** | 4+ stages + lateral effects | Full cascade chain + lateral side effects + mitigation points | Rigorous, failure-mode | Diagram open, callout folded (`-`) |

## 3. Strict Negative Invariants

- **Tag + Body Content Only**: Output ONLY the module tag and the generated diagram and callout directly below it.
- **No Headings or Quote Callouts**: NEVER generate markdown headings (`##`, `###`) or section intro quote callouts (`> [!quote]`).
- **No Conversational Wrapper**: Do not include conversational greetings or commentary.
- **Strict Linear Causality**: Every link in the chain must represent a necessary causal or enabling step, not merely a coincidental chronological sequence.
