# API Reference

This section provides detailed API documentation for `{{ cookiecutter.module_name }}`.

The documentation is automatically generated from source code docstrings using [mkdocstrings](https://mkdocstrings.github.io/). Each module has its own page with detailed documentation of all classes, functions, and methods.

## How to Document Your Code

All API documentation is generated from **docstrings** in your Python code. Follow these guidelines:

### Docstring Format

This project uses **NumPy-style docstrings**. Example:

```python
def process_data(data: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """
    Process the input dataframe by applying filters and transformations.

    Parameters
    ----------
    data : pd.DataFrame
        The input data to process
    threshold : float, optional
        Threshold value for filtering (default: 0.5)

    Returns
    -------
    pd.DataFrame
        The processed dataframe

    Raises
    ------
    ValueError
        If data is empty or threshold is negative

    Examples
    --------
    >>> df = pd.DataFrame({'value': [0.3, 0.7, 0.9]})
    >>> result = process_data(df, threshold=0.6)
    >>> len(result)
    2
    """
    if data.empty:
        raise ValueError("Data cannot be empty")
    return data[data['value'] > threshold]
```

### Adding New Modules to Documentation

When you add new Python files, create corresponding documentation pages. Follow these **step-by-step instructions**:

#### Step 1: Create Documentation File Structure

Match your Python module structure in `docs/content/api_reference/`:

```bash
# If you have: {{ cookiecutter.module_name }}/utils.py
# Create: docs/content/api_reference/utils.md

# If you have: {{ cookiecutter.module_name }}/analysis/metrics.py
# Create: docs/content/api_reference/analysis/metrics.md (and analysis/index.md)
```

#### Step 2: Create the Documentation Page

Create a markdown file for each Python module. Example for `docs/content/api_reference/config.md`:

```markdown
# Configuration

This module handles project configuration and settings.

::: {{ cookiecutter.module_name }}.config
    options:
      show_root_heading: true
      show_source: true
      members_order: source
      show_if_no_docstring: false
      heading_level: 2
```

**mkdocstrings Options Explained:**

- `show_root_heading: true` - Shows the module name as a heading
- `show_source: true` - Includes "View Source" links to GitHub
- `members_order: source` - Orders members as they appear in source code
- `show_if_no_docstring: false` - Hides undocumented items
- `heading_level: 2` - Sets heading level for the module (use `##`)

#### Step 3: Document Subpackages

For subpackages (e.g., `modeling/`), create an index page at `docs/content/api_reference/modeling/index.md`:

```markdown
# Modeling

Machine learning models and training pipelines.

## Submodules

- [train](train.md) - Model training functions
- [predict](predict.md) - Model inference and prediction

## Overview

::: {{ cookiecutter.module_name }}.modeling
    options:
      show_root_heading: false
      members: []
```

Then create individual pages for each submodule:

- `docs/content/api_reference/modeling/train.md`
- `docs/content/api_reference/modeling/predict.md`

#### Step 4: Update mkdocs.yml Navigation

Add your new pages to the navigation section in `mkdocs.yml`:

```yaml
nav:
  - Home: index.md
  - Getting Started: getting_started.md
  - Usage: usage.md
  - Contributing: contributing.md
  - API Reference:
      - Overview: api_reference/index.md
      - config: api_reference/config.md
      - dataset: api_reference/dataset.md
      - features: api_reference/features.md
      - plots: api_reference/plots.md
      - modeling:
          - Overview: api_reference/modeling/index.md
          - train: api_reference/modeling/train.md
          - predict: api_reference/modeling/predict.md
      # Add your new modules here
```

#### Step 5: Build and Check Documentation

Test your documentation locally:

```bash
# Serve documentation locally
mkdocs serve

# Open browser to http://127.0.0.1:8000
# Navigate to API Reference to verify your pages
```

#### Complete Example Workflow

Let's say you add a new file `{{ cookiecutter.module_name }}/preprocessing.py`:

1. **Create the documentation file:**

   ```bash
   touch docs/content/api_reference/preprocessing.md
   ```

2. **Add content to `preprocessing.md`:**

   ```markdown
   # Preprocessing
   
   Data preprocessing and cleaning utilities.
   
   ::: {{ cookiecutter.module_name }}.preprocessing
       options:
         show_root_heading: true
         show_source: true
         members_order: source
   ```

3. **Update `mkdocs.yml`:**

   ```yaml
   - API Reference:
       - Overview: api_reference/index.md
       - config: api_reference/config.md
       - dataset: api_reference/dataset.md
       - preprocessing: api_reference/preprocessing.md  # NEW
       - features: api_reference/features.md
   ```

4. **Write good docstrings in your Python code:**

   ```python
   # {{ cookiecutter.module_name }}/preprocessing.py
   
   def clean_data(df: pd.DataFrame) -> pd.DataFrame:
       """
       Remove invalid rows and standardize column formats.
       
       Parameters
       ----------
       df : pd.DataFrame
           Input dataframe to clean
           
       Returns
       -------
       pd.DataFrame
           Cleaned dataframe
       """
       # implementation
   ```

5. **Test it:**

   ```bash
   mkdocs serve
   # Visit http://127.0.0.1:8000/api_reference/preprocessing/
   ```

## Example: Complete API Documentation Setup

Below is a working example showing how to document all modules in this project:

### config.md

```markdown
# Configuration

Configuration management and settings.

::: {{ cookiecutter.module_name }}.config
    options:
      show_root_heading: true
      show_source: true
      members_order: source
```

### dataset.md

```markdown
# Dataset

Data loading, processing, and saving utilities.

::: {{ cookiecutter.module_name }}.dataset
    options:
      show_root_heading: true
      show_source: true
      members_order: source
```

### features.md

```markdown
# Features

Feature engineering and transformation functions.

::: {{ cookiecutter.module_name }}.features
    options:
      show_root_heading: true
      show_source: true
      members_order: source
```

### plots.md

```markdown
# Plots

Visualization and plotting utilities.

::: {{ cookiecutter.module_name }}.plots
    options:
      show_root_heading: true
      show_source: true
      members_order: source
```

### modeling/index.md

```markdown
# Modeling

Machine learning models and training pipelines.

## Submodules

- [train](train.md) - Model training functions
- [predict](predict.md) - Model inference and prediction
```

### modeling/train.md

```markdown
# Train

Model training functions.

::: {{ cookiecutter.module_name }}.modeling.train
    options:
      show_root_heading: true
      show_source: true
      members_order: source
```

### modeling/predict.md

```markdown
# Predict

Model inference and prediction.

::: {{ cookiecutter.module_name }}.modeling.predict
    options:
      show_root_heading: true
      show_source: true
      members_order: source
```
