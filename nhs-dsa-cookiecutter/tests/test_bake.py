"""Bake tests: the template generates the expected project structure."""

DEFAULT_CONTEXT = {
    "project_name": "Bake Test Project",
    "author_name": "Test Author",
    "description": "A baked test project.",
    "environment_manager": "uv",
    "open_source_license": "MIT",
}


class TestBakeStructure:
    """The default bake produces the directories and files we expect."""

    def test_bakes_without_error(self, cookies):
        result = cookies.bake(extra_context=DEFAULT_CONTEXT)
        assert result.exit_code == 0
        assert result.exception is None
        assert result.project_path.is_dir()

    def test_repo_and_module_names_derived(self, cookies):
        result = cookies.bake(extra_context=DEFAULT_CONTEXT)
        # "Bake Test Project" -> "bake_test_project"
        assert result.project_path.name == "bake_test_project"
        assert (result.project_path / "bake_test_project").is_dir()

    def test_expected_top_level_dirs(self, cookies):
        result = cookies.bake(extra_context=DEFAULT_CONTEXT)
        for d in ["data", "notebooks", "reports", "tests", "guides", "presentation", "scripts"]:
            assert (result.project_path / d).is_dir(), f"missing dir: {d}"

    def test_data_subdirectories(self, cookies):
        result = cookies.bake(extra_context=DEFAULT_CONTEXT)
        for sub in ["raw", "interim", "processed", "external"]:
            assert (result.project_path / "data" / sub).is_dir(), f"missing data/{sub}"

    def test_key_files_present(self, cookies):
        result = cookies.bake(extra_context=DEFAULT_CONTEXT)
        for f in [
            "README.md",
            "pyproject.toml",
            ".pre-commit-config.yaml",
            ".gitignore",
            ".env",
            "LICENSE",
            "OPEN_CODE_CHECKLIST.md",
            "scripts/setup_project.py",
            "tests/test_dataset.py",
        ]:
            assert (result.project_path / f).is_file(), f"missing file: {f}"

    def test_module_files_present(self, cookies):
        result = cookies.bake(extra_context=DEFAULT_CONTEXT)
        module = result.project_path / "bake_test_project"
        for f in ["__init__.py", "config.py", "dataset.py"]:
            assert (module / f).is_file(), f"missing module file: {f}"

    def test_guides_present(self, cookies):
        result = cookies.bake(extra_context=DEFAULT_CONTEXT)
        guides = result.project_path / "guides"
        markdown = list(guides.glob("*.md"))
        # README index + 18 numbered tutorials.
        assert len(markdown) == 19, f"expected 19 guide files, found {len(markdown)}"

    def test_presentation_templates_present(self, cookies):
        result = cookies.bake(extra_context=DEFAULT_CONTEXT)
        pres = result.project_path / "presentation"
        for f in [
            "_quarto.yml",
            "one_page_summary.qmd",
            "poster.qmd",
            "one_page_summary.pptx",
            "poster.pptx",
        ]:
            assert (pres / f).is_file(), f"missing presentation file: {f}"
