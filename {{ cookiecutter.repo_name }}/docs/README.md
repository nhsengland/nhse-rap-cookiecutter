# Documentation

This directory contains the project documentation built with [MkDocs](https://www.mkdocs.org/) and the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.

## Structure

```
docs/
├── content/                # Documentation content
│   ├── index.md            # Home page
│   ├── getting_started.md  # Getting started guide
│   ├── usage.md            # Usage guide
│   ├── contributing.md     # Contributing guidelines
│   ├── api_reference/      # API documentation
│   ├── images/             # Images and assets
│   ├── javascripts/        # JavaScript files
│   ├── stylesheets/        # CSS stylesheets
│   └── overrides/          # Theme overrides
└── README.md               # This file

mkdocs.yml                  # MkDocs configuration (at project root)
```

## Building the Documentation

### Locally

{% if cookiecutter.environment_manager == 'uv' %}Build the documentation:

```bash
uv run mkdocs build
```

Serve the documentation locally with live reload:

```bash
uv run mkdocs serve
```

{% elif cookiecutter.environment_manager == 'poetry' %}Build the documentation:

```bash
poetry run mkdocs build
```

Serve the documentation locally with live reload:

```bash
poetry run mkdocs serve
```

{% elif cookiecutter.environment_manager == 'pixi' %}Build the documentation:

```bash
pixi run mkdocs build
```

Serve the documentation locally with live reload:

```bash
pixi run mkdocs serve
```

{% elif cookiecutter.environment_manager == 'pipenv' %}Build the documentation:

```bash
pipenv run mkdocs build
```

Serve the documentation locally with live reload:

```bash
pipenv run mkdocs serve
```

{% else %}Build the documentation:

```bash
mkdocs build
```

Serve the documentation locally with live reload:

```bash
mkdocs serve
```

{% endif %}

The documentation will be available at <http://127.0.0.1:8000/>

### GitHub Pages

The documentation is automatically built and deployed to GitHub Pages when changes are pushed to the main branch.
