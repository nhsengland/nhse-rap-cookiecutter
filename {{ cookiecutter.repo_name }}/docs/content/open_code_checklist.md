# Open Code Checklist

This page provides guidance on preparing code for publication using the NHS England Open Code Checklist.

!!! info "About This Checklist"
    The Open Code Checklist ensures that code published to private or public repositories meets NHS England standards for clarity, security, and reusability. Use this checklist before publishing or sharing your code.

## How to Use This Checklist

1. **Review all items** before publishing your code
2. **Complete all mandatory items** at minimum
3. **Consider recommended items** to improve code quality
4. **Document your review** by recording completion dates and reviewers

!!! tip "Quick Start"
    A printable version of this checklist is available in the root of this repository as [`OPEN_CODE_CHECKLIST.md`](../OPEN_CODE_CHECKLIST.md).

---

## Checklist Categories

The checklist is organized into five key areas:

### 1. Clear Ownership and Licensing ✓

Ensure others understand who owns the code and how they can use it.

**Key requirements:**

- License and copyright notice
- Clear README with project purpose
- MHRA medical device assessment
- Security disclosure process
- Maintenance responsibilities

**Related Documentation:** See [Contributing Guide](contributing.md) for development standards.

### 2. Sensitive Information Protection 🔒

Verify that no sensitive, personal, or classified information is released.

**Key requirements:**

- No sensitive data in code or test files
- No credentials, API keys, or secrets
- No SQL connection strings
- Clean git history (including past commits)
- Cleared notebook outputs
- Reviewed screenshots and documentation

!!! warning "Critical Security Check"
    Always check both current code AND git history for sensitive information. Even if sensitive data has been removed in the current version, it may still exist in git history and must be purged.

### 3. Repository Management 📁

Store code in appropriate, well-managed repositories.

**Key requirements:**

- Version control using Git
- Hosted in organizational GitHub account
- Proper repository ownership

### 4. Third-Party Tools and Security 🛡️

Ensure third-party tools meet security standards.

**Key requirements:**

- Inventory of all dependencies
- NCSC Cloud Security Principles compliance
- Documented tool usage

**Related Documentation:** Dependencies should be documented in your project's configuration files (e.g., `pyproject.toml`, `requirements.txt`).

### 5. Code Review and Quality Assurance ⭐

Conduct thorough internal reviews before publication.

**Key requirements:**

- Security review by colleague
- Automated security scanning
- Code quality assessment
- RAP level assessment
- Testing in fresh environment

**Related Documentation:** See [Testing Guide](testing.md) for testing standards.

---

## RAP Assessment

As part of the checklist, assess your project's [RAP (Reproducible Analytical Pipeline) level](https://github.com/NHSDigital/rap-community-of-practice/blob/main/what_is_RAP/levels_of_RAP.md):

| RAP Level | Key Characteristics |
|-----------|---------------------|
| **Baseline** | Version control, peer review, documentation, automated testing |
| **Silver** | Functions/modules, config files, unit tests, error handling, logging |
| **Gold** | Packages, integration tests, continuous integration, dependency management |

Document your current RAP status in your README.

---

## Security Tools

Recommended automated security scanning tools:

=== "Python"

    - **Bandit**: Scans for common security issues in Python code
    - **Safety**: Checks dependencies for known vulnerabilities
    - **GitHub Dependabot**: Automated dependency updates and security alerts
    - **pip-audit**: Audits Python packages for known vulnerabilities

=== "Pre-commit Hooks"

    Configure pre-commit hooks to automatically check for:
    
    - Secrets and credentials (e.g., `detect-secrets`)
    - Large files
    - Notebook output stripping
    
    See this project's `.pre-commit-config.yaml` for examples.

---

## Common Issues and Solutions

### Issue: Credentials in Git History

**Problem**: API keys or passwords were committed in the past but later removed.

**Solution**: 

1. Use BFG Repo-Cleaner or `git filter-repo` to remove sensitive data from history
2. Rotate all exposed credentials immediately
3. Add pre-commit hooks to prevent future commits with secrets

### Issue: Test Data Contains Sensitive Information

**Problem**: Test files or example data contain real patient/user data.

**Solution**:

1. Replace with synthetic data generated using tools like Faker or Synthea
2. Document data generation process in README
3. Ensure test data is clearly marked as artificial

### Issue: Notebook Outputs Reveal Sensitive Information

**Problem**: Jupyter notebook outputs show confidential data or system paths.

**Solution**:

1. Clear all notebook outputs before committing
2. Add pre-commit hook to strip outputs automatically
3. Review all cells for inadvertent information disclosure

---

## External Resources

### NHS England Resources

- [NHS RAP Community of Practice](https://github.com/NHSDigital/rap-community-of-practice)
- [NHS England GitHub Organization](https://github.com/nhsengland)

### Government Guidance

- [Government Digital Service: Making Source Code Open](https://www.gov.uk/service-manual/technology/making-source-code-open-and-reusable)
- [Best Practice and Impact: Quality Assurance of Code](https://best-practice-and-impact.github.io/qa-of-code-guidance/)
- [NCSC Cloud Security Guidance](https://www.ncsc.gov.uk/collection/cloud-security)

### Medical Device Regulation

- [MHRA Software as a Medical Device Guidance](https://www.gov.uk/government/publications/medical-devices-software-applications-apps)

---

## Questions?

If you have questions about any checklist items:

1. Review the [Contributing Guide](contributing.md) for development standards
2. Consult your team's security lead or information governance officer
3. Raise an issue in your project repository for clarification

!!! note "Living Document"
    This checklist is periodically updated to reflect new security requirements and best practices. Check for updates when starting new projects or major releases.
