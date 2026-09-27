---
callout_type: "tip"
foldable_callouts: true
---

# Analogy Module Specification

Use this module to clarify counter-intuitive, abstract, or conceptually difficult mechanisms by mapping them to familiar physical or real-world mental models.

---

## 1. Visual Skeleton

```markdown
<!-- MODULE:analogy section="<section_number>" topic="<topic_description>" depth="<1|2|3>" ... -->
> [!tip]- Analogy: <Familiar Metaphor Title>
> Think of <abstract_concept> like <familiar_physical_scenario>:
> 
> - **The Metaphor**: <2-3 sentences explaining the familiar everyday mechanism in plain terms.>
> - **Structural Mapping**:
>   - *<Metaphor Component A>*: Maps to `<Technical Concept A>`.
>   - *<Metaphor Component B>*: Maps to `<Technical Concept B>`.
>   - *<Metaphor Component C>*: Maps to `<Technical Concept C>`.
> - **Where the Analogy Breaks Down**: <1-2 sentences explicitly identifying the boundary where the physical comparison fails to hold technically.>
```

## 2. Depth Matrix

| Depth | Scale / Scope | Components Included | Tone & Rigor | Fold Stance |
| :---: | :--- | :--- | :--- | :--- |
| **`1`** | 1 concise paragraph | Metaphor summary only; omit mapping and breakdown | Simple, relatable | Folded callout (`> [!tip]-`) |
| **`2`** | 2–3 mapping items | Metaphor + bulleted structural mapping | Digestible, grounded | Folded callout (`> [!tip]-`) |
| **`3`** | Full tripartite model | Metaphor + granular mapping + explicit breakdown boundary | Rigorous, boundary-aware | Folded callout (`> [!tip]-`) |

## 3. Strict Negative Invariants

- **Tag + Body Content Only**: Output ONLY the module tag and the generated callout directly below it.
  ```markdown
  <!-- MODULE:analogy section="..." topic="..." depth="..." -->
  > [!tip]- Analogy: ...
  ```
- **No Headings or Quote Callouts**: NEVER generate markdown headings (`##`, `###`) or section intro quote callouts (`> [!quote]`).
- **No Conversational Wrapper**: Do not include conversational greetings or preamble text.
- **No Misleading Mental Models**: The analogy must accurately preserve structural invariants; never oversimplify to the point of technical falsehood.
