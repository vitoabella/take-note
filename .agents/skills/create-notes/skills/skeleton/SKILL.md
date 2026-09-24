---
name: skeleton
description: >-
  Builds the structural markdown skeleton of the lecture note based on the outline and source PDF.
  Inserts frontmatter, TOC, headings, highlighted topic descriptors, and standardized module tags
  for all examples, diagrams, images, graphs, and figures respective to their topics.
# Inherits: tone, detail_level, target_audience, foldable_callouts from create-notes/SKILL.md
# Populated overrides & skill-specific settings:
foldable_callouts: null
---

# Skeleton Skill (`/skeleton`)

Use this skill to construct the structural markdown skeleton of the lecture note based on the hierarchical outline produced by `/overview` and the visual/illustrative assets found in the source PDF.

---

## 1. Mandatory Visual & Illustrative PDF Audit Rule

> [!IMPORTANT]
> **Audit the Source PDF for All Visuals & Examples**:
> While building the skeleton, you MUST inspect the source PDF using the native `view_file` tool to identify every visual and illustrative asset used in the lecture slides. For every single one found, you MUST insert a corresponding module placeholder tag directly under the respective section heading:
>
> 1. **Examples (`example`)**: Place for every concrete case study, real-world attack scenario, walkthrough, operational procedure, or application scenario (e.g., public transit ticket app, fake ticket app mechanics, recovery process abuse).
> 2. **Diagrams & Architectures (`graph` or `image`)**: Place for every architectural schematic, component interaction, and system topology diagram (e.g., mobile ticketing architecture diagram).
> 3. **Graphs & Trees (`graph`)**: Place for every hierarchical tree, threat tree, state machine, protocol sequence flow, or Data Flow Diagram (DFD) rendered via Mermaid.js (e.g., fake ticket threat tree, high-level DFD with trust boundaries).
> 4. **Images, Photos & Figures (`image`)**: Place for every photograph, visual metaphor, UI screenshot, or schematic illustration (e.g., photo of bicycle chained to short bollard, UI screenshot).
> 5. **Analogies (`analogy`)**: Place for conceptual analogies and intuitive mental models (e.g., security pixie dust analogy).
> 6. **Code Blocks (`codeblock`)**: Place ONLY if source code snippets or terminal CLI commands are explicitly present in the source PDF.
> 7. **Formulas (`formula`)**: Place for all mathematical equations, quantitative metrics, or risk definitions (e.g., quantitative risk formula).
> 8. **Comparisons (`vs_comparison` / `multi_comparison`)**: Place for 2-way trade-offs (e.g., security vs. reliability, open vs. closed boarding) or multi-criteria matrices (e.g., risk models).
>
> **Respective Placement Constraint**: Every module tag MUST be anchored in the exact section corresponding to its topic. Never omit, lump together, or misplace any visual or illustrative element from the PDF.

---

## 2. Standardized Module Placeholder Syntax

> [!IMPORTANT]
> **Placeholder Syntax (No ID, Importance Added)**:
> Every placeholder marker MUST strictly follow this syntax:
> ```html
> <!-- MODULE:<MODULE_TYPE> section="<section_number>" topic="<topic_description>" importance="<1-4>" -->
> ```
> *(Note: The `id` attribute is removed. The `importance` attribute from 1 to 4 is required).*
>
> **Importance Scale (1–4)**:
> - `importance="1"`: Supplementary / contextual details (nice-to-know, edge cases).
> - `importance="2"`: Standard topic component (normal lecture depth).
> - `importance="3"`: Core concept, key mechanism, or significant diagram/example (essential exam/production knowledge).
> - `importance="4"`: Critical foundational invariant, primary architectural diagram, or core case study anchor (must be thoroughly dissected).

### Allowed Module Types
- `example`: Concrete real-world scenarios, case studies, walkthrough scenarios, attack vectors, and operational examples from the PDF.
- `graph`: Mermaid.js diagrams for workflows, architectures, state machines, threat trees, and DFDs.
- `image`: Structured Obsidian figure callouts, ASCII schematics, photographs, and UI screenshots.
- `analogy`: In simple terms, concrete real-world analogies, and conceptual unpacking.
- `codeblock`: Replicated code or CLI commands from the PDF with detailed annotations (ONLY if present in PDF).
- `formula`: KaTeX equations, variable breakdown tables, and mathematical derivations.
- `list`: Structured taxonomies, sequential procedures, hierarchical bulleted breakdowns, or takeaway checklists.
- `vs_comparison`: 2-way comparative analysis (Option A vs Option B) with trade-off matrices.
- `multi_comparison`: Multi-dimensional evaluation matrices across 3 or more paradigms/models.
- Appendices:
  - `<!-- MODULE:table_formulas importance="3" -->`
  - `<!-- MODULE:table_definitions importance="4" -->`
  - `<!-- MODULE:summary importance="4" -->`

