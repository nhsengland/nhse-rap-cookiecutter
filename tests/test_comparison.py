"""Tests comparing CLI wrapper and direct cookiecutter usage."""

import subprocess
from pathlib import Path


class TestMethodComparison:
    """Tests comparing CLI wrapper vs direct cookiecutter output."""

    def test_produce_identical_file_structure(self, tmp_path):
        """Both methods create identical set of files."""
        cli_output = tmp_path / "cli"
        cc_output = tmp_path / "cc"
        cli_output.mkdir()
        cc_output.mkdir()

        template_dir = Path.cwd()

        # Generate with CLI wrapper
        subprocess.run(
            [
                "uv",
                "run",
                "nhs-rap-template",
                str(template_dir),
                "--no-input",
                "-o",
                str(cli_output),
            ],
            capture_output=True,
            cwd=template_dir,
        )

        # Generate with cookiecutter
        subprocess.run(
            [
                "cookiecutter",
                str(template_dir),
                "--no-input",
                "-o",
                str(cc_output),
            ],
            capture_output=True,
        )

        # Get all files recursively
        cli_files = {
            str(p.relative_to(cli_output / "project_name"))
            for p in (cli_output / "project_name").rglob("*")
            if p.is_file()
        }
        cc_files = {
            str(p.relative_to(cc_output / "project_name"))
            for p in (cc_output / "project_name").rglob("*")
            if p.is_file()
        }

        assert cli_files == cc_files

    def test_produce_identical_readme_content(self, tmp_path):
        """Both methods generate identical README.md content."""
        cli_output = tmp_path / "cli"
        cc_output = tmp_path / "cc"
        cli_output.mkdir()
        cc_output.mkdir()

        template_dir = Path.cwd()

        subprocess.run(
            [
                "uv",
                "run",
                "nhs-rap-template",
                str(template_dir),
                "--no-input",
                "-o",
                str(cli_output),
            ],
            capture_output=True,
            cwd=template_dir,
        )

        subprocess.run(
            [
                "cookiecutter",
                str(template_dir),
                "--no-input",
                "-o",
                str(cc_output),
            ],
            capture_output=True,
        )

        cli_readme = (cli_output / "project_name" / "README.md").read_text()
        cc_readme = (cc_output / "project_name" / "README.md").read_text()

        assert cli_readme == cc_readme

    def test_produce_identical_pyproject_content(self, tmp_path):
        """Both methods generate identical pyproject.toml content."""
        cli_output = tmp_path / "cli"
        cc_output = tmp_path / "cc"
        cli_output.mkdir()
        cc_output.mkdir()

        template_dir = Path.cwd()

        subprocess.run(
            [
                "uv",
                "run",
                "nhs-rap-template",
                str(template_dir),
                "--no-input",
                "-o",
                str(cli_output),
            ],
            capture_output=True,
            cwd=template_dir,
        )

        subprocess.run(
            [
                "cookiecutter",
                str(template_dir),
                "--no-input",
                "-o",
                str(cc_output),
            ],
            capture_output=True,
        )

        cli_pyproject = (cli_output / "project_name" / "pyproject.toml").read_text()
        cc_pyproject = (cc_output / "project_name" / "pyproject.toml").read_text()

        assert cli_pyproject == cc_pyproject

    def test_produce_identical_makefile_content(self, tmp_path):
        """Both methods generate identical Makefile content."""
        cli_output = tmp_path / "cli"
        cc_output = tmp_path / "cc"
        cli_output.mkdir()
        cc_output.mkdir()

        template_dir = Path.cwd()

        subprocess.run(
            [
                "uv",
                "run",
                "nhs-rap-template",
                str(template_dir),
                "--no-input",
                "-o",
                str(cli_output),
            ],
            capture_output=True,
            cwd=template_dir,
        )

        subprocess.run(
            [
                "cookiecutter",
                str(template_dir),
                "--no-input",
                "-o",
                str(cc_output),
            ],
            capture_output=True,
        )

        cli_makefile = (cli_output / "project_name" / "Makefile").read_text()
        cc_makefile = (cc_output / "project_name" / "Makefile").read_text()

        assert cli_makefile == cc_makefile

    def test_produce_identical_precommit_content(self, tmp_path):
        """Both methods generate identical .pre-commit-config.yaml content."""
        cli_output = tmp_path / "cli"
        cc_output = tmp_path / "cc"
        cli_output.mkdir()
        cc_output.mkdir()

        template_dir = Path.cwd()

        subprocess.run(
            [
                "uv",
                "run",
                "nhs-rap-template",
                str(template_dir),
                "--no-input",
                "-o",
                str(cli_output),
            ],
            capture_output=True,
            cwd=template_dir,
        )

        subprocess.run(
            [
                "cookiecutter",
                str(template_dir),
                "--no-input",
                "-o",
                str(cc_output),
            ],
            capture_output=True,
        )

        cli_precommit = (cli_output / "project_name" / ".pre-commit-config.yaml").read_text()
        cc_precommit = (cc_output / "project_name" / ".pre-commit-config.yaml").read_text()

        assert cli_precommit == cc_precommit
