# Open Code Checklist

This guide explains how to use the NHS England Open Code Checklist to prepare your code for publication.

!!! info "About This Checklist"
    The Open Code Checklist ensures that code published to private or public repositories meets NHS England standards for clarity, security, and reusability. It provides a systematic review process with specific items to verify before publishing.

## Using the Checklist

The checklist is available in the root of this repository as [`OPEN_CODE_CHECKLIST.md`]({{cookiecutter.repository_url}}/blob/main/OPEN_CODE_CHECKLIST.md).

!!! tip "Related Documentation"
    - [Getting Started Guide](getting_started.md) - Set up your development environment
    - [Contributing Guide](contributing.md) - Development standards and workflow
    - [Testing Guide](testing.md) - Writing and running tests
    - [Usage Guide](usage.md) - How to use this template

### Review Process

1. **Print or open the checklist** for reference during review
2. **Complete all mandatory items** before publication
3. **Consider recommended items** to improve code quality  
4. **Mark completion** in the table with dates and notes
5. **Obtain sign-off** from reviewers and senior responsible owner

!!! tip "Practical Format"
    The checklist uses a table format that allows you to track completion dates, add comments, and document reviewer sign-off for each item. This provides an audit trail for your publication process.

---

## Checklist Categories

The checklist contains 47 items across 5 categories:

### 1. Ownership and Licensing

Ensures others understand who owns the code and how they can use it.

**Key mandatory items:**

- LICENSE file with copyright notice
- Clear README with project purpose
- MHRA medical device assessment
- Security disclosure process
- Security monitoring responsibility

**Included in template:**

- LICENSE file (configurable: MIT, BSD-3-Clause, OGL-3.0)
- LICENSE-OGL file for Open Government License
- [README.md]({{cookiecutter.repository_url}}/blob/main/README.md) template with structured sections
- [CODE_OF_CONDUCT.md]({{cookiecutter.repository_url}}/blob/main/CODE_OF_CONDUCT.md)
- [CONTRIBUTING.md]({{cookiecutter.repository_url}}/blob/main/CONTRIBUTING.md)

### 2. Sensitive Information Protection

Verifies that no sensitive, personal, or classified information is released.

**Key mandatory items:**

- No sensitive data in code or files
- No credentials, API keys, or secrets in code or git history
- No SQL connection strings in code or git history
- Notebook outputs cleared
- Git history clean

**Template tools for protection:**

- **Gitleaks**: Pre-commit hook detects hardcoded secrets (see [.pre-commit-config.yaml]({{cookiecutter.repository_url}}/blob/main/.pre-commit-config.yaml))
- **nbstripout**: Pre-commit hook strips Jupyter outputs (see [.pre-commit-config.yaml]({{cookiecutter.repository_url}}/blob/main/.pre-commit-config.yaml))
- **.env template**: Example file showing how to use environment variables
- **.gitignore**: Pre-configured to exclude sensitive files (see [.gitignore]({{cookiecutter.repository_url}}/blob/main/.gitignore))

!!! warning "Critical: Check Git History"
    Even if sensitive data has been removed from current code, it may still exist in git history. Always review the full history and purge if necessary using tools like BFG Repo-Cleaner or `git filter-repo`.

### 3. Repository Management

Store code in appropriate, well-managed repositories.

**Key items:**

- Code version controlled using Git
- Code in organizational GitHub account (e.g., nhsengland)

### 4. Third-Party Tools and Security

Ensure third-party tools meet security standards.

**Key mandatory items:**

- All dependencies identified
- Tools comply with NCSC Cloud Security Principles

**Template dependency management:**

- [pyproject.toml]({{cookiecutter.repository_url}}/blob/main/pyproject.toml): All dependencies listed with versions
- Multiple environment managers supported (uv, poetry, conda, etc.)
- [Makefile]({{cookiecutter.repository_url}}/blob/main/Makefile): `make requirements` for simple dependency installation

### 5. Code Review and Quality

Conduct thorough internal reviews before publication.

**Key items:**

- Security review by colleague
- Automated security scanning
- Code quality review
- RAP level assessment
- Testing with test data

**Template quality tools:**

- **Ruff or Black/Flake8**: Code formatting and linting (configured in [pyproject.toml]({{cookiecutter.repository_url}}/blob/main/pyproject.toml))
- **pytest**: Unit testing framework (configured in [pyproject.toml]({{cookiecutter.repository_url}}/blob/main/pyproject.toml))
- **pytest-cov**: Code coverage measurement
- **Pre-commit hooks**: Automated quality checks (see [.pre-commit-config.yaml]({{cookiecutter.repository_url}}/blob/main/.pre-commit-config.yaml))
- **Makefile targets**: `make lint`, `make format`, `make test` (see [Makefile]({{cookiecutter.repository_url}}/blob/main/Makefile))

