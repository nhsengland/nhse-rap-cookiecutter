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
- **Repository Name**: Repository name (defaults to lowercase project name with underscores)
- **Module Name**: Python module name (defaults to repository name with dashes as underscores)
- **Author Details**: Your name and email
- **Organization**: Organization name (default: NHS England) and team contact email
- **Git Hosting Platform**: github, gitlab, azure_devops, or other
- **Repository URL**: Your repository URL (defaults to GitHub format, can be overridden)
- **Python Version**: Minimum Python version (3.10-3.13)
- **Environment Manager**: uv (recommended), pip + venv, or conda
- **Linting/Formatting**: ruff or flake8+black+isort
- **License**: MIT, Apache-2.0, GPL-3.0, or No license file
- **Documentation**: mkdocs or none
- **Code Scaffold**: Include example code modules (Yes or No)
- **Layout**: Package layout — `flat` (package at the project root) or `src` (package under `src/`, aligned with the RAP community package template)

### Included Packages

**All generated projects automatically include:**

**Runtime packages**: pandas, numpy, matplotlib, seaborn, plotly, scipy, scikit-learn, jupyterlab, notebook, ipython, loguru, tqdm, requests, openpyxl

**Development packages**: pytest, pytest-cov, pre-commit, and your chosen linting/formatting tools (ruff or flake8+black+isort)

**Documentation packages**: mkdocs, mkdocs-material, mkdocstrings (if docs enabled)

### Dependency File Format

The dependency file format is determined automatically by your environment manager choice:

- **uv, pip + venv**: `pyproject.toml` (modern Python standard)
- **conda**: `environment.yml` (conda-specific format)

Both formats include the same packages - the difference is only in file format to match your chosen tool.

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

2. **Run automated setup**:

   ```bash
   make setup
   ```

   This sets up your environment, installs dependencies, configures git, and installs pre-commit hooks.

3. **Start developing**:
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

Add dependencies to your project:

=== "uv"

    ```bash
    uv add pandas numpy
    ```

=== "pip + venv"

    ```bash
    # Add the dependency to pyproject.toml, then:
    pip install -e ".[dev]"
    ```

=== "Conda"

    ```bash
    # Edit environment.yml, then:
    conda install pandas numpy
    ```

### Running Tests

```bash
make test
```

The Makefile automatically uses your chosen environment manager's run command.

### Building Documentation

```bash
make docs        # Serve with live reload
make docs-build  # Build static site
```

The Makefile handles the correct command for your environment manager.

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

## Customizing Your Generated Project

### Customizing Badges

The generated project includes a comprehensive set of badges at the top of the README and a `badges.toml` file with a library of ready-to-use badges you can swap in and out.

#### Default Badges

Your generated project will include these badges automatically in the README:

- **Project Status**: Active (default)
- **RAP Status**: Work in Progress (default)
- **Cookiecutter**: Links to cookiecutter project
- **NHS England RAP**: Links to this template
- **Python Version**: Automatically populated from your configuration
- **License**: MIT, Apache-2.0, or GPL-3.0 (if selected during generation)
- **Code Style**: Ruff or Black/Flake8/isort (based on your selection)
- **Pre-commit**: Pre-commit enabled

#### Using the Badge Library (badges.toml)

Your project includes a `badges.toml` file with ready-to-use badge markdown. Simply copy and paste badges from this file into your README.md or docs/index.md.

**Available in badges.toml:**

**Project Status** (`[project_status]`):

- `concept` - Brainstorming phase, no code or only rough scripts
- `wip` - Work in progress, active development occurring
- `poc` - Proof of Concept, code exists to prove hypothesis but not production-ready
- `mvp` - Minimum Viable Product, functional model/pipeline reliable for initial users
- `active` - Actively maintained and updated (default)
- `on_hold` - Development paused (data availability, shifting priorities, etc.)
- `archived` - Project finished or abandoned, read-only

**RAP Status** (`[rap_status]`) - [RAP maturity levels](https://nhsdigital.github.io/rap-community-of-practice/introduction_to_RAP/levels_of_RAP/):

- `wip` - Beginning RAP journey (default)
- `baseline` - Core RAP requirements met (version control, peer review, documentation)
- `silver` - Enhanced capabilities (automated testing, continuous integration, functions/classes)
- `gold` - Advanced practices (package/repository, error handling, logging, documentation website)

**GitHub CI/CD Badges** (`[github]`) - if you selected GitHub as your hosting platform:

- `tests` - Test workflow status
- `lint` - Lint workflow status
- `docs` - Documentation build status
- `release` - Latest release version
- `pages` - GitHub Pages documentation status

**GitLab CI/CD Badges** (`[gitlab]`) - if you selected GitLab as your hosting platform:

- `pipeline` - Pipeline status
- `coverage` - Code coverage

**Other Badges** (`[other]`):

- `pypi` - PyPI version (if publishing to PyPI)
- `ogl3` - Open Government License badge

#### Example: Updating Project Status

To change your project status from "Active" to "MVP", open `badges.toml` and copy the MVP badge:

```toml
mvp = "[![Project Status: MVP](https://img.shields.io/badge/Project%20Status-MVP-yellowgreen)](https://github.com/your-org/your-repo)"
```

Then replace the project status badge in your README.md with this copied badge markdown.

#### Adding CI/CD Badges

Once you set up GitHub Actions or GitLab CI workflows, copy the relevant badges from the `[github]` or `[gitlab]` sections in `badges.toml`. The badges are pre-configured with your repository URL.

For custom badge options and colors, see [shields.io](https://shields.io/).
