#!/usr/bin/env python3
"""Post-generation hook to rename template files and clean up unused configuration."""

import shutil
import warnings
from datetime import datetime, timezone
from pathlib import Path

year = str(datetime.now(timezone.utc).year)

# Replace year placeholder in all template files
PLACEHOLDER = "@YEAR_PLACEHOLDER@"
repo_root = Path(".")

for file_path in repo_root.rglob("*"):
    if file_path.is_file():
        try:
            content = file_path.read_text(encoding="utf-8")
            if PLACEHOLDER in content:
                content = content.replace(PLACEHOLDER, year)
                file_path.write_text(content, encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            pass
        except Exception as e:
            warnings.warn(f"Failed to update year in {file_path}: {e}", stacklevel=2)

# Rename data directory
data_dir = Path("_data")
if data_dir.exists():
    data_dir.rename("data")

# Rename .env file
env_file = Path("_.env")
if env_file.exists():
    env_file.rename(".env")

# Determine which dependency file to keep based on environment manager
env_manager = "{{ cookiecutter.environment_manager }}"

dependency_files = {
    "virtualenv": "_pyproject.toml",
    "uv": "_pyproject.toml",
    "poetry": "_pyproject.toml",
    "pixi": "_pyproject.toml",
    "pipenv": "_pyproject.toml",
    "none": "_pyproject.toml",
    "conda": "_environment.yml",
}

# Rename the appropriate dependency file
dependency_file = dependency_files.get(env_manager)
if dependency_file:
    dep_path = Path(dependency_file)
    if dep_path.exists():
        dep_path.rename(dep_path.name.lstrip("_"))

# Remove unused dependency files
all_dependency_files = ["_pyproject.toml", "_environment.yml"]
for dep_file in all_dependency_files:
    if dependency_file and dep_file != dependency_file:
        dep_path = Path(dep_file)
        if dep_path.exists():
            dep_path.unlink()

# Remove setup.cfg if not using flake8
linting_choice = "{{ cookiecutter.linting_and_formatting }}"
if linting_choice == "ruff":
    setup_cfg = Path("setup.cfg")
    if setup_cfg.exists():
        setup_cfg.unlink()

# Remove docs and mkdocs config when docs are not enabled
docs_choice = "{{ cookiecutter.docs }}"
if docs_choice != "mkdocs":
    docs_dir = Path("docs")
    if docs_dir.exists():
        shutil.rmtree(docs_dir)
    mkdocs_config = Path("mkdocs.yml")
    if mkdocs_config.exists():
        mkdocs_config.unlink()

# Remove code scaffold when disabled
include_scaffold = "{{ cookiecutter.include_code_scaffold }}"
if include_scaffold != "Yes":
    module_dir = Path("{{ cookiecutter.module_name }}")
    if module_dir.exists():
        shutil.rmtree(module_dir)
    example_test = Path("tests") / "unittests" / "test_data.py"
    if example_test.exists():
        example_test.unlink()
    model_card = Path("models") / "model_card_template.md"
    if model_card.exists():
        model_card.unlink()

# Remove LICENSE when no license is chosen
license_choice = "{{ cookiecutter.open_source_license }}"
if license_choice == "No license file":
    license_file = Path("LICENSE")
    if license_file.exists():
        license_file.unlink()
