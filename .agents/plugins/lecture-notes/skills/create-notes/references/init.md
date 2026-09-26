---
# Module-specific overrides
output_dir: null
tone: null
detail_level: null
---

# Session Initialization Specification

Use this skill at the beginning of a note generation session to register the source PDF, inspect its structure, and initialize session metadata.

---

## Instructions for the Agent


1. **Create Output Directory**:
   - Create the output directory specified in `output_dir`
     ```powershell
     python .agents/plugins/lecture-notes/skills/create-notes/scripts/create_output_dir.py --output-dir "<output_dir>"
     ```

2. **Initialize Session Context**:
   - Record the following session parameters:
     - `document_title`: Title of the lecture or textbook chapter.
     - `source_file`: Absolute path to the PDF.
     - `total_pages`: Total page count.
     - `target_output_file`: `<effective_output_dir>/<Sanitized_Title>.md`.
     - `effective_config`: Inherited frontmatter settings from `create-notes` with any populated local overrides.


3. **Output Session Summary to User**:
   - Present a concise confirmation table:
     | Property | Effective Value | Source |
     | :--- | :--- | :--- |
     | Source PDF | `<path>` | User Input |
     | Document Title | `<title>` | PDF Title |
     | Pages Detected | `<total_pages>` | view_file |
     | Output Target | `<target_output_file>` | Effective Config |
     | Tone / Detail | `<tone>` / `<detail_level>` | Effective Config |
   - Indicate readiness to proceed to `/overview`.
