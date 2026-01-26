# Getting Started

This guide will help you set up and start working with {{ cookiecutter.project_name }}.

## Prerequisites

- Python {{ cookiecutter.python_version_number }}+
{% if cookiecutter.environment_manager != 'none' %}- {{ cookiecutter.environment_manager }} installed{% endif %}

## Installation

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
{% elif cookiecutter.environment_manager == 'pipenv' %}
### Using Pipenv

1. Install dependencies:
   ```bash
   pipenv install --dev
   ```

2. Activate the environment:
   ```bash
   pipenv shell
   ```

3. Install the package in development mode:
   ```bash
   pip install -e .
   ```
{% elif cookiecutter.environment_manager == 'poetry' %}
### Using Poetry

1. Install dependencies:
   ```bash
   poetry install
   ```

2. Activate the environment:
   ```bash
   poetry shell
   ```
{% elif cookiecutter.environment_manager == 'pixi' %}
### Using Pixi

1. Install dependencies:
   ```bash
   pixi install
   ```

2. Run commands with pixi:
   ```bash
   pixi run python
   ```
{% elif cookiecutter.environment_manager == 'uv' %}
### Using UV

1. Create and sync the environment:
   ```bash
   uv sync
   ```

2. Run commands with UV:
   ```bash
   uv run python
   uv run pytest
   ```
{% elif cookiecutter.environment_manager == 'virtualenv' %}
### Using Virtualenv

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the environment:
   ```bash
   source venv/bin/activate  # On Linux/Mac
   # or
   venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```
{% else %}
### Manual Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Install the package in development mode:
   ```bash
   pip install -e .
   ```
{% endif %}

## Project Structure

```
{{ cookiecutter.repo_name }}/
├── {{ cookiecutter.module_name }}/     # Source code
├── data/                               # Data files
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
{% elif cookiecutter.environment_manager == 'poetry' %}
```bash
poetry run pytest
```
{% elif cookiecutter.environment_manager == 'pixi' %}
```bash
pixi run pytest
```
{% elif cookiecutter.environment_manager == 'pipenv' %}
```bash
pipenv run pytest
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
cd docs/mkdocs
uv run mkdocs serve
```
{% elif cookiecutter.environment_manager == 'poetry' %}
```bash
cd docs/mkdocs
poetry run mkdocs serve
```
{% elif cookiecutter.environment_manager == 'pixi' %}
```bash
cd docs/mkdocs
pixi run mkdocs serve
```
{% elif cookiecutter.environment_manager == 'pipenv' %}
```bash
cd docs/mkdocs
pipenv run mkdocs serve
```
{% else %}
```bash
cd docs/mkdocs
mkdocs serve
```
{% endif %}

Then open http://127.0.0.1:8000 in your browser.

## Next Steps

- Read the [Usage Guide](usage.md) to learn how to use the project
- Check out the [API Reference](api_reference/index.md) for detailed documentation
- Review the [Contributing Guide](contributing.md) to contribute to the project
