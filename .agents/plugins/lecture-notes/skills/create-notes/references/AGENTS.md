# Module Reference Specification Rules

Whenever modifying existing module reference specifications or adding new ones in this directory (`references/`):

1. **Strict 3-Part Domain-Agnostic Schema**:
   Every module specification file (`references/<module>.md`) MUST adhere to the following exact 3-section structure:
   - `## 1. Visual Skeleton`:
     - Must begin with the module tag placeholder:
       `<!-- MODULE:<module_type> section="<section_number>" topic="<topic_description>" depth="<1|2|3>" ... -->`
     - Must use universal `<variable>` placeholders for all structural elements (e.g., `<concept>`, `<term>`, `<state_A>`, `<entity_1>`).
   - `## 2. Depth Matrix`:
     - Must be a standardized 5-column Markdown table with columns:
       `| Depth | Scale / Scope | Components Included | Tone & Rigor | Fold Stance |`
     - Must define explicit criteria for **`1`**, **`2`**, and **`3`**.
   - `## 3. Strict Negative Invariants`:
     - Must enforce **Tag + Body Content Only** (the worker module outputs only the comment tag and content directly below).
     - Must explicitly forbid markdown headings (`##`, `###`) and section intro quote callouts (`> [!quote]`).
     - Must forbid conversational commentary, greetings, or wrappers.
     - Must enforce verbatim source grounding.

2. **Prohibit Domain-Specific Exemplars (No Section 4)**:
   - Module specifications MUST remain 100% domain-agnostic.
