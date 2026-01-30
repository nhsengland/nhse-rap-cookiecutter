"""Tests for new setup_repository.py features: colors, status tracking, error handling."""


class TestSetupScriptColorSupport:
    """Tests for colored terminal output."""

    def test_setup_script_has_color_class(self, cookies):
        """Setup script defines Colors class for ANSI codes."""
        result = cookies.bake()

        assert result.exit_code == 0
        setup_script = result.project_path / "scripts" / "setup_repository.py"
        content = setup_script.read_text()
        assert "class Colors:" in content
        assert "GREEN =" in content
        assert "YELLOW =" in content
        assert "RED =" in content
        assert "RESET =" in content

    def test_setup_script_uses_colored_output(self, cookies):
        """Setup script uses colored output for status messages."""
        result = cookies.bake()

        assert result.exit_code == 0
        setup_script = result.project_path / "scripts" / "setup_repository.py"
        content = setup_script.read_text()
        # Check for colored checkmarks and status messages
        assert "Colors.GREEN" in content
        assert "Colors.YELLOW" in content
        assert "Colors.RED" in content


class TestSetupScriptStatusTracking:
    """Tests for status tracking functionality."""

    def test_setup_script_has_status_class(self, cookies):
        """Setup script defines SetupStatus class."""
        result = cookies.bake()

        assert result.exit_code == 0
        setup_script = result.project_path / "scripts" / "setup_repository.py"
        content = setup_script.read_text()
        assert "class SetupStatus:" in content
        assert "git_init" in content
        assert "git_remote" in content
        assert "environment" in content
        assert "dependencies" in content
        assert "precommit" in content
        assert "initial_commit" in content

    def test_setup_script_creates_status_instance(self, cookies):
        """Setup script creates a global status instance."""
        result = cookies.bake()

        assert result.exit_code == 0
        setup_script = result.project_path / "scripts" / "setup_repository.py"
        content = setup_script.read_text()
        assert "status = SetupStatus()" in content


class TestSetupScriptErrorHandling:
    """Tests for error handling and graceful failures."""

    def test_setup_script_has_setup_error_exception(self, cookies):
        """Setup script defines SetupError exception."""
        result = cookies.bake()

        assert result.exit_code == 0
        setup_script = result.project_path / "scripts" / "setup_repository.py"
        content = setup_script.read_text()
        assert "class SetupError(Exception):" in content

    def test_setup_script_wraps_steps_in_try_except(self, cookies):
        """Setup script wraps each step in try-except blocks."""
        result = cookies.bake()

        assert result.exit_code == 0
        setup_script = result.project_path / "scripts" / "setup_repository.py"
        content = setup_script.read_text()
        # Check that main function has try-except for each step
        assert "# Step 1: Git initialization" in content
        assert "# Step 2: Git remote setup" in content
        assert "# Step 3: Environment setup" in content
        assert "# Step 4: Dependencies" in content
        assert "# Step 5: Pre-commit hooks" in content
        assert "# Step 6: Initial commit" in content
        assert "except SetupError" in content
        assert "except subprocess.CalledProcessError" in content

    def test_setup_script_skips_dependent_steps_on_env_failure(self, cookies):
        """Setup script skips remaining steps if environment fails."""
        result = cookies.bake()

        assert result.exit_code == 0
        setup_script = result.project_path / "scripts" / "setup_repository.py"
        content = setup_script.read_text()
        assert "Skipping remaining steps that require the environment" in content
        assert "print_next_steps()" in content
        assert "return" in content

    def test_setup_script_always_shows_summary(self, cookies):
        """Setup script always shows next steps even on failure."""
        result = cookies.bake()

        assert result.exit_code == 0
        setup_script = result.project_path / "scripts" / "setup_repository.py"
        content = setup_script.read_text()
        # print_next_steps should be called in success path and error paths
        assert content.count("print_next_steps()") >= 2


class TestSetupScriptSummary:
    """Tests for setup summary output."""

    def test_setup_script_has_format_status_function(self, cookies):
        """Setup script has function to format status with colors."""
        result = cookies.bake()

        assert result.exit_code == 0
        setup_script = result.project_path / "scripts" / "setup_repository.py"
        content = setup_script.read_text()
        assert "def format_status(" in content
        assert "Success" in content
        assert "Skipped" in content
        assert "Warning" in content
        assert "Failed" in content

    def test_setup_script_shows_detailed_summary(self, cookies):
        """Setup script prints detailed summary of all steps."""
        result = cookies.bake()

        assert result.exit_code == 0
        setup_script = result.project_path / "scripts" / "setup_repository.py"
        content = setup_script.read_text()
        assert "SETUP SUMMARY" in content
        assert "Setup Steps:" in content
        assert "Overall Status:" in content
        assert "format_status(status." in content


class TestSetupScriptRemoteWarning:
    """Tests for clear remote repository warnings."""

    def test_setup_script_has_clear_remote_warning(self, cookies):
        """Setup script shows clear warning when remote doesn't exist."""
        result = cookies.bake()

        assert result.exit_code == 0
        setup_script = result.project_path / "scripts" / "setup_repository.py"
        content = setup_script.read_text()
        assert "REMOTE REPOSITORY DOES NOT EXIST YET" in content
        assert "This is normal for new projects!" in content
        assert "BEFORE YOU CAN PUSH, you must:" in content

    def test_setup_script_provides_remote_creation_steps(self, cookies):
        """Setup script gives step-by-step instructions for creating remote."""
        result = cookies.bake()

        assert result.exit_code == 0
        setup_script = result.project_path / "scripts" / "setup_repository.py"
        content = setup_script.read_text()
        assert "Go to your git hosting platform" in content
        assert "DO NOT initialize with README" in content
        assert "git push -u origin main" in content


class TestSetupScriptPrecommitMessaging:
    """Tests for clear pre-commit failure explanations."""

    def test_setup_script_explains_precommit_failures(self, cookies):
        """Setup script explains that pre-commit failures are expected."""
        result = cookies.bake()

        assert result.exit_code == 0
        setup_script = result.project_path / "scripts" / "setup_repository.py"
        content = setup_script.read_text()
        assert "RUNNING PRE-COMMIT HOOKS - FAILURES ARE EXPECTED AND NORMAL!" in content
        assert "cookiecutter template generates files with minor formatting issues" in content
        assert '"Failed" means the hooks found and fixed formatting issues' in content
        assert "working correctly!" in content
