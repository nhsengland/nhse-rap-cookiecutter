# ruff: noqa: B008
"""Generate test cookiecutter projects with different configurations.

This script creates multiple cookiecutter projects in the tmp/ folder,
each with different combinations of configuration options from test_configs.yaml.
This validates that the template works correctly with all option combinations.

NOTE: This script only GENERATES the template files. It does NOT install
or run any environment managers (conda, poetry, uv, etc.). You don't need
those tools installed to run this script - it just creates the project
structure that WOULD use them.

Examples
--------
Generate all test projects:
    $ uv run python scripts/generate_test_projects.py

Generate specific configuration:
    $ uv run python scripts/generate_test_projects.py --config minimal

Auto-cleanup after successful generation:
    $ uv run python scripts/generate_test_projects.py --auto-cleanup

Handle existing projects differently:
    $ uv run python scripts/generate_test_projects.py --exists skip
    $ uv run python scripts/generate_test_projects.py --exists fail
    $ uv run python scripts/generate_test_projects.py --exists clean
"""

import json
import shutil
import subprocess
import sys
from enum import Enum
from pathlib import Path
from typing import Any

import typer
import yaml
from loguru import logger

app = typer.Typer(help="Generate test cookiecutter projects")


class ExistsStrategy(str, Enum):
    """Strategy for handling existing project directories."""

    CLEAN = "clean"
    SKIP = "skip"
    FAIL = "fail"


def load_cookiecutter_config() -> dict[str, Any]:
    """Load cookiecutter.json configuration.

    Returns
    -------
    dict[str, Any]
        Cookiecutter configuration with available options
    """
    config_path = Path(__file__).parent.parent / "cookiecutter.json"
    logger.debug(f"Loading cookiecutter config from {config_path}")
    with open(config_path) as f:
        return json.load(f)


def load_test_configs() -> dict[str, dict[str, Any]]:
    """Load test configurations from YAML file.

    Returns
    -------
    dict[str, dict[str, Any]]
        Dictionary of test configuration name to configuration values
    """
    config_path = Path(__file__).parent / "test_configs.yaml"
    logger.debug(f"Loading test configs from {config_path}")
    with open(config_path) as f:
        configs = yaml.safe_load(f)
    logger.info(f"Loaded {len(configs)} test configurations")
    return configs


def validate_config(config_name: str, config_values: dict[str, Any]) -> None:
    """Validate that config values match options in cookiecutter.json.

    Parameters
    ----------
    config_name : str
        Name of the configuration being validated
    config_values : dict[str, Any]
        Dictionary of cookiecutter values to validate

    Raises
    ------
    ValueError
        If any config value is not valid according to cookiecutter.json
    """
    logger.debug(f"Validating configuration: {config_name}")
    cookiecutter_config = load_cookiecutter_config()

    list_options = {
        "environment_manager",
        "dependency_file",
        "pydata_packages",
        "linting_and_formatting",
        "open_source_license",
        "docs",
        "include_code_scaffold",
    }

    for key, value in config_values.items():
        if key in list_options:
            valid_options = cookiecutter_config.get(key)
            if isinstance(valid_options, list) and value not in valid_options:
                raise ValueError(
                    f"{config_name}: Invalid value '{value}' for {key}. "
                    f"Valid options: {valid_options}"
                )

    logger.success(f"Configuration '{config_name}' validated")


def cleanup_project(project_path: Path) -> None:
    """Remove a generated project directory.

    Parameters
    ----------
    project_path : Path
        Path to the project directory to remove
    """
    if project_path.exists():
        logger.info(f"Cleaning up {project_path}")
        shutil.rmtree(project_path)
        logger.success(f"Removed {project_path}")
    else:
        logger.debug(f"Project path does not exist: {project_path}")


