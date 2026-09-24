---
name: start
description: >-
  Initializes the lecture note generation session by inspecting the source PDF
  using the native view_file tool, reading configuration settings, and setting up metadata.
# Inherits all properties from create-notes/SKILL.md (output_dir, tone, detail_level, target_audience)
# Only populate properties below to explicitly override:
output_dir: null
tone: null
detail_level: null
---

# Start Session (`/start`)

Use this skill at the beginning of a note generation session to register the source PDF, inspect its structure, and initialize session metadata.

## Configuration Inheritance

> [!NOTE]
> Inherits `output_dir`, `tone`, `detail_level`, and `target_audience` from `create-notes/SKILL.md`.
> Values populated above override parent defaults for this session.

## Critical Compliance Rule

> [!CAUTION]
> **PDF Reading Rule**: You MUST ALWAYS use the native `view_file` tool to inspect and read PDFs.
> **NEVER** write or execute Python code (e.g., `pypdf`, `pdfplumber`, `PyMuPDF`) to extract text or data from a document file.

---

## Instructions for the Agent

1. **Verify the Source PDF**:
   - Check if the user specified a PDF file path or attached a PDF.
   - If not specified, ask the user to provide the path to the PDF.
   - Call `view_file` on the PDF path to inspect the document, check total pages, title slide/header, author, and table of contents.

2. **Initialize Session Context**:
   - Record the following session parameters:
     - `document_title`: Title of the lecture or textbook chapter.
     - `source_file`: Absolute path to the PDF.
     - `total_pages`: Total page count.
     - `target_output_file`: `<effective_output_dir>/<Sanitized_Title>.md`.
     - `effective_config`: Inherited frontmatter settings from `create-notes` with any populated local overrides.

3. **Create Output Directory**:
   - Ensure the directory specified in `output_dir` (default inherited: `./output`) exists.

4. **Output Session Summary to User**:
   - Present a concise confirmation table:
     | Property | Effective Value | Source |
     | :--- | :--- | :--- |
     | Source PDF | `<path>` | User Input |
     | Document Title | `<title>` | PDF Title |
     | Pages Detected | `<total_pages>` | view_file |
     | Output Target | `<target_output_file>` | Effective Config |
     | Tone / Detail | `<tone>` / `<detail_level>` | Effective Config |
   - Indicate readiness to proceed to `/overview`.
