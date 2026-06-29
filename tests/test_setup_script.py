"""Tests for setup_repository.py script in generated projects."""

import pytest


class TestSetupScript:
    """Tests for setup script generation and functionality."""

    def test_setup_script_exists(self, cookies):
        """Setup script is created in generated project."""
        result = cookies.bake()

        assert result.exit_code == 0
        setup_script = result.project_path / "scripts" / "setup_repository.py"
        assert setup_script.exists()

    def test_setup_script_is_executable(self, cookies):
        """Setup script has correct shebang."""
        result = cookies.bake()

        assert result.exit_code == 0
        setup_script = result.project_path / "scripts" / "setup_repository.py"
        content = setup_script.read_text()
        assert content.startswith("#!/usr/bin/env python3")

    def test_setup_script_includes_project_name(self, cookies):
        """Setup script includes the project name."""
        result = cookies.bake(extra_context={"project_name": "Test Project"})

        assert result.exit_code == 0
        setup_script = result.project_path / "scripts" / "setup_repository.py"
        content = setup_script.read_text()
        assert "Test Project" in content

    def test_setup_script_includes_repository_url(self, cookies):
        """Setup script includes the repository URL."""
        test_url = "https://github.com/test/test-repo"
        result = cookies.bake(extra_context={"repository_url": test_url})

        assert result.exit_code == 0
        setup_script = result.project_path / "scripts" / "setup_repository.py"
        content = setup_script.read_text()
        assert test_url in content

    def test_setup_script_includes_environment_manager(self, cookies):
        """Setup script references the selected environment manager."""
        result = cookies.bake(extra_context={"environment_manager": "uv"})

        assert result.exit_code == 0
        setup_script = result.project_path / "scripts" / "setup_repository.py"
        content = setup_script.read_text()
        assert "uv" in content

    def test_setup_script_syntax_is_valid(self, cookies):
        """Setup script has valid Python syntax."""
        result = cookies.bake()

        assert result.exit_code == 0
        setup_script = result.project_path / "scripts" / "setup_repository.py"

        # Check syntax by compiling
        content = setup_script.read_text()
        try:
            compile(content, str(setup_script), "exec")
        except SyntaxError as e:
            pytest.fail(f"Setup script has invalid syntax: {e}")


class TestSetupScriptForEnvironmentManagers:
    """Tests for setup script with different environment managers."""

    @pytest.mark.parametrize(
        "env_manager",
        ["uv", "venv", "conda"],
    )
    def test_setup_script_handles_environment_manager(self, cookies, env_manager):
        """Setup script includes logic for each environment manager."""
        result = cookies.bake(extra_context={"environment_manager": env_manager})

        assert result.exit_code == 0
        setup_script = result.project_path / "scripts" / "setup_repository.py"
        content = setup_script.read_text()

        assert env_manager in content


class TestSetupScriptDocumentation:
    """Tests for setup script documentation strings."""

    def test_setup_script_has_module_docstring(self, cookies):
        """Setup script has a module-level docstring."""
        result = cookies.bake()

        assert result.exit_code == 0
        setup_script = result.project_path / "scripts" / "setup_repository.py"
        content = setup_script.read_text()
        assert '"""Repository setup script' in content

    def test_setup_script_functions_have_docstrings(self, cookies):
        """Setup script functions have docstrings."""
        result = cookies.bake()

        assert result.exit_code == 0
        setup_script = result.project_path / "scripts" / "setup_repository.py"
        content = setup_script.read_text()

        # Check key functions have docstrings
        assert "def setup_git_repository()" in content
        assert '"""Initialize git repository' in content

        assert "def setup_environment()" in content
        assert '"""Set up Python environment' in content

        assert "def setup_precommit()" in content
        assert '"""Install pre-commit hooks' in content
