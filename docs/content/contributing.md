# Contributing

We welcome contributions to the NHS RAP Cookiecutter Template.

## Development Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/nhsengland/nhse-rap-cookiecutter.git
   cd nhse-rap-cookiecutter
   ```

2. Install dependencies:

   ```bash
   uv sync --all-extras
   ```

3. Install pre-commit hooks:

   ```bash
   uv run pre-commit install
   ```

## Making Changes

Create a branch for your changes:

```bash
git checkout -b feature/your-feature-name
```

### Running Tests

All tests must pass before submitting changes:

```bash
uv run pytest tests/ -v
```

With coverage:

```bash
uv run pytest tests/ --cov=nhse_rap_cookiecutter --cov-report=term-missing
```

### Code Quality

Format and lint before committing:

```bash
uv run ruff format .
uv run ruff check .
```

### Testing the Template

Generate a test project to verify your changes:

```bash
uv run nhs-rap-template --no-input
```

## Code Standards

| Standard | Description |
|----------|-------------|
| **Type hints** | Use type hints for all function parameters and return values |
| **Docstrings** | Write Google-style docstrings for all functions and classes |
| **Naming** | Use descriptive variable and function names |
| **Paths** | Use `pathlib.Path` instead of string paths |
| **Logging** | Use `loguru` for logging (not the standard `logging` module) |
| **Formatting** | Code is formatted with `ruff format` |
| **Linting** | Code passes `ruff check` with no errors |

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

## Testing Standards

Tests are organised in `tests/` using pytest:

| Guideline | Description |
|-----------|-------------|
| **Test classes** | Organise tests in classes for clear grouping |
| **Single responsibility** | Each test method should test ONE behaviour |
| **Parametrize** | Use `pytest.mark.parametrize` for multiple input variations |
| **Fixtures** | Use `tmp_path` fixtures for file system operations |
| **Assertions** | Assert exact expected values, not fuzzy matching |

## Dependency Management

Dependencies are managed in `pyproject.toml`:

- `dependencies` - Runtime dependencies
- `dev` - Development dependencies (pytest, ruff, etc.)
- `docs` - Documentation dependencies (mkdocs, etc.)

Update the lock file after changes:

```bash
uv lock
```

## Pull Request Process

1. Create a feature branch from `main`
2. Make your changes following the code standards
3. Ensure all tests pass
4. Run formatting and linting
5. Update documentation if needed
6. Create a pull request with a clear description

### Commit Message Format

```text
type(scope): brief description

Longer explanation if needed.
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## Pre-commit Hooks

The following hooks run automatically on commit:

| Hook | Purpose |
|------|---------|
| **ruff** | Linting with auto-fix |
| **ruff-format** | Code formatting |
| **check-yaml** | Validate YAML files |
| **check-toml** | Validate TOML files |
| **gitleaks** | Check for hardcoded secrets |

## Documentation

Documentation is built with MkDocs Material. To preview changes:

```bash
make docs-serve
```

Or directly with the required flag:

```bash
uv run mkdocs serve --livereload
```

!!! warning "MkDocs Live Reload Bug"
    Due to a bug in this version of MkDocs, the `--livereload` flag is required for live reloading to work properly. The `make docs-serve` command includes this flag automatically.

Then visit `http://localhost:8000`.

## Getting Help

- **Issues**: Use [GitHub Issues](https://github.com/nhsengland/nhse-rap-cookiecutter/issues) for bug reports and feature requests
- **Discussions**: Use GitHub Discussions for questions and ideas

## Licence

By contributing, you agree that your contributions will be licensed under the MIT Licence. Documentation contributions are released under Crown Copyright with the Open Government Licence v3.0.
