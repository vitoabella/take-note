---
foldable_callouts: false
---

# Skeleton & Scaffolding

The structure of the lecture note based on the hierarchical tree produced by `/overview` and the extracted assets from `/convert_pdf`.

---
## Verbatim Source Wording

- The technical terms, and adjectives in topic headers and descriptions MUST strictly follow the source material (the slides/reading text) however you may rephrase to form a cohesive narrative.
- **Do NOT default to sophisticated or flowery adjectives** (e.g., avoid inventing "heterogeneous distributed components", or "confidentiality perimeter collapses" unless those exact terms appear in the source).
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

**Folded Cite Callouts for Images**:
Visual assets from the PDF (diagrams, architectural schematics, flowcharts, photographs, UI screenshots) are extracted into `/assets` by `/convert_pdf`.
- Do **NOT** paste raw `![[...]]` image links outside callouts.
- Always embed images inside folded cite callouts matching this exact format:
  ```markdown
  > [!cite]- Slide|Figure <N>: <Short descriptive caption of what the image shows>
  > ![[<image_filename>.png]]
  > <Short explanation on what's happening in the image>
  ```

---
## Module Placeholder
### Syntax
```markdown
<!-- MODULE:<MODULE_TYPE> section="<section_number>" topic="<topic_description>" depth="<1|2|3>"
SOURCE: "<...>"
OBJECTIVE: "<...>"
SURROUNDING: "<...>"
-->
```
### Properties

**Context Capsule Fields**:
To prevent worker subagents from re-reading the entire source PDF or scanning the skeleton, every module placeholder tag is a self-contained **Context Capsule**:
- **`SOURCE` (Verbatim Grounding)**: 2–4 lines of verbatim bullets, mathematical equations, or raw slide text and slide citations (e.g., `Slide 14-16: ...`).
- **`OBJECTIVE` (What to Build)**: 1 direct sentence declaring the technical angle, mechanism, or trade-off to illustrate.
- **`SURROUNDING` (Narrative Fit)**: 1 sentence summarizing the section's intro quote callout (`> [!quote]`) so the subagent continues the narrative without repeating definitions already stated.

**Information Depth Property**:
Provide a depth value according to how much detail the topic/subtopic was discussed in the source material. This value guides the subagent on how much information to generate:
- `depth="1"`: Mentioned in passing; introductory context, non-technical background; simple, relatable, easy-to-remember terms. Do not over-elaborate.
- `depth="2"`: Discussed, but not fleshed out; standard core principles, definitions, functional descriptions. Short phrases; foldouts folded by default (`> [!...]-`).
- `depth="3"`: Explained in-detail in source (default); step-by-step mechanisms, formal rules, technical invariants, multi-variable systems, and failure modes.

**Source Weighting Signals**:
To determine the appropriate `depth` value, evaluate the source PDF across three objective signals:
1. **Slide Real Estate**:
   - Sub-bullet on a slide covering multiple topics ($< 0.5$ slide) $\rightarrow$ `depth="1"`
   - Dedicated slide or prominent half-slide ($1$ slide) $\rightarrow$ `depth="2"`
   - Multiple dedicated slides ($2+$ slides) or dedicated subsection with diagrams/tables $\rightarrow$ `depth="3"`
2. **Pedagogical Prominence**:
   - Incidental/background mention or historical note $\rightarrow$ `depth="1"`
   - Named slide title, bullet taxonomy, or distinct mechanism $\rightarrow$ `depth="2"`
   - Core foundational invariant, primary architecture, or central exam case study $\rightarrow$ `depth="3"`
3. **Exam Relevance Heuristic**:
   - Contextual background unlikely to be examined independently $\rightarrow$ `depth="1"`
   - Standard testable concept, definition, or primary procedure $\rightarrow$ `depth="2"`
   - High-probability exam question (mechanisms, formal trade-offs, attack scenarios) $\rightarrow$ `depth="3"`

## Topic Output Profiles

| Profile | Quote Callout | Module Allocation | Pedagogical Focus |
| :--- | :--- | :--- | :--- |
| **Depth 1**<br>*(Passing / Contextual)* | 1 concise sentence verbatim from source. | Maximum 0–1 lightweight module (`depth="1"`). | High-level mental hook; simple relatable terms; zero cognitive clutter; no deep breakdowns. |
| **Depth 2**<br>*(Standard Core / Mechanism)* | 1–2 precise sentences capturing definition and core properties. | Exactly 1 primary module (`depth="2"`). | Mechanism and operational trade-offs cleanly structured with details folded by default (`-`). |
| **Depth 3**<br>*(Foundational / In-Depth Invariant)* | 2–3 rigorous sentences capturing formal rules and technical invariants. | 1 major module (`depth="3"`) OR at most 2 complementary modules (Rule of 2). | Full architectural / algorithmic breakdown + self-assessment check or open inquiry thought experiment. |

