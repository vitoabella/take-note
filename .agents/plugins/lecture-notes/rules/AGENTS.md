# Lecture Notes Plugin Operational Rules

When executing tasks within this plugin or generating Obsidian lecture notes:

1. **Strict Verbatim Source Wording for generated content**:
   - All topic descriptions, summaries, adjectives, and technical terms MUST strictly adhere to the source material (the lecture slides and converted Markdown text) verbatim as much as possible.
   - Strictly prohibit invented "sophisticated" or flowery adjectives (e.g. avoid inventing phrases like "heterogeneous distributed components" or "confidentiality perimeter collapses" unless they appear verbatim in the source).

2. **Strict Just-In-Time (JIT) Reference Loading**:
   - The agent MUST NOT view, inspect, or search downstream reference files or module templates for future pipeline steps.
   - Read ONLY the reference markdown document (`references/*.md`) explicitly designated for the current, active step.

3. **No Script Source Inspection (Black-Box Execution)**:
   - Helper scripts (`scripts/*.py`) are command-line utilities, NOT reference documents to be read or inspected with file-viewing tools.
   - Always execute the provided PowerShell commands directly using the exact arguments specified in the skill/reference. Do NOT run `--help` or probe flags beforehand.
   - Run `--help` ONLY as an error-recovery fallback if a command actually fails during execution.