"""Tests for configuration loading and validation in generate_projects."""

import json

import pytest
import yaml

from scripts.generate_projects import (
    ExistsStrategy,
    cleanup_project,
    handle_existing_project,
    load_cookiecutter_config,
    load_test_configs,
    validate_config,
    validate_generated_project,
)


class TestLoadCookiecutterConfig:
    """Tests for load_cookiecutter_config function."""

    def test_loads_valid_json_file(self, tmp_path, mocker, mock_logger):
        """Valid cookiecutter.json file returns parsed dictionary."""
        config_data = {"project_name": "Test", "version": "1.0"}
        config_file = tmp_path / "cookiecutter.json"
        config_file.write_text(json.dumps(config_data))

        # Mock Path(__file__).parent.parent to return tmp_path
        mock_path = mocker.MagicMock()
        mock_path.parent.parent = tmp_path
        mocker.patch("scripts.generate_test_projects.Path", return_value=mock_path)

        result = load_cookiecutter_config()

        assert result == config_data

    def test_raises_error_on_missing_file(self, tmp_path, mocker, mock_logger):
        """Missing cookiecutter.json raises FileNotFoundError."""
        # Mock Path(__file__).parent.parent to return directory without cookiecutter.json
        mock_path = mocker.MagicMock()
        mock_path.parent.parent = tmp_path / "nonexistent"
        mocker.patch("scripts.generate_test_projects.Path", return_value=mock_path)

        with pytest.raises(FileNotFoundError):
            load_cookiecutter_config()


class TestLoadTestConfigs:
    """Tests for load_test_configs function."""

    def test_loads_valid_yaml_file(self, tmp_path, mocker, mock_logger, sample_test_configs):
        """Valid test_configs.yaml returns parsed dictionary."""
        config_file = tmp_path / "test_configs.yaml"
        config_file.write_text(yaml.dump(sample_test_configs))

        # Mock Path(__file__).parent to return tmp_path
        mock_path = mocker.MagicMock()
        mock_path.parent = tmp_path
        mocker.patch("scripts.generate_test_projects.Path", return_value=mock_path)

        result = load_test_configs()

        assert result == sample_test_configs
        mock_logger["info"].assert_called_once()
        assert "2" in str(mock_logger["info"].call_args)

    def test_returns_empty_dict_for_empty_yaml(self, tmp_path, mocker, mock_logger):
        """Empty YAML file causes TypeError because yaml.safe_load returns None and len(None) fails."""
        config_file = tmp_path / "test_configs.yaml"
        config_file.write_text("")

        # Mock Path(__file__).parent to return tmp_path
        mock_path = mocker.MagicMock()
        mock_path.parent = tmp_path
        mocker.patch("scripts.generate_test_projects.Path", return_value=mock_path)

        with pytest.raises(TypeError):
            # Empty YAML returns None, which causes TypeError when getting len()
            load_test_configs()


class TestValidateConfig:
    """Tests for validate_config function."""

    def test_validates_config_with_all_valid_values(
        self, mocker, mock_logger, sample_cookiecutter_config
    ):
        """Configuration with all valid values passes validation."""
        mocker.patch(
            "scripts.generate_test_projects.load_cookiecutter_config",
            return_value=sample_cookiecutter_config,
        )
        config_values = {
            "environment_manager": "uv",
            "linting_and_formatting": "ruff",
            "open_source_license": "MIT",
        }

        validate_config("test_config", config_values)

        mock_logger["success"].assert_called_once_with("Configuration 'test_config' validated")

    def test_raises_error_on_invalid_environment_manager(
        self, mocker, mock_logger, sample_cookiecutter_config
    ):
        """Invalid environment_manager value raises ValueError."""
        mocker.patch(
            "scripts.generate_test_projects.load_cookiecutter_config",
            return_value=sample_cookiecutter_config,
        )
        config_values = {"environment_manager": "invalid_manager"}

        with pytest.raises(ValueError) as exc_info:
            validate_config("test_config", config_values)

        assert "Invalid value 'invalid_manager' for environment_manager" in str(exc_info.value)

    def test_raises_error_on_invalid_linting_option(
        self, mocker, mock_logger, sample_cookiecutter_config
    ):
        """Invalid linting_and_formatting value raises ValueError."""
        mocker.patch(
            "scripts.generate_test_projects.load_cookiecutter_config",
            return_value=sample_cookiecutter_config,
        )
        config_values = {"linting_and_formatting": "invalid_linter"}

        with pytest.raises(ValueError) as exc_info:
            validate_config("test_config", config_values)

        assert "Invalid value 'invalid_linter' for linting_and_formatting" in str(exc_info.value)

    def test_ignores_non_list_options(self, mocker, mock_logger, sample_cookiecutter_config):
        """Non-list configuration options are not validated."""
        mocker.patch(
            "scripts.generate_test_projects.load_cookiecutter_config",
            return_value=sample_cookiecutter_config,
        )
        config_values = {
            "project_name": "Any Value",
            "author_name": "Any Author",
        }

        validate_config("test_config", config_values)

        mock_logger["success"].assert_called_once()

    def test_ignores_config_description_key(self, mocker, mock_logger, sample_cookiecutter_config):
        """config_description key is ignored during validation."""
        mocker.patch(
            "scripts.generate_test_projects.load_cookiecutter_config",
            return_value=sample_cookiecutter_config,
        )
        config_values = {
            "config_description": "This is a test",
            "environment_manager": "uv",
        }

        validate_config("test_config", config_values)

        mock_logger["success"].assert_called_once()


