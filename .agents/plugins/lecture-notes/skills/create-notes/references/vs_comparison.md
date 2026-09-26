---
name: vs_comparison
description: >-
  Generates 2-way comparative analyses (A vs. B) with standard heading syntax,
  filled criteria tables, and decision heuristics.
# Inherits: tone, detail_level, target_audience, foldable_callouts from create-notes/SKILL.md
heading_style: "X vs Y"
foldable_callouts: true
---

# 2-Way Comparison Skill (`/vs_comparison`)

Use this skill to construct structured 2-way comparisons (`<!-- MODULE:vs_comparison ... -->`) marked in the lecture note skeleton.

---

## Core Guidelines & Format Reference

### 1. Heading Convention
- Exactly two compared entities MUST use the heading format:
  ```markdown
  ### X vs Y
  ```
  *(e.g., `### Security vs Reliability`, `### Open Boarding vs Closed Boarding`).*

### 2. Side-by-Side Comparison Table
- Always format the comparison table with Entity X and Entity Y as the columns:
  ```markdown
  | Dimension / Attribute | X | Y |
  | :--- | :--- | :--- |
  | Attribute 1 | ... | ... |
  | Attribute 2 | ... | ... |
  ```
- **Fill Every Cell**: Never leave empty cells or unannotated dashes. Every cell must provide substantive comparison.

### 3. Selection Heuristic Callout
- Accompany the table with a folded tip callout:
  ```markdown
  > [!tip]- Selection Heuristic / Key Trade-Off
  > - **Choose / Rely on X when**: Specific operational constraints or workload profiles.
  > - **Choose / Rely on Y when**: Specific operational constraints or workload profiles.
  ```

---

## Reference Template

```markdown
### Security vs Reliability

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
