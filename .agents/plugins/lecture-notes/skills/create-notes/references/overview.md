---
# Module-specific overrides
depth_levels: 3
max_tree_lines: 25
tone: null
detail_level: null
---

# Overview & Study Tree Specification

Build the hierarchical study map and conceptual outline of the document.

---

## Hard Rules

- **Strict Hierarchy Depth (Max 3 Levels)**:
  - The tree hierarchy is strictly capped at 3 levels:
    - Level 1: `Main Topic`
    - Level 2: `Topic` (becomes H1 header)
    - Level 3: `Subtopic` (becomes H2 header)
- **25-Line Tree Cap Rule**:
  - The total line count of the fenced tree block MUST NOT exceed 25 lines.
  - If the tree exceeds 25 lines, automatically prune 3rd-level subtopics 
- **External / Expanded Topics Marker (`*`)**:
  - Any topic or foundational concept not explicitly mentioned in the source lecture slides/reading that is added for pedagogical completeness or context MUST have a trailing asterisk `*` (e.g. `Topic 2*` or `Subtopic A*`).

---

## Output Shape

````markdown
> Narrative intoduction of the main topic in 1–4 sentences.

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
