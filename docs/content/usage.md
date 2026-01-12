# Usage

## Creating a New Project

There are two ways to create a new NHS RAP project:

### Method 1: Using the NHS RAP Template CLI

If you installed the `nhs-rap-cookiecutter` package:

```bash
nhs-rap-template
```

### Method 2: Using Official Cookiecutter

If you want to use this alongside other cookiecutter templates or prefer the standard cookiecutter workflow:

```bash
# Install cookiecutter if needed
pipx install cookiecutter
# or: pip install cookiecutter

# Create project from GitHub
cookiecutter gh:nhsengland/nhse-rap-cookiecutter

# Or from a local clone
cookiecutter /path/to/nhse-rap-cookiecutter
```

Both methods will prompt you for configuration options and generate a complete project structure.

### Which Method Should I Use?

**Use NHS RAP Template CLI when:**

- You primarily work with NHS RAP projects
- You want the simplest installation and usage
- You prefer a dedicated command (`nhs-rap-template`)

**Use Cookiecutter when:**

- You work with multiple project templates
- You want to integrate with existing cookiecutter workflows
- You need cookiecutter's advanced features (replay, custom config files)
- You prefer using a single tool for all your template needs

## Non-Interactive Mode

For automation or CI/CD, both methods support non-interactive mode:

**With NHS RAP Template CLI:**

```bash
nhs-rap-template --no-input --config-file my-config.json
```

**With Cookiecutter:**

```bash
cookiecutter gh:nhsengland/nhse-rap-cookiecutter --no-input
```

## Using Specific Template Versions

Both methods support using specific versions:

**With NHS RAP Template CLI:**

```bash
# Use latest development version
nhs-rap-template -c main

# Use a specific tag
nhs-rap-template -c v1.0.0

# Use a specific commit
nhs-rap-template -c abc123def
```

**With Cookiecutter:**

```bash
# Use a specific branch
cookiecutter gh:nhsengland/nhse-rap-cookiecutter --checkout main

# Use a specific tag
cookiecutter gh:nhsengland/nhse-rap-cookiecutter --checkout v1.0.0
```

## Configuration Options

When you run `nhs-rap-template`, you'll be prompted for:

- **Project Name**: Human-readable name (e.g., "My Analysis Project")
- **Author Details**: Your name and email
- **Organization**: Organization name and contact email (used in LICENSE)
- **Python Version**: Minimum Python version (3.10+)
- **Environment Manager**: virtualenv, conda, pipenv, uv, pixi, poetry, or none
- **Dependency File**: requirements.txt, pyproject.toml, environment.yml, Pipfile, or pixi.toml
- **PyData Packages**: Include pandas, numpy, matplotlib, etc.
- **Dataset Storage**: Azure, S3, GCS, or none
- **License**: MIT, BSD-3-Clause, or no license
- **Documentation**: mkdocs or none

## Generated Project Structure

The template creates a standardised RAP project with:

- **Data folders**: raw, interim, processed, external
- **Source code**: Python package structure with your module
- **Documentation**: MkDocs setup with NHS styling
- **Testing**: pytest configuration
- **Quality**: ruff for linting/formatting, pre-commit hooks
- **Reproducibility**: Environment management, dependency tracking

## Next Steps After Generation

After creating your project:

1. **Navigate to the project**:

   ```bash
   cd your-project-name
   ```

2. **Create environment** (if using UV):

   ```bash
   uv sync
   ```

3. **Set up pre-commit** (optional but recommended):

   ```bash
   uv run pre-commit install
   ```

4. **Start developing**:
   - Add your code to the module folder
   - Add tests to the `tests/` folder
   - Update documentation in `docs/`

## Customizing After Generation

All generated files can be customised:

- Edit `pyproject.toml` for dependencies
- Modify `Makefile` for custom commands
- Update `mkdocs.yml` for documentation structure
- Add custom pre-commit hooks in `.pre-commit-config.yaml`

## Common Workflows

### Adding Dependencies

With UV:

```bash
uv add pandas numpy
```

With pip:

```bash
pip install pandas numpy
pip freeze > requirements.txt
```

### Running Tests

```bash
make test
# or
uv run pytest tests/
```

### Building Documentation

```bash
uv run mkdocs serve
```

### Code Quality Checks

```bash
make lint    # Check code
make format  # Format code
```

## Cookiecutter-Specific Features

When using the official cookiecutter tool, you get additional features:

### Using Cookiecutter Replay

Cookiecutter saves your previous inputs. To recreate a project with the same configuration:

```bash
# Create first project
cookiecutter gh:nhsengland/nhse-rap-cookiecutter

# Later, replay with same inputs
cookiecutter gh:nhsengland/nhse-rap-cookiecutter --replay
```

### Using a Cookiecutter Config File

Create `~/.cookiecutterrc` with default values:

```yaml
default_context:
    author_name: "Jane Smith"
    author_email: "jane.smith@nhs.net"
    organization_name: "NHS England"
    team_name: "Data Science Team"
    team_email: "datascience@nhs.net"
    python_version_number: "3.11"
    environment_manager: "uv"
    linting_and_formatting: "ruff"
```

Then cookiecutter will use these as defaults:

```bash
cookiecutter gh:nhsengland/nhse-rap-cookiecutter
# Will pre-fill with your defaults!
```

### Using Multiple Templates

With cookiecutter, you can easily switch between different templates:

```bash
# NHS RAP template for analytical projects
cookiecutter gh:nhsengland/nhse-rap-cookiecutter

# Different template for web applications
cookiecutter gh:cookiecutter/cookiecutter-django

# Your organization's custom template
cookiecutter gh:your-org/your-template
```

### Templating from Local Directory

Useful when developing or customizing the template:

```bash
# Clone the template
git clone https://github.com/nhsengland/nhse-rap-cookiecutter.git

# Make local modifications
cd nhse-rap-cookiecutter
# ... edit template files ...

# Use your modified template
cookiecutter ../nhse-rap-cookiecutter
```
