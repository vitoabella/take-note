---
name: overview
description: >-
  Subject-matter expert. Builds the hierarchical study map and conceptual tree for the document.
# Inherits: tone, detail_level, target_audience from create-notes/SKILL.md
depth_levels: 3
tone: null
detail_level: null
---

# Overview Skill (`/overview`)

Subject-matter expert. Build the hierarchical study map.

## Configuration Inheritance

> [!NOTE]
> Inherits `tone`, `detail_level`, and `target_audience` from `create-notes/SKILL.md` unless explicitly populated above.

---

## Hard Rules

- **The tree is the contract for PASS 2**: (1) opener blockquote (1–3 sentences, or 2–4 if bridging a preceding lecture per Preceding lecture), (2) `# Overview`, (3) one fenced tree. Do not emit PASS 1 as a standalone stop; paste this opener + tree into the finished note and keep writing.
- **No sources, page numbers, or slide numbers**.
- **Do not number headings inside the tree** (no "1. Topic").
- **Nest at most 3 levels under the main topic** (Main -> Topic -> Subtopic -> leaf).
- **Reorganize into a logical hierarchy** even if slide order differs.
- **Every tree node MUST become an H1/H2/H3 in PASS 2**. Do not list nodes you will not write.
- **Mark important-but-thin/missing topics with trailing `*`** (e.g. `Type 3*`). Prefer `*` when slides are thin.
- **Tree characters**: use box-drawing `├──`, `│`, `└──` as in the shape below.
- **Optionally state the planned output path/title** in the agent reply if helpful. Do not stop after the tree.

---

## Output Shape

````markdown
> Narrative definition of the whole lecture topic in 1–3 sentences (2–4 if bridging a preceding lecture).

# Overview
```
Main Topic
 ├── Topic 1
 │     ├── Subtopic A
 │     │     ├── Leaf 1
 │     │     ├── Leaf 2
 │     │     └── Leaf 3*
 │     └── Subtopic B
 └── Topic 2
       └── ...
```
````
