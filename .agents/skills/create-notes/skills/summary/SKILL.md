---
name: summary
description: >-
  Synthesizes the entire lecture into a coherent narrative of fit inside a folded [!tldr] callout,
  strictly walking the Overview tree in order.
# Inherits: tone, detail_level, target_audience, foldable_callouts from create-notes/SKILL.md
structure: "overview_aligned"
foldable_callouts: true
---

# Narrative Summary Skill (`/summary`)

Use this skill to populate the master narrative summary (`<!-- MODULE:summary ... -->`) in the lecture note appendix.

---

## Core Guidelines & Format Reference

> [!IMPORTANT]
> **Summary Contract (Must Strictly Follow the Provided Overview Tree)**:
> The summary MUST follow every bullet below without exception.

### 1. Structure & Placement
- Place the summary exclusively under the heading:
  ```markdown
  ## Summary
  > [!tldr]
  > ...
  ```
- **Paragraph Breaks Allowed**: Start a new paragraph when the narrative shifts to a new major section. Separate paragraphs with a blank callout line (`>`). Prefer readable paragraphs over a wall of text.

### 2. Narrative of Fit (Not a Roster)
- Walk the Overview tree **top to bottom in order**.
- Write a **narrative of fit**, not an outline or list: Each **bold** topic must be introduced because the previous concept left a gap, limitation, dual, or practical need that the next idea addresses.
- Show how the pieces lock together into a continuous storyline.

### 3. Weight by Header Depth
- Spend ink proportional to body header hierarchy:
  - **H1 Topics**: Most detail and foundational motivation.
  - **H2 Subtopics**: Medium depth explaining the core mechanism.
  - **H3 / Leaves**: Brief explanatory clauses.
  - **Passing Mentions**: If a node was only named for completeness, **bold the name and move on** with zero further prose.
- **Strict Completeness**: Every Overview node must appear in the summary. Zero extra topics absent from the tree may be introduced.

---

## Reference Template

```markdown
## Summary
> [!tldr]
> Threat analysis begins with **Security Terminology & Foundations**, establishing that **What is Security?** addresses malicious intent rather than random failures, framing security as a moving target against adaptive adversaries. This demands **Fundamental Terminology & Quantitative Risk** to rigorously differentiate latent vulnerabilities from exploits and calculate financial risk. These concepts underpin **Security Goals: The CIA Triad & Beyond**, expanding classical confidentiality, integrity, and availability into granular access control and privacy. Recognizing **The Adversary & Threat Actors** partitions the operational environment into honest and dishonest participants, pinpointing privileged insiders as the most potent threat.
>
> Moving from foundations to practice requires structured **Viewpoints to Threat Analysis**, surveying the target system through **Multi-Dimensional Perspectives** to balance business assets against compliance and engineering realities. These views coalesce into **The 5-Step Productive Threat Modeling Process**, prioritizing iterative architectural understanding over dogmatic compliance forms.
>
> The power of this methodology is demonstrated in the **Case Study: Public-Transport Ticket App Threat Model**. Analyzing the **Mobile Ticket System Architecture** maps trust boundaries between passenger apps, vehicle operators, inspectors, and backend servers. This architecture operates under **Business Model & Boarding Economics**, where open-boarding transit creates severe financial trade-offs between inspection overhead and fare leakage. Cataloging **Asset & Actor Classification** reveals conflicting stakeholder motivations, explaining the proliferation of **Threat Vectors & Attack Scenarios**—including counterfeit ticket apps, ticket sharing, and abuse of human fallback recovery workflows. Managing these vectors requires rigorous **Operational Governance & Security Reporting** to prevent inspector quota abuse and deliver balanced, actionable remediation plans.
>
> Finally, security engineering organizes these insights into **Systematic Threat Modeling Frameworks**. While **Threat Trees & Taxonomies** hierarchically map attack paths, they serve primarily as post-analysis taxonomies. In contrast, **The STRIDE Methodology & Data Flow Diagrams** systematically evaluates component-level exposures across explicit trust boundaries. Discovered threats are prioritized using **Risk Assessment & The DREAD Model**, though arbitrary scoring models must be scrutinized. Ultimately, engineers must navigate **Assessment Pitfalls & Security 'Pixie Dust'**, avoiding the dangerous anti-pattern of sprinkling encryption onto fundamentally broken architectures.
```
