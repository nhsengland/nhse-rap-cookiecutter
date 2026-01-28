#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = {{ cookiecutter.repo_name }}
PYTHON_VERSION = {{ cookiecutter.python_version_number }}
PYTHON_INTERPRETER = python

#################################################################################
# COMMANDS                                                                      #
#################################################################################

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
	{% if cookiecutter.environment_manager == 'uv' -%}
	uv run ruff format --check
	uv run ruff check
	{% elif cookiecutter.environment_manager == 'poetry' -%}
	poetry run ruff format --check
	poetry run ruff check
	{% elif cookiecutter.environment_manager == 'pixi' -%}
	pixi run ruff format --check
	pixi run ruff check
	{% else -%}
	ruff format --check
	ruff check
	{% endif %}

## Format source code with ruff
.PHONY: format
format:
	{% if cookiecutter.environment_manager == 'uv' -%}
	uv run ruff check --fix
	uv run ruff format
	{% elif cookiecutter.environment_manager == 'poetry' -%}
	poetry run ruff check --fix
	poetry run ruff format
	{% elif cookiecutter.environment_manager == 'pixi' -%}
	pixi run ruff check --fix
	pixi run ruff format
	{% else -%}
	ruff check --fix
	ruff format
	{% endif %}
{% elif cookiecutter.linting_and_formatting == 'flake8+black+isort' %}
## Lint using flake8, black, and isort (use `make format` to do formatting)
.PHONY: lint
lint:
	{% if cookiecutter.environment_manager == 'uv' -%}
	uv run flake8 {{ cookiecutter.module_name }}
	uv run isort --check --diff {{ cookiecutter.module_name }}
	uv run black --check {{ cookiecutter.module_name }}
	{% elif cookiecutter.environment_manager == 'poetry' -%}
	poetry run flake8 {{ cookiecutter.module_name }}
	poetry run isort --check --diff {{ cookiecutter.module_name }}
	poetry run black --check {{ cookiecutter.module_name }}
	{% elif cookiecutter.environment_manager == 'pixi' -%}
	pixi run flake8 {{ cookiecutter.module_name }}
	pixi run isort --check --diff {{ cookiecutter.module_name }}
	pixi run black --check {{ cookiecutter.module_name }}
	{% else -%}
	flake8 {{ cookiecutter.module_name }}
	isort --check --diff {{ cookiecutter.module_name }}
	black --check {{ cookiecutter.module_name }}
	{% endif %}

## Format source code with black
.PHONY: format
format:
	{% if cookiecutter.environment_manager == 'uv' -%}
	uv run isort {{ cookiecutter.module_name }}
	uv run black {{ cookiecutter.module_name }}
	{% elif cookiecutter.environment_manager == 'poetry' -%}
	poetry run isort {{ cookiecutter.module_name }}
	poetry run black {{ cookiecutter.module_name }}
	{% elif cookiecutter.environment_manager == 'pixi' -%}
	pixi run isort {{ cookiecutter.module_name }}
	pixi run black {{ cookiecutter.module_name }}
	{% else -%}
	isort {{ cookiecutter.module_name }}
	black {{ cookiecutter.module_name }}
	{% endif %}
{% endif %}

{% if cookiecutter.testing_framework != 'none' %}
## Run tests
.PHONY: test
test:
{%- if cookiecutter.testing_framework == 'unittest' %}
	{% if cookiecutter.environment_manager == 'uv' -%}
	uv run python -m unittest discover -s tests
	{% elif cookiecutter.environment_manager == 'poetry' -%}
	poetry run python -m unittest discover -s tests
	{% elif cookiecutter.environment_manager == 'pixi' -%}
	pixi run python -m unittest discover -s tests
	{% else -%}
	python -m unittest discover -s tests
	{% endif %}
{%- elif cookiecutter.testing_framework == 'pytest' %}
	{% if cookiecutter.environment_manager == 'uv' -%}
	uv run pytest tests
	{% elif cookiecutter.environment_manager == 'poetry' -%}
	poetry run pytest tests
	{% elif cookiecutter.environment_manager == 'pixi' -%}
	pixi run pytest tests
	{% else -%}
	pytest tests
	{% endif %}
{%- endif -%}
{%- endif -%}

{% if cookiecutter.docs == 'mkdocs' %}
## Serve documentation with live reload
.PHONY: docs
docs:
	{% if cookiecutter.environment_manager == 'uv' -%}
	uv run mkdocs serve --livereload
	{% else -%}
	mkdocs serve --livereload
	{% endif %}

## Build documentation
.PHONY: docs-build
docs-build:
	{% if cookiecutter.environment_manager == 'uv' -%}
	uv run mkdocs build
	{% else -%}
	mkdocs build
	{% endif %}
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
	{% if cookiecutter.environment_manager == 'uv' -%}
	uv run python {{ cookiecutter.module_name }}/dataset.py
	{% elif cookiecutter.environment_manager == 'poetry' -%}
	poetry run python {{ cookiecutter.module_name }}/dataset.py
	{% elif cookiecutter.environment_manager == 'pixi' -%}
	pixi run python {{ cookiecutter.module_name }}/dataset.py
	{% else -%}
	$(PYTHON_INTERPRETER) {{ cookiecutter.module_name }}/dataset.py
	{% endif %}
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
