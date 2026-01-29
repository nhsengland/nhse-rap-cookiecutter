"""Tests for NHS RAP Cookiecutter Template."""

import pytest


class TestTemplateGeneration:
    """Tests for basic template generation."""

    def test_generates_successfully_with_defaults(self, cookies):
        """Template generates successfully with default values."""
        result = cookies.bake()

        assert result.exit_code == 0
        assert result.exception is None
        assert result.project_path.name == "project_name"
        assert result.project_path.is_dir()


class TestTemplateFiles:
    """Tests for required files in generated project."""

    @pytest.mark.parametrize(
        "filename",
        [
            "README.md",
            "pyproject.toml",
            "Makefile",
            ".gitignore",
            ".pre-commit-config.yaml",
        ],
    )
    def test_has_required_file(self, cookies, filename):
        """Generated project contains required file."""
        result = cookies.bake()

        assert result.exit_code == 0
        assert (result.project_path / filename).exists()


class TestTemplateDirectories:
    """Tests for required directories in generated project."""

    @pytest.mark.parametrize(
        "dirname",
        ["data", "docs", "models", "notebooks", "references", "reports", "tests", "project_name"],
    )
    def test_has_required_directory(self, cookies, dirname):
        """Generated project contains required directory."""
        result = cookies.bake()

        assert result.exit_code == 0
        assert (result.project_path / dirname).is_dir()


class TestEnvironmentManager:
    """Tests for environment manager configurations."""

    def test_uv_creates_correct_makefile_commands(self, cookies):
        """UV environment manager includes correct commands in Makefile."""
        result = cookies.bake(extra_context={"environment_manager": "uv"})

        assert result.exit_code == 0
        makefile_content = (result.project_path / "Makefile").read_text()
        assert "uv venv" in makefile_content or "uv sync" in makefile_content


class TestTestingFramework:
    """Tests for pytest testing framework setup."""

    def test_creates_unittests_directory(self, cookies):
        """Template creates tests/unittests directory."""
        result = cookies.bake()

        assert result.exit_code == 0
        assert (result.project_path / "tests" / "unittests").is_dir()

    def test_creates_e2e_directory(self, cookies):
        """Template creates tests/e2e directory."""
        result = cookies.bake()

        assert result.exit_code == 0
        assert (result.project_path / "tests" / "e2e").is_dir()

    def test_includes_pytest_in_dependencies(self, cookies):
        """Template includes pytest in project dependencies."""
        result = cookies.bake()

        assert result.exit_code == 0
        pyproject_content = (result.project_path / "pyproject.toml").read_text()
        assert "pytest" in pyproject_content

    def test_includes_testing_documentation(self, cookies):
        """Template includes testing guide in documentation."""
        result = cookies.bake()

        assert result.exit_code == 0
        assert (result.project_path / "docs" / "content" / "testing.md").exists()


class TestLicense:
    """Tests for license file generation."""

    def test_mit_license_creates_license_file(self, cookies):
        """MIT license option creates LICENSE file."""
        result = cookies.bake(extra_context={"open_source_license": "MIT"})

        assert result.exit_code == 0
        assert (result.project_path / "LICENSE").exists()

    def test_mit_license_contains_mit_text(self, cookies):
        """MIT LICENSE file contains MIT license text."""
        result = cookies.bake(extra_context={"open_source_license": "MIT"})

        license_content = (result.project_path / "LICENSE").read_text()
        assert "MIT" in license_content


class TestProjectNaming:
    """Tests for project name conversion."""

    def test_converts_project_name_to_snake_case(self, cookies):
        """Project name with spaces converts to snake_case for directory."""
        result = cookies.bake(extra_context={"project_name": "My Test Project"})

        assert result.exit_code == 0
        assert result.project_path.name == "my_test_project"

    def test_creates_module_with_converted_name(self, cookies):
        """Module directory uses converted project name."""
        result = cookies.bake(extra_context={"project_name": "My Test Project"})

        assert result.exit_code == 0
        assert (result.project_path / "my_test_project").is_dir()


class TestDocumentation:
    """Tests for documentation generation."""

    def test_mkdocs_creates_docs_directory(self, cookies):
        """mkdocs option creates docs directory."""
        result = cookies.bake(extra_context={"docs": "mkdocs"})

        assert result.exit_code == 0
        assert (result.project_path / "docs").is_dir()

    def test_mkdocs_creates_content_directory(self, cookies):
        """mkdocs option creates docs/content directory."""
        result = cookies.bake(extra_context={"docs": "mkdocs"})

        assert result.exit_code == 0
        assert (result.project_path / "docs" / "content").is_dir()

    def test_mkdocs_creates_config_file(self, cookies):
        """mkdocs option creates mkdocs.yml configuration."""
        result = cookies.bake(extra_context={"docs": "mkdocs"})

        assert result.exit_code == 0
        assert (result.project_path / "mkdocs.yml").is_file()
