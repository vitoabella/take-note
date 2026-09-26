#!/usr/bin/env python3
"""
create_output_dir.py - Creates the output directory for lecture notes generation artifacts.
"""
import sys
import argparse
from pathlib import Path

def create_output_directory(out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir

def main():
    parser = argparse.ArgumentParser(description="Create output directory for lecture notes generation.")
    parser.add_argument("--output-dir", "--out-dir", "-o", dest="output_dir", default="./output", help="Directory to create (default: ./output)")
    args = parser.parse_args()

    out_dir = Path(args.output_dir)
    try:
        created_path = create_output_directory(out_dir)
        print(f"SUCCESS: Output directory ready at '{created_path.resolve()}'")
    except Exception as e:
        print(f"Error creating output directory '{out_dir}': {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
