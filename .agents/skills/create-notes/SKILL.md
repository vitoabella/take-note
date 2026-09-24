---
name: create-notes
description: >-
  Master orchestrator skill for generating comprehensive Obsidian lecture notes from a PDF.
  Coordinates outline, skeleton, parallel subagent module population, and appendices.
# Main Configuration (Cascades to all sub-skills unless overridden)
output_dir: "./output"
output_mode: "single_note"       # 'single_note' or 'atomic_moc'
tone: "pedagogical"             # 'academic', 'pedagogical', 'rigorous', 'concise'
detail_level: "detailed"        # 'high_level', 'standard', 'detailed', 'exhaustive'
target_audience: "Undergraduate / Graduate Students"
callout_style: "standard"       # 'standard' ([!NOTE], [!TIP], etc.)
foldable_callouts: false        # If true, uses > [!NOTE]-
use_wikilinks: true             # [[Link]] syntax
math_delimiter: "standard"      # $ for inline, $$ for display block
parallelism:
  max_subagents: 3
---

# Create Notes Orchestrator (`/create-notes`)

Use this skill to orchestrate the end-to-end generation of Obsidian lecture notes from a source PDF document.

## Configuration Inheritance Model

> [!IMPORTANT]
> **Cascading Frontmatter Inheritance**:
> 1. All configuration properties in this frontmatter serve as global defaults.
> 2. Each sub-skill inherits all properties from this main frontmatter.
> 3. A sub-skill only overrides a property if explicitly populated in its own YAML frontmatter.
> 4. When dispatching subagents or executing sub-skills:
>    $$\\text{Effective Config} = \\text{Main Config} \\oplus \\text{Populated Subskill Overrides}$$

---

## Execution Pipeline

1. **Session Init**: `/start`
2. **Outlining**: `/overview`
3. **Scaffolding & Tag Extraction**: `/skeleton` followed by `scripts/extract_modules.py` (generates per-skill module tag input files in `<output_dir>/.modules/<skill>.txt`)
4. **Parallel Body Population**: `/codeblock`, `/formula`, `/graph`, `/image`, `/list`, `/vs_comparison`, `/multi_comparison`, `/analogy`, `/example`
5. **Appendices & Final Compilation**: `/table_formulas`, `/table_definitions`, `/summary`

---

## Instructions for the Agent

### Step 1: Initialize Session
- Prompt the user for the PDF file path if not already provided.
- Execute `/start` using native `view_file` (never Python PDF extraction).

### Step 2: Generate Document Outline
- Execute `/overview`.

### Step 3: Build Markdown Skeleton & Extract Module Input Files
- Execute `/skeleton` to generate the document structure, enriched topic descriptions with bold highlights (`==**...**==`), and module placeholders with `importance="1-4"` (no `id`).
- Run the module extraction script on the skeleton file:
  ```powershell
  python .agents/skills/create-notes/scripts/extract_modules.py --file "<skeleton_path>.md"
  ```
  - **Console Output**: A clean, comma-separated list of unique module types (e.g. `formula, graph, image, list, ...`) indicating which sub-skills need to run.
  - **File Outputs**: Generates one file per skill in `<output_dir>/.modules/<skill_name>.txt` containing all exact module tags for that skill from the skeleton.

### Step 4: Parallel Module Population
- For each unique module type identified by `extract_modules.py`, provide its generated input file (`<output_dir>/.modules/<skill_name>.txt`) to the corresponding sub-skill/subagent.
- Subagents prioritize higher-importance tags (`importance="4"` and `importance="3"`) first.
- Dispatch subagents via `invoke_subagent`:
  > "Read module tags from input file `<output_dir>/.modules/[MODULE_TYPE].txt`. Follow instructions in `skills/[MODULE_TYPE]/SKILL.md`. Dissect the highlighted descriptors (`==**...**==`) in the skeleton sections. Inspect source PDF at `[PDF_PATH]` via native `view_file`. Return the populated Obsidian markdown blocks to replace each tag."
- Replace each placeholder with the subagent output.

### Step 5: Appendices & Final Assembly
- Run `/table_formulas`, `/table_definitions`, and `/summary` to complete the appendices.
