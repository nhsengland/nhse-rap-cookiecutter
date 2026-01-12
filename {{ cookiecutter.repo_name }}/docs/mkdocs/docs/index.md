# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Overview

This project follows NHS England RAP (Reproducible Analytical Pipeline) standards and includes:

- Standardised project structure
- Automated testing with pytest
- Code quality checks with ruff
- Documentation with MkDocs
- Environment management with {{ cookiecutter.environment_manager }}

## Getting Started

See the [Getting Started](getting_started.md) guide for installation and setup instructions.

## Usage

Learn how to use this project in the [Usage Guide](usage.md).

## Contributing

Contributions are welcome! See the [Contributing Guide](contributing.md) for details.

## API Reference

For detailed API documentation, see the [API Reference](api_reference/index.md).

## License

{% if cookiecutter.open_source_license != 'No license file' %}This project is licensed under the {{ cookiecutter.open_source_license }} license.{% else %}This project does not include an open source license.{% endif %}
