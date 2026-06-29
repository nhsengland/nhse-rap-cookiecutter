# Getting Started

This guide will help you install **NHS RAP Cookiecutter Template** and create your first project.

## Prerequisites

| Requirement | Version | Description |
|-------------|---------|-------------|
| **Python** | 3.10-3.13 | Required for running the template tool |
| **Git** | Latest | Version control system for your projects |
| **uv** (Recommended) | Latest | Fast Python package manager |

## Installation

This package is not yet published to PyPI. Install directly from GitHub:

=== "pipx (Recommended)"

    Since this is a command-line tool, pipx is the recommended installation method:

    ```bash
    pipx install git+https://github.com/nhsengland/nhse-rap-cookiecutter.git
    ```

    [Learn more about pipx](https://pipx.pypa.io/stable/)

=== "uv"

    ```bash
    uv tool install git+https://github.com/nhsengland/nhse-rap-cookiecutter.git
    ```

    [Learn more about uv](https://docs.astral.sh/uv/)

=== "pip"

    ```bash
    pip install git+https://github.com/nhsengland/nhse-rap-cookiecutter.git
    ```

!!! tip "Why pipx or uv tool?"
    `pipx` and `uv tool` install command-line tools in isolated environments, preventing dependency conflicts with your other Python projects.

## Creating Your First Project

### Option 1: Using NHS RAP Template CLI

If you installed the package with pipx/uv/pip:

```bash
nhs-rap-template
```

### Option 2: Using Cookiecutter Directly

If you prefer to use the standard cookiecutter tool (useful when working with multiple templates):

```bash
# First, install cookiecutter if you haven't
pipx install cookiecutter

# Then create your project
cookiecutter gh:nhsengland/nhse-rap-cookiecutter
```

!!! tip "Why use cookiecutter directly?"
    Using the official cookiecutter tool allows you to:

    - Use multiple cookiecutter templates in your workflow
    - Leverage cookiecutter's replay feature to recreate projects
    - Use cookiecutter's config file in `~/.cookiecutterrc`
    - Integrate with existing cookiecutter-based workflows

### What You'll Be Prompted For

Both methods will prompt you for:

- Project name
- Author information
- Organization details
- Technical configuration (Python version, environment manager, etc.)

### Example Session

```bash
$ nhs-rap-template
project_name [project_name]: My NHS Analysis
repo_name [my_nhs_analysis]:
module_name [my_nhs_analysis]:
author_name [Your Name]: Jane Smith
author_email [your.email@example.com]: jane.smith@nhs.net
organization_name [NHS England]:
team_name [Your Team]: Data Science Team
team_email []: datascience@nhs.net
description [A short description of the project.]: Analysis of patient outcomes
python_version_number [3.10]: 3.11
Select environment_manager:
1 - uv
2 - venv
3 - conda
Choose from 1, 2, 3 [1]: 1
...
```

## Quick Start After Creation

After your project is created, use the automated setup script:

```bash
# Navigate to your project
cd my_nhs_analysis

# Run automated setup
make setup
```

The setup script will:

- Initialize git repository with default branch
- Configure git remote with your repository URL
- Set up your Python environment (uv, venv, or conda)
- Install all project dependencies
- Install pre-commit hooks
- Create an initial commit

### Manual Commands

If you prefer to set up manually or need to run individual steps, use your chosen environment manager's commands:

=== "uv"

    ```bash
    uv sync
    uv run pre-commit install
    make test
    make docs
    ```

=== "pip + venv"

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    pip install -e ".[dev,docs]"
    pre-commit install
    make test
    make docs
    ```

=== "Conda"

    ```bash
    conda env create -f environment.yml
    conda activate your_project
    pre-commit install
    make test
    make docs
    ```

## Next Steps

- Read the [Usage Guide](usage.md) for detailed information on using the template
- Explore the generated project structure
- See the [Contributing Guide](contributing.md) for development setup
