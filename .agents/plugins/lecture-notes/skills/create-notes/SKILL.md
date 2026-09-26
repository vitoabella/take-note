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
  max_subagents: 3
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
> - **Black-Box Script Execution**: Do NOT view or inspect the Python files in `scripts/`. Execute the documented commands directly. If option discovery is needed, execute `python <script_path> --help` via the shell.

### Step 0: Initialize Session
- Read **only** [references/init.md](references/init.md). Do NOT inspect any other reference files or downstream scripts.
- Register source PDF, inspect metadata, and create output directory:
  ```powershell
  python .agents/plugins/lecture-notes/skills/create-notes/scripts/create_output_dir.py --output-dir "<output_dir>"
  ```

### Step 1: Preprocessing & PDF Conversion
- Convert the PDF into clean Markdown text and extract all visual images, diagrams, and photos into `<output_dir>/assets/`:
  ```powershell
  python .agents/plugins/lecture-notes/skills/create-notes/scripts/convert_pdf.py --pdf "<pdf_path>" --out-dir "<output_dir>" --doc-name "<doc_name>"
  ```
- **User Confirmation Check**: If `pause_between_steps: true`, present the summary and pause for user confirmation before loading or executing Step 2.

### Step 2: Generate Document Outline
- **JIT Reference**: Read [references/overview.md](references/overview.md) ONLY after Step 1 confirmation has been received. Do NOT read ahead to `skeleton.md`.
- Generate the study outline tree following `references/overview.md` using the converted Markdown file as grounding.
- Enforce hard constraints:
  - Tree MUST ALWAYS be enclosed in opening and closing triple backticks (` ``` `) on separate lines.
  - Max 3 levels (Main $\rightarrow$ Topic $\rightarrow$ Subtopic) and $\le 25$ lines total.
  - Trailing `*` on unmentioned topics.
  - **Silent Clean Erasure**: omit pruned branches cleanly without meta-commentary disclaimers.
- If `log_step_outputs: true`, save the overview tree to `<output_dir>/logs/02_overview.md`.
- **User Confirmation Check**: If `pause_between_steps: true`, pause and ask the user for confirmation before reading Step 3 references or proceeding to Step 3.

### Step 3: Build Markdown Skeleton & Extract Module Manifest
- **JIT Reference**: Read [references/skeleton.md](references/skeleton.md) ONLY after Step 2 confirmation has been received.
- Build the structural scaffolding note following `references/skeleton.md`:
  - Save filename using standardized syntax: `NOTE - <Type> <Number> - <Topic>.md` (e.g. `NOTE - Lec 1 - Threat Analysis.md`).
  - **No Document H1 Title & No Table of Contents**: Document begins directly with YAML frontmatter $\rightarrow$ Opener blockquote $\rightarrow$ `# Overview` $\rightarrow$ Section headings.
  - **Silent Clean Erasure**: Excluded or stopped elements are erased cleanly with no commentary or omission notices.
  - **Quote Callout Immediately Below Header**: Section descriptions must be placed inside `> [!quote]` immediately on the line after the header (no blank line in between).
  - **Verbatim Source Phrasing**: Follow words and adjectives from slides/readings verbatim (strictly no invented fancy adjectives).
  - **Folded Cite Image Callouts**: Embed slide images inside `> [!cite]- Slide <N>: <Caption>\n> ![[<image>.png]]`.
  - Insert standardized module tags (`<!-- MODULE:<type> section="..." topic="..." depth="1|2|3" -->`).
- Run the module extraction and dispatch manifest builder:
  ```powershell
  python .agents/plugins/lecture-notes/skills/create-notes/scripts/extract_and_dispatch.py --file "<skeleton_path>.md"
  ```
  This creates `<output_dir>/.modules/<module_type>.txt` and generates `<output_dir>/.modules/dispatch_manifest.json` containing the pre-computed `Subagents` array.
- If `log_step_outputs: true`, save the raw skeleton to `<output_dir>/logs/03_skeleton.md`.
- **User Confirmation Check**: If `pause_between_steps: true`, pause and ask the user for confirmation before proceeding to Step 4.

### Step 4: Parallel Module Population & Live In-Place Note Modification
> [!CAUTION]
> **Manager-Only Delegation Invariant**:
> The orchestrator is strictly prohibited from writing module body content directly in the main thread. You MUST delegate module population to worker subagents.

- Inspect `<output_dir>/.modules/dispatch_manifest.json`.
- Pass the pre-computed `Subagents` array directly into the `invoke_subagent` tool.
- When dispatching subagents to create ANY module, enforce the strict boundary invariant:
Worker modules output ONLY the body content (e.g. table, diagram, formula, list, callout). Do NOT output section headers (##, ###) or quote callouts (> [!quote]), as those are exclusively managed by the skeleton.

Subagents will process their respective tasks according to their assigned reference (loaded JIT by each subagent):
  - `formula`: follow [references/formula.md](references/formula.md)
  - `graph`: follow [references/graph.md](references/graph.md)
  - `example`: follow [references/example.md](references/example.md)
  - `analogy`: follow [references/analogy.md](references/analogy.md)
  - `list`: follow [references/list.md](references/list.md)
  - `vs_comparison`: follow [references/vs_comparison.md](references/vs_comparison.md)
  - `multi_comparison`: follow [references/multi_comparison.md](references/multi_comparison.md)
  - `codeblock`: follow [references/codeblock.md](references/codeblock.md)
  - `quiz`: follow [references/quiz.md](references/quiz.md)
- **Live In-Place Insertion**: Subagents insert their populated content directly underneath the target tag using `insert_module.py`:
  ```powershell
  python .agents/plugins/lecture-notes/skills/create-notes/scripts/insert_module.py --note "<skeleton_path>.md" --module "<module_type>" --section "<section_num>" --content-file "<content_path>"
  ```
  This preserves the comment anchor intact above the content for spot-modifications.
- If `log_step_outputs: true`, log each populated module block to `<output_dir>/logs/04_modules_<module_name>.md` containing strictly the module tag followed by the generated content underneath (no wrapper headers or commentary):
  ```markdown
  <!-- MODULE:<type> section="..." topic="..." depth="..." -->
  <generated module body content>
  ```
- **User Confirmation Check**: If `pause_between_steps: true`, pause and ask the user for confirmation before proceeding to Step 5.

### Step 5: Appendices Assembly
- **JIT Reference**: Inspect appendix references ONLY when this step is reached:
  - `table_formulas`: follow [references/table_formulas.md](references/table_formulas.md)
  - `table_definitions`: follow [references/table_definitions.md](references/table_definitions.md) (with section wikilinks `[[#Section|Term]]`)
  - `summary`: follow [references/summary.md](references/summary.md) (narrative of fit inside `> [!tldr]`)
- Spliced directly underneath their respective tags using `insert_module.py`.

### Step 6: Deterministic Format Enforcement & Verification
- Execute `format_enforcer.py` on the finished note to guarantee all whitespace, callout, and KaTeX invariants:
  ```powershell
  python .agents/plugins/lecture-notes/skills/create-notes/scripts/format_enforcer.py --file "<note_path>.md"
  ```
- If `log_step_outputs: true`, log final state to `<output_dir>/logs/05_final_note.md`.
