---
name: convert_pdf
description: >-
  Preprocesses source PDF documents into clean Markdown text and extracts all visual diagrams,
  figures, and photos into an /assets folder relative to the output directory.
# Inherits: tone, detail_level, target_audience from create-notes/SKILL.md
extract_images: true
render_scale: 2.0
assets_subdir: "assets"
---

# PDF Conversion Skill (`/convert_pdf`)

Use this skill to convert raw lecture slide or textbook PDFs into a unified Markdown representation with extracted image assets before initiating note generation.

---

## Purpose & Architecture

1. **Text Extraction**: Converts all pages of the source PDF into clean Markdown text, preserving slide boundaries (`## Page N: <Title>`) and text content.
2. **Visual & Diagram Extraction**: Identifies slides containing visual images, photos, charts, or vector diagrams (flowcharts, architectures, DFDs, threat trees) and saves high-resolution PNG renders into `<output_dir>/assets/<image_name>.png`.
3. **Markdown Grounding Asset**: Generates `<output_dir>/<doc_name>_converted.md` containing all slide text and embedded Obsidian image links (`![[<image>.png]]` + italic caption). Downstream skills use this converted markdown as their authoritative source of truth.

---

## Instructions for the Agent

1. **Execute Preprocessing Script**:
   Run the standalone conversion script from the terminal:
   ```powershell
   python .agents/plugins/lecture-notes/skills/create-notes/scripts/convert_pdf.py --pdf "<path_to_pdf>" --out-dir "<output_dir>"
   ```
2. **Verify Converted Markdown & Assets**:
   - Check that `<output_dir>/<doc_name>_converted.md` was created.
   - Check that visual figures were placed into `<output_dir>/assets/`.
3. **Pass to Downstream Pipeline**:
   - Supply the converted Markdown file as the primary context for `/start`, `/overview`, and `/skeleton`.
