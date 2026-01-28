# Tests

This directory contains all tests for {{ cookiecutter.project_name }}.

## Structure

```
tests/
├── unittests/     # Unit tests for individual functions and classes
└── e2e/           # End-to-end integration tests for complete workflows
```

## Unit Tests (`unittests/`)

Unit tests verify individual functions and classes in isolation. They should:

- **Be fast** - Unit tests should run in milliseconds
- **Be isolated** - Mock external dependencies (files, databases, APIs)
- **Test one thing** - Each test method tests one specific behavior
- **Use test classes** - Organize tests in classes, one per function/object being tested
- **Have clear names** - Use `test_<what>_<expected_behavior>` format

### Example Unit Test

```python
import pytest
from {{ cookiecutter.module_name }}.dataset import load_data


class TestLoadData:
    """Tests for load_data function."""

    def test_loads_csv_file(self, tmp_path):
        """Loading valid CSV file returns DataFrame."""
        # Create test file
        test_file = tmp_path / "test.csv"
        test_file.write_text("a,b\n1,2\n3,4")
        
        # Test function
        result = load_data(test_file)
        
        # Verify result
        assert len(result) == 2
        assert list(result.columns) == ["a", "b"]

    @pytest.mark.parametrize("extension", [".csv", ".parquet", ".xlsx"])
    def test_supports_multiple_formats(self, extension, tmp_path):
        """Function supports CSV, Parquet, and Excel formats."""
        test_file = tmp_path / f"test{extension}"
        # ... test implementation
```

## End-to-End Tests (`e2e/`)

End-to-end tests verify complete workflows from start to finish. They should:

- **Test realistic scenarios** - Use real data pipelines and workflows
- **Run less frequently** - E2E tests can be slower, run them on CI/CD
- **Test integration** - Verify components work together correctly
- **Use fixtures** - Share test data and setup across E2E tests

### Example E2E Test

```python
import pytest
from {{ cookiecutter.module_name }}.dataset import Dataset


class TestDataPipeline:
    """End-to-end tests for complete data pipeline."""

    def test_full_pipeline_execution(self, tmp_path):
        """Complete pipeline runs from raw data to output."""
        # Setup
        dataset = Dataset(data_dir=tmp_path)
        
        # Execute full pipeline
        dataset.load_raw()
        dataset.process()
        dataset.save_processed()
        
        # Verify final output
        output = tmp_path / "processed" / "output.csv"
        assert output.exists()
        # ... more assertions
```

## Running Tests

```bash
# Run all tests
{% if cookiecutter.environment_manager == 'uv' -%}
uv run pytest
{% elif cookiecutter.environment_manager == 'poetry' -%}
poetry run pytest
{% elif cookiecutter.environment_manager == 'pixi' -%}
pixi run pytest
{% else -%}
pytest
{% endif %}

# Run only unit tests
{% if cookiecutter.environment_manager == 'uv' -%}
uv run pytest tests/unittests/
{% elif cookiecutter.environment_manager == 'poetry' -%}
poetry run pytest tests/unittests/
{% elif cookiecutter.environment_manager == 'pixi' -%}
pixi run pytest tests/unittests/
{% else -%}
pytest tests/unittests/
{% endif %}

# Run only e2e tests
{% if cookiecutter.environment_manager == 'uv' -%}
uv run pytest tests/e2e/
{% elif cookiecutter.environment_manager == 'poetry' -%}
poetry run pytest tests/e2e/
{% elif cookiecutter.environment_manager == 'pixi' -%}
pixi run pytest tests/e2e/
{% else -%}
pytest tests/e2e/
{% endif %}

# Run with coverage
{% if cookiecutter.environment_manager == 'uv' -%}
uv run pytest --cov={{ cookiecutter.module_name }} --cov-report=html
{% elif cookiecutter.environment_manager == 'poetry' -%}
poetry run pytest --cov={{ cookiecutter.module_name }} --cov-report=html
{% elif cookiecutter.environment_manager == 'pixi' -%}
pixi run pytest --cov={{ cookiecutter.module_name }} --cov-report=html
{% else -%}
pytest --cov={{ cookiecutter.module_name }} --cov-report=html
{% endif %}

# Run specific test file
{% if cookiecutter.environment_manager == 'uv' -%}
uv run pytest tests/unittests/test_dataset.py
{% elif cookiecutter.environment_manager == 'poetry' -%}
poetry run pytest tests/unittests/test_dataset.py
{% elif cookiecutter.environment_manager == 'pixi' -%}
pixi run pytest tests/unittests/test_dataset.py
{% else -%}
pytest tests/unittests/test_dataset.py
{% endif %}
```

## Best Practices

1. **NEVER use unittest.mock** - Use `pytest-mock` and the `mocker` fixture instead
2. **Organize in test classes** - One class per function/object being tested
3. **Single responsibility** - Each test tests exactly one thing
4. **Hard assertions** - Assert exact expected values, not fuzzy matching
5. **Use parametrize** - Test multiple inputs with `@pytest.mark.parametrize`
6. **Mock external I/O** - Mock file operations, database calls, API requests
7. **Use fixtures** - Share test data and setup with pytest fixtures
8. **Document transformations** - Comment input → output in docstrings

## Coverage

Aim for 100% test coverage. Use coverage reports to identify untested code:

```bash
{% if cookiecutter.environment_manager == 'uv' -%}
uv run pytest --cov={{ cookiecutter.module_name }} --cov-report=term-missing
{% elif cookiecutter.environment_manager == 'poetry' -%}
poetry run pytest --cov={{ cookiecutter.module_name }} --cov-report=term-missing
{% elif cookiecutter.environment_manager == 'pixi' -%}
pixi run pytest --cov={{ cookiecutter.module_name }} --cov-report=term-missing
{% else -%}
pytest --cov={{ cookiecutter.module_name }} --cov-report=term-missing
{% endif %}
```

The `--cov-report=term-missing` flag shows which lines are not covered by tests.
