"""Tests for dependency file generation based on environment manager."""

import pytest


class TestDependencyFileGeneration:
    """Test that correct dependency files are created based on environment manager."""

    @pytest.mark.parametrize(
        "env_manager,expected_file",
        [
            ("virtualenv", "pyproject.toml"),
            ("uv", "pyproject.toml"),
            ("poetry", "pyproject.toml"),
            ("pixi", "pyproject.toml"),
            ("pipenv", "pyproject.toml"),
            ("none", "pyproject.toml"),
            ("conda", "environment.yml"),
        ],
    )
    def test_creates_correct_dependency_file(self, cookies, env_manager, expected_file):
        """Environment manager creates expected dependency file."""
        result = cookies.bake(extra_context={"environment_manager": env_manager})

        assert result.exit_code == 0
        assert (result.project_path / expected_file).exists()

    @pytest.mark.parametrize(
        "env_manager", ["virtualenv", "uv", "poetry", "pixi", "pipenv", "none"]
    )
    def test_pyproject_managers_do_not_create_environment_yml(self, cookies, env_manager):
        """Pyproject.toml managers should not create environment.yml."""
        result = cookies.bake(extra_context={"environment_manager": env_manager})

        assert not (result.project_path / "environment.yml").exists()

    def test_conda_does_not_create_pyproject_toml(self, cookies):
        """Conda should not create pyproject.toml."""
        result = cookies.bake(extra_context={"environment_manager": "conda"})

        assert not (result.project_path / "pyproject.toml").exists()


class TestPyprojectTomlContent:
    """Test pyproject.toml content."""

    @pytest.mark.parametrize(
        "package",
        [
            "ipython",
            "jupyterlab",
            "loguru",
            "matplotlib",
            "notebook",
            "numpy",
            "openpyxl",
            "pandas",
            "plotly",
            "requests",
            "scikit-learn",
            "scipy",
            "seaborn",
            "tqdm",
        ],
    )
    def test_core_dependency_present(self, cookies, package):
        """Core runtime dependency should be in pyproject.toml."""
        result = cookies.bake(extra_context={"environment_manager": "uv"})

        content = (result.project_path / "pyproject.toml").read_text()
        assert package in content

    @pytest.mark.parametrize("package", ["pytest", "pytest-cov", "pre-commit"])
    def test_dev_dependency_present(self, cookies, package):
        """Dev dependency should be in pyproject.toml."""
        result = cookies.bake(extra_context={"environment_manager": "uv"})

        content = (result.project_path / "pyproject.toml").read_text()
        assert package in content

    def test_ruff_present_when_selected(self, cookies):
        """Ruff should be in pyproject.toml when selected."""
        result = cookies.bake(
            extra_context={"environment_manager": "uv", "linting_and_formatting": "ruff"}
        )

        content = (result.project_path / "pyproject.toml").read_text()
        assert "ruff" in content

    @pytest.mark.parametrize("package", ["flake8", "black", "isort"])
    def test_old_linting_tools_present_when_selected(self, cookies, package):
        """Old linting tools should be in pyproject.toml when selected."""
        result = cookies.bake(
            extra_context={
                "environment_manager": "uv",
                "linting_and_formatting": "flake8+black+isort",
            }
        )

        content = (result.project_path / "pyproject.toml").read_text()
        assert package in content

    def test_ruff_not_present_with_old_linting(self, cookies):
        """Ruff should not be present when flake8+black+isort selected."""
        result = cookies.bake(
            extra_context={
                "environment_manager": "uv",
                "linting_and_formatting": "flake8+black+isort",
            }
        )

        content = (result.project_path / "pyproject.toml").read_text()
        assert "ruff" not in content

    @pytest.mark.parametrize("package", ["mkdocs", "mkdocs-material", "mkdocstrings"])
    def test_docs_dependency_present_when_enabled(self, cookies, package):
        """Docs dependency should be present when docs enabled."""
        result = cookies.bake(extra_context={"environment_manager": "uv", "docs": "mkdocs"})

        content = (result.project_path / "pyproject.toml").read_text()
        assert package in content

    def test_mkdocs_not_present_when_disabled(self, cookies):
        """mkdocs should not be present when docs disabled."""
        result = cookies.bake(extra_context={"environment_manager": "uv", "docs": "none"})

        content = (result.project_path / "pyproject.toml").read_text()
        assert "mkdocs" not in content


class TestEnvironmentYmlContent:
    """Test environment.yml content."""

    @pytest.mark.parametrize(
        "package",
        [
            "pandas",
            "numpy",
            "matplotlib",
            "seaborn",
            "loguru",
            "tqdm",
            "jupyterlab",
            "notebook",
            "ipython",
            "pytest",
        ],
    )
    def test_package_present(self, cookies, package):
        """Package should be in environment.yml."""
        result = cookies.bake(extra_context={"environment_manager": "conda"})

        content = (result.project_path / "environment.yml").read_text()
        assert package in content

    def test_python_version_specified(self, cookies):
        """Python version should be specified in environment.yml."""
        result = cookies.bake(
            extra_context={"environment_manager": "conda", "python_version_number": "3.11"}
        )

        content = (result.project_path / "environment.yml").read_text()
        assert "python=3.11" in content
