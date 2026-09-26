---
# Module-specific overrides
depth: 3
max_tree_lines: 25
tone: null
detail_level: null
---

# Overview & Study Tree

Build the hierarchical study map and conceptual outline of the document.

---

## Hard Rules

  - The tree hierarchy is capped at <depth> levels:
    - Level 1: `Main Topic`
    - Level 2: `Topic` (becomes H1 header)
    - Level x: `Subtopic` (becomes H<x+1> header)
  - The total line count of the fenced tree block MUST NOT exceed <max_tree_lines> lines.
  - If the tree exceeds that, automatically prune 3rd-level subtopics
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
