---
# Module-specific overrides
tone: "rigorous"
include_derivations: true
foldable_callouts: true
---

# Formula Module Specification

Use this skill to populate mathematical, quantitative, and cryptographic equation modules (`<!-- MODULE:formula ... -->`) in the lecture note skeleton.

---

## Core Guidelines & Format Reference

### 1. `$$ ... $$` with Conceptual `\overbrace` and `\underbrace` Part Labels
- Brace meaningful chunks of the expression (terms, factors, operators carrying a distinct idea)—not merely algebraic roles like "numerator" or "denominator".
- Part labels must state the **conceptual role** that chunk plays in the mechanism.
- Good: `\underbrace{\text{Risk}}_{\text{financial exposure}} = \overbrace{P(\text{attack})}^{\text{threat likelihood}} \times \underbrace{\text{Damage}}_{\text{monetary impact in €}}`

### 2. Caption (Required, immediately under `$$`)
- One italic line on its own line: `*...*` (no quotation marks).
- Must restate the equation in words or as a **hybrid** of words + math, preserving operators and structure.

### 3. `> [!info]- Breakdown of the formula`
- **Opening**: What the formula computes/decides and how it serves the surrounding topic.
- **Symbol Analysis**: Plain-text definition of each variable, symbol, and unit.
- **Braced-Section Comparative Effects**: Explain how each piece drives the result.
- **Assumptions & Bounds**: Domain restrictions (e.g., $P \in [0, 1]$, currency scale).

### 4. `> [!example]-` Practice Callout
- **Conceptual Check** (default): 2–3 short Q&As probing meaning, limiting cases, and trade-offs formatted as **Q:** / **A:**.
- **Computational Solve** (if algebraic): Worked numeric or symbolic solve formatted with **Problem:** / **Answer:**.

---

## Depth Specification

- **`depth="1"` (Mentioned in Passing)**:
  - Compact display formula only (`$$ ... $$` with basic conceptual braces and italic caption).
  - Omit breakdown and practice check callouts.
- **`depth="2"` (Discussed, but not fleshed out)**:
  - Display formula + caption + folded breakdown callout (`> [!info]- Breakdown of the formula`).
  - Omit practice check callout.
- **`depth="3"` (Explained in-detail in source - Default)**:
  - Complete mandatory 4-part structure: display formula with conceptual over/underbraces, italic caption, folded breakdown callout, and folded practice check / computational solve.

---

## Expected Output Format

> [!IMPORTANT]
> Worker modules output **ONLY** the body content below. Do not generate section headings (`##`, `###`) or introductory quote callouts (`> [!quote]`).

```markdown
$$\underbrace{\text{Risk}}_{\text{expected annual loss}} = \overbrace{P(\text{Attack})}^{\text{probability of exploit event}} \times \underbrace{\text{Damage}}_{\text{financial impact in €}}$$
*Quantitative Risk = probability of attack occurrence multiplied by financial damage in euros*

> [!info]- Breakdown of the formula
> Computes the expected monetary loss per unit time to prioritize security mitigations based on financial return on investment (ROI).
> - $\text{Risk}$: Expected annualized loss incurred by the organization (measured in € / year).
> - $P(\text{Attack})$: Empirical or subjective probability that a specific threat actor successfully identifies and executes an exploit ($0 \le P \le 1$).
> - $\text{Damage}$: Direct and indirect monetary cost of security failure, including asset replacement, regulatory fines, and reputation loss.
> - **Comparative Dynamics**:
>   - High-probability, low-impact events produce predictable, linear losses manageable via operational reserves.
>   - Low-probability, catastrophic events produce non-linear losses that threaten systemic solvency, warranting heavy proactive defenses.

> [!example]- Conceptual Check
> **Q:** Why do numerical risk values (e.g., "Risk level = 0.42") often fail to provide actionable security guidance in software engineering?
> **A:** Probability estimates for creative human adversaries are subjective and lack historical stationarity. Multiplying an arbitrary likelihood score by a rough severity rating yields a pseudo-precise number that obscures the underlying threat mechanism. Threat modeling is more productive when used to prioritize relative ordering rather than computing absolute euro figures.
```
