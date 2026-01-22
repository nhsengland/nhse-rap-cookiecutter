# {{cookiecutter.project_name}}

[![Project Status: Active](https://img.shields.io/badge/Project%20Status-Active-green)](https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.repo_name}}) [![RAP Status: Work in Progress](https://img.shields.io/badge/RAP%20Status-WIP-red)](https://nhsdigital.github.io/rap-community-of-practice/introduction_to_RAP/levels_of_RAP/) [![Cookiecutter](https://img.shields.io/badge/Cookiecutter-Template-D4AA00?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter) [![NHS England RAP](https://img.shields.io/badge/NHS%20RAP-Project%20template-005EB8?logo=cookiecutter)](https://github.com/nhsengland/nhse-rap-cookiecutter) [![Python {{cookiecutter.python_version_number}}](https://img.shields.io/badge/Python-{{cookiecutter.python_version_number}}-blue)](https://www.python.org/downloads/){% if cookiecutter.open_source_license == "MIT" %} [![Licence: MIT](https://img.shields.io/badge/Licence-MIT-yellow.svg)](https://opensource.org/licenses/MIT){% elif cookiecutter.open_source_license == "BSD-3-Clause" %} [![Licence: BSD-3-Clause](https://img.shields.io/badge/Licence-BSD--3--Clause-yellow.svg)](https://opensource.org/licenses/BSD-3-Clause){% endif %}{% if cookiecutter.linting_and_formatting == "ruff" %} [![Code Style: Ruff](https://img.shields.io/badge/Code%20Style-Ruff-D7FF64.svg)](https://github.com/astral-sh/ruff){% elif cookiecutter.linting_and_formatting == "flake8+black+isort" %} [![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-000000.svg)](https://github.com/psf/black) [![Linting: Flake8](https://img.shields.io/badge/Linting-Flake8-blue)](https://flake8.pycqa.org/) [![Import Sort: isort](https://img.shields.io/badge/Import%20Sort-isort-blue)](https://pycqa.github.io/isort/){% endif %} [![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

<!-- 
Uncomment and customize these optional badges as needed:

CI/CD Status Badges:
[![Tests](https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.repo_name}}/actions/workflows/tests.yml/badge.svg)](https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.repo_name}}/actions/workflows/tests.yml)
[![Lint](https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.repo_name}}/actions/workflows/lint.yml/badge.svg)](https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.repo_name}}/actions/workflows/lint.yml)
[![Docs](https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.repo_name}}/actions/workflows/docs.yml/badge.svg)](https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.repo_name}}/actions/workflows/docs.yml)

Documentation Status:
[![Documentation Status](https://img.shields.io/badge/docs-live-brightgreen)](https://{{cookiecutter.github_organization}}.github.io/{{cookiecutter.repo_name}}/)

Release/Version:
[![Latest Release](https://img.shields.io/github/v/release/{{cookiecutter.github_organization}}/{{cookiecutter.repo_name}})](https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.repo_name}}/releases)
[![PyPI Version](https://img.shields.io/pypi/v/{{cookiecutter.repo_name}})](https://pypi.org/project/{{cookiecutter.repo_name}}/)

Project Status Options:
[![Project Status: Concept](https://img.shields.io/badge/Project%20Status-Concept-lightgrey)](https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.repo_name}})
[![Project Status: WIP](https://img.shields.io/badge/Project%20Status-WIP-orange)](https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.repo_name}})
[![Project Status: Active](https://img.shields.io/badge/Project%20Status-Active-green)](https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.repo_name}})
[![Project Status: Suspended](https://img.shields.io/badge/Project%20Status-Suspended-yellow)](https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.repo_name}})
[![Project Status: Abandoned](https://img.shields.io/badge/Project%20Status-Abandoned-red)](https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.repo_name}})
[![Project Status: Moved](https://img.shields.io/badge/Project%20Status-Moved-blue)](https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.repo_name}})
[![Project Status: Unsupported](https://img.shields.io/badge/Project%20Status-Unsupported-grey)](https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.repo_name}})

RAP Status Options:
[![RAP Status: Baseline](https://img.shields.io/badge/RAP%20Status-Baseline-orange)](https://nhsdigital.github.io/rap-community-of-practice/introduction_to_RAP/levels_of_RAP/)
[![RAP Status: Silver](https://img.shields.io/badge/RAP%20Status-Silver-silver)](https://nhsdigital.github.io/rap-community-of-practice/introduction_to_RAP/levels_of_RAP/)
[![RAP Status: Gold](https://img.shields.io/badge/RAP%20Status-Gold-gold)](https://nhsdigital.github.io/rap-community-of-practice/introduction_to_RAP/levels_of_RAP/)

OGL3 Licence (for documentation):
[![Licence: OGL3](https://img.shields.io/badge/Licence-OGL3-darkgrey)](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
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
