---
name: image
description: >-
  Handles visual figures, slide graphics, screenshots, and photos using standard
  unreproducible figure callouts, verified vault embeds, or clean ASCII schematics.
# Inherits: tone, detail_level, target_audience, foldable_callouts from create-notes/SKILL.md
include_ascii_schematic: true
foldable_callouts: true
---

# Image Skill (`/image`)

Use this skill to capture, anchor, and explain visual graphics, slide figures, photos, and UI screenshots (`<!-- MODULE:image ... -->`) in the lecture note skeleton.

---

## Core Guidelines & Format Reference

### 1. Figure Priority Rules
When handling visual figures from the source PDF:
1. **Reconstructable Figures**: If a figure can be faithfully rebuilt as a Mermaid diagram or Markdown table, prefer those formats (`graph` / `multi_comparison`).
2. **Unreproducible Slide Graphics (Photos, Complex Art, Legacy Screenshots)**:
   Do **NOT** invent fictitious `![[...]]` wikilinks to files not in the vault. Instead, insert the standardized unreproducible figure callout:
   ```markdown
   > [!info]- Figure from slides (not reproduced)
   > Source: `filename.pdf`, slide/page N.
   > Shows: one-line description of what to look for in the deck.
   ```
3. **Verified Vault Image**: If an actual image asset exists in the vault/output folder, use `![[image-name.png]]` followed by an italic caption.
4. **Structural Schematics**: When appropriate, supplement with a clean ASCII / Unicode box-drawing diagram inside a `text` block.

### 2. Required Figure Analysis
Underneath every figure callout or schematic, include a 2–3 bullet analytical breakdown:
- What the visual depicts.
- Key structural boundaries, components, or failure modes shown.
- Why the figure matters to the surrounding conceptual thesis.

---

## Reference Template

```markdown
> [!info]- Figure from slides (not reproduced)
> Source: `Threat analysis - Tuomas Aura (Aalto University 2023).pdf`, slide 37.
> Shows: Photograph of a red bicycle securely chained and padlocked around a short bollard that is shorter than the bicycle frame.

> [!info]- Visual Analysis & Significance
> - **The Visual Paradox**: The bicycle owner invested in an expensive, hardened steel chain and padlock, but fastened it around a waist-high post from which the entire bicycle can be lifted off in seconds without breaking the lock.
> - **Architectural Anti-Pattern**: Represents "security pixie dust"—deploying high-strength cryptographic mechanisms in isolation without analyzing the full system geometry and physical attack vectors.
```
