---
foldable_callouts: false
---

# Skeleton & Scaffolding

The structure of the lecture note based on the hierarchical tree produced by `/overview` and the extracted assets from `/convert_pdf`.

---

## Verbatim Source Wording

- The technical terms, and adjectives in topic headers and descriptions MUST strictly follow the source material (the slides/reading text) however you may rephrase to form a cohesive narrative.
- **Do NOT default to sophisticated or flowery adjectives** (e.g., avoid inventing "heterogeneous distributed components",, or "confidentiality perimeter collapses" unless those exact terms appear in the source).

---

## YAML Frontmatter

```markdown
---
date_created:
course_code:
topic:
---
```

---
## Visual Assets in Folded Cite Callouts (`> [!cite]-`)

> [!IMPORTANT]
> **Folded Cite Callouts for Images**:
> Visual assets from the PDF (diagrams, architectural schematics, flowcharts, photographs, UI screenshots) are extracted into `/assets` by `/convert_pdf`.
> - Do **NOT** paste raw `![[...]]` image links outside callouts.
> - Always embed images inside folded cite callouts matching this exact format:
>   ```markdown
>   > [!cite]- Slide|Figure <N>: <Short descriptive caption of what the image shows>
>   > ![[<image_filename>.png]]
>   > <Short explanation on what's happening in the image>
>   ```

---
## Standardized Module Placeholder Syntax

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

- Be conservative with adding modules. Only add what is needed to learn the topic. The learner may ask for additional information or modules as needed.

| Module Type        | When to Add                                                                                                                                                                 | When to Exclude                                                                                                                                                                                      |
| :----------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `example`          | Real-world case studies, incidents, deployed systems (e.g. BitLocker, HSL ticketing), concrete attack traces, or worked numerical problems in slides.                       | Purely abstract conceptual definitions without real-world context; or when an example merely restates the definition without demonstrating operational workflow.                                     |
| `graph`            | Multi-component architectures, protocol message flows, trust boundaries, state machines, or hierarchical threat trees/taxonomies.                                           | Simple linear 2-step sequences better suited for numbered lists; isolated single-component definitions; or when no relationships or interactions exist.                                              |
| `analogy`          | Counter-intuitive, abstract, or conceptually difficult mechanisms where a familiar physical metaphor clarifies the core idea.                                               | Straightforward, self-explanatory, or descriptive topics (e.g., password expiration); or when an analogy would oversimplify or introduce misleading mental models.                                   |
| `codeblock`        | Verbatim source code, pseudocode, CLI terminal commands, or configuration files that appeared *explicitly* in the source PDF slides.                                        | If no code or terminal commands appeared in the lecture PDF.                                                                                                                                         |
| `formula`          | Mathematical models, quantitative metrics, probabilistic risk equations, cryptographic definitions, or scoring formulas present in the source.                              | Purely qualitative discussions; or when an equation is merely symbolic decoration with no mathematical or operational meaning.                                                                       |
| `list`             | Enumerating properties, taxonomies, multi-step procedures, or unexpounded lists needing callout expansions.                                                                 | Continuous narrative explanations that read better as paragraphs; or when items naturally form a comparative matrix or 2-way trade-off.                                                              |
| `vs_comparison`    | Exactly two competing paradigms, technologies, architectures, or concepts explicitly contrasted in the lecture                                                              | Comparing 3 or more entities (use `multi_comparison`); or when two items are complementary sequential steps in a pipeline rather than competing alternatives.                                        |
| `multi_comparison` | Three or more candidate algorithms, models, tools, or frameworks evaluated across shared technical dimensions.                                                              | Comparing only two entities (use `vs_comparison`); or when entities lack common evaluation dimensions.                                                                                               |
| `quiz`             | At the conclusion of a major section or conceptually rich topic to reinforce learning through self-assessment questions probing mechanisms, limiting cases, and trade-offs. | Trivial introductory sections, purely administrative slides, or sections where a quiz callout would be redundant with conceptual check practice callouts already present in formula/example modules. |

---
## Skeleton scaffold

```markdown
<md_content_from_overview>

# Topic 1
> [!quote] Short introduction of topic 1
## Subtopic A
> [!quote] Short introduction of subtopic A

<!-- MODULE:x ... -->

<!-- MODULE:x ... -->

> [!cite]- <type> <N>: <Short description of what the image shows>
> ![[<image_filename>.png]]
> 
> <!-- MODULE:x ... -->
> 
> ![[<image_filename>.png]]
 
<!-- MODULE:x ... -->

## Subtopic B
> [!quote] Short introduction

<!-- MODULE:x ... -->
...
# Appendix
## Formulas
<!-- MODULE:table_formulas ... -->

## Definition of Terms
<!-- MODULE:table_definitions ... -->

## Summary
<!-- MODULE:summary ... -->
```

---

## Execution Steps for the Agent

1. **Read Converted Markdown**:
   - Inspect the converted Markdown file in `<output_dir>/<doc_name>_converted.md` and check `<output_dir>/assets/` for extracted images.
2. **Read Overview Outline**:
   - Inspect the outline produced by `/overview` to determine the complete section hierarchy.
3. **Generate Frontmatter & Overview:**
   - Insert Obsidian YAML frontmatter
   - Insert Opener Blockquote and `# Overview` fenced tree.
4. **Insert Section Headings & Quote Callout Descriptions**:
   - For every section in the outline, write markdown headings.
   - Immediately under the header line (no blank line in between), insert introductory description inside `> [!quote]` using verbatim source phrasing.
5. **Embed Assets in Folded Cite Callouts**:
   - Embed extracted slide images inside `> [!cite]- Slide N: Caption\n> ![[...]]`
6. **Insert Standardized Module Placeholders**:
   - Insert standardized module tags with appropriate depth (`depth="1|2|3"`).
7. **Insert Appendices Scaffolding**:
   - Under `## Appendix`, insert `### Formulas`, `### Definition of Terms`, and `### Summary` with their respective tags.
8. **Save Skeleton File**:
   - Save to `<output_dir>/NOTE - <Type> <Number> - <Topic>.md`.
   - **Type codes:**
      - `Lec`: Lectures / Slide Decks
      - `Quiz`: Exam / Quiz Reviews
      - `Code`: Jupyter Notebooks / Code Walkthroughs
      - `Read`: Readings / Academic Papers