def handle_existing_project(project_path: Path, strategy: ExistsStrategy) -> bool:
    """Handle an existing project directory based on the chosen strategy.

    Parameters
    ----------
    project_path : Path
        Path to the project directory
    strategy : ExistsStrategy
        Strategy for handling existing directories

    Returns
    -------
    bool
        True if generation should proceed, False if it should be skipped

    Raises
    ------
    FileExistsError
        If strategy is FAIL and the directory exists
    """
    if not project_path.exists():
        return True

    logger.warning(f"Project directory already exists: {project_path}")

    if strategy == ExistsStrategy.CLEAN:
        cleanup_project(project_path)
        return True
    elif strategy == ExistsStrategy.SKIP:
        logger.info(f"Skipping existing project: {project_path}")
        return False
    elif strategy == ExistsStrategy.FAIL:
        raise FileExistsError(
            f"Project directory already exists: {project_path}. "
            "Use --exists clean to remove it first."
        )

    return True


def validate_generated_project(project_path: Path, config_values: dict[str, Any]) -> None:
    """Validate that generated project has basic required structure.

    Validation steps performed:
    1. Check critical files exist (README.md, .gitignore) - fails if missing
    2. Check expected directories exist (data, notebooks, tests, module) - warns if missing
    3. Check optional files exist (Makefile, .pre-commit-config.yaml) - logs if present
    4. List all generated files for debugging
    5. Raise error only if critical files are missing, warn for missing directories

    Parameters
    ----------
    project_path : Path
        Path to the generated project directory
    config_values : dict[str, Any]
        Configuration values used to generate the project

    Raises
    ------
    FileNotFoundError
        If critical files are missing
    """
    logger.debug(f"Validating generated project structure: {project_path}")

    critical_files = [
        "README.md",
        ".gitignore",
    ]

    expected_dirs = [
        "data",
        "notebooks",
        "tests",
    ]

    module_name = config_values.get(
        "module_name",
        config_values.get("project_name", "").lower().replace(" ", "_").replace("-", "_"),
    )
    if module_name:
        expected_dirs.append(module_name)

    logger.debug(f"Checking critical files: {critical_files}")
    missing_critical = []
    for file in critical_files:
        file_path = project_path / file
        if not file_path.exists():
            missing_critical.append(file)
            logger.error(f"Missing critical file: {file}")
        else:
            logger.debug(f"Found critical file: {file}")

    logger.debug(f"Checking expected directories: {expected_dirs}")
    missing_dirs = []
    for dir_name in expected_dirs:
        dir_path = project_path / dir_name
        if not dir_path.exists():
            missing_dirs.append(dir_name)
            logger.warning(f"Missing expected directory: {dir_name}")
        else:
            logger.debug(f"Found expected directory: {dir_name}")

    logger.debug("Checking optional files")
    optional_files = ["Makefile", ".pre-commit-config.yaml"]
    for file in optional_files:
        file_path = project_path / file
        if not file_path.exists():
            logger.debug(f"Optional file not found: {file}")
        else:
            logger.debug(f"Found optional file: {file}")

    actual_files = [
        f.name for f in project_path.iterdir() if f.is_file() and not f.name.startswith(".")
    ]
    logger.debug(f"Generated files: {', '.join(sorted(actual_files))}")

    if missing_critical:
        logger.error("Validation failed: critical files missing")
        raise FileNotFoundError(f"Generated project missing critical files: {missing_critical}")

    if missing_dirs:
        logger.warning(f"Some expected directories missing: {missing_dirs}")

    logger.success("Project structure validated: critical files present")


