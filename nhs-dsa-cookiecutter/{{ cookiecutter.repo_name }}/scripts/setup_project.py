#!/usr/bin/env python3
"""One-time project setup — and a small teaching example.

Run this once, right after creating your project:

    python scripts/setup_project.py

It does the four things you'd otherwise type by hand to get going:

    1. start tracking the project with git        (git init)
    2. create an environment and install packages  (uv sync, or python -m venv)
    3. turn on the pre-commit checks               (pre-commit install)
    4. make your first commit                      (git add + git commit)

The script is deliberately short and readable. Open it up — every command it
runs is one you could run yourself in the terminal. Reading it is a good way
to learn what "setting up a project" actually means.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

# Filled in from your cookiecutter answers when the project was created.
ENV_MANAGER = "{{ cookiecutter.environment_manager }}"
PYTHON_VERSION = "{{ cookiecutter.python_version_number }}"


def run(command: list[str]) -> None:
    """Print a command, then run it. Stops the script if the command fails."""
    print(f"\n$ {' '.join(command)}")
    subprocess.run(command, check=True)


def main() -> None:
    print("Setting up your project...")

    # 1. Start a git repository (skip if one already exists).
    if Path(".git").exists():
        print("\ngit is already set up here — skipping git init.")
    else:
        run(["git", "init"])
        run(["git", "branch", "-M", "main"])  # name the default branch "main"

    # 2. Create the environment and install the project's packages.
    #    "uv" is the recommended, fast option. "pip+venv" uses tools that ship
    #    with Python, which is handy if you can't install anything extra.
    if ENV_MANAGER == "uv":
        run(["uv", "sync"])  # creates .venv and installs everything
        run_in_env = ["uv", "run"]  # how we run a tool inside the new env
    else:  # pip+venv
        run([sys.executable, "-m", "venv", ".venv"])
        pip = ".venv/Scripts/pip" if sys.platform == "win32" else ".venv/bin/pip"
        run([pip, "install", "-e", ".[dev]"])  # install project + dev tools
        precommit = (
            ".venv/Scripts/pre-commit" if sys.platform == "win32" else ".venv/bin/pre-commit"
        )
        run_in_env = [precommit]

    # 3. Turn on pre-commit so the tidy-up checks run on every commit.
    if ENV_MANAGER == "uv":
        run([*run_in_env, "pre-commit", "install"])
    else:
        run([*run_in_env, "install"])

    # 4. Make the first commit so you have a clean starting point.
    run(["git", "add", "."])
    run(["git", "commit", "-m", "Initial commit", "--no-verify"])

    print("\nAll done! Your project is set up and committed.")
    print("Next: open guides/01-project-structure.md to learn your way around.")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as error:
        # A command failed. Show which one, and exit so the problem is obvious.
        print(f"\nSetup stopped: the command {error.cmd} failed.", file=sys.stderr)
        print("Fix the issue above, then run this script again.", file=sys.stderr)
        sys.exit(1)
