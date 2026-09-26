# Obsidian Lecture Notes Suite — Technical Architecture & Reference

This document provides a comprehensive technical reference for developers, agent engineers, and power users. It details the underlying skills architecture, cascading YAML frontmatter configuration, subagent permission scopes, script implementations, and format enforcement contracts.

---

## Table of Contents
1. [Repository Structure](#1-repository-structure)
2. [Configuration & Cascading Frontmatter](#2-configuration--cascading-frontmatter)
3. [Subagent Permission Matrix](#3-subagent-permission-matrix)
4. [Standalone Automation Scripts](#4-standalone-automation-scripts)
5. [Phase-by-Phase Technical Specifications](#5-phase-by-phase-technical-specifications)
6. [Module Skill Implementation Contracts](#6-module-skill-implementation-contracts)
7. [Step Logging & Trajectory Inspection](#7-step-logging--trajectory-inspection)

---

## 1. Repository Structure

```text
agent-skills/
├── .agents/
│   ├── skills.json                           # Antigravity skill discovery registry
│   └── skills/
│       └── create-notes/                     # Master orchestrator skill
│           ├── SKILL.md                      # Global config & orchestrator instructions
│           ├── scripts/
│           │   └── extract_modules.py        # Module placeholder scanner & tag grouper
│           └── skills/                       # Modular subskills
│               ├── convert_pdf/              # Preprocessing & image extraction
│               │   ├── SKILL.md
│               │   └── scripts/
│               │       └── convert_pdf.py    # PDF text/image extractor (pdfplumber/pdfium)
│               ├── start/SKILL.md            # Session initialization & metadata setup
│               ├── overview/SKILL.md         # 3-level tree contract (max 25 lines)
│               ├── skeleton/SKILL.md         # Document scaffolding & direct asset embedder
│               ├── formula/SKILL.md          # 4-part KaTeX math blocks with conceptual labels
│               ├── graph/SKILL.md            # Obsidian-safe Mermaid with verb-object edge labels
│               ├── example/SKILL.md          # Real-world case studies & attack walkthroughs
│               ├── analogy/SKILL.md          # Intuitive mental models with breakdown analysis
│               ├── list/SKILL.md             # Taxonomies, procedures, and characteristic lists
│               ├── vs_comparison/SKILL.md    # 2-way comparative analysis (X vs Y)
│               ├── multi_comparison/SKILL.md # Multi-column evaluation matrices (3+ options)
│               ├── table_formulas/SKILL.md   # Appendix formula sheet (Formula, Name, Usage, Answers what)
│               ├── table_definitions/SKILL.md# Appendix glossary with bidirectional section wikilinks
│               ├── summary/SKILL.md          # Narrative synthesis inside folded [!tldr]
│               └── codeblock/SKILL.md        # Source PDF code replication & annotations
├── output/
│   ├── assets/                               # Extracted PNG figures and diagrams
│   ├── .modules/                             # Per-skill extracted placeholder manifests
│   ├── .logs/                                # Intermediate step outputs (when logging enabled)
│   └── NOTE - Lec 1 - Topic.md               # Final generated Obsidian study note
├── README.md                                 # High-level conceptual overview
└── README-TECHNICAL.md                       # This technical engineering manual
```

---

## 2. Configuration & Cascading Frontmatter

Configuration is managed strictly through YAML frontmatter blocks embedded within each `SKILL.md`. No external configuration folders or disconnected JSON configs are used.

### The Cascading Inheritance Principle
1. The root orchestrator (`create-notes/SKILL.md`) defines the global defaults.
2. Every subskill automatically inherits all parent properties.
3. A subskill only overrides a property when it is **explicitly populated with a non-null value** in its own frontmatter. If omitted, set to `null`, or undefined, the parent value is preserved.
4. **User Manual Edits Preservation**: Agents must never overwrite or clobber manual edits made to YAML frontmatters.

$$\text{Effective Config} = \text{Parent Config} \oplus \text{Populated Subskill Overrides}$$

### Global Configuration Schema (`create-notes/SKILL.md`)
```yaml
---
name: create-notes
description: Master orchestrator skill for generating comprehensive Obsidian lecture notes from a PDF.
output_dir: "./output"
output_mode: "single_note"       # 'single_note' or 'atomic_moc'
tone: "pedagogical"             # 'academic', 'pedagogical', 'rigorous', 'concise'
detail_level: "detailed"        # 'high_level', 'standard', 'detailed', 'exhaustive'
target_audience: "Undergraduate / Graduate Students"
callout_style: "standard"       # Standard callout styling
foldable_callouts: false        # If true, uses folded callouts by default
use_wikilinks: true             # Enables [[Link]] syntax
math_delimiter: "standard"      # $ for inline, $$ for display block
pause_between_steps: true       # Pauses after each phase for user confirmation
log_step_outputs: true          # Saves intermediate step outputs into output/.logs/
parallelism:
  max_subagents: 3              # Max concurrent worker agents
---
```

---

## 3. Subagent Permission Matrix

To ensure deterministic execution and prevent tool pollution or unauthorized operations, subagents are strictly scoped via `define_subagent`:

| Agent Name | Scope / Target Skill | Write Tools | Subagent Dispatch | MCP Tools | Key Operational Invariant |
| :--- | :--- | :---: | :---: | :---: | :--- |
| `notes_orchestrator` | `/create-notes` | Yes | Yes | **Disabled** | Coordinates pipeline, manages pausing & logs, dispatches workers. |
| `formula_agent` | `/formula` | Yes | **Disabled** | **Disabled** | Enforces 4-part formula rule; live in-place document edits. |
| `graph_agent` | `/graph` | Yes | **Disabled** | **Disabled** | Enforces Obsidian Mermaid & verb-object edge labels. |
| `example_agent` | `/example` | Yes | **Disabled** | **Disabled** | Formats inside `> [!example]-`; banishes 1-sentence stubs. |
| `comparison_agent` | `/vs_comparison`, `/multi_comparison` | Yes | **Disabled** | **Disabled** | Enforces complete table filling and selection heuristics. |
| `analogy_agent` | `/analogy` | Yes | **Disabled** | **Disabled** | Tripartite structure: Metaphor, Mapping, Breakdown. |
| `list_agent` | `/list` | Yes | **Disabled** | **Disabled** | Bold lead-ins, 2–3 nesting depth, procedural numbering. |
| `appendix_agent` | `/table_formulas`, `/table_definitions`, `/summary` | Yes | **Disabled** | **Disabled** | Exact 4-col formula table, section wikilinks, narrative of fit. |
| `codeblock_agent` | `/codeblock` | Yes | **Disabled** | **Disabled** | STRICT: Only runs if code was explicitly in PDF slides. |

---

## 4. Standalone Automation Scripts

### A. PDF Converter & Asset Extractor (`convert_pdf.py`)
- **Path**: `.agents/plugins/lecture-notes/skills/create-notes/scripts/convert_pdf.py`
- **Dependencies**: `pdfplumber`, `pypdfium2`, `PIL`
- **CLI Usage**:
  ```powershell
  python .agents/plugins/lecture-notes/skills/create-notes/scripts/convert_pdf.py \
    --pdf "<path_to_pdf>" \
    --out-dir "./output" \
    --assets-dir "./output/assets" \
    --doc-name "NOTE - Lec 1 - Threat Analysis" \
    --scale 2.0
  ```
- **Detection Heuristic**:
  Identifies slides with embedded raster images (`len(page.images) > 0`) or complex vector drawings (`curves + lines + rects >= 10`), rendering high-resolution 2.0x PNG assets into `/assets` with sanitized descriptive names.

### B. Active Tag Scanner & Subagent Dispatcher (`extract_and_dispatch.py`)
- **Path**: `.agents/plugins/lecture-notes/skills/create-notes/scripts/extract_and_dispatch.py`
- **CLI Usage**:
  ```powershell
  python .agents/plugins/lecture-notes/skills/create-notes/scripts/extract_and_dispatch.py --file "./output/NOTE - Lec 1 - Threat Analysis.md"
  ```
- **Functionality**:
  - Dynamically scans active `<!-- MODULE:... -->` tags.
  - Writes per-module task queues into `output/.modules/<module_type>.txt`.
  - Automatically respects `parallelism.max_subagents` from `create-notes/SKILL.md`.
  - Pre-computes `output/.modules/dispatch_manifest.json` containing the exact `Subagents` array for direct input to `invoke_subagent`. Only modules present in the skeleton receive a worker subagent.

### C. Atomic In-Place Content Splicer (`insert_module.py`)
- **Path**: `.agents/plugins/lecture-notes/skills/create-notes/scripts/insert_module.py`
- **CLI Usage**:
  ```powershell
  python .agents/plugins/lecture-notes/skills/create-notes/scripts/insert_module.py \
    --note "./output/NOTE - Lec 1 - Threat Analysis.md" \
    --module "formula" \
    --section "2.1" \
    --content-file "./output/.modules/ready/formula_2.1.md"
  ```
- **Guarantees**:
  - Atomically splices populated content directly underneath the matching tag.
  - Preserves comment anchors intact above content for spot-modifications.
  - Eliminates line-number drift and race conditions during parallel population.

### D. Deterministic Format & Whitespace Enforcer (`format_enforcer.py`)
- **Path**: `.agents/plugins/lecture-notes/skills/create-notes/scripts/format_enforcer.py`
- **CLI Usage**:
  ```powershell
  python .agents/plugins/lecture-notes/skills/create-notes/scripts/format_enforcer.py --file "./output/NOTE - Lec 1 - Threat Analysis.md"
  ```
- **Invariants Enforced**:
  - Strictly encloses `# Overview` study tree in triple backticks on separate lines.
  - Eliminates blank lines between headings and `> [!quote]` callouts.
  - Wraps bare slide images in folded cite callouts (`> [!cite]- Slide <N>: <Caption>\n> ![[<image>.png]]`).
  - Cleans up accidental omission disclaimers (`*(Table of contents omitted)*`).
  - Removes forbidden document H1 titles before Overview.

---

## 5. Phase-by-Phase Technical Specifications

### Phase 1: Preprocessing (`/convert_pdf`)
- Ingests raw PDF document.
- Extracts slide text into `<doc_name>_converted.md`.
- Saves all visual diagrams and photographs to `<output_dir>/assets/`.
- User confirmation check if `pause_between_steps: true`.

### Phase 2: Outlining (`/overview`)
- **Mandatory Triple Backticks**: The hierarchical study tree MUST ALWAYS be enclosed in opening and closing triple backticks (` ``` `) on separate lines.
- **Depth Constraint**: Tree depth is strictly capped at 3 levels:
  - Level 1: `Main Topic`
  - Level 2: `Topic` (maps to H1/H2)
  - Level 3: `Subtopic` (maps to H2/H3)
  - **No 4th-level leaf nodes**.
- **Size Cap**: Fenced tree block MUST NOT exceed 25 lines. Prunes 3rd-level subtopics if length > 25.
- **Silent Clean Erasure**: Pruned branches are removed cleanly without meta-commentary notices or omission disclaimers.
- **Star Notation (`*`)**: Trailing `*` indicates topics expanded beyond the slide deck (e.g., `Topic 2*`).
- **Contract Rule**: Every tree node MUST appear as a header in the final note.

### Phase 3: Scaffolding (`/skeleton`)
- **Filename Syntax**: `NOTE - <Type> <Number> - <Topic>.md` (`Lec`, `Quiz`, `Code`, `Read`).
- **No Document H1 Title & No TOC**: Starts directly with YAML frontmatter, Opener blockquote, and `# Overview`.
- **Silent Clean Erasure**: Excluded or stopped elements are cleanly erased without writing notes/commentary stating they were omitted.
- **Quote Callout Immediately Below Header**: Descriptions are placed inside `> [!quote]` immediately on the line after the header (no blank line in between).
- **Verbatim Source Phrasing & Loaded Term Highlighting**: Words and adjectives strictly follow the source slides verbatim (strictly no invented fancy adjectives). Loaded concepts needing explanation are wrapped in `==**...**==`.
- **Folded Cite Image Callouts**: Visual assets extracted from slides are embedded inside folded cite callouts:
  ```markdown
  > [!cite]- Slide 25: Operational modes of Windows BitLocker and authentication factors.
  > ![[page_25_bitlocker_modes.png]]
  ```
- **Placeholder Syntax**: `<!-- MODULE:<TYPE> section="X.Y" topic="..." importance="1-4" -->` (no `id`).
- Runs `extract_modules.py` to create `output/.modules/`.

### Phase 4: Live Parallel Module Population
- Specialized subagents read their respective `.modules/<skill>.txt`.
- Subagents prioritize higher-importance placeholders (`importance="4"` and `importance="3"`).
- **Live In-Place Modification (Directly Underneath Anchor)**: As soon as a module block is generated, the agent immediately inserts the content directly underneath the `<!-- MODULE:... -->` tag in the main note file, preserving the comment anchor intact above it. This allows the user to watch changes materialize in real-time and enables precise spot-modifications later on.

### Phase 5: Appendices & Final Assembly
- `/table_formulas`: Populates 4-column formula table under `## Formulas` (omitted if no equations).
- `/table_definitions`: Populates 2-column glossary under `## Definition of Terms`, sorted by importance, with wikilinks back to the source section (`**[[#Section Name|Term]]**`).
- `/summary`: Populates narrative of fit under `## Summary` inside `> [!tldr]`.

---

## 6. Module Skill Implementation Contracts

### Formula Contract (`/formula`)
Every display formula in the body must contain all four elements in order:
1. `$$ ... $$` with conceptual `\overbrace{...}^{\text{idea}}` and `\underbrace{...}_{\text{idea}}` labels.
2. Hybrid word+math caption immediately below `$$` on its own line: `*Italicized hybrid caption*`.
3. `> [!info]- Breakdown of the formula` (opening purpose, symbol analysis, braced comparative dynamics, assumptions/bounds).
4. `> [!example]-` practice callout (Conceptual check **Q:**/**A:** or Computational solve **Problem:**/**Answer:**).

### Graph Contract (`/graph`)
- Engine: Obsidian-safe Mermaid (`flowchart TD`, `sequenceDiagram`, `stateDiagram-v2`).
- Alphanumeric/underscore node IDs; quoted special character labels: `node["Label (Details)"]`.
- Subgraphs used for trust boundaries and security domains.
- **Verb-Object Edge Phrasing**: Transition edge labels must use verb-object phrases (e.g., `-->|"Transmits signed token"|`).
- Followed by a concise narrative walkthrough explaining state transitions.

### Example Contract (`/example`)
- Always wrapped in folded callouts: `> [!example]- [Title]`.
- Three supported modes:
  - *Case Study / Attack Walkthrough*: Operational Context $\rightarrow$ Step-by-Step Trace $\rightarrow$ Vulnerability & Mitigations.
  - *Worked Numerical Problem*: **Problem:** $\rightarrow$ **Answer:**.
  - *Conceptual Check*: **Q:** $\rightarrow$ **A:**.

### Analogy Contract (`/analogy`)
- Always wrapped in folded tip callouts: `> [!tip]- Analogy: [Concept]`.
- Tripartite structure:
  1. *Real-World Metaphor*: Grounded physical scenario.
  2. *Structural Mapping*: Element-by-element isomorphism to technical components.
  3. *Breakdown Analysis*: Explicit identification of where the analogy ceases to hold.

### Comparison Contracts (`/vs_comparison` & `/multi_comparison`)
- **2-Way**: Heading `### X vs Y`, side-by-side criteria table, folded callout `> [!tip]- Selection Heuristic`.
- **Multi-Option**: Heading `### Side-by-side comparison`, multi-column criteria table ($\ge 3$ options), row-column dual encodings when relevant, followed by trade-off synthesis.
- **Completeness**: Every table cell must be filled; no empty cells.

### Appendix Summary Contract (`/summary`)
- Exclusively located under `## Summary` inside `> [!tldr]`.
- Strictly walks the `# Overview` tree top-to-bottom in order.
- **Narrative of Fit**: Explains why each **bold** topic is introduced to resolve limitations left by the previous concept.
- Ink weighted by header depth: H1 detailed, H2 medium, H3/leaves brief.
- Passing mentions bolded with zero extra prose.
- Paragraph breaks inside callout using blank `>` lines.

---

## 7. Step Logging & Trajectory Inspection

When `log_step_outputs: true` is configured in `create-notes/SKILL.md`, the orchestrator writes snapshots of intermediate pipeline state to `<output_dir>/.logs/`:

- `01_converted.md`: Clean Markdown output from `convert_pdf.py`.
- `02_overview.md`: The approved hierarchical study map.
- `03_skeleton.md`: Scaffolding note with unpopulated module tags and embedded assets.
- `04_modules_<skill>.md`: Generated module block payloads from worker agents.
- `05_final_note.md`: Full assembled note snapshot for auditing and regression diffing.
