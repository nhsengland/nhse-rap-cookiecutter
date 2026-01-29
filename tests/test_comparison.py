"""Tests comparing CLI wrapper and direct cookiecutter usage."""

import subprocess
from pathlib import Path

import pytest


@pytest.fixture(scope="class")
def generated_projects(tmp_path_factory):
    """Generate projects using both CLI and cookiecutter.

    Returns
    -------
    tuple[Path, Path]
        Tuple of (cli_project_path, cookiecutter_project_path)
    """
    tmp_path = tmp_path_factory.mktemp("comparison")
    cli_output = tmp_path / "cli"
    cc_output = tmp_path / "cc"
    cli_output.mkdir()
    cc_output.mkdir()

    template_dir = Path.cwd()

    # Generate with CLI wrapper
    cli_result = subprocess.run(
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
        text=True,
        cwd=template_dir,
    )
    assert cli_result.returncode == 0, f"CLI generation failed: {cli_result.stderr}"

    # Generate with cookiecutter
    cc_result = subprocess.run(
        [
            "cookiecutter",
            str(template_dir),
            "--no-input",
            "-o",
            str(cc_output),
        ],
        capture_output=True,
        text=True,
    )
    assert cc_result.returncode == 0, f"Cookiecutter generation failed: {cc_result.stderr}"

    return cli_output / "project_name", cc_output / "project_name"


class TestMethodComparison:
    """Tests comparing CLI wrapper vs direct cookiecutter output."""

    def test_produce_identical_file_structure(self, generated_projects):
        """Both methods create identical set of files."""
        cli_project, cc_project = generated_projects

        # Get all files recursively
        cli_files = {
            str(p.relative_to(cli_project)) for p in cli_project.rglob("*") if p.is_file()
        }
        cc_files = {str(p.relative_to(cc_project)) for p in cc_project.rglob("*") if p.is_file()}

        assert cli_files == cc_files

    def test_produce_identical_readme_content(self, generated_projects):
        """Both methods generate identical README.md content."""
        cli_project, cc_project = generated_projects

        cli_readme = (cli_project / "README.md").read_text()
        cc_readme = (cc_project / "README.md").read_text()

        assert cli_readme == cc_readme

    def test_produce_identical_pyproject_content(self, generated_projects):
        """Both methods generate identical pyproject.toml content."""
        cli_project, cc_project = generated_projects

        cli_pyproject = (cli_project / "pyproject.toml").read_text()
        cc_pyproject = (cc_project / "pyproject.toml").read_text()

        assert cli_pyproject == cc_pyproject

    def test_produce_identical_makefile_content(self, generated_projects):
        """Both methods generate identical Makefile content."""
        cli_project, cc_project = generated_projects

        cli_makefile = (cli_project / "Makefile").read_text()
        cc_makefile = (cc_project / "Makefile").read_text()

        assert cli_makefile == cc_makefile

    def test_produce_identical_precommit_content(self, generated_projects):
        """Both methods generate identical .pre-commit-config.yaml content."""
        cli_project, cc_project = generated_projects

        cli_precommit = (cli_project / ".pre-commit-config.yaml").read_text()
        cc_precommit = (cc_project / ".pre-commit-config.yaml").read_text()

        assert cli_precommit == cc_precommit
