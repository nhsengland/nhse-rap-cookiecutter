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
- {{ cookiecutter.environment_manager }}
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

{% elif cookiecutter.environment_manager == 'conda' %}

   ```bash
   conda env create -f environment.yml
   conda activate {{ cookiecutter.repo_name }}
   ```

{% else %}

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -e ".[dev{% if cookiecutter.docs == 'mkdocs' %},docs{% endif %}]"
   ```

{% endif %}

1. Verify the setup:
{% if cookiecutter.environment_manager == 'uv' %}

   ```bash
   uv run pytest
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

## Open Code Standards

Before publishing or sharing code, review the [Open Code Checklist](open_code_checklist.md) to ensure:

- Appropriate licensing and documentation
- No sensitive information in code or git history
- Security and quality standards are met
- Third-party dependencies are secure and documented

The checklist is also available as [`OPEN_CODE_CHECKLIST.md`](../OPEN_CODE_CHECKLIST.md) in the repository root.

Thank you for contributing to {{ cookiecutter.project_name }}!
