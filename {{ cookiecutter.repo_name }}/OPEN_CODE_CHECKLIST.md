# Open Code Checklist

Complete this checklist before publishing code to verify it meets NHS England standards for clarity, security, and reusability.

**Instructions**:

- Complete all **Mandatory** items before publication
- **Recommended** items represent best practices that significantly improve code quality
- Fill in the completion section at the end with dates, comments, and sign-off{% if cookiecutter.docs == "mkdocs" %}
- For detailed guidance, see the [documentation site](https://{{cookiecutter.organization_name.lower().replace(' ', '')}}.github.io/{{cookiecutter.repo_name}}/contributing/open_code_checklist/){% else %}
- For detailed guidance, see [docs/content/open_code_checklist.md](docs/content/open_code_checklist.md){% endif %}

**Key Template Resources**:

- [README.md](README.md) - Project overview and setup instructions
- [CONTRIBUTING.md](CONTRIBUTING.md) - Development workflow and standards
- [.pre-commit-config.yaml](.pre-commit-config.yaml) - Pre-configured security hooks
- [Makefile](Makefile) - Common development commands

---

## Checklist

| # | Item | Priority | Completed | Date | Comments | Reviewer |
|---|------|----------|-----------|------|----------|----------|
| **1. Ownership and Licensing** |
| 1.1 | Code has appropriate license with copyright notice (LICENSE file) | Mandatory | ☐ | | | |
| 1.2 | README documents project purpose and scope | Mandatory | ☐ | | | |
| 1.3 | README is clear, concise and complete (see template examples) | Recommended | ☐ | | | |
| 1.4 | MHRA 'software as medical device' assessment completed | Mandatory | ☐ | | | |
| 1.5 | Designated person/team responsible for ongoing support | Recommended | ☐ | | | |
| 1.6 | Security disclosure process defined (SECURITY.md or README) | Mandatory | ☐ | | | |
| 1.7 | Person assigned to monitor security concerns | Mandatory | ☐ | | | |
| 1.8 | Project uses semantic versioning (MAJOR.MINOR.PATCH) | Recommended | ☐ | | | |
| 1.9 | Contribution guidelines included (CONTRIBUTING.md) | Recommended | ☐ | | | |
| 1.10 | Dependencies documented with versions (pyproject.toml) | Recommended | ☐ | | | |
| 1.11 | Code linked to published outputs (papers, reports) | Recommended | ☐ | | | |
| **2. Sensitive Information Protection** |
| 2.1 | No sensitive, personal, secret, or classified data in code | Mandatory | ☐ | | | |
| 2.2 | No unreleased policy information | Mandatory | ☐ | | | |
| 2.3 | No business-sensitive algorithms without approval | Mandatory | ☐ | | | |
| 2.4 | Written permission obtained for any stored data | Mandatory | ☐ | | | |
| 2.5 | Service owners aware of code release | Mandatory | ☐ | | | |
| 2.6 | Data transfers conducted securely (encryption) | Mandatory | ☐ | | | |
| 2.7 | No credentials (API keys, passwords, tokens) in code or history | Mandatory | ☐ | | | |
| 2.8 | No secret keys in code or history | Mandatory | ☐ | | | |
| 2.9 | No SQL addresses or connection strings in code or history | Mandatory | ☐ | | | |
| 2.10 | Commit messages clear and informative | Recommended | ☐ | | | |
| 2.11 | No sensitive information in commit messages | Mandatory | ☐ | | | |
| 2.12 | Git history clean (no previously committed sensitive data) | Mandatory | ☐ | | | |
| 2.13 | Notebook outputs reviewed and cleared (use `nbstripout`) | Mandatory | ☐ | | | |
| 2.14 | Configuration separated from analytical code | Recommended | ☐ | | | |
| 2.15 | Screenshots and figures reviewed for sensitive information | Mandatory | ☐ | | | |
| **3. Repository Management** |
| 3.1 | Code version controlled using Git | Recommended | ☐ | | | |
| 3.2 | Code in organization's GitHub account (e.g., nhsengland) | Recommended | ☐ | | | |
| **4. Third-Party Tools and Security** |
| 4.1 | All third-party tools and dependencies identified | Mandatory | ☐ | | | |
| 4.2 | Third-party tools comply with NCSC Cloud Security Principles | Mandatory | ☐ | | | |
| **5. Code Review and Quality** |
| 5.1 | Colleague reviewed code for security vulnerabilities | Mandatory | ☐ | | | |
| 5.2 | Automated security scanning completed (Gitleaks, pre-commit) | Mandatory | ☐ | | | |
| 5.3 | Code quality review completed | Recommended | ☐ | | | |
| 5.4 | RAP level assessment completed (see RAP checklist below) | Recommended | ☐ | | | |
| 5.5 | Code tested in fresh environment with test data | Recommended | ☐ | | | |
| 5.6 | Unit tests implemented and passing | Recommended | ☐ | | | |
| 5.7 | Linting and formatting checks pass (`make lint`) | Recommended | ☐ | | | |

---

## RAP Level Assessment

Assess your project's [RAP (Reproducible Analytical Pipeline)](https://nhsdigital.github.io/rap-community-of-practice/introduction_to_RAP/levels_of_RAP/) maturity level. The Baseline level is the minimum standard for a RAP.

**Current RAP Level**: ___________ (Baseline / Silver / Gold)

### Baseline RAP - Getting the Fundamentals Right

**All requirements must be met for Baseline RAP:**

| # | Requirement | Completed | Notes / Template Support |
|---|-------------|-----------|-------------------------|
| B.1 | Data produced by code in an open-source language (Python, R, SQL) | ☐ | Template uses Python |
| B.2 | Code is version controlled (Git) | ☐ | Use Git from project start |
| B.3 | Repository includes README.md with clear reproduction steps | ☐ | Template provides README structure |
| B.4 | Code has been peer reviewed | ☐ | Use GitHub pull requests |
| B.5 | Code is published in the open and linked to publication (if relevant) | ☐ | See Open Code Checklist above |

### Silver RAP - Implementing Best Practice

**Meeting all Baseline requirements, plus:**

| # | Requirement | Completed | Notes / Template Support |
|---|-------------|-----------|-------------------------|
| S.1 | Outputs produced by code with minimal manual intervention | ☐ | Automate data processing |
| S.2 | Code well-documented (user guidance, code structure, docstrings) | ☐ | Use NumPy-style docstrings |
| S.3 | Code well-organised following standard directory format | ☐ | Template provides standard structure |
| S.4 | Reusable functions and/or classes used where appropriate | ☐ | Modularize code in module files |
| S.5 | Code adheres to agreed coding standards (e.g., PEP8) | ☐ | Use `ruff` or `black` (included) |
| S.6 | Pipeline includes testing framework (unit tests, back tests) | ☐ | Use `pytest` (included) |
| S.7 | Repository includes dependency information | ☐ | Template uses `pyproject.toml` |
| S.8 | Logs automatically recorded to ensure outputs as expected | ☐ | Use `loguru` (included) |
| S.9 | Data handled and output in Tidy data format | ☐ | Follow Tidy data principles |

### Gold RAP - Analysis as a Product

**Meeting all Baseline and Silver requirements, plus:**

| # | Requirement | Completed | Notes / Template Support |
|---|-------------|-----------|-------------------------|
| G.1 | Code is fully packaged | ☐ | Use `pyproject.toml` (included) |
| G.2 | Repository automatically runs tests via CI/CD or integration tool | ☐ | Set up GitHub Actions |
| G.3 | Process runs on event-based triggers or schedule | ☐ | Configure automation as needed |
| G.4 | Changes clearly signposted (changelog, releases, semantic versioning) | ☐ | Use Git tags and releases |

---

## Guidance Notes

### Security Tools Included in Template

This template includes pre-configured security tools in `.pre-commit-config.yaml`:

- **Gitleaks**: Detects hardcoded secrets
- **nbstripout**: Removes Jupyter notebook outputs
- **Pre-commit hooks**: Automatic checks on commit
- **Ruff**: Linting and formatting (configured in `pyproject.toml`)

**To use these tools:**

1. Install pre-commit hooks: `pre-commit install`
2. Run all hooks: `pre-commit run --all-files`
3. Check for secrets: Gitleaks runs automatically on commit
4. Lint code: `make lint`
5. Format code: `make format`
{% if cookiecutter.docs == "mkdocs" %}
**For detailed guidance**, see the [Security Tools Guide](https://{{cookiecutter.organization_name.lower().replace(' ', '')}}.github.io/{{cookiecutter.repo_name}}/contributing/open_code_checklist/#security-tools-guide) on the documentation site.{% else %}
**For detailed guidance**, see `docs/content/open_code_checklist.md`.{% endif %}

### Common Issues and Solutions

#### Issue: Secrets in Git History

**Problem**: API keys or passwords committed in the past but later removed.

**Solution**:

1. Use BFG Repo-Cleaner or `git filter-repo` to purge history
2. Rotate all exposed credentials immediately
3. Enable Gitleaks pre-commit hook: `pre-commit install`
4. Use environment variables (`.env` file, not committed)

#### Issue: Test Data Contains Real Information

**Problem**: Test files contain real patient/user data.

**Solution**:

1. Replace with synthetic data (use Faker, Synthea)
2. Store test data in `data/raw/` (see README for directory structure)
3. Document data generation in `tests/README.md`
4. Ensure `.gitignore` excludes data directories

#### Issue: Notebook Outputs Reveal Sensitive Data

**Problem**: Jupyter notebooks show confidential data or system paths.

**Solution**:

1. Enable `nbstripout` pre-commit hook: `pre-commit install`
2. Clear outputs: `jupyter nbconvert --clear-output --inplace notebook.ipynb`
3. Review all notebooks in `notebooks/` directory
4. Verify `.pre-commit-config.yaml` includes `nbstripout`

#### Issue: Large Files in Repository

**Problem**: Data files or models accidentally committed.

**Solution**:

1. Check `.gitignore` includes data and model directories
2. Use Git LFS for necessary large files
3. Pre-commit hook `check-added-large-files` will catch issues

---

## Additional Resources

- [NHS England RAP Community of Practice](https://github.com/NHSDigital/rap-community-of-practice)
- [Best Practice and Impact: Quality Assurance of Code](https://best-practice-and-impact.github.io/qa-of-code-guidance/)
- [Government Digital Service: Making Source Code Open](https://www.gov.uk/service-manual/technology/making-source-code-open-and-reusable)
- [NCSC Cloud Security Guidance](https://www.ncsc.gov.uk/collection/cloud-security)
- [MHRA Software as Medical Device Guidance](https://www.gov.uk/government/publications/medical-devices-software-applications-apps)

---

## Completion and Sign-Off

### Project Information

| Field | Value |
|-------|-------|
| **Project Name** | |
| **Publication Date** | |
| **Release Version** | |

### Review and Approval

| Review Role | Name | Title | Email | Date of Sign-Off |
|-------------|------|-------|-------|------------------|
| Primary Reviewer | | | | |
| Security Reviewer | | | | |
| Senior Responsible Owner (SRO) | | | | |

### Notes and Exceptions

| Notes/Exceptions |
|------------------|
| |
| |
| |  
