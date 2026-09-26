---
# Module-specific overrides
include_toc: false
foldable_callouts: null
---

# Skeleton & Scaffolding Specification

Use this skill to construct the structural markdown skeleton of the lecture note based on the hierarchical tree produced by `/overview` and the extracted assets from `/convert_pdf`.

---

## 1. Document Structure & Filename Rules

> [!IMPORTANT]
> **No Document H1 Title & Clean Silent Erasure**:
> - Do **NOT** insert a document H1 title (e.g., do NOT write `# Encrypting Stored Data` or `# NOTE - Lec 1 - Topic`).
> - The document begins directly with the YAML frontmatter, followed immediately by the Opener blockquote (`> ...`), then `# Overview` and the fenced tree, then section headings (`## 1. ...`).
> - Table of Contents is also omitted.
> - **Silent Clean Erasure Rule**: When stopping or excluding something that was previously included or requested (e.g., Table of Contents, document H1 title, or pruned sections), cleanly erase that part completely. **Never explicitly write that that part is omitted, removed, or excluded**. Do not leave placeholder notices like `*(Table of contents omitted)*` or `[Omitted]`.

**Standardized Filename Syntax**:
```text
NOTE - <Type> <Number> - <Topic>.md
```
- `Lec`: Lectures / Slide Decks (e.g., `NOTE - Lec 6 - Encrypting Stored Data.md`)
- `Quiz`: Exam / Quiz Reviews (e.g., `NOTE - Quiz 1 - Cryptography Review.md`)
- `Code`: Jupyter Notebooks / Code Walkthroughs (e.g., `NOTE - Code 1 - Socket Programming.md`)
- `Read`: Readings / Academic Papers (e.g., `NOTE - Read 1 - Bitcoin Whitepaper.md`)

---

## 2. Section Descriptions in Quote Callouts Immediately After Header

> [!IMPORTANT]
> **Quote Callout Immediately Below Header (No Blank Line)**:
> Under each section heading (`##`, `###`), do NOT output raw unstyled paragraphs and do NOT insert an empty blank line between the header and the callout.
> The `> [!quote]` callout MUST come immediately after the line of the header:
> ```markdown
> # Header
> > [!quote] <description>
> ```
> **Example**:
> ```markdown
> ### 1.1 What is Security?
> > [!quote] When talking about security, we are concerned about bad events caused with malicious intent. Security is a non-functional property, comparable to quality, and is a moving target because adversaries are intelligent and creative.
> ```

---

## 3. Verbatim Source Wording

> [!IMPORTANT]
> **Strict Verbatim Source Wording (Ban on Invented Fancy Adjectives)**:
> - The words, technical terms, and adjectives in topic descriptions MUST strictly follow the source material (the slides/reading text) **verbatim** as much as possible.
> - **Do NOT default to sophisticated or flowery adjectives** (e.g., avoid inventing "heterogeneous distributed components", "asymmetric threat model", or "confidentiality perimeter collapses" unless those exact terms appear in the source).

---

## 4. Visual Assets in Folded Cite Callouts (`> [!cite]-`)

> [!IMPORTANT]
> **Folded Cite Callouts for Images**:
> Visual assets from the PDF (diagrams, architectural schematics, flowcharts, photographs, UI screenshots) are extracted into `/assets` by `/convert_pdf`.
> - Do **NOT** paste raw `![[...]]` image links outside callouts.
> - Always embed images inside folded cite callouts matching this exact format:
>   ```markdown
>   > [!cite]- Slide <N>: <Short descriptive caption of what the slide shows>
>   > ![[<image_filename>.png]]
>   ```
> - **Example**:
>   ```markdown
>   > [!cite]- Slide 25: Operational modes of Windows BitLocker and authentication factors.
>   > ![[page_25_bitlocker_modes.png]]
>   ```

---

## 5. Standardized Module Placeholder Syntax

> [!IMPORTANT]
> **Placeholder Syntax with Depth Property**:
> Placeholders for text, math, code, and diagram modules MUST strictly follow this syntax:
> ```html
> <!-- MODULE:<MODULE_TYPE> section="<section_number>" topic="<topic_description>" depth="<1|2|3>" -->
> ```
>
> **Global Depth Scale (1–3)**:
> - `depth="1"`: Mentioned in passing; do not over-elaborate; simple, relatable, easy-to-remember terms.
> - `depth="2"`: Discussed, but not fleshed out; foldouts folded by default (`> [!...]-`); short phrases if no foldouts.
> - `depth="3"`: Explained in-detail in source (default).

