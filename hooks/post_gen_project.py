#!/usr/bin/env python3
"""Post-generation hook to rename template files and clean up unused configuration."""

from pathlib import Path

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

# Mapping of environment manager to dependency file
# Most use pyproject.toml, only conda needs environment.yml
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
    if dep_file != dependency_file:
        dep_path = Path(dep_file)
        if dep_path.exists():
            dep_path.unlink()

# Remove setup.cfg if not using flake8
linting_choice = "{{ cookiecutter.linting_and_formatting }}"
if linting_choice == "ruff":
    setup_cfg = Path("setup.cfg")
    if setup_cfg.exists():
        setup_cfg.unlink()
