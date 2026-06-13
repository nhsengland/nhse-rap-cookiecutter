# Contributing to NHS RAP Cookiecutter Template

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

## Running Tests

All tests must pass before submitting changes:

```bash
# Run all tests
uv run pytest tests/ -v

# Run with coverage
uv run pytest tests/ --cov=nhse_rap_cookiecutter --cov-report=term-missing

# Run specific test file
uv run pytest tests/test_cli.py -v

# Run tests across multiple Python versions with tox
uv run tox

# Run tox for specific Python version
uv run tox -e py310  # or py311, py312, py313
```

### Testing Across Python Versions

The project uses `tox` to test across Python 3.10-3.13:

```bash
# Run all Python versions
uv run tox

# Run specific version
uv run tox -e py312

# Run in parallel
uv run tox -p
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

Always use `@YEAR_PLACEHOLDER@` in template files — never hardcode a year and never use
the `{% now %}` Jinja2 extension (it was removed from cookiecutter in v2.3+).

The post-generation hook (`hooks/post_gen_project.py`) replaces every occurrence of
`@YEAR_PLACEHOLDER@` with the current year at project-generation time. This works across
all file types, including copy-without-render files such as `*.html`.

```text
CORRECT  →  Copyright (c) @YEAR_PLACEHOLDER@ NHS England
WRONG    →  Copyright (c) 2026 NHS England          (hardcoded)
WRONG    →  Copyright (c) {% now 'utc', '%Y' %}     (removed extension)
```

**Files using `@YEAR_PLACEHOLDER@`:**

- `{{ cookiecutter.repo_name }}/LICENSE`
- `{{ cookiecutter.repo_name }}/mkdocs.yml`
- `{{ cookiecutter.repo_name }}/docs/content/overrides/partials/footer.html`
- `{{ cookiecutter.repo_name }}/README.md`
- `{{ cookiecutter.repo_name }}/docs/content/index.md`

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
