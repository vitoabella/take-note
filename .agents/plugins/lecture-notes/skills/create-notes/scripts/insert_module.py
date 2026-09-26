#!/usr/bin/env python3
"""
insert_module.py - Atomically splices generated module content directly underneath
its target <!-- MODULE:... --> comment tag in the markdown note file, preserving the tag intact.
"""
import sys
import os
import re
import argparse
import tempfile
from pathlib import Path

def find_tag_line(lines: list[str], exact_tag: str = None, module_type: str = None, section: str = None) -> int:
    """Finds the 0-indexed line number of the matching tag."""
    if exact_tag:
        clean_tag = exact_tag.strip()
        for idx, line in enumerate(lines):
            if clean_tag in line:
                return idx

    # If module_type and section provided
    if module_type:
        pattern_str = rf'<!--\s*MODULE:{re.escape(module_type)}'
        if section:
            pattern_str += rf'\s+[^>]*section="{re.escape(section)}"'
        pattern = re.compile(pattern_str)
        for idx, line in enumerate(lines):
            if pattern.search(line):
                return idx

    return -1

def insert_content(note_path: Path, content: str, exact_tag: str = None, module_type: str = None, section: str = None) -> bool:
    if not note_path.is_file():
        print(f"Error: Note file '{note_path}' does not exist.", file=sys.stderr)
        return False

    raw_text = note_path.read_text(encoding="utf-8")
    lines = raw_text.splitlines(keepends=True)

    tag_idx = find_tag_line(lines, exact_tag, module_type, section)
    if tag_idx == -1:
        identifier = exact_tag or f"module={module_type}, section={section}"
        print(f"Error: Could not locate tag [{identifier}] in '{note_path}'.", file=sys.stderr)
        return False

    # Check for duplicate insertion
    clean_insert = content.strip()
    next_lines_chunk = "".join(lines[tag_idx+1:tag_idx+10])
    if clean_insert[:50] in next_lines_chunk:
        print(f"Warning: Content appears already inserted under tag at line {tag_idx+1}. Skipping.")
        return True

    # Prepare insertion block (ensure newline termination)
    formatted_block = clean_insert + "\n\n"

    # Insert directly below the tag line
    lines.insert(tag_idx + 1, formatted_block)

    # Atomic write via temp file
    note_dir = note_path.parent
    with tempfile.NamedTemporaryFile("w", dir=note_dir, encoding="utf-8", delete=False) as tmp:
        tmp.writelines(lines)
        tmp_name = tmp.name

    import time
    for attempt in range(10):
        try:
            os.replace(tmp_name, str(note_path))
            break
        except PermissionError:
            if attempt == 9:
                raise
            time.sleep(0.2)
    print(f"Successfully inserted content directly underneath tag at line {tag_idx+1}.")
    return True

def main():
    parser = argparse.ArgumentParser(description="Atomically insert content underneath a MODULE comment tag.")
    parser.add_argument("--note", "-n", required=True, help="Path to the markdown note file")
    parser.add_argument("--tag", "-t", help="Exact MODULE comment tag string")
    parser.add_argument("--module", "-m", help="Module type (e.g. formula, graph)")
    parser.add_argument("--section", "-s", help="Section identifier (e.g. 2.1)")
    parser.add_argument("--content-file", "-f", help="Path to file containing content to insert")
    parser.add_argument("--content", "-c", help="Direct string content to insert")

    args = parser.parse_args()

    content = ""
    if args.content_file:
        c_path = Path(args.content_file)
        if not c_path.is_file():
            print(f"Error: Content file '{c_path}' not found.", file=sys.stderr)
            sys.exit(1)
        content = c_path.read_text(encoding="utf-8")
    elif args.content:
        content = args.content
    else:
        print("Error: Either --content-file or --content must be provided.", file=sys.stderr)
        sys.exit(1)

    if not args.tag and not args.module:
        print("Error: Either --tag or --module must be specified.", file=sys.stderr)
        sys.exit(1)

    success = insert_content(
        note_path=Path(args.note),
        content=content,
        exact_tag=args.tag,
        module_type=args.module,
        section=args.section
    )

    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
