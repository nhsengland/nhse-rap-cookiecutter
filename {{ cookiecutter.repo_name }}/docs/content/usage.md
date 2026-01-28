# Usage Guide

This guide covers common tasks and workflows for working with {{ cookiecutter.project_name }}.

## Project Structure

The project follows the standard RAP (Reproducible Analytical Pipeline) structure:

- `{{ cookiecutter.module_name }}/` - Main source code
    - `config.py` - Configuration management
    - `dataset.py` - Data loading and processing
    - `features.py` - Feature engineering
    - `plots.py` - Visualisation utilities
    - `modeling/` - Machine learning models
- `data/` - Data storage (raw, interim, processed, external)
- `notebooks/` - Jupyter notebooks for exploration
- `tests/` - Unit and integration tests
- `docs/` - Project documentation

## Common Tasks

### Working with Data

#### Loading Data

```python
from {{ cookiecutter.module_name }}.dataset import Dataset

# Load raw data
dataset = Dataset()
data = dataset.load_raw("path/to/data.csv")
```

#### Processing Data

```python
# Process data
processed_data = dataset.process(data)

# Save processed data
dataset.save_processed(processed_data, "output.csv")
```

### Configuration Management

The `config.py` module handles project configuration:

```python
from {{ cookiecutter.module_name }}.config import Config

# Load configuration
config = Config.load("config.yaml")

# Access config values
data_path = config.get("data_path")
```

### Feature Engineering

```python
from {{ cookiecutter.module_name }}.features import FeatureBuilder

# Build features
builder = FeatureBuilder()
features = builder.transform(data)
```

### Creating Visualisations

```python
from {{ cookiecutter.module_name }}.plots import create_plot

# Create a plot
fig = create_plot(data, plot_type="scatter")
fig.savefig("reports/figures/plot.png")
```

### Training Models

```python
from {{ cookiecutter.module_name }}.modeling.train import train_model

# Train a model
model = train_model(features, labels)

# Save the model
model.save("models/model.pkl")
```

### Making Predictions

```python
from {{ cookiecutter.module_name }}.modeling.predict import predict

# Load model and make predictions
predictions = predict(new_data, model_path="models/model.pkl")
```

## Running the Pipeline

{% if cookiecutter.environment_manager == 'uv' %}

```bash
# Run the full pipeline
uv run python -m {{ cookiecutter.module_name }}

# Run specific steps
uv run python -m {{ cookiecutter.module_name }}.dataset
uv run python -m {{ cookiecutter.module_name }}.modeling.train
```

{% elif cookiecutter.environment_manager == 'poetry' %}

```bash
# Run the full pipeline
poetry run python -m {{ cookiecutter.module_name }}

# Run specific steps
poetry run python -m {{ cookiecutter.module_name }}.dataset
poetry run python -m {{ cookiecutter.module_name }}.modeling.train
```

{% elif cookiecutter.environment_manager == 'pixi' %}

```bash
# Run the full pipeline
pixi run python -m {{ cookiecutter.module_name }}

# Run specific steps
pixi run python -m {{ cookiecutter.module_name }}.dataset
pixi run python -m {{ cookiecutter.module_name }}.modeling.train
```

{% elif cookiecutter.environment_manager == 'pipenv' %}

```bash
# Run the full pipeline
pipenv run python -m {{ cookiecutter.module_name }}

# Run specific steps
pipenv run python -m {{ cookiecutter.module_name }}.dataset
pipenv run python -m {{ cookiecutter.module_name }}.modeling.train
```

{% else %}

```bash
# Run the full pipeline
python -m {{ cookiecutter.module_name }}

# Run specific steps
python -m {{ cookiecutter.module_name }}.dataset
python -m {{ cookiecutter.module_name }}.modeling.train
```

{% endif %}

## Working with Notebooks

Jupyter notebooks are stored in the `notebooks/` directory. Use them for:

- Exploratory data analysis
- Prototyping new features
- Visualizing results
- Documenting analysis

{% if cookiecutter.environment_manager == 'uv' %}

```bash
# Start Jupyter
uv run jupyter lab
```

{% elif cookiecutter.environment_manager == 'poetry' %}

```bash
# Start Jupyter
poetry run jupyter lab
```

{% elif cookiecutter.environment_manager == 'pixi' %}

```bash
# Start Jupyter
pixi run jupyter lab
```

{% elif cookiecutter.environment_manager == 'pipenv' %}

```bash
# Start Jupyter
pipenv run jupyter lab
```

{% else %}

```bash
# Start Jupyter
jupyter lab
```

{% endif %}

## Code Quality

### Testing

The project uses pytest for all testing. Tests are organized into two categories:

- `tests/unittests/` - Unit tests for individual functions and classes
- `tests/e2e/` - End-to-end integration tests for complete workflows

#### Writing Unit Tests

Unit tests should:

