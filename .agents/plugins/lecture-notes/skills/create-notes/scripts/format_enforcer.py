#!/usr/bin/env python3
"""
format_enforcer.py - Deterministic Markdown normalization and invariant enforcement.

Enforces:
1. Triple-backtick fencing for # Overview tree.
2. Zero blank lines between section headers (##, ###) and introductory > [!quote] callouts.
3. Bare image links wrapped in folded cite callouts.
4. Clean silent erasure: strips accidental placeholder notices like *(Table of contents omitted)*.
5. Accidental duplicate headers/quotes immediately under <!-- MODULE:... --> tags stripped.
"""
import sys
import re
import argparse
from pathlib import Path

def enforce_overview_fencing(content: str) -> str:
    pattern = r'(# Overview\s*\n)(```[a-zA-Z]*\n)?([\s\S]*?)(```\s*\n|(?=\n---)|(?=\n##\s))'
    def repl(m):
        header = m.group(1)
        tree = m.group(3).strip()
        return f"{header}```\n{tree}\n```\n"
    return re.sub(pattern, repl, content, count=1)

def enforce_header_quote_adjacency(content: str) -> str:
    pattern = r'(^(?:#{2,4})\s+[^\n]+)\n+(\s*>\s*\[!quote\])'
    return re.sub(pattern, r'\1\n\2', content, flags=re.MULTILINE)

def enforce_cite_callouts(content: str) -> str:
    lines = content.splitlines()
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        match = re.match(r'^!\[\[(.*\.(?:png|jpe?g|webp|svg))\]\]', line.strip())
        if match:
            prev_line = lines[i - 1].strip() if i > 0 else ""
            if not prev_line.startswith(">"):
                img_name = match.group(1)
                caption = f"Slide illustration: {Path(img_name).stem.replace('_', ' ').capitalize()}"
                new_lines.append(f"> [!cite]- {caption}")
                new_lines.append(f"> ![[{img_name}]]")
                i += 1
                continue
        new_lines.append(line)
        i += 1
    return "\n".join(new_lines)

def enforce_silent_erasure(content: str) -> str:
    disclaimers = [
        r'\*\(Table of contents omitted[^\)]*\)\*',
        r'\[Table of contents omitted[^\]]*\]',
        r'\*\(Omitted for brevity\)\*',
        r'\[Omitted\]',
        r'\*\(Omitted\)\*'
    ]
    for d in disclaimers:
        content = re.sub(d, '', content, flags=re.IGNORECASE)
    return content

def enforce_module_body_cleanliness(content: str) -> str:
    """Strip accidental duplicate headers or quote callouts immediately below module tags."""
    lines = content.splitlines()
    new_lines = []
    i = 0
    in_module = False
    while i < len(lines):
        line = lines[i]
        if re.match(r'^<!--\s*MODULE:[A-Za-z0-9_-]+.*-->', line.strip()):
            new_lines.append(line)
            i += 1
            # Check lines immediately following module tag
            while i < len(lines):
                next_line = lines[i].strip()
                # If blank line immediately after tag, advance
                if not next_line:
                    new_lines.append(lines[i])
                    i += 1
                    continue
                # If redundant header or quote callout, skip it
                if re.match(r'^#{2,4}\s+', next_line) or re.match(r'^>\s*\[!quote\]', next_line):
                    i += 1
                    # Also skip any following lines that were part of that quote callout
                    while i < len(lines) and lines[i].strip().startswith(">"):
                        i += 1
                    continue
                break
            continue
        new_lines.append(line)
        i += 1
    return "\n".join(new_lines)

def run_format_enforcer(file_path: Path) -> bool:
    if not file_path.is_file():
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        return False

    raw = file_path.read_text(encoding="utf-8")
    content = raw
    content = enforce_overview_fencing(content)
    content = enforce_header_quote_adjacency(content)
    content = enforce_cite_callouts(content)
    content = enforce_silent_erasure(content)
    content = enforce_module_body_cleanliness(content)

    if content != raw:
        file_path.write_text(content, encoding="utf-8")
        print(f"Format enforcer: Applied normalizations to {file_path}")
        return True
    else:
        print(f"Format enforcer: Note is already compliant: {file_path}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Deterministic format enforcer for Obsidian lecture notes.")
    parser.add_argument("--file", "-f", required=True, help="Path to markdown note")
    args = parser.parse_args()

    run_format_enforcer(Path(args.file))

if __name__ == "__main__":
    main()
