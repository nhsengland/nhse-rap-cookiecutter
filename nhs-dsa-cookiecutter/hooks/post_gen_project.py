#!/usr/bin/env python3
"""Post-generation hook.

Cookiecutter runs this script inside the freshly generated project. It does
three small jobs:

1. Rename the underscore-prefixed "staging" files to their real names. We ship
   them as ``_.env`` and ``_pyproject.toml`` (and the data folder as ``_data``)
   so they don't interfere with the template repository's own tooling. Here we
   restore them to ``.env``, ``pyproject.toml`` and ``data/``.
2. Replace the ``@YEAR_PLACEHOLDER@`` marker in the LICENSE with the current year.
3. Remove the LICENSE file if the user chose "No license file".
"""

import warnings
from datetime import datetime, timezone
from pathlib import Path

YEAR = str(datetime.now(timezone.utc).year)
PLACEHOLDER = "@YEAR_PLACEHOLDER@"

# 1. Rename the staging files/folders to their real names.
renames = {
    "_data": "data",
    "_.env": ".env",
    "_pyproject.toml": "pyproject.toml",
}
for staged, final in renames.items():
    path = Path(staged)
    if path.exists():
        path.rename(final)

# 2. Replace the year placeholder anywhere it appears (the LICENSE, mainly).
for file_path in Path(".").rglob("*"):
    if not file_path.is_file():
        continue
    try:
        content = file_path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, PermissionError):
        continue  # Skip binary files such as the .pptx templates.
    if PLACEHOLDER in content:
        try:
            file_path.write_text(content.replace(PLACEHOLDER, YEAR), encoding="utf-8")
        except OSError as e:
            warnings.warn(f"Could not update year in {file_path}: {e}", stacklevel=2)

# 3. Drop the LICENSE file when no licence was chosen.
if "{{ cookiecutter.open_source_license }}" == "No license file":
    license_file = Path("LICENSE")
    if license_file.exists():
        license_file.unlink()
