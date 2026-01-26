"""Tests for direct cookiecutter template usage."""

import subprocess
from pathlib import Path

import pytest


@pytest.fixture
def template_dir():
    """Return the path to the template directory."""
    return Path.cwd()


class TestCookiecutterProjectGeneration:
    """Tests for cookiecutter command project generation."""

    def test_generates_project_directory(self, tmp_path, template_dir):
        """Cookiecutter creates project directory with correct name."""
        result = subprocess.run(
            [
                "cookiecutter",
                str(template_dir),
                "--no-input",
                "-o",
                str(tmp_path),
            ],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0
        assert (tmp_path / "project_name").is_dir()

    def test_generates_exact_required_files(self, tmp_path, template_dir):
        """Cookiecutter generates exactly the expected root-level files."""
        subprocess.run(
            [
                "cookiecutter",
                str(template_dir),
                "--no-input",
                "-o",
                str(tmp_path),
            ],
            capture_output=True,
        )

        project_path = tmp_path / "project_name"
        expected_files = {
            "README.md",
            "pyproject.toml",
            "Makefile",
            ".gitignore",
            ".pre-commit-config.yaml",
            "LICENSE",
            "LICENSE-OGL",
            ".env",
            "badges.toml",
            "mkdocs.yml",
        }
        actual_files = {f.name for f in project_path.iterdir() if f.is_file()}

        assert expected_files == actual_files

    def test_generates_exact_required_directories(self, tmp_path, template_dir):
        """Cookiecutter generates exactly the expected root-level directories."""
        subprocess.run(
            [
                "cookiecutter",
                str(template_dir),
                "--no-input",
                "-o",
                str(tmp_path),
            ],
            capture_output=True,
        )

        project_path = tmp_path / "project_name"
        expected_dirs = {
            "project_name",
            "data",
            "docs",
            "models",
            "notebooks",
            "references",
            "reports",
            "tests",
        }
        actual_dirs = {d.name for d in project_path.iterdir() if d.is_dir()}

        assert expected_dirs == actual_dirs


class TestCookiecutterModuleStructure:
    """Tests for the Python module structure created by cookiecutter."""

    def test_creates_exact_module_files(self, tmp_path, template_dir):
        """Cookiecutter creates exactly the expected module files."""
        subprocess.run(
            [
                "cookiecutter",
                str(template_dir),
                "--no-input",
                "-o",
                str(tmp_path),
            ],
            capture_output=True,
        )

        module_path = tmp_path / "project_name" / "project_name"
        expected_files = {
            "__init__.py",
            "config.py",
            "dataset.py",
            "features.py",
            "plots.py",
        }
        actual_files = {f.name for f in module_path.iterdir() if f.is_file()}

        assert expected_files == actual_files

    def test_creates_modeling_submodule(self, tmp_path, template_dir):
        """Cookiecutter creates modeling submodule with correct structure."""
        subprocess.run(
            [
                "cookiecutter",
                str(template_dir),
                "--no-input",
                "-o",
                str(tmp_path),
            ],
            capture_output=True,
        )

        modeling_path = tmp_path / "project_name" / "project_name" / "modeling"
        expected_files = {"__init__.py", "train.py", "predict.py"}
        actual_files = {f.name for f in modeling_path.iterdir() if f.is_file()}

        assert expected_files == actual_files


class TestCookiecutterCustomNames:
    """Tests for cookiecutter with custom project names."""

    def test_converts_project_name_to_snake_case(self, tmp_path, template_dir):
        """Cookiecutter converts project name to snake_case for directory."""
        custom_name = "My Test Project"
        expected_dir = "my_test_project"

        result = subprocess.run(
            [
                "cookiecutter",
                str(template_dir),
                "--no-input",
                "-o",
                str(tmp_path),
                f"project_name={custom_name}",
            ],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0
        assert (tmp_path / expected_dir).is_dir()

    def test_creates_module_with_converted_name(self, tmp_path, template_dir):
        """Cookiecutter creates module directory with converted name."""
        custom_name = "My Test Project"
        expected_module = "my_test_project"

        subprocess.run(
            [
                "cookiecutter",
                str(template_dir),
                "--no-input",
                "-o",
                str(tmp_path),
                f"project_name={custom_name}",
            ],
            capture_output=True,
        )

        project_path = tmp_path / expected_module
        module_path = project_path / expected_module
        assert module_path.is_dir()
        assert (module_path / "__init__.py").is_file()


class TestCookiecutterFileContent:
    """Tests for cookiecutter generated file content."""

    def test_readme_contains_project_name(self, tmp_path, template_dir):
        """README.md contains the project name in header."""
        subprocess.run(
            [
                "cookiecutter",
                str(template_dir),
                "--no-input",
                "-o",
                str(tmp_path),
            ],
            capture_output=True,
        )

        readme_path = tmp_path / "project_name" / "README.md"
        content = readme_path.read_text()

        assert "# project_name" in content

    def test_pyproject_toml_is_valid(self, tmp_path, template_dir):
        """pyproject.toml is valid TOML and can be parsed."""
        try:
            import tomllib
        except ModuleNotFoundError:
            import tomli as tomllib

        subprocess.run(
            [
                "cookiecutter",
                str(template_dir),
                "--no-input",
                "-o",
                str(tmp_path),
            ],
            capture_output=True,
        )

        pyproject_path = tmp_path / "project_name" / "pyproject.toml"
        content = pyproject_path.read_text()
        parsed = tomllib.loads(content)

        assert "project" in parsed
        assert parsed["project"]["name"] == "project_name"
