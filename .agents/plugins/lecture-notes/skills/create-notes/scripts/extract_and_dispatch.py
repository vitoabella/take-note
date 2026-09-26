#!/usr/bin/env python3
"""
extract_and_dispatch.py - Scans skeleton note for module tags, outputs isolated task queues,
and dynamically generates the dispatch_manifest.json payload for invoke_subagent.

Only modules actually present in the skeleton will be included in the dispatch manifest.
"""
import sys
import os
import re
import json
import argparse
from pathlib import Path

MODULE_REGEX = re.compile(r'(<!--\s*MODULE:([A-Za-z0-9_-]+)(?:\s+(.*?))?-->)')
ATTR_REGEX = re.compile(r'([a-zA-Z_]+)="([^"]*)"')

ROLE_TITLES = {
    'formula': 'Formula Specialist',
    'graph': 'Diagram Specialist',
    'analogy': 'Analogy Specialist',
    'example': 'Example Specialist',
    'list': 'List Specialist',
    'vs_comparison': 'Comparison Specialist',
    'multi_comparison': 'Matrix Comparison Specialist',
    'codeblock': 'Code Specialist',
    'quiz': 'Quiz Specialist',
    'table_formulas': 'Appendix Formula Specialist',
    'table_definitions': 'Glossary Specialist',
    'summary': 'Summary Specialist'
}

def parse_yaml_max_subagents(skill_path: Path) -> int:
    """Extract max_subagents from create-notes/SKILL.md frontmatter."""
    if not skill_path or not skill_path.is_file():
        return 3
    try:
        content = skill_path.read_text(encoding="utf-8")
        match = re.search(r'max_subagents:\s*(\d+)', content)
        if match:
            return int(match.group(1))
    except Exception:
        pass
    return 3

def extract_and_build_manifest(file_path: Path, out_dir: Path, max_subagents: int = 3, plugin_root: str = None) -> dict:
    text = file_path.read_text(encoding="utf-8")
    grouped = {}
    tag_details = []

    for line_idx, line in enumerate(text.splitlines(), start=1):
        for match in MODULE_REGEX.finditer(line):
            full_tag = match.group(1).strip()
            m_type = match.group(2).strip()
            attr_str = match.group(3) or ""
            attrs = dict(ATTR_REGEX.findall(attr_str))

            raw_depth = attrs.get("depth") or attrs.get("importance", 3)
            try:
                depth_val = int(raw_depth)
                if depth_val < 1 or depth_val > 3:
                    depth_val = 3
            except ValueError:
                depth_val = 3

            if m_type not in grouped:
                grouped[m_type] = []
            grouped[m_type].append(full_tag)

            tag_details.append({
                "type": m_type,
                "section": attrs.get("section", ""),
                "topic": attrs.get("topic", ""),
                "depth": depth_val,
                "full_tag": full_tag,
                "line": line_idx
            })

    out_dir.mkdir(parents=True, exist_ok=True)
    ready_dir = out_dir / "ready"
    ready_dir.mkdir(parents=True, exist_ok=True)

    # 1. Write per-skill task files
    for m_type, tags in grouped.items():
        skill_file = out_dir / f"{m_type}.txt"
        skill_file.write_text("\n".join(tags) + "\n", encoding="utf-8")

    # Resolve reference path
    ref_base = ".agents/plugins/lecture-notes/skills/create-notes/references"
    if plugin_root:
        ref_base = f"{plugin_root}/skills/create-notes/references"

    # 2. Build Subagents array dynamically ONLY for detected modules
    all_subagents = []
    for m_type in sorted(grouped.keys()):
        role = ROLE_TITLES.get(m_type, f"{m_type.capitalize()} Specialist")
        task_count = len(grouped[m_type])
        ref_doc = f"{ref_base}/{m_type}.md"
        
        prompt = (
            f"You are the {role}.\n"
            f"1. Read the specification guidelines in '{ref_doc}'. Follow its Depth Specification and Expected Output Format.\n"
            f"2. Your task queue has {task_count} item(s) in '{out_dir.as_posix()}/{m_type}.txt'.\n"
            f"3. For each placeholder tag in '{file_path.as_posix()}', generate the complete block matching the target depth attribute in the tag.\n"
            f"4. CRITICAL FORMAT RULE: Output ONLY the module body content (e.g. table, diagram, formula, list, callout). "
            f"The section header and quote callout are already provided in the skeleton. "
            f"Do NOT output any section headers (##, ###) or quote callouts (> [!quote]).\n"
            f"5. Insert each populated block directly underneath its tag using:\n"
            f"   python .agents/plugins/lecture-notes/skills/create-notes/scripts/insert_module.py "
            f"--note \"{file_path.as_posix()}\" --tag \"<EXACT_TAG>\" --content-file \"<FILE>\"\n"
            f"Do NOT delete or replace the <!-- MODULE:... --> comment tag."
        )

        all_subagents.append({
            "TypeName": "self",
            "Role": role,
            "Model": "inherit",
            "Workspace": "inherit",
            "Prompt": prompt
        })

    # 3. Create concurrency batches respecting max_subagents
    batches = []
    for i in range(0, len(all_subagents), max_subagents):
        batch = all_subagents[i:i + max_subagents]
        batches.append({
            "batch_number": (i // max_subagents) + 1,
            "subagents_count": len(batch),
            "Subagents": batch
        })

    manifest = {
        "source_note": str(file_path),
        "total_placeholders": len(tag_details),
        "detected_modules": sorted(grouped.keys()),
        "max_concurrent_subagents": max_subagents,
        "total_batches": len(batches),
        "batches": batches,
        "all_subagents": all_subagents
    }

    manifest_path = out_dir / "dispatch_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    return manifest

def main():
    parser = argparse.ArgumentParser(description="Extract active module tags and build invoke_subagent dispatch manifest.")
    parser.add_argument("--file", "-f", required=True, help="Path to skeleton markdown note")
    parser.add_argument("--out-dir", "-o", help="Directory for manifests (defaults to <note_dir>/.modules)")
    parser.add_argument("--max-subagents", "-m", type=int, help="Max concurrent subagents (overrides config)")
    parser.add_argument("--config", "-c", help="Path to create-notes/SKILL.md to read max_subagents")
    parser.add_argument("--plugin-root", help="Path to plugin root")
    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.is_file():
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    out_dir = Path(args.out_dir) if args.out_dir else file_path.parent / ".modules"
    
    max_sub = args.max_subagents
    if max_sub is None:
        skill_cfg = Path(args.config) if args.config else Path(".agents/plugins/lecture-notes/skills/create-notes/SKILL.md")
        max_sub = parse_yaml_max_subagents(skill_cfg)

    manifest = extract_and_build_manifest(file_path, out_dir, max_subagents=max_sub, plugin_root=args.plugin_root)

    print(f"Detected {len(manifest['detected_modules'])} active module types: {', '.join(manifest['detected_modules'])}")
    print(f"Total placeholders: {manifest['total_placeholders']} across {manifest['total_batches']} batch(es).")
    print(f"Manifest generated: {out_dir / 'dispatch_manifest.json'}")

if __name__ == "__main__":
    main()
