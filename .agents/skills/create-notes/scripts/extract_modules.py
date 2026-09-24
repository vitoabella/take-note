#!/usr/bin/env python3
"""
extract_modules.py - Extract exact module tags grouped per skill into individual input files.
"""
import sys
import re
import argparse
from pathlib import Path

MODULE_REGEX = re.compile(r'(<!--\s*MODULE:([A-Za-z0-9_-]+)(?:\s+.*?)?-->)')

def extract_and_group(file_path: Path, out_dir: Path) -> list[str]:
    text = file_path.read_text(encoding="utf-8")
    grouped = {}

    for line in text.splitlines():
        for match in MODULE_REGEX.finditer(line):
            full_tag = match.group(1).strip()
            m_type = match.group(2).strip()
            if m_type not in grouped:
                grouped[m_type] = []
            grouped[m_type].append(full_tag)

    out_dir.mkdir(parents=True, exist_ok=True)
    for m_type, tags in grouped.items():
        skill_file = out_dir / f"{m_type}.txt"
        skill_file.write_text("\n".join(tags) + "\n", encoding="utf-8")

    return sorted(grouped.keys())

def main():
    parser = argparse.ArgumentParser(description="Extract exact module tags grouped per skill into files.")
    parser.add_argument("--file", "-f", required=True, help="Path to skeleton markdown note")
    parser.add_argument("--out-dir", "-o", help="Directory to save per-skill files (defaults to <skeleton_dir>/.modules)")
    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.is_file():
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    out_dir = Path(args.out_dir) if args.out_dir else file_path.parent / ".modules"
    unique_types = extract_and_group(file_path, out_dir)

    # Print clean comma-separated list without triple quotes
    print(", ".join(unique_types))

if __name__ == "__main__":
    main()
