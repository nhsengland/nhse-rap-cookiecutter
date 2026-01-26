# {{ cookiecutter.project_name }}

[![Project Status: Active](https://img.shields.io/badge/Project%20Status-Active-green)]({{cookiecutter.repository_url}}) [![RAP Status: Work in Progress](https://img.shields.io/badge/RAP%20Status-WIP-red)](https://nhsdigital.github.io/rap-community-of-practice/introduction_to_RAP/levels_of_RAP/) [![Cookiecutter](https://img.shields.io/badge/Cookiecutter-Template-D4AA00?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter) [![NHS England RAP](https://img.shields.io/badge/NHS%20RAP-Project%20template-005EB8?logo=cookiecutter)](https://github.com/nhsengland/nhse-rap-cookiecutter) [![Python {{cookiecutter.python_version_number}}](https://img.shields.io/badge/Python-{{cookiecutter.python_version_number}}-blue)](https://www.python.org/downloads/){% if cookiecutter.open_source_license == "MIT" %} [![Licence: MIT](https://img.shields.io/badge/Licence-MIT-yellow.svg)](https://opensource.org/licenses/MIT){% elif cookiecutter.open_source_license == "BSD-3-Clause" %} [![Licence: BSD-3-Clause](https://img.shields.io/badge/Licence-BSD--3--Clause-yellow.svg)](https://opensource.org/licenses/BSD-3-Clause){% endif %}{% if cookiecutter.linting_and_formatting == "ruff" %} [![Code Style: Ruff](https://img.shields.io/badge/Code%20Style-Ruff-D7FF64.svg)](https://github.com/astral-sh/ruff){% elif cookiecutter.linting_and_formatting == "flake8+black+isort" %} [![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-000000.svg)](https://github.com/psf/black) [![Linting: Flake8](https://img.shields.io/badge/Linting-Flake8-blue)](https://flake8.pycqa.org/) [![Import Sort: isort](https://img.shields.io/badge/Import%20Sort-isort-blue)](https://pycqa.github.io/isort/){% endif %} [![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

<!-- 
Additional badge options available in badges.toml:
- Project status: concept, wip, poc, mvp, active, on_hold, archived
- RAP status: wip, baseline, silver, gold
- Optional badges: github_tests, github_lint, github_docs, github_release, github_pages
                   gitlab_pipeline, gitlab_coverage, pypi, ogl3

Copy badges from badges.toml and paste them above to customize your documentation.
-->

{{ cookiecutter.description }}

## Overview

This project follows NHS England RAP (Reproducible Analytical Pipeline) standards and includes:

- Standardised project structure
- Automated testing with pytest
- Code quality checks with ruff
- Documentation with MkDocs
- Environment management with {{ cookiecutter.environment_manager }}

## Getting Started

See the [Getting Started](getting_started.md) guide for installation and setup instructions.

## Usage

Learn how to use this project in the [Usage Guide](usage.md).

## Contributing

Contributions are welcome! See the [Contributing Guide](contributing.md) for details.

## API Reference

For detailed API documentation, see the [API Reference](api_reference/index.md).

## License

{% if cookiecutter.open_source_license != 'No license file' %}This project is licensed under the {{ cookiecutter.open_source_license }} license.{% else %}This project does not include an open source license.{% endif %}