def generate_project(
    config_name: str,
    config_values: dict[str, Any],
    output_dir: Path,
    exists_strategy: ExistsStrategy = ExistsStrategy.CLEAN,
) -> Path | None:
    """Generate a single cookiecutter project with the given configuration.

    Generation process:
    1. Validate configuration against cookiecutter.json options
    2. Create output directory for this configuration
    3. Determine expected project path from repo_name
    4. Handle existing project based on exists_strategy
    5. Build and execute cookiecutter command
    6. Validate generated project structure

    Parameters
    ----------
    config_name : str
        Name of the configuration (used for subfolder name)
    config_values : dict[str, Any]
        Dictionary of cookiecutter values
    output_dir : Path
        Directory to output the project to
    exists_strategy : ExistsStrategy, optional
        Strategy for handling existing project directories

    Returns
    -------
    Path | None
        Path to the generated project directory, or None if skipped

    Raises
    ------
    subprocess.CalledProcessError
        If cookiecutter command fails
    ValueError
        If configuration validation fails
    FileExistsError
        If exists_strategy is FAIL and directory exists
    FileNotFoundError
        If generated project is missing expected files
    """
    logger.info(f"Starting generation for config: {config_name}")

    validate_config(config_name, config_values)

    logger.debug("Creating output directory for configuration")
    config_output = output_dir / config_name
    config_output.mkdir(parents=True, exist_ok=True)
    logger.debug(f"Created output directory: {config_output}")

    logger.debug("Determining project path from repo_name")
    project_name = config_values.get("project_name", "project_name")
    repo_name = project_name.lower().replace(" ", "_")
    project_path = config_output / repo_name
    logger.debug(f"Expected project path: {project_path}")

    if not handle_existing_project(project_path, exists_strategy):
        logger.info(f"Skipped generation for {config_name} (already exists)")
        return None

    logger.debug("Building cookiecutter command")
    cmd = [
        "cookiecutter",
        ".",
        "--no-input",
        "--output-dir",
        str(config_output),
    ]

    logger.debug("Adding configuration values to cookiecutter command")
    for key, value in config_values.items():
        if key != "config_description":
            cmd.append(f"{key}={value}")

    logger.info(f"Executing cookiecutter for {config_name}")
    logger.debug(f"Command: {' '.join(cmd)}")

    try:
        result = subprocess.run(
            cmd,
            cwd=Path(__file__).parent.parent,
            check=True,
            capture_output=True,
            text=True,
        )
        logger.success(f"Cookiecutter generation completed for {config_name}")
        if result.stdout:
            logger.debug(f"Cookiecutter stdout: {result.stdout}")

        logger.info(f"Validating project structure for {config_name}")
        validate_generated_project(project_path, config_values)

        logger.success(f"Successfully generated and validated {config_name} -> {project_path}")
        return project_path

    except subprocess.CalledProcessError as e:
        logger.error(f"Cookiecutter failed for {config_name}: {e}")
        logger.error(f"Command: {' '.join(cmd)}")
        logger.error(f"Error output: {e.stderr}")
        raise
    except FileNotFoundError as e:
        logger.error(f"Validation failed for {config_name}: {e}")
        raise


