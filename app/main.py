#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: @spacemany2k38
# 2025-12-24

import sys
from pathlib import Path

# Allow running both as module and as script
if __name__ == "__main__" and __package__ is None:
    sys.path.append(str(Path(__file__).resolve().parent.parent))
    __package__ = "app"

from app import __version__
from app.core.date_calc import (
    get_day_of_year,
    get_week_of_year,
    get_day_name,
    get_month_calendar,
    get_complete_date
)
from app.utils.doc_reader import read_app_doc


def print_help():
    """Print help message from documentation."""
    doc = read_app_doc('yday')
    
    desc = doc.get('description', 'prints the current day of the year (1-366)')
    usage = doc.get('usage', ['yday', 'yday --help', 'yday --version'])
    
    print(f"yday - {desc}")
    print("\nUSAGE:")
    for u in usage:
        print(f"    {u}")
    print("\nOPTIONS:")
    print("    -h, --help        Show help message")
    print("    -v, --version     Show version information")
    print("    -w                Show week of the year")
    print("    -n                Show full name of the day in lowercase (localized)")
    print("    -m                Show calendar for current month")
    print("    -c                Show complete date/time")


def print_version():
    """Print version from documentation."""
    doc = read_app_doc('yday')
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

    if args[0] == "-w":
        print(get_week_of_year())
        return 0

    if args[0] == "-n":
        print(get_day_name())
        return 0

    if args[0] == "-m":
        print(get_month_calendar())
        return 0

    if args[0] == "-c":
        print(get_complete_date())
        return 0

    # Unknown arg
    print(f"Unknown option: {args[0]}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
