"""Tests for NHS RAP Cookiecutter Template."""


def test_template_generates_successfully(cookies):
    """Test that the template generates successfully with default values."""
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "project_name"
    assert result.project_path.is_dir()


def test_template_has_required_files(cookies):
    """Test that generated project has all required files."""
    result = cookies.bake()

    assert result.exit_code == 0

    # Check for key files
    assert (result.project_path / "README.md").exists()
    assert (result.project_path / "pyproject.toml").exists()
    assert (result.project_path / "Makefile").exists()
    assert (result.project_path / ".gitignore").exists()
    assert (result.project_path / ".pre-commit-config.yaml").exists()


def test_template_has_required_directories(cookies):
    """Test that generated project has all required directories."""
    result = cookies.bake()

    assert result.exit_code == 0

    # Check for key directories
    assert (result.project_path / "data").is_dir()
    assert (result.project_path / "docs").is_dir()
    assert (result.project_path / "models").is_dir()
    assert (result.project_path / "notebooks").is_dir()
    assert (result.project_path / "references").is_dir()
    assert (result.project_path / "reports").is_dir()
    assert (result.project_path / "tests").is_dir()
    assert (result.project_path / "project_name").is_dir()


def test_template_with_uv_environment(cookies):
    """Test template generation with UV environment manager."""
    result = cookies.bake(extra_context={"environment_manager": "uv"})

    assert result.exit_code == 0
    makefile_content = (result.project_path / "Makefile").read_text()
    assert "uv venv" in makefile_content or "uv sync" in makefile_content


def test_template_with_pytest_framework(cookies):
    """Test template generation with pytest testing framework."""
    result = cookies.bake(extra_context={"testing_framework": "pytest"})

    assert result.exit_code == 0
    assert (result.project_path / "tests" / "pytest").is_dir()


def test_template_with_mit_license(cookies):
    """Test template generation with MIT license."""
    result = cookies.bake(extra_context={"open_source_license": "MIT"})

    assert result.exit_code == 0
    assert (result.project_path / "LICENSE").exists()
    license_content = (result.project_path / "LICENSE").read_text()
    assert "MIT" in license_content


def test_template_project_name_conversion(cookies):
    """Test that project name is correctly converted to repo and module names."""
    result = cookies.bake(extra_context={"project_name": "My Test Project"})

    assert result.exit_code == 0
    assert result.project_path.name == "my_test_project"

    # Check module directory exists with correct name
    assert (result.project_path / "my_test_project").is_dir()


def test_template_with_mkdocs_documentation(cookies):
    """Test template generation with mkdocs documentation."""
    result = cookies.bake(extra_context={"docs": "mkdocs"})

    assert result.exit_code == 0
    assert (result.project_path / "docs").is_dir()
    assert (result.project_path / "docs" / "content").is_dir()
    assert (result.project_path / "mkdocs.yml").is_file()
