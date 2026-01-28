# Contributing Guide

Thank you for considering contributing to {{ cookiecutter.project_name }}! This guide will help you get started.

## Development Philosophy

This project follows NHS England RAP (Reproducible Analytical Pipeline) principles:

- **Reproducibility**: Code should produce consistent results
- **Quality**: Follow coding standards and write tests
- **Documentation**: Code should be well-documented
- **Collaboration**: Use version control and code review

## Getting Started

### Prerequisites

- Python {{ cookiecutter.python_version_number }}+
{% if cookiecutter.environment_manager != 'none' %}- {{ cookiecutter.environment_manager }}{% endif %}
- Git

### Setting Up Development Environment

1. Clone the repository:

   ```bash
   git clone {{ cookiecutter.repo_name }}
   cd {{ cookiecutter.repo_name }}
   ```

2. Set up the development environment:
{% if cookiecutter.environment_manager == 'uv' %}

   ```bash
   uv sync
   ```

{% elif cookiecutter.environment_manager == 'poetry' %}

   ```bash
   poetry install
   ```

{% elif cookiecutter.environment_manager == 'pixi' %}

   ```bash
   pixi install
   ```

{% elif cookiecutter.environment_manager == 'pipenv' %}

   ```bash
   pipenv install --dev
   ```

{% elif cookiecutter.environment_manager == 'conda' %}

   ```bash
   conda env create -f environment.yml
   conda activate {{ cookiecutter.repo_name }}
   ```

{% elif cookiecutter.environment_manager == 'virtualenv' %}

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   pip install -e .
   ```

{% else %}

   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

{% endif %}

1. Verify the setup:
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

## Code Standards

### Style Guide

- Follow PEP 8 style guidelines
- Use type hints for all functions
- Write docstrings in NumPy style
- Maximum line length: 100 characters

### Type Hints

```python
from typing import List, Dict, Optional

def process_data(
    input_data: pd.DataFrame,
    config: Dict[str, any],
    verbose: bool = False
) -> pd.DataFrame:
    """Process input data according to config.
    
    Parameters
    ----------
    input_data : pd.DataFrame
        Raw input data
    config : Dict[str, any]
        Configuration parameters
    verbose : bool, default False
        Whether to print progress
        
    Returns
    -------
    pd.DataFrame
        Processed data
    """
    pass
```

### Docstrings

Use NumPy-style docstrings:

```python
def calculate_metric(data: pd.DataFrame, metric_type: str) -> float:
    """Calculate the specified metric from data.
    
    Parameters
    ----------
    data : pd.DataFrame
        Input data containing required columns
    metric_type : str
        Type of metric to calculate. Options: 'mean', 'median', 'std'
        
    Returns
    -------
    float
        Calculated metric value
        
    Raises
    ------
    ValueError
        If metric_type is not recognized
        
    Examples
    --------
    >>> data = pd.DataFrame({'values': [1, 2, 3, 4, 5]})
    >>> calculate_metric(data, 'mean')
    3.0
    """
    pass
```

## Testing

This project uses pytest for testing. See the [Testing Guide](testing.md) for detailed information on writing and running tests.

Quick reference:

{% if cookiecutter.environment_manager == 'uv' %}

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov={{ cookiecutter.module_name }} --cov-report=html
```

{% elif cookiecutter.environment_manager == 'poetry' %}

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov={{ cookiecutter.module_name }} --cov-report=html
```

```
{% elif cookiecutter.environment_manager == 'pixi' %}
```bash
# Run all tests
pixi run pytest

# Run with coverage
pixi run pytest --cov={{ cookiecutter.module_name }} --cov-report=html
```

{% elif cookiecutter.environment_manager == 'pipenv' %}

```bash
# Run all tests
pipenv run pytest

# Run with coverage
pipenv run pytest --cov={{ cookiecutter.module_name }} --cov-report=html
```

{% else %}

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov={{ cookiecutter.module_name }} --cov-report=html
```

{% endif %}

## Code Quality Checks

### Linting and Formatting

{% if cookiecutter.environment_manager == 'uv' %}

```bash
# Check code style
uv run ruff check .

# Format code
uv run ruff format .

# Fix auto-fixable issues
uv run ruff check --fix .
```

{% elif cookiecutter.environment_manager == 'poetry' %}

```bash
# Check code style
poetry run ruff check .

# Format code
poetry run ruff format .

# Fix auto-fixable issues
poetry run ruff check --fix .
```

{% elif cookiecutter.environment_manager == 'pixi' %}

```bash
# Check code style
pixi run ruff check .

# Format code
pixi run ruff format .

# Fix auto-fixable issues
pixi run ruff check --fix .
```

{% elif cookiecutter.environment_manager == 'pipenv' %}

```bash
# Check code style
pipenv run ruff check .

# Format code
pipenv run ruff format .

# Fix auto-fixable issues
pipenv run ruff check --fix .
```

{% else %}

```bash
# Check code style
ruff check .

# Format code
ruff format .

# Fix auto-fixable issues
ruff check --fix .
```

{% endif %}

## Contribution Workflow

### 1. Create a Branch

```bash
git checkout -b feature/my-new-feature
# or
git checkout -b fix/bug-description
```

### 2. Make Changes

- Write clear, focused commits
- Include tests for new functionality
- Update documentation as needed

### 3. Test Your Changes

{% if cookiecutter.environment_manager == 'uv' %}

```bash
# Run tests
uv run pytest

# Check code style
uv run ruff check .
uv run ruff format .
```

{% elif cookiecutter.environment_manager == 'poetry' %}

```bash
# Run tests
poetry run pytest

# Check code style
poetry run ruff check .
poetry run ruff format .
```

{% elif cookiecutter.environment_manager == 'pixi' %}

```bash
# Run tests
pixi run pytest

# Check code style
pixi run ruff check .
pixi run ruff format .
```

{% elif cookiecutter.environment_manager == 'pipenv' %}

```bash
# Run tests
pipenv run pytest

# Check code style
pipenv run ruff check .
pipenv run ruff format .
```

{% else %}

```bash
# Run tests
pytest

# Check code style
ruff check .
ruff format .
```

{% endif %}

### 4. Commit Your Changes

```bash
git add .
git commit -m "Add feature: description of changes"
```

Use clear commit messages:

- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `test:` for test additions/changes
- `refactor:` for code refactoring

### 5. Push and Create Pull Request

```bash
git push origin feature/my-new-feature
```

Then create a pull request on the repository.

## Documentation

### Building Documentation

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

Visit <http://127.0.0.1:8000> to view the documentation.

### Writing Documentation

- Keep documentation up-to-date with code changes
- Use clear, concise language
- Include code examples where helpful
- Update the API reference if adding new modules/functions

## Questions or Problems?

If you have questions or run into problems:

1. Check existing documentation
2. Search existing issues
3. Create a new issue with:
   - Clear description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - Your environment details

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the project and community
- Show empathy towards other contributors

Thank you for contributing to {{ cookiecutter.project_name }}!
