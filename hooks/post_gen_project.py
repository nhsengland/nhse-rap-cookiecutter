#!/usr/bin/env python3
"""Post-generation hook to rename template files."""

from pathlib import Path

# Rename _pyproject.toml to pyproject.toml
pyproject = Path("_pyproject.toml")
replace_list = [
    Path("_pyproject.toml"),
    Path("_docs"),
]
for path in replace_list:
    if path.exists():
        path.rename(path.name.lstrip("_"))
