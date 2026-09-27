---
callout_type: "quote"
foldable_callouts: true
---

# Inquiry Module Specification

Use this module to provoke curiosity through boundary-pushing research thought experiments, hardware/OS deep-dive puzzles, and counterfactual edge cases without spoon-feeding solutions.

---

## 1. Visual Skeleton

```markdown
<!-- MODULE:inquiry section="<section_number>" topic="<topic_description>" depth="<1|2|3>" ... -->
> [!quote]- 💭 Open Inquiry & Thought Experiment: <Topic / Problem Title>
> **The Conceptual Puzzle**: <1-2 provocative questions probing an unexamined edge case, counterfactual scenario, or systemic friction where default assumptions fail.>
> 
> **Why This Matters**: <2-3 sentences explaining the systemic stakes, trade-offs, or latent architectural vulnerabilities exposed by this puzzle.>
> 
> **Direction to Investigate**:
> - *<Investigation Vector 1>*: <Guiding question or mechanism to research.>
> - *<Investigation Vector 2>*: <Specific protocol edge case, RFC, or hardware constraint to explore.>
```

## 2. Depth Matrix

| Depth | Scale / Scope | Components Included | Tone & Rigor | Fold Stance |
| :---: | :--- | :--- | :--- | :--- |
| **`1`** | 1 focused puzzle | 1 concise "What if?" puzzle probing a boundary condition | Provocative, accessible | Folded callout (`> [!quote]-`) |
| **`2`** | Puzzle + context | Conceptual puzzle + why it matters + 2 investigation vectors | Socratic, architectural | Folded callout (`> [!quote]-`) |
| **`3`** | Research thought experiment | Deep system puzzle + architectural failure mode + 3 research/experimentation vectors | Socratic, advanced | Folded callout (`> [!quote]-`) |

## 3. Strict Negative Invariants

- **Tag + Body Content Only**: Output ONLY the module tag and the generated callout directly below it.
- **No Headings or Quote Callouts**: NEVER generate markdown headings (`##`, `###`) or section intro quote callouts (`> [!quote]`).
- **No Spoon-Feeding**: Do NOT provide immediate trivial answers. The goal is to stimulate student inquiry and active reasoning.
- **No Distracting Tangents**: The inquiry must probe fundamental mechanics of the assigned topic, not random unrelated curiosities.
