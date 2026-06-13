"""Regression tests: no unrendered Jinja markers or stale placeholders.

Bakes every configuration in scripts/configs.yaml and asserts that the
generated project contains no leftover ``{{``/``{%`` markers, no
``@YEAR_PLACEHOLDER@``, and no underscore-prefixed staging files.
"""

from pathlib import Path

import pytest
import yaml

CONFIGS_PATH = Path(__file__).parent.parent / "scripts" / "configs.yaml"

# Keys that exist in cookiecutter.json; any extras in configs.yaml are dropped.
COOKIECUTTER_KEYS = {
    "project_name",
    "author_name",
    "description",
    "python_version_number",
    "environment_manager",
    "open_source_license",
}

# Text file types where a leftover marker would be a real bug.
CHECKED_EXTENSIONS = {".md", ".toml", ".yaml", ".yml", ".py", ".txt", ".env", ".qmd"}


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
        result = cookies.bake(extra_context=context)
        assert result.exit_code == 0, (
            f"[{config_name}] bake failed with exception: {result.exception}"
        )

    def test_no_jinja_markers_in_text_files(self, cookies, config_name, context):
        result = cookies.bake(extra_context=context)
        assert result.exit_code == 0

        for file_path in _text_files(result.project_path):
            try:
                content = file_path.read_text(encoding="utf-8")
            except (UnicodeDecodeError, PermissionError):
                continue
            rel = file_path.relative_to(result.project_path)
            assert "{%" not in content, f"[{config_name}] '{{%' marker in {rel}"
            assert "{{" not in content, f"[{config_name}] '{{{{' marker in {rel}"

    def test_no_year_placeholder_in_text_files(self, cookies, config_name, context):
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
        result = cookies.bake(extra_context=context)
        assert result.exit_code == 0

        for name in ["_.env", "_pyproject.toml"]:
            assert not (result.project_path / name).exists(), (
                f"[{config_name}] '{name}' should have been renamed by the hook"
            )
        assert not (result.project_path / "_data").exists(), (
            f"[{config_name}] '_data/' should have been renamed to 'data/' by the hook"
        )

    def test_license_handling(self, cookies, config_name, context):
        """LICENSE is present with the right body, or absent for 'No license file'."""
        result = cookies.bake(extra_context=context)
        assert result.exit_code == 0

        license_choice = context.get("open_source_license", "MIT")
        license_path = result.project_path / "LICENSE"

        if license_choice == "No license file":
            assert not license_path.exists(), (
                f"[{config_name}] LICENSE should be removed for 'No license file'"
            )
            return

        assert license_path.exists(), f"[{config_name}] LICENSE missing"
        content = license_path.read_text()
        assert "{%" not in content, f"[{config_name}] Raw Jinja found in LICENSE"
        phrase = {"MIT": "MIT License", "Apache-2.0": "Apache License"}[license_choice]
        assert phrase in content, (
            f"[{config_name}] '{phrase}' not found in LICENSE for {license_choice}"
        )