---

## Anti-Crowding Constraints & Selection Rules

- **Anti-Crowding Invariant**: Be conservative with adding modules. Only add what is needed to learn the topic. The learner will ask for additional information or modules as needed.
- **The Rule of 1 (Default)**: Every subtopic receives at most **one** primary module.
- **The Rule of 2 (Strict Exception)**: A subtopic may receive **two** modules *only* if:
	1. The topic is **Depth 3** (Foundational / In-Depth Invariant), AND
	2. The two modules come from **different cognitive categories**:

| Category                           | Allowed Modules                                                   |
| :--------------------------------- | :---------------------------------------------------------------- |
| Architectural & Structural         | `graph`, `layered_stack`, `codeblock`                             |
| Temporal & Sequential Flow         | `process_flow`, `pipeline_stage`, `state_machine`, `causal_chain` |
| Comparative & Dimensional Analysis | `vs_comparison`, `multi_comparison`, `spectrum`, `formula`        |
| Conceptual & Empirical Grounding   | `analogy`, `example`, `list`                                      |
| Evaluative & Socratic Inquiry      | `quiz`, `inquiry`                                                 |
### How to Choose a Module: Intent Filter

Ask: **"What is the single best way to clarify this topic?"**

1. **Did the slide contain verbatim code or math?** *(Deterministic Gates)*
   - Verbatim source code, pseudocode, or CLI commands $\rightarrow$ `codeblock`
   - Explicit mathematical model, risk equation, or scoring formula $\rightarrow$ `formula`

2. **Need to show how components are arranged?** *(Architectural & Structural)*
   - Vertical abstraction hierarchies (OSI, hardware/OS/app stack) $\rightarrow$ `layered_stack`
   - Interconnected topologies, trust boundaries, or distributed message flows $\rightarrow$ `graph`

3. **Need to show movement, time, or state evolution?** *(Temporal & Sequential Flow)*
   - Discrete system states with trigger events and transitions $\rightarrow$ `state_machine`
   - Data transforming into different representations across stages $\rightarrow$ `pipeline_stage`
   - Failure cascade, security breach, or root-cause domino progression $\rightarrow$ `causal_chain`
   - Formal algorithmic execution (Input $\to$ Transformation $\to$ Output) $\rightarrow$ `process_flow`

4. **Need to weigh options or trade-offs?** *(Comparative & Dimensional Analysis)*
   - Exactly 2 options head-to-head (A vs B) with selection heuristic $\rightarrow$ `vs_comparison`
   - 3 or more candidate systems evaluated across shared criteria $\rightarrow$ `multi_comparison`
   - A sliding continuum between two opposing architectural poles $\rightarrow$ `spectrum`

5. **Need to build intuition or ground the concept?** *(Conceptual & Empirical Grounding)*
   - Physical real-world metaphor for a counter-intuitive abstract concept $\rightarrow$ `analogy`
   - Concrete attack trace, real incident case study, or worked problem $\rightarrow$ `example`
   - Structured taxonomy, properties, or unexpounded list expansions $\rightarrow$ `list`

6. **Concluding a major section or testing the learner?** *(Evaluative & Socratic Inquiry)*
   - Check lecture comprehension with self-assessment questions $\rightarrow$ `quiz`
   - Provocative "What if?" edge-case puzzle / thought experiment $\rightarrow$ `inquiry`

---

## Output Shape

```markdown
<yaml_frontmatter>
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

1. Read Converted Markdown:
   - Inspect the converted Markdown file in `<output_dir>/<doc_name>_converted.md` and check `<output_dir>/assets/` for extracted images.
2. Read Overview Outline:
   - Inspect the outline produced by `/overview` to determine the complete section hierarchy.
3. Insert Obsidian YAML frontmatter, Opener Blockquote and # Overview fenced tree
4. Insert Section Headings & Quote Callout Descriptions:
   - For every section in the outline, write unnumbered markdown headings.
   - Immediately under the header line (no blank line in between), insert introductory description inside `> [!quote]`.
   - Ensure that the description highlights the topic's importance and relevance to the main topic or the previous topic/subtopic.
   - If there is an abbreviated word that hasn't been explained, comment the first occurrence in this format `{==<word>==}{{author="Definition">><definition of the abbreviated word><<}}`
5. Embed Assets in Folded Cite Callouts
6. Insert Standardized Module Placeholders as Context Capsules
7. Insert Appendices Scaffolding