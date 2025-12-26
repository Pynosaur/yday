#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: @spacemany2k38
# 2025-12-24

import datetime
import re
import sys
from pathlib import Path

# Allow running both as module and as script
if __name__ == "__main__" and __package__ is None:
    sys.path.append(str(Path(__file__).resolve().parent.parent))
    __package__ = "app"

from app import __version__


def get_day_of_year():
    """Return the current day of the year (1-366)."""
    today = datetime.date.today()
    return today.timetuple().tm_yday


def read_doc():
    """Read yday.yaml from doc directory."""
    doc_paths = [
        Path(__file__).parent.parent.parent / "doc" / "yday.yaml",  # Source
        Path("doc") / "yday.yaml",  # Bundled
    ]
    
    # Nuitka onefile support
    if hasattr(sys, '_MEIPASS'):
        doc_paths.insert(0, Path(sys._MEIPASS) / "doc" / "yday.yaml")
    
    for path in doc_paths:
        if path.exists():
            try:
                content = path.read_text()
                
                # Extract VERSION
                version = re.search(r'^VERSION:\s*"([^"]+)"', content, re.MULTILINE)
                version = version.group(1) if version else __version__
                
                # Extract DESCRIPTION
                desc = re.search(r'^DESCRIPTION:\s*>\s*(.+?)(?=^[A-Z_]+:)', content, re.MULTILINE | re.DOTALL)
                desc = desc.group(1).strip() if desc else ''
                
                # Extract USAGE items (between USAGE: and OPTIONS:)
                usage_section = re.search(r'^USAGE:(.+?)^OPTIONS:', content, re.MULTILINE | re.DOTALL)
                usage = re.findall(r'-\s*"([^"]+)"', usage_section.group(1)) if usage_section else []
                
                return {'version': version, 'description': desc, 'usage': usage}
            except (OSError, UnicodeDecodeError):
                continue
    
    return {}


def print_help():
    """Print help message from documentation."""
    doc = read_doc()
    
    desc = doc.get('description', 'prints the current day of the year (1-366)')
    usage = doc.get('usage', ['yday', 'yday --help', 'yday --version'])
    
    print(f"yday - {desc}")
    print("\nUSAGE:")
    for u in usage:
        print(f"    {u}")
    print("\nOPTIONS:")
    print("    -h, --help        Show help message")
    print("    -v, --version     Show version information")


def print_version():
    """Print version from documentation."""
    doc = read_doc()
    print(doc.get('version', __version__))


def main():
    """Print the current day of the year or version/help."""
    args = sys.argv[1:]

    if not args:
        print(get_day_of_year())
        return 0

    if args[0] in ("-h", "--help"):
        print_help()
        return 0

    if args[0] in ("-v", "--version"):
        print_version()
        return 0

    # Unknown arg
    print(f"Unknown option: {args[0]}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())

