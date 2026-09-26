---
name: create-notes
description: >-
  Orchestrator skill for generating comprehensive Obsidian lecture notes from a PDF.
# Main Configuration (Cascades to all sub-skills unless overridden)
output_dir: "output"
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
  max_subagents: 10
---

# Create Notes Orchestrator (`/create-notes`)

## Configuration Inheritance Model

> [!IMPORTANT]
> **Cascading Frontmatter Inheritance**:
> 1. All configuration properties in this frontmatter serve as global defaults.
> 2. Each reference module inherits all properties from this main frontmatter.
> 3. When dispatching subagents, pass the effective configuration combining these global defaults with any step-specific parameters.

---

## Instructions for the Agent

### Execution Model: Strict Phase Gating

> [!IMPORTANT]
> **Strict Just-In-Time (JIT) Phase Gating**:
> - **Execute One Phase at a Time**: The pipeline MUST proceed strictly sequentially.
> - **Zero Speculative Lookahead**: The orchestrator MUST NOT view, inspect, or search reference files or scripts for future pipeline steps (e.g., do NOT inspect `overview.md`, `skeleton.md`, or module specifications during Step 0 or Step 1).
> - **Just-In-Time Loading**: Read a step's reference file ONLY after the preceding step is complete and explicit user confirmation has been granted (when `pause_between_steps: true`).
> - ...**User Confirmation Check**: If `pause_between_steps: true`, pause and ask the user for confirmation before proceeding to next step.

### Step 1: Preprocessing & PDF Conversion
- **Base Path Resolution**: 
> Let `<SKILL_DIR>` be the absolute or workspace-relative directory containing this `SKILL.md` file 
- Run command below to convert the PDF into clean Markdown text into `<output_dir>` and extract images into `<output_dir>/assets/`:
  ```powershell
  python <SKILL_DIR>/scripts/convert_pdf.py --pdf "<pdf_path>" --out-dir "<output_dir>" --doc-name "<doc_name>"
  ```
- **Perform User Confirmation Check**: If `pause_between_steps: true`, present the summary and pause for user confirmation before loading or executing Step 2:
  | Property | Effective Value | Source |
  | :--- | :--- | :--- |
  | Source PDF | `<path>` | User Input |
  | Document Title | `<title>` | PDF Title |
  | Pages Detected | `<total_pages>` | view_file |
  | Output Target | `<target_output_file>` | Effective Config |
  | Tone / Detail | `<tone>` / `<detail_level>` | Effective Config |

### Step 2: Generate Document Outline
- Generate the study outline tree following `references/overview.md` using the converted Markdown file as grounding.
- If `log_step_outputs: true`, save the overview tree to `<output_dir>/logs/02_overview.md` via `write_to_file` tool.
- ...**Perform User Confirmation Check**

### Step 3: Build Markdown Skeleton
- Build the structural scaffolding note following `references/skeleton.md`
- If `log_step_outputs: true`, save the it to `<output_dir>/logs/03_skeleton.md` via `write_to_file` tool.
- Save `<file>` as `NOTE - <Type> <Number> - <Topic>.md` to `<output_dir>/` via `write_to_file` tool.
   - **Type codes:**
      - `Lec`: Lectures / Slide Decks
      - `Quiz`: Exam / Quiz Reviews
      - `Code`: Jupyter Notebooks / Code Walkthroughs
      - `Read`: Readings / Academic Papers
- ...**Perform User Confirmation Check**

### Step 4: Parallel Module Population & Live In-Place Note Modification

- Run script
```powershell
python <SKILL_DIR>/scripts/extract_modules.py --file "<output_dir>/<file>"
```
- Use `invoke_subagent` tool for each module in the response with the prompt:
  ````markdown
  - Write the module: <module> following the [reference file](references/<module>.md)
  - If `lot_step_outputs: true`, save the output using `write_to_file` in `<output_dir>/logs/04_<module>.md`
  - Use `multi_replace_file_content` to insert the module on file `<output_dir>/NOTE - <Type> <Number> - <Topic>.md` according to the <!-- Module: ... --> tag. Put the output below the module tag without removing the tag. For example:
  ```markdown
  <!-- MODULE:<type> section="..." topic="..." depth="..." -->
  <generated module content>
  ```
  ````
- **Perform User Confirmation Check**

### Step 5: Appendices Assembly
- **JIT Reference**: Inspect appendix references ONLY when this step is reached:
  - `table_formulas`: follow [references/table_formulas.md](references/table_formulas.md)
  - `table_definitions`: follow [references/table_definitions.md](references/table_definitions.md) (with section wikilinks `[[#Section|Term]]`)
  - `summary`: follow [references/summary.md](references/summary.md) (narrative of fit inside `> [!tldr]`)
- Spliced directly underneath their respective tags using `insert_module.py`.

### Step 6: Deterministic Format Enforcement & Verification
- Execute `format_enforcer.py` on the finished note to guarantee all whitespace, callout, and KaTeX invariants:
  ```powershell
  python <SKILL_DIR>/scripts/format_enforcer.py --file "<note_path>.md"
  ```
- If `log_step_outputs: true`, log final state to `<output_dir>/logs/05_final_note.md`.
