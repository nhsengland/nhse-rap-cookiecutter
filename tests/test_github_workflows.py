"""Tests for the generated GitHub Actions workflows and CI status badges."""

import yaml


class TestWorkflowsPresent:
    """Workflows are generated for GitHub-hosted projects."""

    def test_core_workflows_exist(self, cookies):
        """tests, lint and gitleaks workflows are always generated for GitHub."""
        result = cookies.bake(extra_context={"git_hosting_platform": "github"})

        assert result.exit_code == 0
        workflows = result.project_path / ".github" / "workflows"
        assert (workflows / "tests.yml").exists()
        assert (workflows / "lint.yml").exists()
        assert (workflows / "gitleaks.yml").exists()

    def test_docs_workflow_present_when_mkdocs(self, cookies):
        """The docs workflow is generated when MkDocs is enabled."""
        result = cookies.bake(extra_context={"git_hosting_platform": "github", "docs": "mkdocs"})

        assert result.exit_code == 0
        assert (result.project_path / ".github" / "workflows" / "docs.yml").exists()

    def test_docs_workflow_absent_when_docs_none(self, cookies):
        """The docs workflow is removed when documentation is disabled."""
        result = cookies.bake(extra_context={"git_hosting_platform": "github", "docs": "none"})

        assert result.exit_code == 0
        assert not (result.project_path / ".github" / "workflows" / "docs.yml").exists()


class TestWorkflowsRemovedForNonGitHub:
    """GitHub Actions are only useful on GitHub."""

    def test_github_dir_removed_for_gitlab(self, cookies):
        """The .github directory is removed for non-GitHub hosting."""
        result = cookies.bake(extra_context={"git_hosting_platform": "gitlab"})

        assert result.exit_code == 0
        assert not (result.project_path / ".github").exists()


class TestWorkflowContent:
    """Generated workflows are valid YAML and reference the chosen tooling."""

    def test_workflows_are_valid_yaml(self, cookies):
        """Every generated workflow parses as YAML."""
        result = cookies.bake(extra_context={"git_hosting_platform": "github"})

        assert result.exit_code == 0
        workflows = result.project_path / ".github" / "workflows"
        for workflow in workflows.glob("*.yml"):
            yaml.safe_load(workflow.read_text())

    def test_tests_workflow_uses_uv(self, cookies):
        """uv projects run pytest via uv in CI."""
        result = cookies.bake(
            extra_context={"git_hosting_platform": "github", "environment_manager": "uv"}
        )

        assert result.exit_code == 0
        content = (result.project_path / ".github" / "workflows" / "tests.yml").read_text()
        assert "uv run pytest" in content

    def test_tests_workflow_uses_conda(self, cookies):
        """conda projects set up the environment from environment.yml in CI."""
        result = cookies.bake(
            extra_context={"git_hosting_platform": "github", "environment_manager": "conda"}
        )

        assert result.exit_code == 0
        content = (result.project_path / ".github" / "workflows" / "tests.yml").read_text()
        assert "setup-miniconda" in content
        assert "environment.yml" in content

    def test_lint_workflow_matches_linter_choice(self, cookies):
        """The lint workflow runs the selected linting tool."""
        result = cookies.bake(
            extra_context={
                "git_hosting_platform": "github",
                "linting_and_formatting": "ruff",
            }
        )

        assert result.exit_code == 0
        content = (result.project_path / ".github" / "workflows" / "lint.yml").read_text()
        assert "ruff check" in content

    def test_gitleaks_token_preserved(self, cookies):
        """The GitHub Actions secret expression survives templating."""
        result = cookies.bake(extra_context={"git_hosting_platform": "github"})

        assert result.exit_code == 0
        content = (result.project_path / ".github" / "workflows" / "gitleaks.yml").read_text()
        assert "${{ secrets.GITHUB_TOKEN }}" in content


class TestCIBadges:
    """README advertises CI status badges for GitHub projects."""

    def test_badges_present_for_github(self, cookies):
        """README includes workflow status badges when hosted on GitHub."""
        result = cookies.bake(extra_context={"git_hosting_platform": "github"})

        assert result.exit_code == 0
        readme = (result.project_path / "README.md").read_text()
        assert "actions/workflows/tests.yml/badge.svg" in readme
        assert "actions/workflows/lint.yml/badge.svg" in readme
        assert "actions/workflows/gitleaks.yml/badge.svg" in readme

    def test_badges_absent_for_gitlab(self, cookies):
        """README does not include GitHub Actions badges for GitLab projects."""
        result = cookies.bake(extra_context={"git_hosting_platform": "gitlab"})

        assert result.exit_code == 0
        readme = (result.project_path / "README.md").read_text()
        assert "actions/workflows/tests.yml/badge.svg" not in readme
