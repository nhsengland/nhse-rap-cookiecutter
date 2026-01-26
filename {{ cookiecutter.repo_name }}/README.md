# {{cookiecutter.project_name}}

[![Project Status: Active](https://img.shields.io/badge/Project%20Status-Active-green)]({{cookiecutter.repository_url}}) [![RAP Status: Work in Progress](https://img.shields.io/badge/RAP%20Status-WIP-red)](https://nhsdigital.github.io/rap-community-of-practice/introduction_to_RAP/levels_of_RAP/) [![Cookiecutter](https://img.shields.io/badge/Cookiecutter-Template-D4AA00?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter) [![NHS England RAP](https://img.shields.io/badge/NHS%20RAP-Project%20template-005EB8?logo=cookiecutter)](https://github.com/nhsengland/nhse-rap-cookiecutter) [![Python {{cookiecutter.python_version_number}}](https://img.shields.io/badge/Python-{{cookiecutter.python_version_number}}-blue)](https://www.python.org/downloads/){% if cookiecutter.open_source_license == "MIT" %} [![Licence: MIT](https://img.shields.io/badge/Licence-MIT-yellow.svg)](https://opensource.org/licenses/MIT){% elif cookiecutter.open_source_license == "Apache-2.0" %} [![Licence: Apache-2.0](https://img.shields.io/badge/Licence-Apache%202.0-yellow.svg)](https://opensource.org/licenses/Apache-2.0){% elif cookiecutter.open_source_license == "GPL-3.0" %} [![Licence: GPL-3.0](https://img.shields.io/badge/Licence-GPL--3.0-yellow.svg)](https://www.gnu.org/licenses/gpl-3.0){% endif %}{% if cookiecutter.linting_and_formatting == "ruff" %} [![Code Style: Ruff](https://img.shields.io/badge/Code%20Style-Ruff-D7FF64.svg)](https://github.com/astral-sh/ruff){% elif cookiecutter.linting_and_formatting == "flake8+black+isort" %} [![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-000000.svg)](https://github.com/psf/black) [![Linting: Flake8](https://img.shields.io/badge/Linting-Flake8-blue)](https://flake8.pycqa.org/) [![Import Sort: isort](https://img.shields.io/badge/Import%20Sort-isort-blue)](https://pycqa.github.io/isort/){% endif %} [![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

<!-- 
Additional badge options available in badges.toml:
- Project status: concept, wip, poc, mvp, active, on_hold, archived
- RAP status: wip, baseline, silver, gold
- Optional badges: github_tests, github_lint, github_docs, github_release, github_pages
                   gitlab_pipeline, gitlab_coverage, pypi, ogl3

Copy badges from badges.toml and paste them above to customize your README.
-->

{{cookiecutter.description}}

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         {{ cookiecutter.module_name }} and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── {{ cookiecutter.module_name }}   <- Source code for use in this project.
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

The documentation is © Crown copyright and available under the terms of the [Open Government License v3.0](LICENSE-OGL).
