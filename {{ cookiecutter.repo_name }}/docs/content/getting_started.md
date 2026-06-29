# Getting Started

This guide will help you set up and start working with {{ cookiecutter.project_name }}.

## Prerequisites

- Python {{ cookiecutter.python_version_number }}+
- {{ cookiecutter.environment_manager }} installed

## What's Included

This project comes pre-configured with:

**Core Python packages** for data analysis:

- pandas, numpy, matplotlib, seaborn, plotly
- scipy, scikit-learn
- jupyterlab, notebook, ipython
- loguru (logging), tqdm (progress bars), requests, openpyxl

**Development tools**:

- pytest and pytest-cov (testing)
- pre-commit (git hooks)
{% if cookiecutter.linting_and_formatting == "ruff" %}- ruff (linting and formatting){% else %}- flake8 (linting), black (formatting), isort (import sorting){% endif %}

{% if cookiecutter.docs == "mkdocs" %}**Documentation tools**:

- mkdocs, mkdocs-material, mkdocstrings (for building this documentation)
{% endif %}

All dependencies are managed through {% if cookiecutter.environment_manager == "conda" %}`environment.yml`{% else %}`pyproject.toml`{% endif %}, ensuring reproducible installations.

## Quick Setup

The easiest way to set up this project is using the automated setup script:

```bash
make setup
```

This script will:

- Initialize git repository with default branch
- Configure git remote ({{ cookiecutter.repository_url }})
- Set up your Python environment
- Install all dependencies
- Install pre-commit hooks
- Create an initial commit

## Manual Installation

If you prefer manual setup or need to run individual steps:

{% if cookiecutter.environment_manager == 'conda' %}

### Using Conda

1. Create and activate the environment:

   ```bash
   conda env create -f environment.yml
   conda activate {{ cookiecutter.repo_name }}
   ```

2. Install the package in development mode:

   ```bash
   pip install -e .
   ```

{% elif cookiecutter.environment_manager == 'uv' %}

### Using uv

1. Create and sync the environment:

   ```bash
   uv sync
   ```

2. Run commands with uv:

   ```bash
   uv run python
   uv run pytest
   ```

{% else %}

### Using pip + venv

1. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

2. Activate the environment:

   ```bash
   source .venv/bin/activate  # On Linux/Mac
   # or
   .venv\Scripts\activate  # On Windows
   ```

3. Install the package and its dependencies:

   ```bash
   pip install -e ".[dev{% if cookiecutter.docs == 'mkdocs' %},docs{% endif %}]"
   ```

{% endif %}

## Project Structure

```
{{ cookiecutter.repo_name }}/
{% if cookiecutter.layout == 'src' %}├── src/{{ cookiecutter.module_name }}/ # Source code (src layout)
{% else %}├── {{ cookiecutter.module_name }}/     # Source code
{% endif %}├── data/                               # Data files
│   ├── external/                       # External data sources
│   ├── interim/                        # Intermediate processed data
│   ├── processed/                      # Final processed data
│   └── raw/                            # Raw data
├── docs/                               # Documentation
├── models/                             # Trained models
├── notebooks/                          # Jupyter notebooks
├── references/                         # Reference materials
├── reports/                            # Generated reports
│   └── figures/                        # Report figures
└── tests/                              # Test files
```

## Running Tests

{% if cookiecutter.environment_manager == 'uv' %}

```bash
uv run pytest
```

{% else %}

```bash
pytest
```

{% endif %}

## Building Documentation

This documentation is built with MkDocs. To serve it locally:

{% if cookiecutter.environment_manager == 'uv' %}

```bash
uv run mkdocs serve
```

{% else %}

```bash
mkdocs serve
```

{% endif %}

Then open <http://127.0.0.1:8000> in your browser.

## Next Steps

- Read the [Usage Guide](usage.md) to learn how to use the project
- Check out the [API Reference](api_reference/index.md) for detailed documentation
- Review the [Contributing Guide](contributing.md) to contribute to the project
