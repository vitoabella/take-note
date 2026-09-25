---
name: create-notes
description: >-
  Master orchestrator skill for generating comprehensive Obsidian lecture notes from a PDF.
  Coordinates preprocessing, outline, skeleton, live parallel subagent module population, and appendices.
# Main Configuration (Cascades to all sub-skills unless overridden)
output_dir: "output"
output_mode: "single_note"       # 'single_note' or 'atomic_moc'
tone: "pedagogical"             # 'academic', 'pedagogical', 'rigorous', 'concise'
detail_level: "standard"        # 'high_level', 'standard', 'detailed', 'exhaustive'
target_audience: "Undergraduate / Graduate Students"
callout_style: "standard"       # 'standard' ([!NOTE], [!TIP], etc.)
foldable_callouts: true        # If true, uses > [!NOTE]-
use_wikilinks: true             # [[Link]] syntax
math_delimiter: "standard"      # $ for inline, $$ for display block
pause_between_steps: true       # If true, pauses after each pipeline phase for user confirmation
log_step_outputs: true          # If true, saves intermediate step outputs to <output_dir>/logs/
parallelism:
  max_subagents: 3
---

# Create Notes Orchestrator (`/create-notes`)

Use this skill to orchestrate the end-to-end generation of publication-grade Obsidian lecture notes from a source PDF document.

## Configuration Inheritance Model

> [!IMPORTANT]
> **Cascading Frontmatter Inheritance**:
> 1. All configuration properties in this frontmatter serve as global defaults.
> 2. Each sub-skill inherits all properties from this main frontmatter.
> 3. A sub-skill only overrides a property if explicitly populated in its own YAML frontmatter.
> 4. When dispatching subagents or executing sub-skills:
>    $$\text{Effective Config} = \text{Main Config} \oplus \text{Populated Subskill Overrides}$$

---

## Execution Pipeline

1. **Preprocessing & Asset Extraction**: `/convert_pdf` (runs `convert_pdf.py` to produce converted markdown + `/assets`)
2. **Session Init**: `/start`
3. **Outlining**: `/overview` (max 3 levels, $\le 25$ lines, `*` notation for extra topics)
4. **Scaffolding & Tag Extraction**: `/skeleton` (standard filename `NOTE - <Type> <Number> - <Topic>.md`, direct image embeds, no TOC) followed by `scripts/extract_modules.py`
5. **Parallel Module Population & Live Updates**: `/codeblock`, `/formula`, `/graph`, `/list`, `/vs_comparison`, `/multi_comparison`, `/analogy`, `/example`
6. **Appendices & Final Compilation**: `/table_formulas`, `/table_definitions` (with section wikilinks), `/summary` (narrative of fit)

---

## Instructions for the Agent

### Step 1: Preprocessing & PDF Conversion (`/convert_pdf`)
- Convert the PDF into clean Markdown text and extract all visual images, diagrams, and photos into `<output_dir>/assets/`:
  ```powershell
  python .agents/skills/create-notes/skills/convert_pdf/scripts/convert_pdf.py --pdf "<pdf_path>" --out-dir "<output_dir>" --doc-name "<doc_name>"
  ```
- If `log_step_outputs: true`, verify the converted file is saved and log the result to `<output_dir>/logs/01_converted.md`.
- **User Confirmation Check**: If `pause_between_steps: true`, pause and ask the user for confirmation before proceeding to Step 2.

### Step 2: Generate Document Outline (`/overview`)
- Execute `/overview` using the converted Markdown file as grounding.
- Enforce hard constraints:
  - Tree MUST ALWAYS be enclosed in opening and closing triple backticks (` ``` `) on separate lines.
  - Max 3 levels (Main $\rightarrow$ Topic $\rightarrow$ Subtopic) and $\le 25$ lines total.
  - Trailing `*` on unmentioned topics.
  - Silent clean erasure: omit pruned branches cleanly without meta-commentary disclaimers.
- If `log_step_outputs: true`, save the overview tree to `<output_dir>/logs/02_overview.md`.
- **User Confirmation Check**: If `pause_between_steps: true`, pause and ask the user for confirmation before proceeding to Step 3.

### Step 3: Build Markdown Skeleton & Extract Module Tags (`/skeleton`)
- Execute `/skeleton` to generate the structural scaffolding:
  - Save filename using standardized syntax: `NOTE - <Type> <Number> - <Topic>.md` (e.g. `NOTE - Lec 1 - Threat Analysis.md`).
  - **No Document H1 Title & No Table of Contents**: Document begins directly with YAML frontmatter $\rightarrow$ Opener blockquote $\rightarrow$ `# Overview` $\rightarrow$ Section headings.
  - **Silent Clean Erasure**: Excluded or stopped elements are erased cleanly with no commentary or omission notices.
  - **Quote Callout Immediately Below Header**: Section descriptions must be placed inside `> [!quote]` immediately on the line after the header (no blank line in between).
  - **Verbatim Source Phrasing**: Follow words and adjectives from slides/readings verbatim (strictly no invented fancy adjectives), assessing which verbatim terms are loaded and marking them in `==**bold highlight**==`.
  - **Folded Cite Image Callouts**: Embed slide images inside `> [!cite]- Slide <N>: <Caption>\n> ![[<image>.png]]`.
  - Insert standardized module tags (`<!-- MODULE:<type> section="..." topic="..." importance="1-4" -->`).
- Run the module extraction script:
  ```powershell
  python .agents/skills/create-notes/scripts/extract_modules.py --file "<skeleton_path>.md"
  ```
  Generates per-skill tag lists in `<output_dir>/.modules/<skill_name>.txt`.
- If `log_step_outputs: true`, save the raw skeleton to `<output_dir>/logs/03_skeleton.md`.
- **User Confirmation Check**: If `pause_between_steps: true`, pause and ask the user for confirmation before proceeding to Step 4.

### Step 4: Parallel Module Population & Live In-Place Note Modification
- For each unique module type in `<output_dir>/.modules/`, dispatch subagents or execute the corresponding subskill.
- Subagents prioritize higher-importance placeholders (`importance="4"` and `importance="3"`) first.
- **Live In-Place Modification Rule (Insert Directly Underneath Tag)**:
  > [!IMPORTANT]
  > As soon as an individual module/subagent finishes generating content for a placeholder, it MUST **immediately insert the populated content directly underneath the `<!-- MODULE:... -->` tag in the main note file**, leaving the comment tag intact above it.
  > Do NOT delete or replace the `<!-- MODULE:... -->` tag. Preserving the comment anchor allows the user and future agents to reference it for spot-modifications, targeted re-runs, and granular edits.
  > Do NOT buffer or wait for all modules to finish before editing the main document. This ensures the user can watch the document evolve live in Obsidian.
- If `log_step_outputs: true`, log each populated module block to `<output_dir>/logs/04_modules_<module_name>.md`.
- **User Confirmation Check**: If `pause_between_steps: true`, pause and ask the user for confirmation before proceeding to Step 5.

### Step 5: Appendices & Final Assembly
- Run `/table_formulas`, `/table_definitions` (with section wikilinks `[[#Section|Term]]`), and `/summary` (narrative of fit inside `> [!tldr]`).
- Live-modify the main document to insert each appendix block directly underneath its corresponding `<!-- MODULE:... -->` tag, keeping the tag intact for future reference.
- If `log_step_outputs: true`, log final state to `<output_dir>/logs/05_final_note.md`.
