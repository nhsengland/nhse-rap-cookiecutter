.PHONY: docs-serve docs-build

# Serve documentation with livereload (required for mkdocs bug)
docs-serve:
	mkdocs serve --livereload

# Build documentation
docs-build:
	mkdocs build
