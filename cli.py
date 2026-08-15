#!/usr/bin/env python3
"""Minimal RIM registry CLI.

This first executable slice validates module contracts and lists available modules.
It intentionally has no network credentials or destructive behavior.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re

ROOT = Path(__file__).parent
MODULES = ROOT / "modules"
REQUIRED = {"name", "subname", "description", "inputs", "use_case", "default", "result", "revolt", "version", "type", "status"}


def parse_top_level_yaml(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line[0].isspace() or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"\'')
    return values


def validate() -> int:
    files = sorted(MODULES.glob("*/module.yaml"))
    if not files:
        print("No modules found")
        return 1
    failed = False
    for path in files:
        data = parse_top_level_yaml(path)
        missing = REQUIRED - data.keys()
        if missing:
            failed = True
            print(f"FAIL {path}: missing {', '.join(sorted(missing))}")
        else:
            print(f"OK   {data['subname']} v{data['version']}")
    return 1 if failed else 0


def list_modules() -> int:
    for path in sorted(MODULES.glob("*/module.yaml")):
        data = parse_top_level_yaml(path)
        print(f"{data.get('subname', path.parent.name)}\tv{data.get('version', '?')}\t{data.get('status', '?')}")
    return 0


parser = argparse.ArgumentParser(prog="rim", description="Reusable Intelligence Modules registry")
parser.add_argument("command", choices=["list", "validate"])
args = parser.parse_args()
raise SystemExit(list_modules() if args.command == "list" else validate())
