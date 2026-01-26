# {{ cookiecutter.project_name }}

[![Project Status: Active](https://img.shields.io/badge/Project%20Status-Active-green)]({{cookiecutter.repository_url}}) [![RAP Status: Work in Progress](https://img.shields.io/badge/RAP%20Status-WIP-red)](https://nhsdigital.github.io/rap-community-of-practice/introduction_to_RAP/levels_of_RAP/) [![Cookiecutter](https://img.shields.io/badge/Cookiecutter-Template-D4AA00?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter) [![NHS England RAP](https://img.shields.io/badge/NHS%20RAP-Project%20template-005EB8?logo=cookiecutter)](https://github.com/nhsengland/nhse-rap-cookiecutter) [![Python {{cookiecutter.python_version_number}}](https://img.shields.io/badge/Python-{{cookiecutter.python_version_number}}-blue)](https://www.python.org/downloads/){% if cookiecutter.open_source_license == "MIT" %} [![Licence: MIT](https://img.shields.io/badge/Licence-MIT-yellow.svg)](https://opensource.org/licenses/MIT){% elif cookiecutter.open_source_license == "Apache-2.0" %} [![Licence: Apache-2.0](https://img.shields.io/badge/Licence-Apache%202.0-yellow.svg)](https://opensource.org/licenses/Apache-2.0){% elif cookiecutter.open_source_license == "GPL-3.0" %} [![Licence: GPL-3.0](https://img.shields.io/badge/Licence-GPL--3.0-yellow.svg)](https://www.gnu.org/licenses/gpl-3.0){% endif %}{% if cookiecutter.linting_and_formatting == "ruff" %} [![Code Style: Ruff](https://img.shields.io/badge/Code%20Style-Ruff-D7FF64.svg)](https://github.com/astral-sh/ruff){% elif cookiecutter.linting_and_formatting == "flake8+black+isort" %} [![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-000000.svg)](https://github.com/psf/black) [![Linting: Flake8](https://img.shields.io/badge/Linting-Flake8-blue)](https://flake8.pycqa.org/) [![Import Sort: isort](https://img.shields.io/badge/Import%20Sort-isort-blue)](https://pycqa.github.io/isort/){% endif %} [![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

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

{% if cookiecutter.open_source_license == 'MIT' %}Unless stated otherwise, the codebase is released under the [MIT License](../LICENSE). This covers both the codebase and any sample code in the documentation.
{% elif cookiecutter.open_source_license == 'Apache-2.0' %}Unless stated otherwise, the codebase is released under the [Apache License 2.0](../LICENSE). This covers both the codebase and any sample code in the documentation.
{% elif cookiecutter.open_source_license == 'GPL-3.0' %}Unless stated otherwise, the codebase is released under the [GNU General Public License v3.0](../LICENSE). This covers both the codebase and any sample code in the documentation.
{% else %}This project does not currently have an open source license.
{% endif %}

The documentation is © Crown copyright and available under the terms of the [Open Government License v3.0](../LICENSE-OGL).
