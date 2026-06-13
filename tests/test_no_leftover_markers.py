"""Regression tests: no unrendered Jinja markers or stale placeholders in baked projects."""

from pathlib import Path

import pytest
import yaml

CONFIGS_PATH = Path(__file__).parent.parent / "scripts" / "configs.yaml"

# Keys that exist in cookiecutter.json; extras in configs.yaml are filtered out
COOKIECUTTER_KEYS = {
    "project_name",
    "repo_name",
    "module_name",
    "author_name",
    "author_email",
    "organization_name",
    "team_name",
    "team_email",
    "git_hosting_platform",
    "repository_url",
    "description",
    "python_version_number",
    "environment_manager",
    "linting_and_formatting",
    "open_source_license",
    "docs",
    "include_code_scaffold",
}

# File extensions where leftover Jinja/placeholder markers would be a bug.
# Excludes *.html because docs/overrides/ are copy-without-render MkDocs templates.
CHECKED_EXTENSIONS = {".md", ".toml", ".yaml", ".yml", ".cfg", ".py", ".txt", ".env"}


def load_configs() -> list[tuple[str, dict]]:
    with open(CONFIGS_PATH) as f:
        raw = yaml.safe_load(f)
    return [
        (name, {k: v for k, v in cfg.items() if k in COOKIECUTTER_KEYS})
        for name, cfg in raw.items()
    ]


CONFIGS = load_configs()


def _text_files(project_path: Path):
    for p in project_path.rglob("*"):
        if p.is_file() and p.suffix in CHECKED_EXTENSIONS:
            yield p


@pytest.mark.parametrize("config_name,context", CONFIGS)
class TestNoLeftoverMarkers:
    """Bake every config and verify no unrendered markers remain."""

    def test_bakes_successfully(self, cookies, config_name, context):
        """Template bakes without errors for this configuration."""
        result = cookies.bake(extra_context=context)
        assert result.exit_code == 0, (
            f"[{config_name}] bake failed with exception: {result.exception}"
        )

    def test_no_jinja_markers_in_text_files(self, cookies, config_name, context):
        """No raw {{ or {% markers remain in rendered text files."""
        result = cookies.bake(extra_context=context)
        assert result.exit_code == 0

        for file_path in _text_files(result.project_path):
            try:
                content = file_path.read_text(encoding="utf-8")
            except (UnicodeDecodeError, PermissionError):
                continue
            rel = file_path.relative_to(result.project_path)
            assert "{%" not in content, f"[{config_name}] '{{% marker in {rel}"
            assert "{{" not in content, f"[{config_name}] '{{{{' marker in {rel}"

    def test_no_year_placeholder_in_text_files(self, cookies, config_name, context):
        """@YEAR_PLACEHOLDER@ is fully replaced in all checked text files."""
        result = cookies.bake(extra_context=context)
        assert result.exit_code == 0

        for file_path in _text_files(result.project_path):
            try:
                content = file_path.read_text(encoding="utf-8")
            except (UnicodeDecodeError, PermissionError):
                continue
            rel = file_path.relative_to(result.project_path)
            assert "@YEAR_PLACEHOLDER@" not in content, (
                f"[{config_name}] '@YEAR_PLACEHOLDER@' not replaced in {rel}"
            )

    def test_no_underscore_prefixed_files_remain(self, cookies, config_name, context):
        """Underscore-prefixed staging files are renamed/removed by the hook."""
        result = cookies.bake(extra_context=context)
        assert result.exit_code == 0

        for name in ["_.env", "_pyproject.toml", "_environment.yml"]:
            assert not (result.project_path / name).exists(), (
                f"[{config_name}] '{name}' should have been renamed/removed by hook"
            )

    def test_docs_removed_when_docs_none(self, cookies, config_name, context):
        """docs/ directory and mkdocs.yml are absent when docs=none."""
        if context.get("docs", "mkdocs") != "none":
            pytest.skip("docs != none — skipping")
        result = cookies.bake(extra_context=context)
        assert result.exit_code == 0

        assert not (result.project_path / "docs").exists(), (
            f"[{config_name}] 'docs/' should be removed when docs=none"
        )
        assert not (result.project_path / "mkdocs.yml").exists(), (
            f"[{config_name}] 'mkdocs.yml' should be removed when docs=none"
        )

    def test_module_scaffold_removed_when_disabled(self, cookies, config_name, context):
        """Python module directory is absent when include_code_scaffold=No."""
        if context.get("include_code_scaffold", "Yes") != "No":
            pytest.skip("include_code_scaffold != No — skipping")
        result = cookies.bake(extra_context=context)
        assert result.exit_code == 0

        module_name = context.get("module_name") or (
            context.get("project_name", "project_name").lower().replace(" ", "_").replace("-", "_")
        )
        assert not (result.project_path / module_name).exists(), (
            f"[{config_name}] '{module_name}/' should be removed when include_code_scaffold=No"
        )

    def test_license_removed_when_no_license_chosen(self, cookies, config_name, context):
        """LICENSE file is absent when open_source_license='No license file'."""
        if context.get("open_source_license", "MIT") != "No license file":
            pytest.skip("open_source_license != 'No license file' — skipping")
        result = cookies.bake(extra_context=context)
        assert result.exit_code == 0

        assert not (result.project_path / "LICENSE").exists(), (
            f"[{config_name}] 'LICENSE' should be removed when 'No license file' is chosen"
        )

    def test_license_contains_only_chosen_license(self, cookies, config_name, context):
        """LICENSE file contains only the selected licence text (no raw Jinja blocks)."""
        # Maps SPDX identifier → a unique phrase found in that licence body
        license_phrases = {
            "MIT": "MIT License",
            "Apache-2.0": "Apache License",
            "GPL-3.0": "GNU GENERAL PUBLIC LICENSE",
        }
        license_choice = context.get("open_source_license", "MIT")
        if license_choice == "No license file":
            pytest.skip("No license file — skipping")
        result = cookies.bake(extra_context=context)
        assert result.exit_code == 0

        license_path = result.project_path / "LICENSE"
        assert license_path.exists(), f"[{config_name}] LICENSE file missing"
        content = license_path.read_text()
        # Raw Jinja conditionals must not be present
        assert "{%" not in content, f"[{config_name}] Raw Jinja found in LICENSE"
        # The correct licence body text should appear
        expected_phrase = license_phrases.get(license_choice, license_choice)
        assert expected_phrase in content, (
            f"[{config_name}] '{expected_phrase}' not found in LICENSE for {license_choice}"
        )
