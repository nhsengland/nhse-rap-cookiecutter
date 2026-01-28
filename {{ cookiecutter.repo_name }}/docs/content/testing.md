# Testing

This project uses pytest for all testing. Tests are organized to separate fast unit tests from slower integration tests.

## Test Structure

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

### Leverage pytest Features

pytest provides powerful features that make testing easier:

- **[Fixtures](https://docs.pytest.org/en/stable/fixture.html)** - Share test data and setup logic across tests
- **[Parametrize](https://docs.pytest.org/en/stable/parametrize.html)** - Run the same test with multiple inputs using `@pytest.mark.parametrize`
- **[tmp_path](https://docs.pytest.org/en/stable/tmpdir.html)** - Built-in fixture for temporary directories/files
- **[monkeypatch](https://docs.pytest.org/en/stable/monkeypatch.html)** - Modify objects, dictionaries, environment variables
- **[pytest-mock](https://pytest-mock.readthedocs.io/)** - Mocking library (avoid `unittest.mock`)
- **[Marks](https://docs.pytest.org/en/stable/mark.html)** - Categorize tests (e.g., `@pytest.mark.slow`, `@pytest.mark.skip`)
- **[pytest-cov](https://pytest-cov.readthedocs.io/)** - Generate coverage reports

### Writing Effective Tests

**Organize with test classes** - Group related tests in classes, typically one class per function/object:

```python
class TestLoadData:
    """Tests for load_data function."""
    
    def test_loads_csv_file(self, tmp_path):
        """Test CSV loading."""
        # test implementation
    
    def test_handles_missing_file(self):
        """Test error handling."""
        # test implementation
```

**Use parametrize for multiple scenarios** - Test variations efficiently:

```python
@pytest.mark.parametrize("extension,expected", [
    (".csv", "csv"),
    (".parquet", "parquet"),
    (".xlsx", "excel"),
])
def test_detects_file_format(extension, expected, tmp_path):
    """Correctly identifies file formats."""
    # test implementation
```

**Mock external dependencies** - Isolate your code from external systems:

```python
def test_api_call(mocker):
    """Test without making real API calls."""
    mock_get = mocker.patch("requests.get")
    mock_get.return_value.json.return_value = {"data": "test"}
    # test implementation
```

**Assert exact values** - Be specific about what you expect:

```python
# Good - exact assertion
assert result == {"name": "Alice", "age": 30}
assert list(df.columns) == ["id", "name", "value"]

# Avoid - vague assertions
assert len(result) > 0  # What should the exact length be?
assert "name" in result  # What else should be in result?
```

**Keep tests simple** - Each test should verify one specific behavior with clear arrange/act/assert phases.

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
