#!/usr/bin/env python3
"""Repository setup script for {{ cookiecutter.project_name }}.

This script automates the initial setup of the repository including:
- Git initialization and remote configuration
- Python environment setup
- Dependency installation
- Pre-commit hook installation
- Initial commit creation

Run this script after generating the project from the cookiecutter template.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from textwrap import dedent


# ANSI color codes for terminal output
class Colors:
    """ANSI color codes for terminal output."""
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    BOLD = "\033[1m"
    RESET = "\033[0m"


# Status tracking for setup steps
class SetupStatus:
    """Track status of each setup step."""
    def __init__(self):
        self.git_init = "not_run"
        self.git_remote = "not_run"
        self.remote_accessible = False
        self.environment = "not_run"
        self.dependencies = "not_run"
        self.precommit = "not_run"
        self.initial_commit = "not_run"


status = SetupStatus()


class SetupError(Exception):
    """Raised when setup encounters an error that requires user action."""


def run_command(cmd: list[str], capture_output: bool = False) -> subprocess.CompletedProcess:
    """Run a shell command and return the result.

    Parameters
    ----------
    cmd : list[str]
        Command to run as list of arguments
    capture_output : bool
        Whether to capture stdout/stderr instead of displaying

    Returns
    -------
    subprocess.CompletedProcess
        Result of the command execution

    Raises
    ------
    subprocess.CalledProcessError
        If command returns non-zero exit code
    """
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(
        cmd,
        capture_output=capture_output,
        text=True,
        check=True,
    )
    return result


def check_command_available(cmd: str) -> bool:
    """Check if a command is available in PATH.

    Parameters
    ----------
    cmd : str
        Command name to check

    Returns
    -------
    bool
        True if command is available, False otherwise
    """
    try:
        subprocess.run(
            ["which", cmd],
            capture_output=True,
            check=True,
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def setup_git_repository() -> None:
    """Initialize git repository if not already initialized."""
    print(f"\n{Colors.BOLD}=== Git Repository Setup ==={Colors.RESET}")

    if (Path(".git")).exists():
        print(f"{Colors.YELLOW}✓ Git repository already initialized{Colors.RESET}")
        status.git_init = "skipped"
        return

    if not check_command_available("git"):
        status.git_init = "failed"
        raise SetupError(
            "Git is not installed. Please install git:\n"
            "  Ubuntu/Debian: sudo apt-get install git\n"
            "  macOS: brew install git\n"
            "  Windows: https://git-scm.com/download/win"
        )

    run_command(["git", "init"])
    run_command(["git", "branch", "-M", "main"])
    print(f"{Colors.GREEN}✓ Git repository initialized with default branch 'main'{Colors.RESET}")
    status.git_init = "success"


def setup_git_remote() -> None:
    """Configure git remote if not already set up."""
    print(f"\n{Colors.BOLD}=== Git Remote Setup ==={Colors.RESET}")

    repository_url = "{{ cookiecutter.repository_url }}"

    # Check if remote already exists
    try:
        result = run_command(["git", "remote", "get-url", "origin"], capture_output=True)
        existing_url = result.stdout.strip()

        if existing_url == repository_url:
            print(f"{Colors.YELLOW}✓ Remote 'origin' already configured: {repository_url}{Colors.RESET}")
        else:
            print(f"{Colors.BLUE}Remote 'origin' exists with different URL: {existing_url}{Colors.RESET}")
            print(f"Updating to: {repository_url}")
            run_command(["git", "remote", "set-url", "origin", repository_url])
            print(f"{Colors.GREEN}✓ Remote 'origin' updated{Colors.RESET}")
    except subprocess.CalledProcessError:
        # Remote doesn't exist, add it
        run_command(["git", "remote", "add", "origin", repository_url])
        print(f"{Colors.GREEN}✓ Remote 'origin' configured: {repository_url}{Colors.RESET}")

    # Verify remote accessibility
    print(f"Verifying remote repository accessibility...")
    try:
        result = run_command(["git", "ls-remote", "--heads", repository_url], capture_output=True)
        print(f"✓ Remote repository verified: {repository_url}")
    except subprocess.CalledProcessError:
        print()
        print("!" * 70)
        print("REMOTE REPOSITORY DOES NOT EXIST YET")
        print("!" * 70)
        repo_name = repository_url.split('/')[-1]
        print(dedent(f"""
            The remote repository has not been created yet: {repository_url}
            
            This is normal for new projects!
            
            ⚠️  BEFORE YOU CAN PUSH, you must:
            1. Go to your git hosting platform (GitHub/GitLab/etc.)
            2. Create a new repository called: {repo_name}
            3. DO NOT initialize it with README, .gitignore, or license
               (your local repo already has these files)
            4. Then run: git push -u origin main
            
            See the "NEXT STEPS" section below for detailed instructions.
        """).strip())
        print("!" * 70)
        print()
        status.git_remote = "warning"
        status.remote_accessible = False


def setup_environment() -> None:
    """Set up Python environment based on environment manager."""
    print(f"\n{Colors.BOLD}=== Environment Setup ==={Colors.RESET}")

    env_manager = "{{ cookiecutter.environment_manager }}"

    # venv ships with Python 3, so only the interpreter needs to be available.
    command_to_check = "python" if env_manager == "venv" else env_manager
    if not check_command_available(command_to_check):
        install_instructions = {
            "uv": "Install uv: curl -LsSf https://astral.sh/uv/install.sh | sh",
            "conda": "Install conda: https://docs.conda.io/en/latest/miniconda.html",
            "venv": "venv ships with Python 3 - please install Python 3.",
        }
        instruction = install_instructions.get(env_manager, f"Please install {env_manager}")
        raise SetupError(dedent(f"""
            {command_to_check} is not installed.
            {instruction}
        """).strip())

    print(f"Using environment manager: {env_manager}")

    # Set up environment based on manager
    if env_manager == "uv":
        if Path(".venv").exists():
            print(f"{Colors.YELLOW}→ Virtual environment already exists{Colors.RESET}")
            status.environment = "skipped"
        else:
            run_command(["uv", "venv"])
            print(f"{Colors.GREEN}✓ Virtual environment created with uv{Colors.RESET}")
            status.environment = "success"

    elif env_manager == "venv":
        if Path(".venv").exists():
            print(f"{Colors.YELLOW}✓ Virtual environment already exists{Colors.RESET}")
            status.environment = "skipped"
        else:
            run_command([sys.executable, "-m", "venv", ".venv"])
            print(f"{Colors.GREEN}✓ Virtual environment created at .venv{Colors.RESET}")
            status.environment = "success"

    elif env_manager == "conda":
        env_name = "{{ cookiecutter.repo_name }}"
        result = subprocess.run(
            ["conda", "env", "list"],
            capture_output=True,
            text=True
        )
        if env_name in result.stdout:
            print(f"{Colors.YELLOW}✓ Conda environment '{env_name}' already exists{Colors.RESET}")
            status.environment = "skipped"
        else:
            run_command(["conda", "env", "create", "-f", "environment.yml"])
            print(f"{Colors.GREEN}✓ Conda environment created{Colors.RESET}")
            status.environment = "success"


def install_dependencies() -> None:
    """Install project dependencies."""
    print("\n=== Dependency Installation ===")

    env_manager = "{{ cookiecutter.environment_manager }}"

    if env_manager == "uv":
        run_command(["uv", "sync", "--all-extras"])
        print(f"{Colors.GREEN}✓ Dependencies installed with uv (including all extras){Colors.RESET}")
        status.dependencies = "success"

    elif env_manager == "venv":
        # Activate and install with pip
        if sys.platform == "win32":
            pip_cmd = [".venv/Scripts/pip"]
        else:
            pip_cmd = [".venv/bin/pip"]
        run_command(pip_cmd + ["install", "-e", ".[dev{% if cookiecutter.docs == 'mkdocs' %},docs{% endif %}]"])
        print(f"{Colors.GREEN}✓ Dependencies installed with pip{Colors.RESET}")
        status.dependencies = "success"

    elif env_manager == "conda":
        # Conda dependencies are in environment.yml
        print(f"{Colors.GREEN}✓ Dependencies installed via conda environment.yml{Colors.RESET}")
        status.dependencies = "success"


def setup_precommit() -> None:
    """Install pre-commit hooks."""
    print("\n=== Pre-commit Setup ===")

    env_manager = "{{ cookiecutter.environment_manager }}"

    # Build command based on environment manager
    if env_manager == "uv":
        cmd = ["uv", "run", "pre-commit", "install"]
    elif env_manager == "conda":
        env_name = "{{ cookiecutter.repo_name }}"
        cmd = ["conda", "run", "-n", env_name, "pre-commit", "install"]
    elif env_manager == "venv":
        if sys.platform == "win32":
            cmd = [".venv/Scripts/pre-commit", "install"]
        else:
            cmd = [".venv/bin/pre-commit", "install"]
    else:
        print("Attempting to use system pre-commit.")
        cmd = ["pre-commit", "install"]

    try:
        run_command(cmd)
        print(f"{Colors.GREEN}✓ Pre-commit hooks installed successfully{Colors.RESET}")
        status.precommit = "success"
    except subprocess.CalledProcessError:
        print(f"{Colors.RED}✗ Warning: Could not install pre-commit hooks{Colors.RESET}")
        print("You can install them later with: pre-commit install")
        status.precommit = "failed"


def create_initial_commit() -> None:
    """Create initial git commit."""
    print("\n=== Initial Commit ===")

    # Check if there are any commits
    try:
        run_command(["git", "rev-parse", "HEAD"], capture_output=True)
        print(f"{Colors.YELLOW}\u2713 Repository already has commits{Colors.RESET}")
        status.initial_commit = "skipped"
        return
    except subprocess.CalledProcessError:
        # No commits yet, create initial commit
        pass

    # Stage all files first so pre-commit can check them
    run_command(["git", "add", "."])
    print("Staged all files")

    print()
    print("=" * 70)
    print("RUNNING PRE-COMMIT HOOKS - FAILURES ARE EXPECTED AND NORMAL!")
    print("=" * 70)
    print(dedent("""
        The cookiecutter template generates files with minor formatting issues
        (trailing whitespace, missing newlines, etc.) that need to be fixed.
        
        Pre-commit hooks will now automatically fix these template-generated issues.
        
        ⚠️  IMPORTANT: Hooks showing "Failed" is NORMAL and EXPECTED!
        
        "Failed" means the hooks found and fixed formatting issues - this is GOOD!
        
        The process works like this:
        1. Hooks check the template-generated files
        2. Find minor formatting issues (whitespace, newlines, etc.)
        3. Automatically fix them
        4. Report "Failed" because they modified files
        5. We re-stage the fixed files
        6. Commit again - this time hooks pass because files are clean
        
        Don't worry if you see "Failed" messages below - that's the template
        being cleaned up automatically. It's working correctly!
    """))
    print("=" * 70)
    print()

    env_manager = "{{ cookiecutter.environment_manager }}"

    try:
        if env_manager == "uv":
            run_command(["uv", "run", "pre-commit", "run", "--all-files"])
        elif env_manager == "conda":
            env_name = "{{ cookiecutter.repo_name }}"
            run_command(["conda", "run", "-n", env_name, "pre-commit", "run", "--all-files"])
        elif env_manager == "venv":
            if sys.platform == "win32":
                run_command([".venv/Scripts/pre-commit", "run", "--all-files"])
            else:
                run_command([".venv/bin/pre-commit", "run", "--all-files"])
        else:
            run_command(["pre-commit", "run", "--all-files"])
        print()
        print("✓ All pre-commit checks passed - files were already clean!")
        print()
    except subprocess.CalledProcessError:
        # Pre-commit fixed files, which is expected and good!
        print()
        print("=" * 70)
        print("✓ Pre-commit hooks automatically fixed formatting issues")
        print("=" * 70)
        print("Re-staging fixed files and committing again...")
        print()
        run_command(["git", "add", "."])

    # Commit - pre-commit hooks will run again to verify everything is clean
    run_command(
        ["git", "commit", "-m", "Initial commit from NHS RAP cookiecutter template"]
    )
    print(f"{Colors.GREEN}\u2713 Initial commit created{Colors.RESET}")
    status.initial_commit = "success"


def print_next_steps() -> None:
    """Print instructions for next steps."""
    env_manager = "{{ cookiecutter.environment_manager }}"
    repository_url = "{{ cookiecutter.repository_url }}"

    # Print summary with colors
    print("\n" + "=" * 70)
    print(f"{Colors.BOLD}SETUP SUMMARY{Colors.RESET}")
    print("=" * 70)

    def format_status(step_status: str) -> str:
        """Format status with color and symbol."""
        if step_status == "success":
            return f"{Colors.GREEN}\u2713 Success{Colors.RESET}"
        elif step_status == "skipped":
            return f"{Colors.YELLOW}\u2192 Skipped (already exists){Colors.RESET}"
        elif step_status == "warning":
            return f"{Colors.YELLOW}\u26a0 Warning{Colors.RESET}"
        elif step_status == "failed":
            return f"{Colors.RED}\u2717 Failed{Colors.RESET}"
        else:
            return f"{Colors.BLUE}- Not run{Colors.RESET}"

    print(f"\n{Colors.BOLD}Setup Steps:{Colors.RESET}")
    print(f"  Git repository:      {format_status(status.git_init)}")
    print(f"  Git remote:          {format_status(status.git_remote)}")
    if not status.remote_accessible and status.git_remote != "not_run":
        print(f"                       {Colors.YELLOW}(Remote needs to be created){Colors.RESET}")
    print(f"  Python environment:  {format_status(status.environment)}")
    print(f"  Dependencies:        {format_status(status.dependencies)}")
    print(f"  Pre-commit hooks:    {format_status(status.precommit)}")
    print(f"  Initial commit:      {format_status(status.initial_commit)}")

    print(f"\n{Colors.BOLD}Overall Status:{Colors.RESET}")
    if (status.git_init in ["success", "skipped"] and 
        status.git_remote in ["success", "warning"] and
        status.environment in ["success", "skipped"] and
        status.dependencies in ["success", "skipped"] and
        status.precommit in ["success", "skipped"] and
        status.initial_commit in ["success", "skipped"]):
        print(f"  {Colors.GREEN}\u2713 Repository setup complete and ready for development!{Colors.RESET}")
        if not status.remote_accessible:
            print(f"  {Colors.YELLOW}\u26a0 Remember to create the remote repository before pushing{Colors.RESET}")
    else:
        print(f"  {Colors.YELLOW}\u26a0 Setup partially complete - review steps above{Colors.RESET}")

    # Print next steps
    print("\n" + "=" * 70)
    print(f"{Colors.BOLD}NEXT STEPS{Colors.RESET}")
    print("=" * 70)

    print("\n1. Verify your setup:")
    if env_manager == "uv":
        print("   uv run pytest tests/unittests/ -v")
    elif env_manager == "conda":
        env_name = "{{ cookiecutter.repo_name }}"
        print(f"   conda activate {env_name}")
        print("   pytest tests/unittests/ -v")
    elif env_manager == "venv":
        print("   source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate")
        print("   pytest tests/unittests/ -v")
    else:
        print("   pytest tests/unittests/ -v")

    if status.git_remote in ["success", "warning"]:
        if status.remote_accessible:
            print("\n2. Push to remote repository:")
            print("   git push -u origin main")
        else:
            repo_name = repository_url.split('/')[-1]
            base_url = '/'.join(repository_url.split('/')[:-1])
            print(dedent(f"""
                2. Create the remote repository (if it doesn't exist yet):
                   a) Go to your git hosting platform: {base_url}
                   b) Click "New repository" or "Create new project"
                   c) Name it: {repo_name}
                   d) DO NOT initialize with README, .gitignore, or license
                      (your local repo already has these)
                   
                   Then push your code:
                   git push -u origin main
                   
                   If the remote URL is different, update it:
                   git remote set-url origin <correct-url>
            """).strip())

    print(f"\n3. Repository URL: {repository_url}")

    print(dedent("""
        4. Review the documentation:
           - README.md: Project overview and quick start
           - CONTRIBUTING.md: How to contribute
           - OPEN_CODE_CHECKLIST.md: Checklist before publishing code
    """).strip())

    docs_choice = "{{ cookiecutter.docs }}"
    if docs_choice == "mkdocs":
        print("\n5. Build and view documentation:")
        if env_manager == "uv":
            print("   uv run mkdocs serve")
        elif env_manager == "conda":
            print("   conda activate {{ cookiecutter.repo_name }}")
            print("   mkdocs serve")
        elif env_manager == "venv":
            print("   source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate")
            print("   mkdocs serve")
        else:
            print("   mkdocs serve")
        print("   Then visit: http://127.0.0.1:8000")

    print("\n" + "=" * 70)


def main() -> None:
    """Run the repository setup process."""
    print("NHS RAP Repository Setup")
    print("=" * 50)
    print("Project: {{ cookiecutter.project_name }}")
    print("Repository: {{ cookiecutter.repository_url }}")
    print("=" * 50)

    try:
        # Step 1: Git initialization
        try:
            setup_git_repository()
        except SetupError as e:
            print(f"{Colors.RED}\u2717 Git setup failed: {e}{Colors.RESET}")
            status.git_init = "failed"
        except subprocess.CalledProcessError as e:
            print(f"{Colors.RED}\u2717 Git setup command failed: {' '.join(e.cmd)}{Colors.RESET}")
            status.git_init = "failed"

        # Step 2: Git remote setup
        try:
            setup_git_remote()
        except SetupError as e:
            print(f"{Colors.RED}\u2717 Git remote setup failed: {e}{Colors.RESET}")
            status.git_remote = "failed"
        except subprocess.CalledProcessError as e:
            print(f"{Colors.RED}\u2717 Git remote command failed: {' '.join(e.cmd)}{Colors.RESET}")
            status.git_remote = "failed"

        # Step 3: Environment setup - skip remaining steps if this fails
        try:
            setup_environment()
        except SetupError as e:
            print(f"{Colors.RED}\u2717 Environment setup failed: {e}{Colors.RESET}")
            print(f"{Colors.YELLOW}Skipping remaining steps that require the environment{Colors.RESET}")
            status.environment = "failed"
            print_next_steps()
            return
        except subprocess.CalledProcessError as e:
            print(f"{Colors.RED}\u2717 Environment command failed: {' '.join(e.cmd)}{Colors.RESET}")
            print(f"{Colors.YELLOW}Skipping remaining steps that require the environment{Colors.RESET}")
            status.environment = "failed"
            print_next_steps()
            return

        # Step 4: Dependencies
        try:
            install_dependencies()
        except subprocess.CalledProcessError as e:
            print(f"{Colors.RED}\u2717 Dependency installation failed: {' '.join(e.cmd)}{Colors.RESET}")
            status.dependencies = "failed"

        # Step 5: Pre-commit hooks
        try:
            setup_precommit()
        except subprocess.CalledProcessError as e:
            print(f"{Colors.RED}\u2717 Pre-commit setup failed: {' '.join(e.cmd)}{Colors.RESET}")
            status.precommit = "failed"

        # Step 6: Initial commit
        try:
            create_initial_commit()
        except subprocess.CalledProcessError as e:
            print(f"{Colors.RED}\u2717 Initial commit failed: {' '.join(e.cmd)}{Colors.RESET}")
            status.initial_commit = "failed"

        # Always show next steps
        print_next_steps()

    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Setup interrupted by user{Colors.RESET}", file=sys.stderr)
        print_next_steps()
        sys.exit(1)


if __name__ == "__main__":
    main()
