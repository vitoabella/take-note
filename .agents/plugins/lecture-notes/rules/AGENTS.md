# Lecture Notes Plugin Operational Rules

When executing tasks within this plugin or generating Obsidian lecture notes:

1. **Strict Verbatim Source Wording**:
   - All topic descriptions, summaries, adjectives, and technical terms MUST strictly adhere to the source material (the lecture slides and converted Markdown text) verbatim as much as possible.
   - Strictly prohibit invented "sophisticated" or flowery adjectives (e.g. avoid inventing phrases like "heterogeneous distributed components" or "confidentiality perimeter collapses" unless they appear verbatim in the source).
2. **Loaded Terms Highlighting**:
   - Assess which words or adjectives from the source text carry heavy conceptual weight (loaded terms needing detailed unpacking), and mark them with `==**bold highlight**==`.
3. **Clean Silent Erasure**:
   - When stopping or excluding elements that were previously included (e.g., Table of Contents, Document H1 Title, or pruned sections), cleanly erase that part completely.
   - Never write meta-commentary, explanatory disclaimers, or placeholder notices stating that an item was omitted or excluded.
4. **Header and Quote Callout Formatting**:
   - Under each section heading (`##`, `###`), the introductory description MUST be placed inside an Obsidian `> [!quote]` callout.
   - The `> [!quote]` callout MUST immediately follow the line of the header without an empty blank line in between:
     ```markdown
     ### Section Header
     > [!quote] Verbatim source description with ==**loaded terms**== highlighted.
     ```
5. **Visual Assets in Folded Cite Callouts**:
   - Extracted visual figures and diagrams must be embedded inside folded cite callouts:
     ```markdown
     > [!cite]- Slide <N>: <Caption/Title>
     > ![[<image_filename>.png]]
     ```
6. **Filesystem Boundaries**:
   - All generated notes and assets must strictly be placed within the designated output directory (`output/`).
