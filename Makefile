.PHONY: docs-serve docs-build lint format format-check test check

# Serve documentation with livereload (required for mkdocs bug)
docs-serve:
	mkdocs serve --livereload

# Build documentation
docs-build:
	mkdocs build

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
	uv run pytest tests/unittests/ -v

# Run all checks (lint + format-check + test)
check: lint format-check test
	@echo "All checks passed!"
