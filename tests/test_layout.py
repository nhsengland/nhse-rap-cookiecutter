"""Tests for the flat vs src project layout option."""


class TestFlatLayout:
    """The default flat layout keeps the package at the project root."""

    def test_module_at_root_by_default(self, cookies):
        """By default the importable package lives at the project root."""
        result = cookies.bake(extra_context={"project_name": "My Project"})

        assert result.exit_code == 0
        assert (result.project_path / "my_project").is_dir()
        assert not (result.project_path / "src").exists()

    def test_module_at_root_when_flat(self, cookies):
        """Explicit flat layout keeps the package at the project root."""
        result = cookies.bake(extra_context={"project_name": "My Project", "layout": "flat"})

        assert result.exit_code == 0
        assert (result.project_path / "my_project" / "__init__.py").is_file()
        assert not (result.project_path / "src").exists()


class TestSrcLayout:
    """The src layout nests the package under src/."""

    def test_module_under_src(self, cookies):
        """src layout moves the package under src/."""
        result = cookies.bake(extra_context={"project_name": "My Project", "layout": "src"})

        assert result.exit_code == 0
        assert (result.project_path / "src" / "my_project" / "__init__.py").is_file()
        assert not (result.project_path / "my_project").exists()

    def test_modeling_submodule_under_src(self, cookies):
        """Nested submodules are preserved under the src layout."""
        result = cookies.bake(extra_context={"project_name": "My Project", "layout": "src"})

        assert result.exit_code == 0
        modeling = result.project_path / "src" / "my_project" / "modeling"
        assert (modeling / "train.py").is_file()
        assert (modeling / "predict.py").is_file()

    def test_src_dir_present_without_scaffold(self, cookies):
        """src/ is still created (as a placeholder) when no scaffold is included."""
        result = cookies.bake(extra_context={"layout": "src", "include_code_scaffold": "No"})

        assert result.exit_code == 0
        assert (result.project_path / "src").is_dir()


class TestLayoutAwareConfig:
    """Tooling references the correct package path for each layout."""

    def test_ruff_src_points_to_src_layout(self, cookies):
        """ruff `src` setting points at src/ for the src layout."""
        result = cookies.bake(
            extra_context={
                "project_name": "My Project",
                "layout": "src",
                "linting_and_formatting": "ruff",
            }
        )

        assert result.exit_code == 0
        content = (result.project_path / "pyproject.toml").read_text()
        assert 'src = ["src"]' in content

    def test_ruff_src_points_to_module_for_flat(self, cookies):
        """ruff `src` setting points at the module for the flat layout."""
        result = cookies.bake(
            extra_context={
                "project_name": "My Project",
                "layout": "flat",
                "linting_and_formatting": "ruff",
            }
        )

        assert result.exit_code == 0
        content = (result.project_path / "pyproject.toml").read_text()
        assert 'src = ["my_project"]' in content

    def test_makefile_module_path_uses_src(self, cookies):
        """The Makefile MODULE_PATH variable reflects the src layout."""
        result = cookies.bake(extra_context={"project_name": "My Project", "layout": "src"})

        assert result.exit_code == 0
        content = (result.project_path / "Makefile").read_text()
        assert "MODULE_PATH = src/my_project" in content

    def test_makefile_module_path_flat(self, cookies):
        """The Makefile MODULE_PATH variable reflects the flat layout."""
        result = cookies.bake(extra_context={"project_name": "My Project", "layout": "flat"})

        assert result.exit_code == 0
        content = (result.project_path / "Makefile").read_text()
        assert "MODULE_PATH = my_project" in content
