# {{cookiecutter.project_name}}

[![Project Status: Active](https://img.shields.io/badge/Project%20Status-Active-green)]({{cookiecutter.repository_url}}) [![RAP Status: Work in Progress](https://img.shields.io/badge/RAP%20Status-WIP-red)](https://nhsdigital.github.io/rap-community-of-practice/introduction_to_RAP/levels_of_RAP/) [![Cookiecutter](https://img.shields.io/badge/Cookiecutter-Template-D4AA00?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter) [![NHS England RAP](https://img.shields.io/badge/NHS%20RAP-Project%20template-005EB8?logo=cookiecutter)](https://github.com/nhsengland/nhse-rap-cookiecutter) [![Python {{cookiecutter.python_version_number}}](https://img.shields.io/badge/Python-{{cookiecutter.python_version_number}}-blue)](https://www.python.org/downloads/){% if cookiecutter.open_source_license == "MIT" %} [![Licence: MIT](https://img.shields.io/badge/Licence-MIT-yellow.svg)](https://opensource.org/licenses/MIT){% elif cookiecutter.open_source_license == "Apache-2.0" %} [![Licence: Apache-2.0](https://img.shields.io/badge/Licence-Apache%202.0-yellow.svg)](https://opensource.org/licenses/Apache-2.0){% elif cookiecutter.open_source_license == "GPL-3.0" %} [![Licence: GPL-3.0](https://img.shields.io/badge/Licence-GPL--3.0-yellow.svg)](https://www.gnu.org/licenses/gpl-3.0){% endif %}{% if cookiecutter.linting_and_formatting == "ruff" %} [![Code Style: Ruff](https://img.shields.io/badge/Code%20Style-Ruff-D7FF64.svg)](https://github.com/astral-sh/ruff){% elif cookiecutter.linting_and_formatting == "flake8+black+isort" %} [![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-000000.svg)](https://github.com/psf/black) [![Linting: Flake8](https://img.shields.io/badge/Linting-Flake8-blue)](https://flake8.pycqa.org/) [![Import Sort: isort](https://img.shields.io/badge/Import%20Sort-isort-blue)](https://pycqa.github.io/isort/){% endif %} [![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit){% if cookiecutter.git_hosting_platform == "github" %} [![Tests]({{cookiecutter.repository_url}}/actions/workflows/tests.yml/badge.svg)]({{cookiecutter.repository_url}}/actions/workflows/tests.yml) [![Lint]({{cookiecutter.repository_url}}/actions/workflows/lint.yml/badge.svg)]({{cookiecutter.repository_url}}/actions/workflows/lint.yml) [![Gitleaks]({{cookiecutter.repository_url}}/actions/workflows/gitleaks.yml/badge.svg)]({{cookiecutter.repository_url}}/actions/workflows/gitleaks.yml){% if cookiecutter.docs == "mkdocs" %} [![Docs]({{cookiecutter.repository_url}}/actions/workflows/docs.yml/badge.svg)]({{cookiecutter.repository_url}}/actions/workflows/docs.yml){% endif %}{% endif %}

<!-- 
Additional badge options available in badges.toml:
- Project status: concept, wip, poc, mvp, active, on_hold, archived
- RAP status: wip, baseline, silver, gold
- Optional badges: github_tests, github_lint, github_gitleaks, github_docs, github_release, github_pages
                   gitlab_pipeline, gitlab_coverage, pypi, ogl3

Copy badges from badges.toml and paste them above to customize your README.
-->

{{cookiecutter.description}}

| **Development Status** | **Intended Users** | **Environment** |
|------------------------|-------------------|------------------|
| Active | [Specify target audience - analysts, data scientists, clinicians, etc.] | [Development/Testing/Production] |

**Primary Contact**: [{{cookiecutter.team_name}}](mailto:{{cookiecutter.team_email}}){% if cookiecutter.docs == "mkdocs" %} | **Website**: [View documentation](https://{{cookiecutter.organization_name.lower().replace(' ', '')}}.github.io/{{cookiecutter.repo_name}}/){% endif %} | **Issues**: [Report a bug or request a feature]({{cookiecutter.repository_url}}/issues)

## What does this project do?

[Describe the project's intended purpose when implemented, its operating environment (or clinical use, if any), and the specific problems it solves or analysis it performs.]

## Data

**Data sources**: [List data sources, formats, and any prerequisites]

**Data handling**: [Note any sensitive data handling requirements, data dictionaries, or dummy data for testing]

## Getting Started

### Prerequisites

- Python {{cookiecutter.python_version_number}}
- {{cookiecutter.environment_manager}} for environment management
- [List any other required software, APIs, or system dependencies]

### Quick Setup

Use the automated setup script to initialize your repository:

```bash
make setup
```

This script will:

- Initialize git repository with default branch
- Configure git remote ({{cookiecutter.repository_url}})
- Set up your Python environment
- Install all dependencies
- Install pre-commit hooks
- Create an initial commit

### Manual Installation

Alternatively, set up manually:

1. Clone this repository:

   ```bash
   git clone {{cookiecutter.repository_url}}
   cd {{cookiecutter.repo_name}}
   ```

2. Set up your environment:
{% if cookiecutter.environment_manager == "conda" %}   ```bash
   conda env create -f environment.yml
   conda activate {{cookiecutter.repo_name}}

   ```

{% elif cookiecutter.environment_manager == "uv" %}   ```bash
   uv sync

   ```
{% else %}   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -e ".[dev{% if cookiecutter.docs == 'mkdocs' %},docs{% endif %}]"

   ```
{% endif %}

3. [Add any additional setup steps such as environment variables, API keys, or database configuration]

### Usage

[Provide clear examples of how to use the project, including command-line usage, key scripts, expected inputs and outputs, and common workflows.]

Example:
```bash
# Run the main pipeline
make data
make analysis
```

## Contributing

Contributions are welcome! Please [open an issue]({{cookiecutter.repository_url}}/issues) to report bugs, request features, or discuss improvements.

See our [Contributing Guidelines](CONTRIBUTING.md) for details on:

- How to submit issues and feature requests
- Our code review process
- Coding standards and style guides

Before publishing or sharing code, please review the [Open Code Checklist](OPEN_CODE_CHECKLIST.md) to ensure compliance with NHS England standards for security, licensing, and quality.

{% if cookiecutter.git_hosting_platform == "github" %}## Continuous Integration

This project ships with a small set of GitHub Actions workflows in `.github/workflows/`:

| Workflow | File | Purpose |
|----------|------|---------|
| **Tests** | `tests.yml` | Runs the `pytest` suite on every push and pull request to `main`. |
| **Lint** | `lint.yml` | Checks code style with {% if cookiecutter.linting_and_formatting == "ruff" %}`ruff`{% else %}`flake8`, `black` and `isort`{% endif %}. |
| **Gitleaks** | `gitleaks.yml` | Scans the repository for accidentally committed secrets. |
{% if cookiecutter.docs == "mkdocs" %}| **Docs** | `docs.yml` | Builds the MkDocs site and deploys it to GitHub Pages from `main`. |
{% endif %}
The status of each workflow is shown by the badges at the top of this README. The workflows are intentionally simple - edit them in `.github/workflows/` to suit your project.

{% endif %}## Project Organization

```
{% if cookiecutter.git_hosting_platform == "github" %}├── .github/workflows     <- GitHub Actions CI workflows (tests, lint, gitleaks{% if cookiecutter.docs == "mkdocs" %}, docs{% endif %})
{% endif %}├── LICENSE                <- Project license (MIT/Apache-2.0/GPL-3.0)
├── LICENSE-OGL            <- Open Government License v3.0 for documentation
├── CODE_OF_CONDUCT.md     <- Community guidelines and code of conduct
├── CONTRIBUTING.md        <- Contribution guidelines
├── OPEN_CODE_CHECKLIST.md <- Checklist for publishing code to public repositories
├── Makefile               <- Makefile with convenience commands like `make data` or `make train`
├── README.md              <- The top-level README for developers using this project
├── pyproject.toml         <- Project configuration file with package metadata
├── .pre-commit-config.yaml <- Pre-commit hooks configuration
├── .env                   <- Environment variables (not tracked in git)
│
├── data
│   ├── external           <- Data from third party sources
│   ├── interim            <- Intermediate data that has been transformed
│   ├── processed          <- The final, canonical data sets for modeling
│   └── raw                <- The original, immutable data dump
│
├── docs                   <- MkDocs documentation{% if cookiecutter.docs == "mkdocs" %} (see docs/README.md){% endif %}
│
├── models                 <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks              <- Jupyter notebooks. Naming convention is a number (for ordering),
│                             the creator's initials, and a short `-` delimited description, e.g.
│                             `1.0-jqp-initial-data-exploration`
│
├── references             <- Data dictionaries, manuals, and all other explanatory materials
│
├── reports                <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures            <- Generated graphics and figures to be used in reporting
│
├── tests                  <- Unit tests, integration tests, and test fixtures
│
└── {{ cookiecutter.module_name }}      <- Source code for use in this project
    │
    ├── __init__.py             <- Makes {{ cookiecutter.module_name }} a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualisations
```

--------

## License

{% if cookiecutter.open_source_license == 'MIT' %}Unless stated otherwise, the codebase is released under the [MIT License](LICENSE). This covers both the codebase and any sample code in the documentation.
{% elif cookiecutter.open_source_license == 'Apache-2.0' %}Unless stated otherwise, the codebase is released under the [Apache License 2.0](LICENSE). This covers both the codebase and any sample code in the documentation.
{% elif cookiecutter.open_source_license == 'GPL-3.0' %}Unless stated otherwise, the codebase is released under the [GNU General Public License v3.0](LICENSE). This covers both the codebase and any sample code in the documentation.
{% else %}This project does not currently have an open source license.
{% endif %}

The documentation is © @YEAR_PLACEHOLDER@ Crown copyright and available under the terms of the [Open Government License v3.0](LICENSE-OGL).