---

## RAP Assessment

The checklist includes a comprehensive [RAP (Reproducible Analytical Pipeline)](https://nhsdigital.github.io/rap-community-of-practice/introduction_to_RAP/levels_of_RAP/) level assessment. The Baseline level is the minimum standard for a RAP.

### Baseline RAP - Getting the Fundamentals Right

**All requirements must be met:**

1. **Data produced by code in an open-source language** (Python, R, SQL)
   - Template uses Python with common data analysis libraries

2. **Code is version controlled** (Git)
   - Initialize Git from project start

3. **Repository includes README.md** with clear reproduction steps
   - Template provides structured README with all required sections

4. **Code has been peer reviewed**
   - Use GitHub pull requests for code review

5. **Code is published in the open** and linked to publication (if relevant)
   - Follow the Open Code Checklist above before publication

### Silver RAP - Implementing Best Practice

**Meeting all Baseline requirements, plus:**

1. **Outputs produced by code with minimal manual intervention**
   - Automate data processing end-to-end

2. **Code well-documented** (user guidance, code structure, docstrings)
   - Use NumPy-style docstrings for functions and classes
   - Document methodology in README and docs/

3. **Code well-organised following standard directory format**
   - Template provides standard structure out of the box

4. **Reusable functions and/or classes** used where appropriate
   - Modularize code in module files under `{{ cookiecutter.module_name }}/`

5. **Code adheres to agreed coding standards** (e.g., PEP8)
   - Template includes `ruff` or `black` for automatic formatting
   - Run `make lint` and `make format`

6. **Pipeline includes testing framework** (unit tests, back tests)
   - Template includes `pytest` - add tests in `tests/unittests/`
   - Run tests with `make test`

7. **Repository includes dependency information**
   - Template uses `pyproject.toml` with all dependencies listed
   - Install with `make requirements`

8. **Logs automatically recorded** to ensure outputs as expected
   - Template includes `loguru` for logging
   - Add logging to your pipeline code

9. **Data handled and output in Tidy data format**
   - Follow [Tidy data principles](https://nhsdigital.github.io/rap-community-of-practice/implementing_RAP/workflow/tidy-data/)

### Gold RAP - Analysis as a Product

**Meeting all Baseline and Silver requirements, plus:**

1. **Code is fully packaged**
   - Template includes `pyproject.toml` for packaging
   - Build with `pip install -e .`

2. **Repository automatically runs tests via CI/CD** or integration tool
   - Set up GitHub Actions for continuous integration
   - Template structure supports CI/CD

3. **Process runs on event-based triggers or schedule**
   - Configure automation based on your needs (e.g., GitHub Actions schedule)

4. **Changes clearly signposted** (changelog, releases, semantic versioning)
   - Use Git tags for releases
   - Maintain CHANGELOG.md
   - Follow semantic versioning (MAJOR.MINOR.PATCH)

!!! success "Template RAP Support"
    This cookiecutter template provides the foundation for all three RAP levels. Many Silver and Gold RAP tools are pre-configured—you just need to use them effectively in your analysis pipeline.

---

## Security Tools Guide

### Pre-configured Security Tools

The template includes these security tools ready to use:

#### Gitleaks (Mandatory)

Detects hardcoded secrets before they reach your repository.

**Enable:**

```bash
pre-commit install
```

**Test:**

```bash
pre-commit run gitleaks --all-files
```

**What it catches:**

- API keys and tokens
- Passwords
- Private keys
- AWS credentials
- Database connection strings

#### nbstripout (Mandatory for Notebooks)

Removes Jupyter notebook outputs that might contain sensitive data.

**Already configured** in `.pre-commit-config.yaml`

**Manual strip:**

```bash
jupyter nbconvert --clear-output --inplace notebook.ipynb
```

#### Additional Pre-commit Hooks

- `check-added-large-files`: Prevents large files from being committed
- `check-merge-conflict`: Detects unresolved merge conflicts
- `check-yaml`: Validates YAML syntax
- `check-toml`: Validates TOML syntax

### Running All Security Checks

```bash
# Install hooks (run once)
pre-commit install

# Run all checks on all files
pre-commit run --all-files

# Run specific check
pre-commit run gitleaks --all-files
```

### Code Quality Checks

```bash
# Check code formatting and linting
make lint

# Auto-format code
make format

# Run tests
make test
```

---

## Common Issues and Solutions

### Secrets in Git History

**Problem:** API keys or passwords were committed in the past but later removed.

**Detection:**

```bash
# Template includes Gitleaks which will catch this
pre-commit run gitleaks --all-files
```

**Solution:**

1. Purge history using BFG Repo-Cleaner or `git filter-repo`
2. Rotate all exposed credentials immediately
3. Use environment variables (template includes `.env` example file)
4. Enable Gitleaks pre-commit hook (run `pre-commit install`)

### Test Data Contains Sensitive Information

**Problem:** Test files in `data/` or `tests/` contain real data.

**Solution:**

1. Replace with synthetic data (use libraries like Faker or Synthea)
2. Use template's data directory structure:
   - `data/raw/`: Raw inputs (gitignored)
   - `data/processed/`: Outputs (gitignored)
   - Create synthetic test data explicitly for `tests/`
3. Document data generation in `tests/README.md`

### Notebook Outputs Reveal Sensitive Data

**Problem:** Jupyter notebooks in `notebooks/` show confidential data.

**Solution:**

1. Template includes `nbstripout` pre-commit hook—ensure it's installed
2. Clear outputs manually if needed:

   ```bash
   jupyter nbconvert --clear-output --inplace notebooks/*.ipynb
   ```

3. Review all notebooks before committing
4. Consider adding output review to your PR process

### Large Files Accidentally Committed

**Problem:** Data files or model files in repository.

**Solution:**

1. Template's `.gitignore` excludes common data/model directories
2. Pre-commit hook `check-added-large-files` catches large files
3. For necessary large files, use Git LFS
4. Remove accidentally committed files:

   ```bash
   git rm --cached large_file.csv
   ```

### Dependencies Not Documented

**Problem:** Unclear what packages are required.

**Solution:**

1. Template uses `pyproject.toml` for all dependencies
2. Update dependencies:

   ```bash
   # Add to [project.dependencies] in pyproject.toml
   # Then sync:
   make requirements
   ```

3. Lock exact versions for reproducibility
4. Document any system-level dependencies in README

---

## Tools Reference

### Makefile Commands

The template provides convenient commands:

```bash
make requirements    # Install dependencies
make lint           # Check code quality
make format         # Auto-format code
make test           # Run unit tests
make clean          # Remove temporary files
make docs           # Build documentation (if mkdocs configured)
```

### Pre-commit Hooks

```bash
pre-commit install              # Enable hooks
pre-commit run --all-files     # Run all hooks
pre-commit autoupdate          # Update hook versions
```

### Testing Commands

```bash
# Run all tests
make test

# Run with coverage
pytest --cov={{ cookiecutter.module_name }} tests/unittests/ --cov-report=term-missing

# Run specific test file
pytest tests/unittests/test_data.py -v
```

---

## Additional Resources

### NHS England Resources

- [NHS RAP Community of Practice](https://github.com/NHSDigital/rap-community-of-practice)
- [NHS England GitHub Organization](https://github.com/nhsengland)
- [RAP Levels of Maturity](https://github.com/NHSDigital/rap-community-of-practice/blob/main/what_is_RAP/levels_of_RAP.md)

### Government Guidance

- [Making Source Code Open and Reusable](https://www.gov.uk/service-manual/technology/making-source-code-open-and-reusable)
- [Quality Assurance of Code for Analysis and Research](https://best-practice-and-impact.github.io/qa-of-code-guidance/)
- [NCSC Cloud Security Principles](https://www.ncsc.gov.uk/collection/cloud-security)

### Medical Device Regulation

- [MHRA Software as a Medical Device Guidance](https://www.gov.uk/government/publications/medical-devices-software-applications-apps)
- [MHRA Decision Flowchart](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/999908/Software_flow_chart_Ed_1-08b-IVD.pdf)

### Security Tools

- [Gitleaks Documentation](https://github.com/gitleaks/gitleaks)
- [Pre-commit Framework](https://pre-commit.com/)
- [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/) (for cleaning git history)

---

## Questions and Support

### Common Questions

**Q: Do I need to complete the checklist for every commit?**  
A: No. Complete the checklist before initial publication and before major releases. Use pre-commit hooks for ongoing security checks.

**Q: What if I can't complete all mandatory items?**  
A: Document any exceptions in the checklist's "Notes/Exceptions" section with justification and approval from your senior responsible owner.

**Q: How do I handle medical device software?**  
A: Complete the [MHRA flowchart](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/999908/Software_flow_chart_Ed_1-08b-IVD.pdf) assessment and document the outcome. Consult your organization's medical device regulatory team if applicable.

**Q: Can I modify the checklist?**  
A: The checklist is a minimum standard. You can add organization-specific items but should not remove mandatory items.

### Getting Help

1. Review the [Contributing Guide](contributing.md) for development standards
2. Consult your team's security lead or information governance officer
3. Raise an issue in the [cookiecutter repository](https://github.com/nhsengland/nhse-rap-cookiecutter)
4. Join the NHS RAP Community of Practice

!!! note "Living Document"
    This checklist is periodically updated to reflect new security requirements and best practices. Check for updates when starting new projects or major releases.