- Be organized in test classes (one class per function/object being tested)
- Test one behavior per test method
- Use descriptive names: `test_<what>_<expected_behavior>`
- Use `pytest.mark.parametrize` for testing multiple input variations

Example:

```python
import pytest

class TestDataLoading:
    """Tests for data loading functionality."""
    
    def test_loads_csv_file(self):
        """Loading valid CSV returns DataFrame."""
        result = load_data("test.csv")
        assert len(result) > 0
    
    @pytest.mark.parametrize("value", [1, 2, 3])
    def test_validates_positive_values(self, value):
        """Validation accepts positive values."""
        assert validate(value) is True
```

#### Running Tests

{% if cookiecutter.environment_manager == 'uv' %}

```bash
# Run all tests
uv run pytest

# Run unit tests only
uv run pytest tests/unittests/

# Run specific test file
uv run pytest tests/unittests/test_dataset.py

# Run with coverage
uv run pytest --cov={{ cookiecutter.module_name }} --cov-report=html
```

{% elif cookiecutter.environment_manager == 'poetry' %}

```bash
# Run all tests
poetry run pytest

# Run unit tests only
poetry run pytest tests/unittests/

# Run specific test file
poetry run pytest tests/unittests/test_dataset.py

# Run with coverage
poetry run pytest --cov={{ cookiecutter.module_name }} --cov-report=html
```

{% elif cookiecutter.environment_manager == 'pixi' %}

```bash
# Run all tests
pixi run pytest

# Run unit tests only
pixi run pytest tests/unittests/

# Run specific test file
pixi run pytest tests/unittests/test_dataset.py

# Run with coverage
pixi run pytest --cov={{ cookiecutter.module_name }} --cov-report=html
```

{% elif cookiecutter.environment_manager == 'pipenv' %}

```bash
# Run all tests
pipenv run pytest

# Run unit tests only
pipenv run pytest tests/unittests/

# Run specific test file
pipenv run pytest tests/unittests/test_dataset.py

# Run with coverage
pipenv run pytest --cov={{ cookiecutter.module_name }} --cov-report=html
```

{% else %}

```bash
# Run all tests
pytest

# Run unit tests only
pytest tests/unittests/

# Run specific test file
pytest tests/unittests/test_dataset.py

# Run with coverage
pytest --cov={{ cookiecutter.module_name }} --cov-report=html
```

{% endif %}

### Code Formatting and Linting

{% if cookiecutter.environment_manager == 'uv' %}

```bash
# Check code style
uv run ruff check .

# Format code
uv run ruff format .

# Run both
uv run ruff check . && uv run ruff format .
```

{% elif cookiecutter.environment_manager == 'poetry' %}

```bash
# Check code style
poetry run ruff check .

# Format code
poetry run ruff format .

# Run both
poetry run ruff check . && poetry run ruff format .
```

{% elif cookiecutter.environment_manager == 'pixi' %}

```bash
# Check code style
pixi run ruff check .

# Format code
pixi run ruff format .

# Run both
pixi run ruff check . && pixi run ruff format .
```

{% elif cookiecutter.environment_manager == 'pipenv' %}

```bash
# Check code style
pipenv run ruff check .

# Format code
pipenv run ruff format .

# Run both
pipenv run ruff check . && pipenv run ruff format .
```

{% else %}

```bash
# Check code style
ruff check .

# Format code
ruff format .

# Run both
ruff check . && ruff format .
```

{% endif %}

## Make Commands

The project includes a Makefile with convenient commands for common tasks:

```bash
# Run tests
make test

# Lint and format code
make lint     # Check code style without changing files
make format   # Auto-format code
{% if cookiecutter.docs == 'mkdocs' %}
# Build and serve documentation
make docs        # Serve documentation with live reload
make docs-build  # Build static documentation site
{% endif %}
{% if cookiecutter.include_code_scaffold == 'Yes' %}
# Run data pipeline
make data     # Execute the data processing pipeline
{% endif %}
# Set up environment
make create_environment  # Create virtual environment
make requirements        # Install dependencies

# Clean up
make clean    # Remove compiled Python files
```

All Make commands automatically use the correct command runner based on your chosen environment manager ({% if cookiecutter.environment_manager == 'uv' %}uv{% elif cookiecutter.environment_manager == 'poetry' %}poetry{% elif cookiecutter.environment_manager == 'pixi' %}pixi{% else %}python{% endif %}).

## Best Practices

1. **Keep data out of version control** - Use `.gitignore` to exclude data files
2. **Use configuration files** - Store parameters in `config.yaml`, not hardcoded
3. **Write tests** - Aim for good test coverage of core functionality
4. **Document your code** - Use docstrings and type hints
5. **Keep notebooks clean** - Move reusable code to modules
6. **Version your models** - Save models with timestamps or version numbers
7. **Log your pipeline** - Use logging to track pipeline execution

## Next Steps

- Explore the [API Reference](api_reference/index.md) for detailed module documentation
- Check the [Contributing Guide](contributing.md) to contribute improvements
