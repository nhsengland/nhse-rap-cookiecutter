# NHS RAP Cookiecutter Template

[![Project Status: Active](https://img.shields.io/badge/Status-Active-green)](https://github.com/nhsengland/nhse-rap-cookiecutter) [![Python: 3.10 | 3.11 | 3.12 | 3.13](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue)](https://www.python.org/downloads/) [![Cookiecutter](https://img.shields.io/badge/Cookiecutter-Template-D4AA00?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter) [![Checks](https://github.com/nhsengland/nhse-rap-cookiecutter/actions/workflows/checks.yml/badge.svg)](https://github.com/nhsengland/nhse-rap-cookiecutter/actions/workflows/checks.yml) [![Deploy Docs](https://github.com/nhsengland/nhse-rap-cookiecutter/actions/workflows/deploy-docs.yml/badge.svg)](https://nhsengland.github.io/nhse-rap-cookiecutter/) [![Code Style: Ruff](https://img.shields.io/badge/Code%20Style-Ruff-D7FF64.svg)](https://github.com/astral-sh/ruff) [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

A Cookiecutter template for creating standardised NHS England Reproducible Analytical Pipeline (RAP) projects.

---

## Overview

This template provides a standardised project structure for developing Reproducible Analytical Pipelines within NHS England. It includes pre-configured tooling for testing, linting, documentation, and dependency management following modern Python development practices.

**What you get:**

- Standardised structure following RAP principles
- Pre-configured tooling for testing, linting, and formatting
- Multiple environment options (uv, conda, poetry, virtualenv, etc.)
- NHS-branded documentation ready to customise
- Security scanning with gitleaks pre-commit hook
- Flexible configuration for different project needs

---

## What is RAP?

Reproducible Analytical Pipelines (RAP) is a set of tools, principles, and techniques to help you improve your analytical processes. With RAP, you leverage open-source tools to make your work more efficient, more reusable, and less error-prone.

Learn more at the [NHS RAP Community of Practice](https://nhsdigital.github.io/rap-community-of-practice/introduction_to_RAP/what_is_RAP/).

**Core RAP Principles:**

| Principle | Description |
|-----------|-------------|
| **Automation** | Minimise manual, error-prone steps. Automate data retrieval, processing, and output generation. |
| **Modular, reusable code** | Write code in independent, loosely-coupled functions that can be tested and reused. |
| **Transparency** | Publish code openly under appropriate licences to improve trust and collaboration. |
| **Open-source tools** | Use Python, R, SQL, and other freely available languages instead of proprietary software. |
| **Version control** | Use Git to track changes, enable collaboration, and maintain an audit trail. |
| **Good coding practices** | Follow standards like PEP8, write clear documentation, and use logical project structures. |
| **Testing** | Implement automated tests to ensure reliability and catch errors early. |
| **Peer review** | Review code collaboratively to ensure quality, accuracy, and adherence to standards. |

---

## Installation

This package is not published to PyPI. Install directly from GitHub:

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

---

## Quick Start

**Using the CLI:**

```bash
nhs-rap-template
```

**Using cookiecutter directly:**

```bash
cookiecutter gh:nhsengland/nhse-rap-cookiecutter
```

---

## Configuration Options

The template prompts for the following:

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

---

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
│   ├── unittests/       # Unit tests (pytest)
│   └── e2e/             # End-to-end integration tests
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

Each directory serves a specific purpose in the RAP workflow. The structure follows data science best practices while accommodating NHS-specific requirements.

---

## Next Steps

- [Getting Started](getting_started.md) - Step-by-step guide to your first project
- [Usage Guide](usage.md) - Configuration options and workflows
- [Contributing](contributing.md) - Help improve the template

---

## Licence

Unless stated otherwise, the codebase is released under the [MIT Licence](https://github.com/nhsengland/nhse-rap-cookiecutter/blob/main/LICENSE). This covers both the codebase and any sample code in the documentation.

HTML and Markdown documentation is © Crown copyright and available under the terms of the [Open Government 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) licence.

## Acknowledgements

This template is based on [Cookiecutter Data Science](https://github.com/drivendataorg/cookiecutter-data-science), adapted for NHS England RAP standards and modern Python tooling.
