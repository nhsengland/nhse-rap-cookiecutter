# Repository Migration Checklist

This document tracks the changes needed when migrating from `josephwilson8-nhs/nhse-rap-cookiecutter` to `nhsengland/nhs-rap-cookiecutter`.

## Files with Commented Updates

All files below have commented sections marked with `TODO: Update to nhsengland organization once transferred`. Simply uncomment the `nhsengland` lines and remove the `josephwilson8-nhs` lines.

### 1. pyproject.toml

- Lines 51-56: Update project URLs
    - Homepage
    - Source Code
    - Bug Tracker

### 2. mkdocs.yml

- Lines 5-7: Update site_url and repo_url
- Lines 54-56: Update social link in footer

### 3. README.md

- Lines 7-10: Update badges for NHS RAP and tests
- Lines 168-170: Update contributing guide link
- Lines 176-178: Update contributing section link
- Lines 184-186: Update git clone command

### 4. {{ cookiecutter.repo_name }}/README.md

- Lines 3-5: Update template badge link

### 5. docs/content/index.md

- Lines 6-8: Update tests badge

### 6. docs/content/contributing.md

- Lines 187-190: Update GitHub Issues and documentation links

### 7. docs/content/getting_started.md

- Lines 112-114: Update git clone command

## Post-Migration Steps

1. **Search and Replace**

   ```bash
   # Find all remaining references (should only be in comments)
   grep -r "josephwilson8-nhs" .
   
   # Uncomment nhsengland lines and remove josephwilson8-nhs lines
   ```

2. **Update GitHub Settings**
   - Enable GitHub Pages from the `main` branch `/docs` folder or set up GitHub Actions
   - Configure branch protection rules
   - Set up required status checks

3. **Update PyPI** (if published)
   - Update package metadata
   - Upload new version with updated URLs

4. **Test Everything**

   ```bash
   # Test template generation
   uv run nhs-rap-template --no-input
   
   # Test documentation build
   uv run mkdocs build
   
   # Run tests
   uv run pytest tests/
   ```

5. **Verify Links**
   - Check all documentation links work
   - Verify badges display correctly
   - Test GitHub Actions workflows (if any)

## Quick Find & Replace Commands

```bash
# After migration, run these from the repository root:

# Update pyproject.toml
sed -i 's|josephwilson8-nhs/nhse-rap-cookiecutter|nhsengland/nhs-rap-cookiecutter|g' pyproject.toml
sed -i 's|josephwilson8-nhs\.github\.io/nhse-rap-cookiecutter|nhsengland.github.io/nhs-rap-cookiecutter|g' pyproject.toml

# Update mkdocs.yml
sed -i 's|josephwilson8-nhs/nhse-rap-cookiecutter|nhsengland/nhs-rap-cookiecutter|g' mkdocs.yml
sed -i 's|josephwilson8-nhs\.github\.io/nhse-rap-cookiecutter|nhsengland.github.io/nhs-rap-cookiecutter|g' mkdocs.yml

# Update README.md
sed -i 's|josephwilson8-nhs/nhse-rap-cookiecutter|nhsengland/nhs-rap-cookiecutter|g' README.md
sed -i 's|josephwilson8-nhs\.github\.io/nhse-rap-cookiecutter|nhsengland.github.io/nhs-rap-cookiecutter|g' README.md

# Update template README
sed -i 's|josephwilson8-nhs/nhse-rap-cookiecutter|nhsengland/nhs-rap-cookiecutter|g' "{{ cookiecutter.repo_name }}/README.md"

# Update docs
sed -i 's|josephwilson8-nhs/nhse-rap-cookiecutter|nhsengland/nhs-rap-cookiecutter|g' docs/content/*.md
sed -i 's|josephwilson8-nhs\.github\.io/nhse-rap-cookiecutter|nhsengland.github.io/nhs-rap-cookiecutter|g' docs/content/*.md

# Then manually review and uncomment the TODO sections, removing old commented lines
```

## Notes

- All current URLs use `josephwilson8-nhs` and are fully functional
- All future URLs using `nhsengland` are included as comments for easy migration
- No functionality is affected by the current setup
- Migration can be done quickly using the commands above
