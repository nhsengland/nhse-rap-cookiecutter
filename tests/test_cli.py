"""Tests for the NHS RAP Template CLI wrapper."""

import subprocess
from pathlib import Path


class TestCLIHelp:
    """Tests for the nhs-rap-template CLI help command."""

    def test_displays_help_message(self):
        """--help flag displays help message."""
        result = subprocess.run(
            ["uv", "run", "nhs-rap-template", "--help"],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0
        assert "Generate a new NHS RAP project" in result.stdout

    def test_lists_checkout_option(self):
        """--help lists --checkout option."""
        result = subprocess.run(
            ["uv", "run", "nhs-rap-template", "--help"],
            capture_output=True,
            text=True,
        )

        assert "--checkout" in result.stdout

    def test_lists_no_input_option(self):
        """--help lists --no-input option."""
        result = subprocess.run(
            ["uv", "run", "nhs-rap-template", "--help"],
            capture_output=True,
            text=True,
        )

        assert "--no-input" in result.stdout


class TestCLIProjectGeneration:
    """Tests for the nhs-rap-template project generation."""

    def test_generates_project_directory(self, tmp_path):
        """CLI creates project directory with correct name."""
        output_dir = tmp_path / "output"
        output_dir.mkdir()

        result = subprocess.run(
            [
                "uv",
                "run",
                "nhs-rap-template",
                "--no-input",
                "-o",
                str(output_dir),
            ],
            capture_output=True,
            text=True,
            cwd=Path.cwd(),
        )

        assert result.returncode == 0
        assert (output_dir / "project_name").is_dir()

    def test_generates_exact_required_files(self, tmp_path):
        """CLI generates exactly the expected root-level files."""
        output_dir = tmp_path / "output"
        output_dir.mkdir()

        subprocess.run(
            [
                "uv",
                "run",
                "nhs-rap-template",
                "--no-input",
                "-o",
                str(output_dir),
            ],
            capture_output=True,
            cwd=Path.cwd(),
        )

        project_path = output_dir / "project_name"
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

    def test_generates_exact_required_directories(self, tmp_path):
        """CLI generates exactly the expected root-level directories."""
        output_dir = tmp_path / "output"
        output_dir.mkdir()

        subprocess.run(
            [
                "uv",
                "run",
                "nhs-rap-template",
                "--no-input",
                "-o",
                str(output_dir),
            ],
            capture_output=True,
            cwd=Path.cwd(),
        )

        project_path = output_dir / "project_name"
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

    def test_respects_custom_output_directory(self, tmp_path):
        """CLI creates project in specified output directory."""
        custom_dir = tmp_path / "custom" / "nested" / "path"
        custom_dir.mkdir(parents=True)

        result = subprocess.run(
            [
                "uv",
                "run",
                "nhs-rap-template",
                "--no-input",
                "-o",
                str(custom_dir),
            ],
            capture_output=True,
            text=True,
            cwd=Path.cwd(),
        )

        assert result.returncode == 0
        assert (custom_dir / "project_name").is_dir()
        assert (custom_dir / "project_name" / "README.md").is_file()


class TestCLIModuleStructure:
    """Tests for the Python module structure created by CLI."""

    def test_creates_exact_module_files(self, tmp_path):
        """CLI creates exactly the expected module files."""
        output_dir = tmp_path / "output"
        output_dir.mkdir()

        subprocess.run(
            [
                "uv",
                "run",
                "nhs-rap-template",
                "--no-input",
                "-o",
                str(output_dir),
            ],
            capture_output=True,
            cwd=Path.cwd(),
        )

        module_path = output_dir / "project_name" / "project_name"
        expected_files = {
            "__init__.py",
            "config.py",
            "dataset.py",
            "features.py",
            "plots.py",
        }
        actual_files = {f.name for f in module_path.iterdir() if f.is_file()}

        assert expected_files == actual_files

    def test_creates_modeling_submodule(self, tmp_path):
        """CLI creates modeling submodule with correct structure."""
        output_dir = tmp_path / "output"
        output_dir.mkdir()

        subprocess.run(
            [
                "uv",
                "run",
                "nhs-rap-template",
                "--no-input",
                "-o",
                str(output_dir),
            ],
            capture_output=True,
            cwd=Path.cwd(),
        )

        modeling_path = output_dir / "project_name" / "project_name" / "modeling"
        expected_files = {"__init__.py", "train.py", "predict.py"}
        actual_files = {f.name for f in modeling_path.iterdir() if f.is_file()}

        assert expected_files == actual_files
