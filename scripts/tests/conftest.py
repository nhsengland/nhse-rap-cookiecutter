"""Shared pytest fixtures for generate_test_projects tests."""

import pytest


@pytest.fixture
def mock_logger(mocker):
    """Mock all loguru logger levels.

    Returns
    -------
    dict
        Dictionary with keys: info, warning, error, success, debug
        Each value is a MagicMock for that logger level
    """
    return {
        "info": mocker.patch("scripts.generate_test_projects.logger.info"),
        "warning": mocker.patch("scripts.generate_test_projects.logger.warning"),
        "error": mocker.patch("scripts.generate_test_projects.logger.error"),
        "success": mocker.patch("scripts.generate_test_projects.logger.success"),
        "debug": mocker.patch("scripts.generate_test_projects.logger.debug"),
    }


@pytest.fixture
def sample_cookiecutter_config():
    """Sample cookiecutter.json configuration for testing.

    Returns
    -------
    dict
        Minimal cookiecutter configuration with list options
    """
    return {
        "project_name": "Test Project",
        "environment_manager": ["uv", "conda", "poetry", "none"],
        "linting_and_formatting": ["ruff", "flake8+black+isort"],
        "open_source_license": ["MIT", "BSD-3-Clause", "No license file"],
        "docs": ["yes", "no"],
        "include_code_scaffold": ["yes", "no"],
    }


@pytest.fixture
def sample_test_configs():
    """Sample test_configs.yaml data for testing.

    Returns
    -------
    dict
        Dictionary of test configuration name to configuration values
    """
    return {
        "minimal": {
            "project_name": "Minimal Project",
            "environment_manager": "uv",
            "linting_and_formatting": "ruff",
            "config_description": "Minimal test config",
        },
        "full": {
            "project_name": "Full Project",
            "environment_manager": "conda",
            "docs": "yes",
            "config_description": "Full test config",
        },
    }


@pytest.fixture
def temp_project_dir(tmp_path):
    """Create a temporary project directory with basic structure.

    Parameters
    ----------
    tmp_path : Path
        Pytest's tmp_path fixture

    Returns
    -------
    Path
        Path to temporary project directory with README.md and .gitignore
    """
    project = tmp_path / "test_project"
    project.mkdir()
    (project / "README.md").write_text("# Test Project")
    (project / ".gitignore").write_text("*.pyc\n")
    (project / "data").mkdir()
    (project / "tests").mkdir()
    (project / "notebooks").mkdir()
    return project
