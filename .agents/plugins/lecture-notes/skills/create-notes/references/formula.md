---
tone: "rigorous"
foldable_callouts: true
---
# Formula Module Specification

Use this module to format mathematical formulations, probabilistic equations, physical laws, scoring rubrics, or cryptographic definitions, providing intuitive plain-English translations, algorithmic pseudocode, and sensitivity dynamics.

---

## 1. Visual Skeleton

```markdown
<!-- MODULE:formula section="<section_number>" topic="<topic_description>" depth="<1|2|3>" ... -->
**The Driving Question**: *"<1 sentence stating the fundamental dilemma, invariant, or practical question this formula resolves>"*

$$\overbrace{<Target_Output>}^{<conceptual\_role>} = \underbrace{<Input_Term\_1>}_{<operational\_meaning>} \times \overbrace{<Input\_Term\_2>}^{<operational\_meaning>}$$

> [!quote]- 🗣️ Plain-English & Pseudocode Translation
> - **In Plain Words**: "<Complete, grammatically correct English sentence expressing the equation in words without symbolic jargon: 'The Target equals the Input 1 multiplied by Input 2 for every...'>"
> - **In Pseudocode**:
>   ```python
>   def calculate_<target>(<input_1>, <input_2>):
>       return <input_1> * <input_2>
>   ```

> [!info]- Breakdown & Directional Levers
> - **Output Variable ($<Target\_Output>$)**: <Definition, measurement unit, and valid numerical domain.>
> - **Term 1 ($<Input\_Term\_1>$)**: <Definition, measurement unit, and baseline assumptions.>
> - **Term 2 ($<Input\_Term\_2>$)**: <Definition, measurement unit, and baseline assumptions.>
> - **Sensitivity & Levers**:
>   - *If $<Term\_1> \uparrow$*: $<Directional effect on output variable>$.
>   - *At the Extreme ($<Term\_1> \to 0$)*: $<System behavior and output at lower bound>$.
>   - *At the Extreme ($<Term\_1> \to \infty$)*: $<System behavior and output at upper bound>$.
> - **The #1 Exam Trap**: <The most common student misconception, invalid assumption, or computational failure mode.>

> [!example]- Conceptual Check
> **Q:** <Diagnostic question probing edge cases, limits, or trade-offs.>
> **A:** <Precise technical explanation resolving the diagnostic question.>
```

## 2. Depth Matrix

| Depth | Scale / Scope | Components Included | Tone & Rigor | Fold Stance |
| :---: | :--- | :--- | :--- | :--- |
| **`1`** | Equation + Words | Display math with conceptual braces + 1-sentence Plain Words translation | Intuitive, mental hook | Math & words open |
| **`2`** | Core Mechanics | Math + Plain Words + Pseudocode + Breakdown & Sensitivity levers | Standard analytical | Math open, breakdown folded (`-`) |
| **`3`** | Full Rigor & Traps | Driving Question + Math + Full Translations + Levers & Limits + Exam Trap + Conceptual Check | Formal, diagnostic | Math open, callouts folded (`-`) |

## 3. Strict Negative Invariants

- **Tag + Body Content Only**: Output ONLY the module tag and the formula/callouts directly below it.
  ```markdown
  <!-- MODULE:formula section="..." topic="..." depth="..." -->
  ...
  ```
- **No Headings or Quote Callouts**: NEVER generate markdown headings (`##`, `###`) or section intro quote callouts (`> [!quote]`).
- **No Conversational Wrapper**: Do not include conversational greetings or preamble text.
- **Mandatory Plain Words Translation**: Every formula MUST include a complete grammatical English sentence translation; never leave an equation unexplained.
- **No Bare Algebraic Labels**: Never label braces as generic algebraic roles like "numerator"; part labels must describe the conceptual role in the mechanism.
- **No Decorative Math**: Only generate formulas for genuine quantitative models or formal computational definitions present in the source.
