# NHS RAP Cookiecutter Template

[![Project Status: Active](https://img.shields.io/badge/Status-Active-green)](https://github.com/nhsengland/nhse-rap-cookiecutter)
[![Python: 3.10 | 3.11 | 3.12 | 3.13](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue)](https://www.python.org/downloads/)
[![Cookiecutter](https://img.shields.io/badge/Cookiecutter-Template-D4AA00?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter)
[![Checks](https://github.com/nhsengland/nhse-rap-cookiecutter/actions/workflows/checks.yml/badge.svg)](https://github.com/nhsengland/nhse-rap-cookiecutter/actions/workflows/checks.yml)
[![Deploy Docs](https://github.com/nhsengland/nhse-rap-cookiecutter/actions/workflows/deploy-docs.yml/badge.svg)](https://nhsengland.github.io/nhse-rap-cookiecutter/)
[![Code Style: Ruff](https://img.shields.io/badge/Code%20Style-Ruff-D7FF64.svg)](https://github.com/astral-sh/ruff)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

A Cookiecutter template for creating standardised NHS England Reproducible Analytical Pipeline (RAP) projects.

## Introduction

This template provides a standardised project structure for developing Reproducible Analytical Pipelines within NHS England. It includes pre-configured tooling for testing, linting, documentation, and dependency management following modern Python development practices.

## What is RAP?

Reproducible Analytical Pipelines (RAP) is a set of tools, principles, and techniques to help you improve your analytical processes. With RAP, you leverage open-source tools to make your work more efficient, more reusable, and less error-prone.

The core RAP principles from the [NHS RAP Community of Practice](https://nhsdigital.github.io/rap-community-of-practice/) are:

| Principle | Description |
|-----------|-------------|
| **Automation** | Minimise manual, error-prone steps through automation |
| **Modular, reusable code** | Write code in independent, loosely-coupled functions |
| **Transparency** | Publish code openly under appropriate licences |
| **Open-source tools** | Use Python, R, and other freely available languages |
| **Version control** | Use Git to track changes to code |
| **Good coding practices** | Follow standards like PEP8, use clear documentation |
| **Testing** | Implement automated tests for reliability |
| **Peer review** | Review code collaboratively to ensure quality |

Learn more about RAP at the [NHS RAP Community of Practice website](https://nhsdigital.github.io/rap-community-of-practice/introduction_to_RAP/what_is_RAP/).

## Installation

This template requires Python 3.10 to 3.13. This package is not published to PyPI, so install directly from GitHub:

**pipx** (recommended for CLI tools):

```bash
pipx install git+https://github.com/nhsengland/nhse-rap-cookiecutter.git
```

See the [pipx documentation](https://pipx.pypa.io/stable/) for installation instructions.

**uv**:

```bash
uv tool install git+https://github.com/nhsengland/nhse-rap-cookiecutter.git
```

See the [uv documentation](https://docs.astral.sh/uv/) for installation instructions.

**pip**:

```bash
pip install git+https://github.com/nhsengland/nhse-rap-cookiecutter.git
```

## Quick Start

Generate a new project using the CLI tool:

```bash
nhs-rap-template
```

Or use the official cookiecutter command:

```bash
cookiecutter gh:nhsengland/nhse-rap-cookiecutter
```

## Configuration Options

The template prompts for the following information:

| Category | Option | Description | Choices |
|----------|--------|-------------|---------|
| **Project** | project_name | Human-readable project name | Text |
| | description | Brief project description | Text |
| | author_name | Your full name | Text |
| | author_email | Your email address | Text |
| | organization_name | Your organisation (fixed: NHS England) | Text |
| | team_name | Your team name | Text |
| | team_email | Team contact email (optional) | Text |
| **Python** | python_version_number | Minimum Python version | 3.10, 3.11, 3.12, 3.13 |
| | environment_manager | Virtual environment tool | virtualenv, conda, pipenv, uv, pixi, poetry, none |
| **Options** | include_code_scaffold | Include example code modules | yes, no |
| | linting_and_formatting | Code quality tools | ruff, flake8+black+isort |
| | testing_framework | Testing framework | pytest, unittest |
| | license | Project licence | MIT, BSD-3-Clause, none |
| | documentation | Documentation tool | mkdocs, none |

**Note**: All generated projects include core Python packages (pandas, numpy, matplotlib, seaborn, jupyter, etc.) and development tools (pytest, pre-commit, linting) by default. The dependency file format (pyproject.toml or environment.yml) is determined automatically based on your environment manager choice.

## Generated Project Structure

```text
your-project/
├── data/
│   ├── external/        # Data from third-party sources
│   ├── interim/         # Intermediate transformed data
│   ├── processed/       # Final canonical datasets
│   └── raw/             # Original immutable data
├── docs/                # MkDocs documentation with NHS styling
├── models/              # Trained models and predictions
├── notebooks/           # Jupyter notebooks for exploration
├── references/          # Data dictionaries and documentation
├── reports/
│   └── figures/         # Generated graphics
├── tests/
│   ├── pytest/          # Pytest tests
│   └── unittest/        # Unittest tests
├── your_module/         # Source code package
│   ├── __init__.py
│   ├── config.py        # Configuration management
│   ├── dataset.py       # Data loading and processing
│   ├── features.py      # Feature engineering
│   ├── plots.py         # Visualisation functions
│   └── modeling/
│       ├── train.py     # Model training
│       └── predict.py   # Model inference
├── LICENSE
├── Makefile             # Convenience commands
├── README.md
└── pyproject.toml       # Project configuration and dependencies
```

## Using the Generated Project

After generating a project:

```bash
cd your-project-name
uv sync                      # Set up environment
uv run pre-commit install    # Install pre-commit hooks
make test                    # Run tests
make docs                    # Build documentation
```

## Documentation

Full documentation: [https://nhsengland.github.io/nhse-rap-cookiecutter](https://nhsengland.github.io/nhse-rap-cookiecutter)

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and contribution guidelines.

```bash
uv run pytest tests/ -v                                              # Run tests
uv run pytest tests/ --cov=nhse_rap_cookiecutter --cov-report=term   # With coverage
uv run ruff format . && uv run ruff check .                                    # Format and lint
make docs-serve                                                                # Serve docs with live reload
```

## Licence

Unless stated otherwise, the codebase is released under the [MIT Licence](./LICENSE). This covers both the codebase and any sample code in the documentation.

HTML and Markdown documentation is © Crown copyright and available under the terms of the [Open Government 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) licence.

## Acknowledgements

This template is based on [Cookiecutter Data Science](https://github.com/drivendataorg/cookiecutter-data-science), adapted for NHS England RAP standards and modern Python tooling.
