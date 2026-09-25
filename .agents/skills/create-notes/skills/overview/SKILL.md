---
name: overview
description: >-
  Subject-matter expert. Builds the hierarchical study map and conceptual tree for the document.
# Inherits: tone, detail_level, target_audience from create-notes/SKILL.md
depth_levels: 3
max_tree_lines: 25
tone: null
detail_level: null
---

# Overview Skill (`/overview`)

Subject-matter expert. Build the hierarchical study map and conceptual outline of the document.

## Configuration Inheritance

> [!NOTE]
> Inherits `tone`, `detail_level`, and `target_audience` from `create-notes/SKILL.md` unless explicitly populated above.

---

## Hard Rules

- **Mandatory Triple Backtick Enclosure**:
  - The hierarchical tree MUST ALWAYS be enclosed in opening and closing triple backticks (` ``` `):
    ````text
    # Overview
    ```
    Main Topic
     ├── Topic 1
     │     ├── Subtopic A
     │     └── Subtopic B*
     └── Topic 2
    ```
    ````
  - Both the opening ` ``` ` and closing ` ``` ` MUST be present on their own separate lines. Never output the tree as bare unquoted text or inside standard blockquotes.
- **Strict Hierarchy Depth (Max 3 Levels)**:
  - The tree hierarchy is strictly capped at 3 levels:
    - Level 1: `Main Topic`
    - Level 2: `Topic` (becomes H1/H2 header in PASS 2)
    - Level 3: `Subtopic` (becomes H2/H3 header in PASS 2)
  - **NEVER output 4th-level leaf nodes**. Prune all deeper branches so the tree stops cleanly at Subtopic.
- **25-Line Tree Cap Rule**:
  - The total line count of the fenced tree block MUST NOT exceed 25 lines.
  - If the tree exceeds 25 lines, automatically prune 3rd-level subtopics (collapsing that section to Main $\rightarrow$ Topic) until the total tree length is $\le 25$ lines.
- **Silent Clean Erasure**:
  - When subtopics or branches are pruned or excluded, cleanly erase them without writing any meta-commentary, explanatory disclaimers, or placeholder notices stating that items were omitted.
- **External / Expanded Topics Marker (`*`)**:
  - Any topic or foundational concept not explicitly mentioned in the source lecture slides/reading that is added for pedagogical completeness or context MUST have a trailing asterisk `*` (e.g. `Topic 2*` or `Subtopic A*`).
- **The Tree is the Contract for the Note**:
  - Format: (1) Opener blockquote (1–3 sentences, or 2–4 if bridging a preceding lecture), (2) `# Overview`, (3) exactly one fenced tree block.
  - Every tree node MUST become a header in the body note. Do not list nodes you will not write.
  - Do not emit PASS 1 as a standalone stop; paste this opener + tree into the finished note and keep writing.
- **Tree Formatting Constraints**:
  - No sources, page numbers, or slide numbers.
  - Do not number headings inside the tree (no "1. Topic").
  - Reorganize into a logical hierarchy even if slide order differs.
  - Tree characters: strictly use standard box-drawing `├──`, `│`, `└──`.

---

## Output Shape

````markdown
> Narrative definition of the whole lecture topic in 1–3 sentences (2–4 if bridging a preceding lecture).

# Overview
```
Main Topic
 ├── Topic 1
 │     ├── Subtopic A
 │     └── Subtopic B*
 ├── Topic 2
 │     ├── Subtopic C
 │     └── Subtopic D
 └── Topic 3*
       └── Subtopic E
```
````
