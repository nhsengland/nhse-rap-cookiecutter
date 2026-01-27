.PHONY: docs docs-serve docs-build lint format format-check test check

# Serve documentation (default docs command)
docs: docs-serve

# Serve documentation with livereload (workaround for mkdocs issue)
docs-serve:
	uv run mkdocs serve --livereload

# Build documentation
docs-build:
	uv run mkdocs build

# Run ruff linting on source code
lint:
	uv run ruff check .

# Run ruff formatting on source code
format:
	uv run ruff format .

# Check formatting without making changes
format-check:
	uv run ruff format --check .

# Run tests
test:
	uv run pytest tests/ -v

# Run all checks (lint + format-check + test)
check: lint format-check test
	@echo "All checks passed!"