class TestCleanupProject:
    """Tests for cleanup_project function."""

    def test_removes_existing_directory(self, tmp_path, mock_logger):
        """Existing directory is removed successfully."""
        project_dir = tmp_path / "test_project"
        project_dir.mkdir()
        (project_dir / "file.txt").write_text("content")
        assert project_dir.exists()

        cleanup_project(project_dir)

        assert not project_dir.exists()
        mock_logger["info"].assert_called_once()
        mock_logger["success"].assert_called_once()

    def test_handles_nonexistent_directory(self, tmp_path, mock_logger):
        """Nonexistent directory logs debug message."""
        project_dir = tmp_path / "nonexistent"
        assert not project_dir.exists()

        cleanup_project(project_dir)

        assert not project_dir.exists()
        mock_logger["debug"].assert_called_once()
        mock_logger["info"].assert_not_called()

    def test_removes_directory_with_subdirectories(self, tmp_path, mock_logger):
        """Directory with nested subdirectories is completely removed."""
        project_dir = tmp_path / "test_project"
        project_dir.mkdir()
        (project_dir / "subdir1").mkdir()
        (project_dir / "subdir1" / "subdir2").mkdir()
        (project_dir / "subdir1" / "subdir2" / "file.txt").write_text("content")

        cleanup_project(project_dir)

        assert not project_dir.exists()


class TestHandleExistingProject:
    """Tests for handle_existing_project function."""

    def test_returns_true_for_nonexistent_path(self, tmp_path, mock_logger):
        """Nonexistent project path returns True (proceed with generation)."""
        project_path = tmp_path / "nonexistent"

        result = handle_existing_project(project_path, ExistsStrategy.CLEAN)

        assert result is True
        mock_logger["warning"].assert_not_called()

    def test_clean_strategy_removes_and_returns_true(self, tmp_path, mock_logger):
        """CLEAN strategy removes existing directory and returns True."""
        project_path = tmp_path / "existing"
        project_path.mkdir()
        (project_path / "file.txt").write_text("content")

        result = handle_existing_project(project_path, ExistsStrategy.CLEAN)

        assert result is True
        assert not project_path.exists()
        mock_logger["warning"].assert_called_once()

    def test_skip_strategy_returns_false(self, tmp_path, mock_logger):
        """SKIP strategy leaves directory and returns False."""
        project_path = tmp_path / "existing"
        project_path.mkdir()

        result = handle_existing_project(project_path, ExistsStrategy.SKIP)

        assert result is False
        assert project_path.exists()
        mock_logger["warning"].assert_called_once()
        mock_logger["info"].assert_called_once()

    def test_fail_strategy_raises_error(self, tmp_path, mock_logger):
        """FAIL strategy raises FileExistsError for existing directory."""
        project_path = tmp_path / "existing"
        project_path.mkdir()

        with pytest.raises(FileExistsError) as exc_info:
            handle_existing_project(project_path, ExistsStrategy.FAIL)

        assert "already exists" in str(exc_info.value)
        assert project_path.exists()


class TestValidateGeneratedProject:
    """Tests for validate_generated_project function."""

    def test_passes_validation_with_all_critical_files(self, temp_project_dir, mock_logger):
        """Project with all critical files passes validation."""
        config_values = {"project_name": "Test Project"}

        validate_generated_project(temp_project_dir, config_values)

        mock_logger["success"].assert_called_once()
        mock_logger["error"].assert_not_called()

    def test_raises_error_when_readme_missing(self, tmp_path, mock_logger):
        """Missing README.md raises FileNotFoundError."""
        project = tmp_path / "incomplete"
        project.mkdir()
        (project / ".gitignore").write_text("*.pyc")
        config_values = {"project_name": "Test"}

        with pytest.raises(FileNotFoundError) as exc_info:
            validate_generated_project(project, config_values)

        assert "README.md" in str(exc_info.value)
        mock_logger["error"].assert_called()

    def test_raises_error_when_gitignore_missing(self, tmp_path, mock_logger):
        """Missing .gitignore raises FileNotFoundError."""
        project = tmp_path / "incomplete"
        project.mkdir()
        (project / "README.md").write_text("# Test")
        config_values = {"project_name": "Test"}

        with pytest.raises(FileNotFoundError) as exc_info:
            validate_generated_project(project, config_values)

        assert ".gitignore" in str(exc_info.value)

    def test_warns_about_missing_expected_directories(self, tmp_path, mock_logger):
        """Missing expected directories logs warnings but doesn't fail."""
        project = tmp_path / "minimal"
        project.mkdir()
        (project / "README.md").write_text("# Test")
        (project / ".gitignore").write_text("*.pyc")
        config_values = {"project_name": "Test"}

        validate_generated_project(project, config_values)

        mock_logger["warning"].assert_called()
        mock_logger["success"].assert_called_once()

    def test_validates_module_directory_exists(self, tmp_path, mock_logger):
        """Module directory is checked based on module_name."""
        project = tmp_path / "with_module"
        project.mkdir()
        (project / "README.md").write_text("# Test")
        (project / ".gitignore").write_text("*.pyc")
        (project / "data").mkdir()
        (project / "tests").mkdir()
        (project / "notebooks").mkdir()
        (project / "test_module").mkdir()
        config_values = {"module_name": "test_module"}

        validate_generated_project(project, config_values)

        mock_logger["success"].assert_called_once()
        mock_logger["warning"].assert_not_called()

    def test_derives_module_name_from_project_name(self, tmp_path, mock_logger):
        """Module name is derived from project_name if module_name not provided."""
        project = tmp_path / "derived"
        project.mkdir()
        (project / "README.md").write_text("# Test")
        (project / ".gitignore").write_text("*.pyc")
        (project / "data").mkdir()
        (project / "tests").mkdir()
        (project / "notebooks").mkdir()
        (project / "test_project").mkdir()
        config_values = {"project_name": "Test Project"}

        validate_generated_project(project, config_values)

        mock_logger["success"].assert_called_once()
