# Obsidian Lecture Notes Agent & Skills Suite

Transform academic lecture slides, technical slide decks, and textbook PDFs into comprehensive, publication-grade study notes designed specifically for **Obsidian**.

Powered by an autonomous multi-agent skills architecture in **Antigravity (AGY)**, the suite orchestrates structured document decomposition, visual diagram extraction, parallel topic synthesis, and bidirectional graph connectivity.

---

## At a Glance

```text
       Source PDF / Deck
              │
              ▼
   ┌──────────────────────┐
   │  1. Ingestion & Pre  │──► Extracts slide text & high-res figures to /assets
   │     (/convert_pdf)   │
   └──────────┬───────────┘
              │
              ▼
   ┌──────────────────────┐
   │  2. Study Map Tree   │──► Builds hierarchical contract (max 3 levels, ≤ 25 lines)
   │     (/overview)      │
   └──────────┬───────────┘
              │
              ▼
   ┌──────────────────────┐
   │  3. Note Scaffolding │──► Embeds images directly (![[...]]) & inserts module tags
   │     (/skeleton)      │
   └──────────┬───────────┘
              │
              ▼
   ┌──────────────────────┐
   │  4. Parallel Workers │──► Specialized subagents populate math, graphs, case studies
   │   (Live Updates)     │    *Updates main note live in-place for real-time viewing*
   └──────────┬───────────┘
              │
              ▼
   ┌──────────────────────┐
   │  5. Appendices       │──► 4-column formula sheet, glossary with section wikilinks,
   │  (/summary, tables)  │    and narrative summary inside folded [!tldr]
   └──────────────────────┘
```

---

## Key Highlights

- **Master Orchestrator (`/create-notes`)**: Coordinates the entire 5-phase pipeline end-to-end or runs individual phases on demand with interactive step pausing.
- **Live Document Evolution**: Rather than waiting for long batch runs, specialized worker agents write their output directly underneath the placeholder tags in the main note as they finish. This preserves the `<!-- MODULE:... -->` tags intact for future spot-modifications while letting you watch your note materialize live in Obsidian.
- **First-Class Obsidian Visuals**:
  - **Folded Cite Image Callouts**: High-resolution diagrams and photos are automatically extracted to `/assets` and embedded in folded cite callouts (`> [!cite]- Slide N: Caption\n> ![[figure.png]]`).
  - **Interactive Mermaid Diagrams**: Architecture diagrams, state machines, and threat trees rendered natively with descriptive verb-object edge labels.
  - **Folded Modern Callouts**: Pedagogical analogies (`> [!tip]-`), attack walkthroughs (`> [!example]-`), and formula breakdowns (`> [!info]-`).
- **Pedagogical Depth & Anti-Laziness**:
  - **4-Part Formula Standard**: Equations feature KaTeX display math, conceptual `\overbrace`/`\underbrace` labels, hybrid word-math captions, structural breakdowns, and worked practice problems.
  - **Grounding & Descriptors**: Key adjectives and mechanisms are highlighted (`==**descriptor**==`) to ensure deep conceptual dissection rather than superficial bullet lists.
- **Bidirectional Vault Connectivity**:
  - The appendix glossary links directly back to the exact section where each concept was introduced (`[[#Section Heading|Term]]`), creating a dense web of internal connections for Obsidian graph view.
- **Configurable Control**:
  - Control tone, detail level, interactive step pausing (`pause_between_steps`), and intermediate step logging (`log_step_outputs`) directly in YAML frontmatter.

---

## 5-Phase Note Generation Lifecycle

| Phase | Skill | What It Does | Output Artifact |
| :--- | :--- | :--- | :--- |
| **1. Ingestion** | `/convert_pdf` | Converts PDF text to Markdown and extracts visual figures, diagrams, and photos into local storage. | `NOTE - Lec 1 - Topic_converted.md`<br>`assets/<figure>.png` |
| **2. Outlining** | `/overview` | Analyzes core topics and builds an authoritative 3-level hierarchical study tree (strictly $\le 25$ lines). | Conceptual outline tree |
| **3. Scaffolding** | `/skeleton` | Builds the document skeleton (no doc H1), wraps verbatim descriptions in immediate `> [!quote]`, embeds visuals in folded `> [!cite]-`, and places module tags. | `NOTE - Lec 1 - Topic.md` (Scaffold) |
| **4. Live Population** | Subagents | Dispatches parallel specialized agents (Formula, Graph, Example, Comparison, List, Analogy) that populate content live in-place. | `NOTE - Lec 1 - Topic.md` (Populated) |
| **5. Appendices** | Appendices | Generates an appendix formula cheat sheet, a technical glossary with section links, and an overview-guided narrative summary. | Final publication-grade note |

---

## Standardized Output Naming

All generated notes follow a clean, uniform naming scheme based on content type:

```text
NOTE - <Type> <Number> - <Topic>.md
```

- **Lectures**: `NOTE - Lec 1 - Threat Analysis.md`
- **Quizzes & Exam Reviews**: `NOTE - Quiz 1 - Cryptography.md`
- **Code & Notebooks**: `NOTE - Code 1 - Socket Programming.md`
- **Readings & Whitepapers**: `NOTE - Read 1 - Bitcoin Architecture.md`

---

## Quick Start

### Run the Pipeline
In the Antigravity chat, trigger the master orchestrator slash command:
```text
/create-notes
```
Provide the path to your source PDF when prompted. The orchestrator automatically:
1. Converts the PDF and extracts visual diagrams into `/assets` (`references/convert_pdf.md`).
2. Generates the 3-level `# Overview` study tree (`references/overview.md`).
3. Scaffolds the note with verbatim source descriptors and cite callouts (`references/skeleton.md`).
4. Dispatches specialized subagents to populate KaTeX formulas, Mermaid graphs, and case studies in parallel.
5. Assembles formula cheat sheets, glossary wikilinks, and narrative summaries in the appendices.

---

## Documentation

- **High-Level Overview**: This file (`README.md`) provides the conceptual overview, user workflow, and visual standards.
- **Technical Architecture**: For the engineering manual, cascading frontmatter inheritance model, subagent permission matrix, script CLI references, and skill contracts, see:
  👉 **[Technical Architecture & Developer Guide (README-TECHNICAL.md)](README-TECHNICAL.md)**
