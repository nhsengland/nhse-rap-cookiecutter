#!/usr/bin/env python3
"""Post-generation hook to rename template files and clean up unused configuration."""

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

# Remove setup.cfg if not using flake8
linting_choice = "{{ cookiecutter.linting_and_formatting }}"
if linting_choice == "ruff":
    setup_cfg = Path("setup.cfg")
    if setup_cfg.exists():
        setup_cfg.unlink()
