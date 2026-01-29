# Open Code Checklist

This checklist ensures that code published to private or public repositories meets NHS England standards for clarity, security, and reusability. Review all items before publishing your code, completing mandatory items at minimum.

## Overview

Use this checklist to verify your code is ready for publication. Items marked **Mandatory** must be completed. Items marked **Recommended** represent best practices that significantly improve code quality.

---

## 1. Clear Ownership and Licensing

Ensure others understand who owns the code and how they can use it.

### License and Documentation

- [ ] **Mandatory**: Does your code have an appropriate license with copyright notice?
  - *Add a LICENSE file (e.g., MIT, Apache-2.0, OGL-3.0)*
  - *Include copyright notice: `Copyright © [Year] Crown Copyright ([Organization])`*

- [ ] **Mandatory**: Does the README document the project's intended purpose?
  - *Clearly state what the code does and what problems it solves*

- [ ] **Recommended**: Is the README clear, concise, and complete?
  - *Consider using the [NHS England template](https://github.com/nhsengland/nhse-rap-cookiecutter) or [best practice examples](https://github.com/othneildrew/Best-README-Template)*
  - *Include: purpose, installation, usage, contributing guidelines*

### Regulatory Compliance

- [ ] **Mandatory**: Have you assessed whether MHRA 'software as a medical device' guidance applies?
  - *Use the [MHRA flowchart](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/999908/Software_flow_chart_Ed_1-08b-IVD.pdf)*
  - *Document the assessment outcome in your README*

### Maintenance and Support

- [ ] **Recommended**: Is there a designated person/team responsible for ongoing support?
  - *State in README: "Maintained by [Team/Person]" or "No longer actively maintained (last updated: [Date])"*

- [ ] **Mandatory**: Has a responsible disclosure process for security issues been defined?
  - *Add SECURITY.md or document in README*
  - *Consider using GitHub Security Advisories*

- [ ] **Mandatory**: Is someone assigned to monitor and address security concerns?
  - *Assign responsibility for reviewing security reports*

### Versioning and Collaboration

- [ ] **Recommended**: Does the project use semantic versioning?
  - *Follow [semver](https://semver.org/): MAJOR.MINOR.PATCH (e.g., 1.2.3)*
  - *Tag releases in Git*

- [ ] **Recommended**: Are contribution guidelines included?
  - *Add CONTRIBUTING.md with guidelines for pull requests, code style, and testing*
  - *See examples: [GOV.UK contribution guidelines](https://github.com/alphagov/govuk-frontend/blob/master/CONTRIBUTING.md)*

- [ ] **Recommended**: Are dependencies documented with version numbers?
  - *Use requirements.txt, pyproject.toml, environment.yml, or equivalent*
  - *Pin or specify compatible version ranges*

- [ ] **Recommended**: Is the code linked to published outputs (papers, reports)?
  - *Add links/DOIs in README to help others cite your work*

---

## 2. Sensitive Information Protection

Verify that no sensitive, personal, or classified information is released.

### Data and Policy

- [ ] **Mandatory**: Does the code contain any sensitive, personal, secret, or classified data?
  - *Review all data files, test data, and example datasets*
  - *Use synthetic/dummy data only*

- [ ] **Mandatory**: Does the code contain unreleased policy information?
  - *Confirm all policy references are public*

- [ ] **Mandatory**: Does the code include business-sensitive algorithms (e.g., financial allocations)?
  - *Obtain approval before publishing proprietary algorithms*

- [ ] **Mandatory**: Has written permission been obtained from data owners for any stored data?
  - *Document data usage agreements*

- [ ] **Mandatory**: Are service owners aware of the code release?
  - *Notify and obtain approval from relevant stakeholders*

- [ ] **Mandatory**: Are data transfers conducted securely?
  - *Use encryption for data in transit*
  - *Follow NHS data handling guidelines*

### Secrets and Credentials

- [ ] **Mandatory**: Are there any credentials in the source code?
  - *Check current code AND git history*
  - *Remove: API keys, passwords, access tokens, service accounts*

- [ ] **Mandatory**: Are there any secret keys in the source code?
  - *Check current code AND git history*
  - *Use environment variables or secret management services*

- [ ] **Mandatory**: Are there SQL server addresses or connection strings in the source code?
  - *Check current code AND git history*
  - *Use environment variables or configuration files (not committed)*

### Git History and Commits

- [ ] **Recommended**: Are commit messages clear and informative?
  - *Use conventional commits: `feat:`, `fix:`, `docs:`, etc.*

- [ ] **Mandatory**: Do commit messages contain sensitive information (e.g., names, credentials)?
  - *Review entire git history*

- [ ] **Mandatory**: Does the git history contain any previously committed sensitive information?
  - *Even if removed in current version, sensitive data in history must be purged*
  - *Consider using tools like BFG Repo-Cleaner if needed*

### Notebooks and Documentation

- [ ] **Mandatory**: Have notebook outputs been reviewed and cleared?
  - *Check Jupyter notebooks for sensitive data in outputs*
  - *Consider using pre-commit hooks to strip outputs: [Example](https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.pre-commit-config.yaml)*

- [ ] **Recommended**: Is configuration separated from analytical code?
  - *Use config files (YAML, JSON, TOML) separate from analysis scripts*

- [ ] **Mandatory**: Have screenshots and figures been reviewed for sensitive information?
  - *Check all images in documentation, presentations, and reports*

---

## 3. Repository Management

Store code in appropriate, well-managed repositories.

- [ ] **Recommended**: Is the code version controlled using Git?
  - *All production code should use version control*

- [ ] **Recommended**: Is the code in your organization's GitHub account?
  - *Ensure repository ownership aligns with funding organization*
  - *Use NHS England GitHub organization for NHS England projects*

---

## 4. Third-Party Tools and Security

Ensure third-party tools meet security standards.

- [ ] **Mandatory**: Have you identified all third-party tools and dependencies?
  - *Maintain an inventory of external libraries, APIs, and services*
  - *Document in README or DEPENDENCIES.md*

- [ ] **Mandatory**: Do all third-party tools comply with [NCSC Cloud Security Principles](https://www.ncsc.gov.uk/collection/cloud-security/implementing-the-cloud-security-principles)?
  - *Verify compliance for cloud services, hosting platforms, and external APIs*

---

## 5. Code Review and Quality Assurance

Conduct thorough internal reviews before publication.

### Security Review

- [ ] **Mandatory**: Has a colleague reviewed the code for sensitive data and security vulnerabilities?
  - *Use automated security scanning tools (e.g., Bandit, safety, GitHub Dependabot)*
  - *Document tools used and review date*

### Code Quality

- [ ] **Recommended**: Has a code quality review been completed focusing on usability and clarity?
  - *Consider using quality frameworks like [BIP Code Quality Checklist](https://best-practice-and-impact.github.io/qa-of-code-guidance/checklist_higher.html)*
  - *Review: readability, maintainability, documentation, modularity*

- [ ] **Recommended**: Has the code been assessed for its [RAP (Reproducible Analytical Pipeline) level](https://github.com/NHSDigital/rap-community-of-practice/blob/main/what_is_RAP/levels_of_RAP.md)?
  - *Determine level: Baseline, Silver, or Gold*
  - *Document current RAP status in README*

### Testing

- [ ] **Recommended**: Has the code been tested?
  - *At minimum: verify code runs in a fresh environment with artificial/test data*
  - *Best practice: unit tests, integration tests, continuous integration*
  - *Document testing approach in README or TESTING.md*

---

## Additional Resources

- [NHS England RAP Community of Practice](https://github.com/NHSDigital/rap-community-of-practice)
- [Best Practice and Impact: Quality Assurance of Code](https://best-practice-and-impact.github.io/qa-of-code-guidance/)
- [Government Digital Service: Making Source Code Open](https://www.gov.uk/service-manual/technology/making-source-code-open-and-reusable)
- [NCSC Cloud Security Guidance](https://www.ncsc.gov.uk/collection/cloud-security)

---

## Completion

Once you have completed this checklist:

1. **Document**: Record completion date and reviewer name in your project
2. **Archive**: Keep a copy of this checklist with your project documentation
3. **Review**: Revisit this checklist for major updates or before each release

**Checklist completed by**: ________________  
**Date**: ________________  
**Reviewer**: ________________  
**Date**: ________________  
