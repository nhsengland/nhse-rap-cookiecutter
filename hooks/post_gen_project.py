#!/usr/bin/env python3
"""Post-generation hook to rename template files."""

from pathlib import Path

# List of paths to rename by stripping leading underscore
replace_list = [
    Path("_pyproject.toml"),
    Path("_data"),
    Path("_.env"),
]

for path in replace_list:
    if path.exists():
        path.rename(path.name.lstrip("_"))
