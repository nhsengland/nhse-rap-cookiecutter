#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = {{ cookiecutter.repo_name }}
PYTHON_VERSION = {{ cookiecutter.python_version_number }}
{% if cookiecutter.environment_manager == 'uv' -%}
PYTHON_INTERPRETER = uv run python
RUN_PREFIX = uv run
{% elif cookiecutter.environment_manager == 'poetry' -%}
PYTHON_INTERPRETER = poetry run python
RUN_PREFIX = poetry run
{% elif cookiecutter.environment_manager == 'pixi' -%}
PYTHON_INTERPRETER = pixi run python
RUN_PREFIX = pixi run
{% elif cookiecutter.environment_manager == 'pipenv' -%}
PYTHON_INTERPRETER = pipenv run python
RUN_PREFIX = pipenv run
{% elif cookiecutter.environment_manager == 'conda' -%}
PYTHON_INTERPRETER = python
RUN_PREFIX = 
{% elif cookiecutter.environment_manager == 'virtualenv' -%}
PYTHON_INTERPRETER = python
RUN_PREFIX = 
{% else -%}
PYTHON_INTERPRETER = python
RUN_PREFIX = 
{% endif %}

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Initialize repository (run once after generating from template)
.PHONY: setup
setup:
	$(PYTHON_INTERPRETER) scripts/setup_repository.py

## Install Python dependencies
.PHONY: requirements
requirements:
	{% if "uv" == cookiecutter.environment_manager -%}
	uv sync
	{% elif "pixi" == cookiecutter.environment_manager -%}
	pixi install
	{% elif "poetry" == cookiecutter.environment_manager -%}
	poetry install
	{% elif "conda" == cookiecutter.environment_manager -%}
	conda env update --name $(PROJECT_NAME) --file environment.yml --prune
	{% elif "pipenv" == cookiecutter.environment_manager -%}
	pipenv install
	{% elif "virtualenv" == cookiecutter.environment_manager -%}
	pip install -e .
	{% elif "none" == cookiecutter.environment_manager -%}
	pip install -e .
	{% endif -%}



## Delete all compiled Python files
.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

{% if cookiecutter.linting_and_formatting == 'ruff' %}
## Lint using ruff (use `make format` to do formatting)
.PHONY: lint
lint:
	$(RUN_PREFIX) ruff format --check
	$(RUN_PREFIX) ruff check

## Format source code with ruff
.PHONY: format
format:
	$(RUN_PREFIX) ruff check --fix
	$(RUN_PREFIX) ruff format
{% elif cookiecutter.linting_and_formatting == 'flake8+black+isort' %}
## Lint using flake8, black, and isort (use `make format` to do formatting)
.PHONY: lint
lint:
	$(RUN_PREFIX) flake8 {{ cookiecutter.module_name }}
	$(RUN_PREFIX) isort --check --diff {{ cookiecutter.module_name }}
	$(RUN_PREFIX) black --check {{ cookiecutter.module_name }}

## Format source code with black
.PHONY: format
format:
	$(RUN_PREFIX) isort {{ cookiecutter.module_name }}
	$(RUN_PREFIX) black {{ cookiecutter.module_name }}
{% endif %}

## Run tests
.PHONY: test
test:
	$(RUN_PREFIX) pytest tests

{% if cookiecutter.docs == 'mkdocs' %}
## Serve documentation with live reload
.PHONY: docs
docs:
	$(RUN_PREFIX) mkdocs serve --livereload

## Build documentation
.PHONY: docs-build
docs-build:
	$(RUN_PREFIX) mkdocs build
{% endif %}

{% if cookiecutter.environment_manager != 'none' %}
## Set up Python interpreter environment
.PHONY: create_environment
create_environment:
	{% if cookiecutter.environment_manager == 'conda' -%}
	conda env create --name $(PROJECT_NAME) -f environment.yml
	@echo ">>> conda env created. Activate with:\nconda activate $(PROJECT_NAME)"
	{% elif cookiecutter.environment_manager == 'virtualenv' -%}
	@bash -c "if [ ! -z `which virtualenvwrapper.sh` ]; then source `which virtualenvwrapper.sh`; mkvirtualenv $(PROJECT_NAME) --python=$(PYTHON_INTERPRETER); else mkvirtualenv.bat $(PROJECT_NAME) --python=$(PYTHON_INTERPRETER); fi"
	@echo ">>> New virtualenv created. Activate with:\nworkon $(PROJECT_NAME)"
	{% elif cookiecutter.environment_manager == 'pipenv' -%}
	pipenv --python $(PYTHON_VERSION)
	@echo ">>> New pipenv created. Activate with:\npipenv shell"
	{% elif cookiecutter.environment_manager == 'uv' -%}
	uv venv --python $(PYTHON_VERSION)
	@echo ">>> New uv virtual environment created. Activate with:"
	@echo ">>> Windows: .\\\\.venv\\\\Scripts\\\\activate"
	@echo ">>> Unix/macOS: source ./.venv/bin/activate"
	{% elif cookiecutter.environment_manager == 'pixi' -%}
	@echo ">>> Pixi environment configured in pyproject.toml. Run 'make requirements' to install dependencies."
	@echo ">>> Activate with:\npixi shell"
	{% elif cookiecutter.environment_manager == 'poetry' -%}
	poetry env use $(PYTHON_VERSION)
	@echo ">>> Poetry environment created. Activate with: "
	@echo '$$(poetry env activate)'
	@echo ">>> Or run commands with:\npoetry run <command>"
{% endif %}
{% endif %}


#################################################################################
# PROJECT RULES                                                                 #
#################################################################################

{% if cookiecutter.include_code_scaffold == 'Yes' %}
## Make dataset
.PHONY: data
data: requirements
	$(PYTHON_INTERPRETER) {{ cookiecutter.module_name }}/dataset.py
{% endif %}

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys; \
lines = '\n'.join([line for line in sys.stdin]); \
matches = re.findall(r'\n## (.*)\n[\s\S]+?\n([a-zA-Z_-]+):', lines); \
print('Available rules:\n'); \
print('\n'.join(['{:25}{}'.format(*reversed(match)) for match in matches]))
endef
export PRINT_HELP_PYSCRIPT

help:
	@$(PYTHON_INTERPRETER) -c "${PRINT_HELP_PYSCRIPT}" < $(MAKEFILE_LIST)