### Allowed Module Types & Decision Matrix

| Module Type | When to Add (Inclusion Criteria) | When to Exclude (Exclusion Criteria) |
| :--- | :--- | :--- |
| `example` | Real-world case studies, incidents, deployed systems (e.g. BitLocker, HSL ticketing), concrete attack traces, or worked numerical problems in slides. | Purely abstract conceptual definitions without real-world context; or when an example merely restates the definition without demonstrating operational workflow. |
| `graph` | Multi-component architectures, protocol message flows, trust boundaries, state machines, or hierarchical threat trees/taxonomies. | Simple linear 2-step sequences better suited for numbered lists; isolated single-component definitions; or when no relationships or interactions exist. |
| `analogy` | Counter-intuitive, abstract, or conceptually difficult mechanisms (e.g. asymmetric key exchange, TPM measured boot) where a familiar physical metaphor clarifies the core idea. | Straightforward, self-explanatory, or descriptive topics (e.g., password expiration); or when an analogy would oversimplify or introduce misleading mental models. |
| `codeblock` | Verbatim source code, pseudocode, CLI terminal commands, or configuration files that appeared *explicitly* in the source PDF slides. | **STRICT RULE**: If no code or terminal commands appeared in the lecture PDF. Never hallucinate or synthesize speculative code snippets. |
| `formula` | Mathematical models, quantitative metrics, probabilistic risk equations, cryptographic definitions, or scoring formulas present in the source. | Purely qualitative discussions; or when an equation is merely symbolic decoration with no mathematical or operational meaning. |
| `list` | Slide bullet points enumerating properties, taxonomies, multi-step procedures, or unexpounded enumerations needing callout expansions. | Continuous narrative explanations that read better as paragraphs; or when items naturally form a comparative matrix or 2-way trade-off. |
| `vs_comparison` | Exactly two competing paradigms, technologies, architectures, or concepts explicitly contrasted in the lecture (e.g. Security vs Reliability, EFS vs BitLocker). | Comparing 3 or more entities (use `multi_comparison`); or when two items are complementary sequential steps in a pipeline rather than competing alternatives. |
| `multi_comparison` | Three or more candidate algorithms, models, tools, or frameworks evaluated across shared technical dimensions. | Comparing only two entities (use `vs_comparison`); or when entities lack common evaluation dimensions. |
| `quiz` | At the conclusion of a major section or conceptually rich topic to reinforce learning through self-assessment questions probing mechanisms, limiting cases, and trade-offs. | Trivial introductory sections, purely administrative slides, or sections where a quiz callout would be redundant with conceptual check practice callouts already present in formula/example modules. |

### Appendix Scaffolding
In the skeleton, place the section headings directly in the scaffolding under `## Appendix`:
```markdown
## Appendix

### Formulas
<!-- MODULE:table_formulas depth="3" -->

### Definition of Terms
<!-- MODULE:table_definitions depth="3" -->

### Summary
<!-- MODULE:summary depth="3" -->
```
*(Note: If the lecture contains no mathematical or cryptographic formulas, omit `### Formulas` and its placeholder tag completely).*

---

## 6. Execution Steps for the Agent

1. **Read Converted Markdown**:
   - Inspect the converted Markdown file produced by `/convert_pdf` (and check `<output_dir>/assets/` for extracted images).
2. **Read Overview Outline**:
   - Inspect the outline produced by `/overview` to determine the complete section hierarchy.
3. **Generate Frontmatter & Overview (NO Document H1 Title)**:
   - Insert Obsidian YAML frontmatter (title, course, instructor, year, tags, source).
   - Insert Opener Blockquote and `# Overview` fenced tree.
4. **Insert Section Headings & Quote Callout Descriptions**:
   - For every section in the outline, write markdown headings (`##`, `###`).
   - Immediately under the header line (no blank line in between), insert introductory description inside `> [!quote]` using verbatim source phrasing.
5. **Embed Assets in Folded Cite Callouts**:
   - Embed extracted slide images inside `> [!cite]- Slide N: Caption\n> ![[...]]`.
6. **Insert Standardized Module Placeholders**:
   - Insert standardized module tags with appropriate depth (`depth="1|2|3"`).
7. **Insert Appendices Scaffolding**:
   - Under `## Appendix`, insert `### Formulas`, `### Definition of Terms`, and `### Summary` with their respective tags.
8. **Save Skeleton File**:
   - Save to `<output_dir>/NOTE - <Type> <Number> - <Topic>.md`.