@app.command()
def generate(  # noqa: B008
    config: str | None = typer.Option(
        None,
        "--config",
        "-c",
        help="Generate only a specific configuration by name",
    ),
    output_dir: Path = typer.Option(
        None,
        "--output-dir",
        "-o",
        help="Output directory for generated projects (default: tmp/)",
    ),
    exists: ExistsStrategy = typer.Option(
        ExistsStrategy.CLEAN,
        "--exists",
        "-e",
        help="Strategy for handling existing project directories",
    ),
    auto_cleanup: bool = typer.Option(
        False,
        "--auto-cleanup",
        help="Automatically cleanup generated projects after successful generation",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Enable verbose debug logging",
    ),
) -> None:
    """Generate test cookiecutter projects with different configurations.

    Generates projects in tmp/ folder by default. Each configuration tests
    different combinations of cookiecutter options to validate the template.

    Execution flow:
    1. Configure logger level based on verbose flag
    2. Set default output directory (tmp/) if not specified
    3. Load test configurations from YAML file
    4. Filter to specific config if requested
    5. Generate each project with validation
    6. Print summary of successes and failures
    7. Auto-cleanup if requested
    8. Exit with error code if any failures occurred

    Parameters
    ----------
    config : str | None
        Name of specific configuration to generate (generates all if None)
    output_dir : Path | None
        Custom output directory (uses tmp/ if None)
    exists : ExistsStrategy
        How to handle existing project directories
    auto_cleanup : bool
        Whether to automatically cleanup after successful generation
    verbose : bool
        Enable verbose debug logging
    """
    if not verbose:
        logger.remove()
        logger.add(sys.stderr, level="INFO")

    if output_dir is None:
        output_dir = Path(__file__).parent.parent / "tmp"

    output_dir.mkdir(parents=True, exist_ok=True)
    logger.info(f"Output directory: {output_dir}")

    try:
        test_configs = load_test_configs()
    except Exception as e:
        logger.error(f"Failed to load test configurations: {e}")
        raise typer.Exit(code=1) from None

    if config:
        if config not in test_configs:
            logger.error(f"Configuration '{config}' not found in test_configs.yaml")
            logger.info(f"Available configurations: {', '.join(test_configs.keys())}")
            raise typer.Exit(code=1)
        test_configs = {config: test_configs[config]}

    logger.info(f"Starting generation of {len(test_configs)} configuration(s)")

    generated_projects: list[Path] = []
    failed_configs: list[str] = []

    for idx, (config_name, config_values) in enumerate(test_configs.items(), 1):
        logger.info(f"Processing config {idx}/{len(test_configs)}: {config_name}")
        try:
            project_path = generate_project(config_name, config_values, output_dir, exists)
            if project_path:
                generated_projects.append(project_path)
                logger.info(f"Config {idx}/{len(test_configs)} completed: {config_name}")
        except Exception as e:
            logger.error(f"Config {idx}/{len(test_configs)} failed: {config_name} - {e}")
            failed_configs.append(config_name)
            continue

    logger.info(
        f"Generation complete: {len(generated_projects)} successful, {len(failed_configs)} failed, output_dir={output_dir}"
    )

    if failed_configs:
        logger.warning(f"Failed configurations: {', '.join(failed_configs)}")

    if generated_projects:
        for project in generated_projects:
            logger.success(f"Generated project: {project.parent.name}/{project.name}")

    if auto_cleanup and generated_projects:
        logger.info("Auto-cleanup enabled, removing generated projects...")
        config_dirs = {project.parent for project in generated_projects}
        for config_dir in config_dirs:
            cleanup_project(config_dir)
        logger.success("Cleanup complete")

    if failed_configs:
        raise typer.Exit(code=1)


@app.command()
def list_configs() -> None:
    """List all available test configurations."""
    try:
        test_configs = load_test_configs()
    except Exception as e:
        logger.error(f"Failed to load test configurations: {e}")
        raise typer.Exit(code=1) from None

    print(f"\nAvailable test configurations ({len(test_configs)}):\n")
    for name, config in test_configs.items():
        desc = config.get("config_description", "No description")
        print(f"{name} - {desc}")


@app.command()
def cleanup(  # noqa: B008
    output_dir: Path = typer.Option(
        None,
        "--output-dir",
        "-o",
        help="Output directory to cleanup (default: tmp/)",
    ),
    config: str | None = typer.Option(
        None,
        "--config",
        "-c",
        help="Cleanup only a specific configuration",
    ),
) -> None:
    """Cleanup generated test projects.

    Parameters
    ----------
    output_dir : Path | None
        Directory containing generated projects (uses tmp/ if None)
    config : str | None
        Name of specific configuration to cleanup (cleans all if None)
    """
    if output_dir is None:
        output_dir = Path(__file__).parent.parent / "tmp"

    if not output_dir.exists():
        logger.info(f"Output directory does not exist: {output_dir}")
        return

    if config:
        logger.info(f"Cleaning up specific config: {config}")
        config_dir = output_dir / config
        cleanup_project(config_dir)
    else:
        logger.info(f"Cleaning up all projects in {output_dir}")
        for item in output_dir.iterdir():
            if item.name not in [".gitkeep"]:
                if item.is_dir():
                    shutil.rmtree(item)
                    logger.success(f"Removed {item.name}")
                else:
                    item.unlink()
                    logger.success(f"Removed {item.name}")
        logger.success("Cleanup complete")


if __name__ == "__main__":
    app()
