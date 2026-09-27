#!/usr/bin/env python3
"""
extract_modules.py - Extract exact module tags (including multi-line Context Capsules)
grouped per skill into individual input files.
"""
import sys
import re
import json
import argparse
from pathlib import Path
from typing import Optional

MODULE_REGEX = re.compile(r'(<!--\s*MODULE:([A-Za-z0-9_-]+)(?:[\s\S]*?)?-->)')

def extract_and_group(file_path: Path, out_dir: Optional[Path] = None) -> list:
    text = file_path.read_text(encoding="utf-8")
    grouped = {}

    for match in MODULE_REGEX.finditer(text):
        full_tag = match.group(1).strip()
        m_type = match.group(2).strip()
        if m_type not in grouped:
            grouped[m_type] = []
        grouped[m_type].append(full_tag)

    if out_dir:
        out_dir.mkdir(parents=True, exist_ok=True)
        for m_type, tags in grouped.items():
            skill_file = out_dir / f"{m_type}.txt"
            skill_file.write_text("\n\n".join(tags) + "\n", encoding="utf-8")

    return [
        {
            "module": m_type,
            "count": len(tags),
            "tags": tags,
        }
        for m_type, tags in sorted(grouped.items())
    ]

def main():
    parser = argparse.ArgumentParser(description="Extract exact module tags grouped per module.")
    parser.add_argument("--file", "-f", required=True, help="Path to skeleton markdown note")
    parser.add_argument("--out-dir", "-o", default=None, help="Optional directory to save per-module txt files")
    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.is_file():
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    out_dir = Path(args.out_dir) if args.out_dir else None
    modules = extract_and_group(file_path, out_dir)

    # Print JSON array directly to stdout
    print(json.dumps(modules, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
