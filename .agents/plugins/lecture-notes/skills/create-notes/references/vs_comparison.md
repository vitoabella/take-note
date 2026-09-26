---
# Module-specific overrides
foldable_callouts: true
---

# 2-Way Comparison Module Specification

Use this skill to construct structured 2-way comparisons (`<!-- MODULE:vs_comparison ... -->`) marked in the lecture note skeleton.

---

## Core Guidelines & Format Reference

### 1. Side-by-Side Comparison Table
- Always format the comparison table with Entity X and Entity Y as the columns:
  ```markdown
  | Dimension / Attribute | X | Y |
  | :--- | :--- | :--- |
  | Attribute 1 | ... | ... |
  | Attribute 2 | ... | ... |
  ```
- **Fill Every Cell**: Never leave empty cells or unannotated dashes. Every cell must provide substantive comparison.

### 2. Selection Heuristic Callout
- Accompany the table with a folded tip callout:
  ```markdown
  > [!tip]- Selection Heuristic / Key Trade-Off
  > - **Choose / Rely on X when**: Specific operational constraints or workload profiles.
  > - **Choose / Rely on Y when**: Specific operational constraints or workload profiles.
  ```

---

## Depth Specification

- **`depth="1"` (Mentioned in Passing)**:
  - 3-row compact comparison table highlighting high-level contrasts using simple, relatable terminology.
  - Omit the selection heuristic callout.
- **`depth="2"` (Discussed, but not fleshed out)**:
  - Standard comparison table (4–5 rows) covering primary operational dimensions.
  - Includes folded selection heuristic callout (`> [!tip]- Selection Heuristic / Key Trade-Off`) using concise phrases.
- **`depth="3"` (Explained in-detail in source - Default)**:
  - Exhaustive multi-attribute comparison table (6+ rows) analyzing technical invariants, threat behavior, and failure modes.
  - Includes a comprehensive folded trade-off insight callout (`> [!tip]- Trade-Off & Integration Insight`) dissecting architectural edge cases and integration guidance.

---

## Expected Output Format

> [!IMPORTANT]
> Worker modules output **ONLY** the body content below. Do not generate section headings (`##`, `###`) or introductory quote callouts (`> [!quote]`).

```markdown
| Dimension / Attribute | Security Engineering | Reliability Engineering |
| :--- | :--- | :--- |
| **Nature of Threat** | Intelligent, adaptive adversaries with malicious intent | Random physical faults, environmental decay, and benign design errors |
| **Probability Distribution** | Non-stationary, strategic, and adversarial (game-theoretic) | Stationary statistical distributions (e.g., Poisson processes, MTBF) |
| **System Property** | Non-functional, qualitative property (difficult to verify) | Quantitative metric (uptime percentage, failure rates) |
| **Behavior Under Pressure** | Adversary actively probes for the weakest path | Failures occur uniformly across probabilistic component lifetimes |
| **Goal / Invariant** | Prevent unauthorized bad things despite active subversion | Ensure normal operations continue across expected random stresses |

> [!tip]- Trade-Off & Integration Insight
> - **Prioritize Security Engineering** whenever external untrusted parties can interact with system interfaces, APIs, or physical assets. A system can be 99.999% reliable under benign workloads while remaining 100% vulnerable to a single malicious packet.
> - **Prioritize Reliability Engineering** for internal fault containment, hardware redundancy, and gracefully degrading services under natural physical faults.
```
