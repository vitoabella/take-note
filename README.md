# Obsidian Lecture Notes Agent & Skills Suite

An agentic skills suite designed for **Antigravity (AGY)** that transforms lecture slides and textbook chapters (PDF) into comprehensive, publication-grade markdown notes tailored for **Obsidian**.

---

## Key Features

- **Single Master Orchestrator (`/create-notes`)**: Coordinates the entire workflow end-to-end or runs individual skills on demand.
- **Parallel Subagent Generation**: Scaffolds the document using standardized module anchors (`<!-- MODULE:X ... -->`) so multiple subagents can populate content concurrently without merge conflicts.
- **Temporary Working Skeleton**: The skeleton generated after outlining serves as a temporary working file (`.skeleton_<Title>.tmp.md`) read only by skills and `extract_modules.py`, and is cleaned up once the final note is assembled.
- **Self-Contained Skills**: Reference templates, guidelines, and rules are fully integrated into each sub-skill's `SKILL.md` (no external reference folders).
- **Source-Faithful Code Replication (`/codeblock`)**: Strictly replicates code present in the source PDF and augments it with line annotations and Big-O complexity analysis.
- **Obsidian First-Class Citizen**:
  - Native callouts (`> [!NOTE]`, `> [!TIP]`, `> [!WARNING]`, `> [!EXAMPLE]`, `> [!ABSTRACT]`).
  - Seamless KaTeX math formatting (`$...$` inline, `$$...$$` display blocks).
  - Clean Mermaid.js flowcharts, state diagrams, and sequence charts.
  - `[[wikilinks]]` and tags for rich graph view interconnectivity.
- **No External Config Folder**: All document and skill parameters live directly within YAML frontmatter in each respective `SKILL.md` with cascading inheritance.
- **Strict PDF Reading Compliance**: Adheres to the native `view_file` tool rule, guaranteeing zero Python PDF parsing scripts.

---

## Directory Structure

```text
agent-skills/
├── .agents/
│   ├── skills.json                           # Discovery registry for nested slash commands
│   └── skills/
│       └── create-notes/                     # Master orchestrator skill
│           ├── SKILL.md                      # Orchestrator runbook & global config frontmatter
│           ├── scripts/
│           │   └── extract_modules.py        # Lean scanner to identify module placeholders in skeleton
│           └── skills/                       # Fully self-contained sub-skills
│               ├── start/SKILL.md            # /start: Session initialization & PDF inspection
│               ├── overview/SKILL.md         # /overview: Conceptual outline & learning objectives
│               ├── skeleton/SKILL.md         # /skeleton: Temporary scaffolding & module anchors
│               ├── codeblock/SKILL.md        # /codeblock: Source PDF code replication & annotations
│               ├── formula/SKILL.md          # /formula: KaTeX equations, variable tables & derivations
│               ├── graph/SKILL.md            # /graph: Obsidian Mermaid diagrams
│               ├── image/SKILL.md            # /image: Textual schematics & figure callouts
│               ├── list/SKILL.md             # /list: Taxonomies, procedures & checklists
│               ├── vs_comparison/SKILL.md    # /vs_comparison: 2-way comparative analysis (A vs B)
│               ├── multi_comparison/SKILL.md # /multi_comparison: Multi-dimensional matrix tables (3+ options)
│               ├── table_formulas/SKILL.md   # /table_formulas: Appendix formula cheat sheet
│               ├── table_definitions/SKILL.md# /table_definitions: Chronological glossary grouped by concept
│               ├── summary/SKILL.md          # /summary: Overview-guided narrative synthesis
│               ├── analogy/SKILL.md          # /analogy: In simple terms, example, unpack
│               └── example/SKILL.md          # /example: Concrete examples & scenarios
└── README.md
```

---

## Slash Commands Quick Reference

