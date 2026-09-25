---
name: skeleton
description: >-
  Builds the structural markdown skeleton of the lecture note based on the overview tree and source PDF.
  Inserts frontmatter, headings, verbatim quote callout descriptors, folded cite image callouts,
  and standardized module tags for all remaining conceptual components.
# Inherits: tone, detail_level, target_audience, foldable_callouts from create-notes/SKILL.md
include_toc: false
foldable_callouts: null
---

# Skeleton Skill (`/skeleton`)

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
> > [!quote] When talking about security, we are concerned about ==**bad events**== caused with ==**malicious intent**==. Security is a ==**non-functional property**==, comparable to quality, and is a ==**moving target**== because adversaries are intelligent and creative.
> ```

---

## 3. Verbatim Source Wording & Highlighting Loaded Terms

> [!IMPORTANT]
> **Strict Verbatim Source Wording (Ban on Invented Fancy Adjectives)**:
> - The words, technical terms, and adjectives in topic descriptions MUST strictly follow the source material (the slides/reading text) **verbatim** as much as possible.
> - **Do NOT default to sophisticated or flowery adjectives** (e.g., avoid inventing "heterogeneous distributed components", "asymmetric threat model", or "confidentiality perimeter collapses" unless those exact terms appear in the source).
> - Based on the verbatim source text, assess which words or adjectives are **loaded** (carry heavy conceptual weight and need to be explained or unpacked in that specific context).
> - Mark those loaded terms with `==**bold highlight**==` so downstream module skills can thoroughly dissect them.

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
> **Placeholder Syntax (No ID, Importance Added)**:
> Placeholders for text, math, code, and diagram modules MUST strictly follow this syntax:
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
- `graph`: Mermaid.js diagrams for workflows, architectures, state machines, threat trees, and DFDs with verb-object edge labels.
- `analogy`: In simple terms, concrete real-world analogies, and conceptual unpacking using `> [!tip]-`.
- `codeblock`: Replicated code or CLI commands from the PDF with detailed annotations (STRICT RULE: ONLY if present in PDF).
- `formula`: KaTeX equations with conceptual overbrace/underbrace labels, hybrid caption, formula breakdown, and practice callouts.
- `list`: Structured taxonomies, sequential procedures, hierarchical bulleted breakdowns, or takeaway checklists.
- `vs_comparison`: 2-way comparative analysis (Option A vs Option B) with trade-off matrices.
- `multi_comparison`: Multi-dimensional evaluation matrices across 3 or more paradigms/models.
- Appendices:
  - `<!-- MODULE:table_formulas importance="3" -->`
  - `<!-- MODULE:table_definitions importance="4" -->`
  - `<!-- MODULE:summary importance="4" -->`

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
   - Immediately under the header line (no blank line in between), insert introductory description inside `> [!quote]` using verbatim source phrasing with `==**loaded terms**==` bold-highlighted.
5. **Embed Assets in Folded Cite Callouts**:
   - Embed extracted slide images inside `> [!cite]- Slide N: Caption\n> ![[...]]`.
6. **Insert Standardized Module Placeholders**:
   - Insert standardized module tags (`example`, `graph`, `analogy`, `formula`, `list`, `vs_comparison`, `multi_comparison`).
7. **Insert Appendices Scaffolding**:
   - Include anchors:
     - `<!-- MODULE:table_formulas importance="3" -->`
     - `<!-- MODULE:table_definitions importance="4" -->`
     - `<!-- MODULE:summary importance="4" -->`
8. **Save Skeleton File**:
   - Save to `<output_dir>/NOTE - <Type> <Number> - <Topic>.md`.
