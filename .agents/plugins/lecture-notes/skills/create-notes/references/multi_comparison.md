---
name: multi_comparison
description: >-
  Generates multi-dimensional matrix tables and comparative evaluations across 3 or more
  algorithms, architectures, or paradigms.
# Inherits: tone, detail_level, target_audience, foldable_callouts from create-notes/SKILL.md
heading_style: "Side-by-side comparison"
foldable_callouts: true
---

# Multi-Option Comparison Skill (`/multi_comparison`)

Use this skill to populate multi-dimensional comparison tables across 3 or more candidate entities (`<!-- MODULE:multi_comparison ... -->`) in the lecture note skeleton.

---

## Core Guidelines & Format Reference

### 1. Heading Convention
- Always use the standardized heading: `### Side-by-side comparison`.

### 2. Table Construction Rules
- Hard Rule: **Fill every single table cell**. Never leave empty cells or unexplained dashes.
- Include concrete, technical evaluation dimensions: Primary Goal, Adversarial Invariant, Overhead, Typical Failure Mode.
- **Matrix Duals / Encodings**: When comparing access-control or dual models (e.g., ACL vs Capability), emphasize the relevant perspective with bold/highlighted cells.

### 3. Synthesis & Pareto Frontier
Follow the matrix with a concise breakdown specifying:
- Which option is optimal under what specific resource or operational constraints.
- Why no single option dominates all evaluation dimensions.

---

## Reference Template

```markdown
### Side-by-side comparison

| Evaluation Dimension | STRIDE | DREAD | Risk = P × Damage |
| :--- | :--- | :--- | :--- |
| **Primary Paradigm** | Component-level threat categorization | Quantitative threat ranking heuristic | Classical economic risk formula |
| **Input Artifact** | Data Flow Diagram (DFD) with trust boundaries | Discovered threat candidate | Probability distribution & financial loss |
| **Dimensions Evaluated** | 6 threat classes (S, T, R, I, D, E) | 5 criteria (Damage, Reproducibility, Exploitability, Users, Discoverability) | Likelihood $\times$ Monetary impact (€) |
| **Scoring Output** | Qualitative presence/absence matrix | Numerical score (e.g., 1–10 per dimension) | Single expected financial value |
| **Major Strength** | Systematic coverage across software boundaries | Structured multi-factor deliberation | Direct alignment with executive business budgets |
| **Primary Pitfall** | Identifies threats but does not prioritize | Arbitrary numerical scales masquerading as precision | Adversaries lack historical probability data |

> [!info]- Architectural Trade-Off Synthesis
> - **Use STRIDE** during system design and architecture review to uncover latent component vulnerabilities.
> - **Use Risk = P × Damage** when justifying security capital allocation and compliance expenditures to executive management.
> - **Caution on DREAD**: Treat DREAD numerical scores as rough relative rankings rather than objective mathematical truths.
```