| Slash Command | Role | Description |
| :--- | :--- | :--- |
| **`/create-notes`** | **Master Orchestrator** | Executes the full pipeline end-to-end and dispatches parallel subagents. |
| **`/start`** | Session Init | Ingests the PDF via `view_file`, checks pages, and sets output metadata. |
| **`/overview`** | Planning | Analyzes PDF structure and produces topic hierarchy and learning objectives. |
| **`/skeleton`** | Scaffolding | Builds temporary working skeleton with headings, TOC, and module anchors. |
| **`/codeblock`** | Body Module | Replicates code from PDF with line-by-line annotations & complexity. |
| **`/formula`** | Body Module | Renders KaTeX equations, variable breakdown tables, and derivations. |
| **`/graph`** | Body Module | Generates Obsidian Mermaid.js architecture and workflow diagrams. |
| **`/image`** | Body Module | Creates ASCII architecture schematics and figure callouts with captions. |
| **`/list`** | Body Module | Generates structured taxonomies, algorithmic steps, and checklists. |
| **`/vs_comparison`**| Body Module | Produces 2-way comparative tables with trade-offs and selection rules. |
| **`/multi_comparison`**| Body Module | Produces multi-column matrix tables evaluating 3+ options across criteria. |
| **`/table_formulas`**| Appendix | Summary cheat sheet of all formulas mentioned in the document. |
| **`/table_definitions`**| Appendix | Exhaustive glossary, grouped by concept, ranked chronologically by appearance. |
| **`/summary`** | Appendix | Narrative synthesis connecting all topics according to the overview map. |

---

## Configuration via YAML Frontmatter

All configurations are declared directly inside YAML frontmatter in `SKILL.md` files, following a **cascading inheritance model**:

### 1. Global Parent Configuration (`create-notes/SKILL.md`)
All properties in `create-notes/SKILL.md` serve as global defaults for the entire note generation session:
```yaml
---
name: create-notes
description: Master orchestrator skill for generating comprehensive Obsidian lecture notes from a PDF.
output_dir: "./output"
output_mode: "single_note"       # 'single_note' or 'atomic_moc'
tone: "pedagogical"             # 'academic', 'pedagogical', 'rigorous', 'concise'
detail_level: "detailed"        # 'high_level', 'standard', 'detailed', 'exhaustive'
target_audience: "Undergraduate / Graduate Students"
callout_style: "standard"       # [!NOTE], [!TIP], [!WARNING], [!EXAMPLE], [!ABSTRACT]
foldable_callouts: false        # If true, uses > [!NOTE]-
use_wikilinks: true             # [[Link]] syntax
math_delimiter: "standard"      # $ for inline, $$ for display block
parallelism:
  max_subagents: 3
---
```

### 2. Cascading Inheritance & Override Rule
- **Automatic Inheritance**: Every sub-skill (`/start`, `/overview`, `/codeblock`, `/formula`, etc.) automatically inherits all parent properties (`tone`, `detail_level`, `target_audience`, `foldable_callouts`, `use_wikilinks`, `math_delimiter`, `output_dir`).
- **Selective Override**: A sub-skill only overrides a property if that property is **explicitly populated** with a non-null value in its own frontmatter. If omitted, set to `null`, or left blank, the parent setting is preserved.

---

## Parallel Subagent Workflow & Temporary Skeleton

1. `/skeleton` generates a **temporary working skeleton** (`.skeleton_<Title>.tmp.md`).
2. `scripts/extract_modules.py` scans the temporary skeleton:
   ```powershell
   python .agents/skills/create-notes/scripts/extract_modules.py --file "./output/.skeleton_Consensus.tmp.md"
   ```
   This outputs the list of unique module types and IDs ready for parallel population.
3. The orchestrator batches placeholders and launches subagents concurrently via `invoke_subagent`:
   ```python
   invoke_subagent(Subagents=[
       {"TypeName": "self", "Role": "Formula Generator", "Prompt": "...populate module 'bayes-rule'..."},
       {"TypeName": "self", "Role": "Graph Generator", "Prompt": "...populate module 'inference-flow'..."}
   ])
   ```
4. Subagents read the temporary skeleton file to gather context and return populated markdown blocks.
5. Once all body modules and appendices are populated, the final note is written to `./output/<Title>.md`, and the temporary skeleton file is deleted.