---

## 3. Topic Description Highlighting Rule

> [!IMPORTANT]
> **Bold & Highlight Meaningful Descriptors**:
> In the 1–2 sentence narrative description under each section heading in the skeleton:
> - Bold and highlight (enclosed in `==**...**==`) key adjectives, noun phrases, and descriptor words that carry heavy meaning and need to be dissected.
> - **Example**: *"Certificates are public tokens rather than encrypted secrets, and a certificate alone does not authenticate an identity without ==**cryptographic proof**== of private key possession."*
> - **Example**: *"==**Scalable trust delegation**== relies on hierarchical trees of CAs originating from ==**trusted root authorities**== down through intermediate sub-CAs to end-entity leaf certificates."*
> - **Example**: *"Security is a ==**non-functional, qualitative property**== of a system continuously challenged by ==**intelligent, adaptive adversaries**==."*

---

## 4. PDF Grounding Reference Patterns

When auditing the lecture PDF, align module tags with the visual and illustrative patterns present in the material. For example, in a threat analysis lecture:
- **Architecture Diagram (Slide 14)** $
ightarrow$ `<!-- MODULE:graph section="3.1" topic="Mobile ticket system architecture showing passenger, app, inspector, backend APIs, and trust boundaries" importance="4" -->`
- **Economic/Boarding Trade-Off (Slide 15)** $
ightarrow$ `<!-- MODULE:vs_comparison section="3.2" topic="Open boarding vs closed boarding security, throughput, and financial trade-offs" importance="3" -->`
- **Case Study Example (Slide 15)** $
ightarrow$ `<!-- MODULE:example section="3.2" topic="Public transport business model: 50% public subsidy and purchaser-provider regulation" importance="2" -->`
- **Attack Implementation Examples (Slide 19)** $
ightarrow$ `<!-- MODULE:example section="3.4" topic="Passenger attack scenarios: fake ticket apps replicating animations, passback, timesharing, and relay" importance="3" -->`
- **Recovery Abuse Example (Slide 20)** $
ightarrow$ `<!-- MODULE:example section="3.4" topic="Misuse of failure recovery processes: dead battery excuse and borrowing tickets to cancel penalty fees" importance="3" -->`
- **Threat Tree Diagram (Slide 29)** $
ightarrow$ `<!-- MODULE:graph section="4.1" topic="Hierarchical threat tree taxonomy decomposing fake ticket attacks into insider fraud and external cybercrime" importance="3" -->`
- **Data Flow Diagram (Slide 32)** $
ightarrow$ `<!-- MODULE:graph section="4.2" topic="High-level Data Flow Diagram (DFD) for the transport ticket app with trust boundaries between authority, provider, and operator" importance="4" -->`
- **Analogy (Slide 36)** $
ightarrow$ `<!-- MODULE:analogy section="4.4" topic="Security pixie dust analogy: sprinkling encryption onto systems without understanding the threat model" importance="3" -->`
- **Photo / Visual Figure (Slide 37)** $
ightarrow$ `<!-- MODULE:image section="4.4" topic="Security pixie dust visual figure: photo of bicycle chained to a short removable bollard" importance="3" -->`

---

## 5. Execution Steps for the Agent

1. **Read Overview Outline**:
   - Inspect the outline produced by `/overview` to determine the complete section hierarchy.

2. **Audit Source PDF for All Visuals & Illustrative Content**:
   - Use `view_file` to review all slides/pages of the source PDF.
   - Note every diagram, flowchart, photo, UI screenshot, case-study example, attack scenario, and equation.

3. **Generate Frontmatter & Header**:
   - Insert Obsidian YAML frontmatter (title, tags, source, etc.).
   - Insert document H1 title and Table of Contents (if `include_toc` is true).

4. **Insert Section Headings & Enriched Topic Descriptions**:
   - For every section in the outline, write the markdown heading (`##`, `###`).
   - Write a 1-2 sentence introductory description for the section.
   - Apply the bold & highlight rule: wrap high-meaning adjectives, descriptors, and critical concepts in `==**...**==`.

5. **Insert Standardized Module Placeholders**:
   - Under each section heading, insert module placeholders for:
     - All mapped concepts from the outline.
     - All examples, diagrams, images, graphs, and figures identified in the PDF for that section.
   - Use standardized syntax with `section`, `topic`, and `importance` (1–4), omitting `id`.

6. **Insert Appendices Scaffolding**:
   - Include anchors:
     - `<!-- MODULE:table_formulas importance="3" -->`
     - `<!-- MODULE:table_definitions importance="4" -->`
     - `<!-- MODULE:summary importance="4" -->`

7. **Save Skeleton File**:
   - Save the note file to the output directory (e.g. `<output_dir>/<Title>.md`).
