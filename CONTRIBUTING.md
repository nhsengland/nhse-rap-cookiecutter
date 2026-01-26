# Contributing to NHS RAP Cookiecutter Template

We welcome contributions to the NHS RAP Cookiecutter Template.

## Development Setup

1. Clone the repository:

```bash
git clone https://github.com/nhsengland/nhse-rap-cookiecutter.git
cd nhse-rap-cookiecutter
```

1. Install dependencies:

```bash
uv sync --all-extras
```

1. Install pre-commit hooks:

```bash
uv run pre-commit install
```

## Running Tests

All tests must pass before submitting changes:

```bash
# Run all tests
uv run pytest tests/ -v

# Run with coverage
uv run pytest tests/ --cov=nhse_rap_cookiecutter --cov-report=term-missing

# Run specific test file
uv run pytest tests/test_cli.py -v
```

## Code Quality

Before submitting changes, ensure code passes all quality checks:

```bash
# Format code
uv run ruff format .

# Check linting
uv run ruff check .

# Run all pre-commit hooks
uv run pre-commit run --all-files
```

## Testing the Template

Generate a test project to verify your changes:

```bash
# Using the CLI
uv run nhs-rap-template --no-input

# Using cookiecutter directly
cookiecutter . --no-input
```

## Template Development Guidelines

### Dynamic Year Values

Always use dynamic year values instead of hardcoding them. The approach depends on whether the file is processed by cookiecutter or by MkDocs:

**For cookiecutter-processed files** (e.g., LICENSE, Python files):

```jinja
{# CORRECT - Processed by cookiecutter during generation #}
Copyright (c) {% now 'utc', '%Y' %} NHS England

{# WRONG - Hardcoded year #}
Copyright (c) 2026 NHS England
```

**For MkDocs template files** (e.g., footer.html):

```jinja
{# CORRECT - Evaluated by MkDocs at build time #}
&copy; {{ "now().year" }} Crown Copyright (NHS England)

{# WRONG - Hardcoded year #}
&copy; 2026 Crown Copyright (NHS England)
```

This ensures generated projects always display the current year without manual updates.

**Files using dynamic years:**
- `{{ cookiecutter.repo_name }}/LICENSE` - Uses cookiecutter's `{% now 'utc', '%Y' %}`
- `{{ cookiecutter.repo_name }}/docs/content/overrides/partials/footer.html` - Uses MkDocs' `{{ "now().year" }}`
- `docs/overrides/partials/footer.html` - Cookiecutter repo footer, uses MkDocs' `{{ "now().year" }}`

## Making Changes

1. Create a new branch for your changes:

```bash
git checkout -b feature/your-feature-name
```

1. Make your changes following the code standards below
2. Add tests for new functionality
3. Update documentation as needed
4. Commit your changes with descriptive messages

### Commit Message Format

```text
type(scope): brief description

Longer explanation if needed.
```

Types: `fix`, `feat`, `refactor`, `test`, `docs`, `style`, `build`

## Code Standards

| Standard | Description |
|----------|-------------|
| **Type hints** | Use type hints for all function parameters and return values |
| **Docstrings** | Write Google-style docstrings for functions, classes, and modules |
| **Naming** | Use descriptive variable and function names |
| **Paths** | Use `pathlib.Path` instead of string paths |
| **Logging** | Use `loguru` for logging (not the standard `logging` module) |

### Example Docstring

```python
def process_data(input_path: Path, config: dict) -> pd.DataFrame:
    """Process raw data according to configuration.

    Args:
        input_path: Path to the input CSV file.
        config: Configuration dictionary with processing options.

    Returns:
        Processed DataFrame with standardised columns.

    Raises:
        FileNotFoundError: If input_path does not exist.
        ValueError: If config is missing required keys.
    """
```

## Testing Guidelines

- Organise tests in test classes for clear grouping
- Each test method should test ONE behaviour
- Use `pytest.mark.parametrize` for testing multiple input variations
- Use `tmp_path` fixtures for file system operations
- Assert exact expected values, not fuzzy matching

## Pull Request Process

1. Ensure all tests pass and code quality checks succeed
2. Update documentation if you've changed functionality
3. Push your branch
4. Open a pull request against the main repository
5. Describe your changes clearly in the PR description
6. Link any relevant issues

## Documentation

Documentation is built with MkDocs Material. To preview documentation changes:

```bash
uv run mkdocs serve
```

Then visit `http://localhost:8000` in your browser.

## Questions or Issues?

- Open an issue for bugs or feature requests
- Start a discussion for questions or ideas
- Check existing issues before creating new ones

## Licence

By contributing, you agree that your contributions will be licensed under the MIT Licence. Documentation contributions are released under Crown Copyright with the Open Government Licence v3.0.
