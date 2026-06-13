# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

> Created with the [NHS DSA beginner data-science template](https://github.com/nhsengland/nhs-dsa-cookiecutter).
> New to data-science projects? Start with the **[guides/](guides/)** folder — it
> teaches the good habits this template is built around.

## Quick start

1. **Set up the project** (do this once):

   ```bash
   python scripts/setup_project.py
   ```

   This starts git, creates your environment, installs the packages, turns on
   the pre-commit checks, and makes your first commit. The script is short and
   commented — open it to see exactly what it does.

{% if cookiecutter.environment_manager == 'uv' %}2. **Run the example test** to check everything works:

   ```bash
   uv run pytest
   ```

3. **Start exploring** in a notebook:

   ```bash
   uv run jupyter lab
   ```
{% else %}2. **Activate your environment**, then run the example test:

   ```bash
   source .venv/bin/activate    # on Windows: .venv\Scripts\activate
   pytest
   ```

3. **Start exploring** in a notebook:

   ```bash
   jupyter lab
   ```
{% endif %}

## Learn as you go

The **[guides/](guides/)** folder contains short, friendly tutorials written
for people doing their first real project:

1. [Project structure & why it matters](guides/01-project-structure.md)
2. [From notebooks to modules](guides/02-notebooks-to-modules.md)
3. [Virtual environments](guides/03-virtual-environments.md)
4. [Git basics](guides/04-git-basics.md)
5. [Writing your first test](guides/05-writing-a-first-test.md)
6. [Reading data safely](guides/06-reading-data-safely.md)
7. [Making your first plot](guides/07-making-a-first-plot.md)
8. [What good looks like — a checklist](guides/08-what-good-looks-like.md)

## What's in here

```text
{{ cookiecutter.repo_name }}/
├── README.md            <- You are here
├── pyproject.toml       <- Project + its packages (dependencies)
├── .pre-commit-config.yaml  <- Automatic checks on each commit
├── .env                 <- Secrets and settings (never committed)
│
├── data/                <- Your data (kept out of git)
│   ├── raw/             <- Original data — never edit by hand
│   ├── interim/         <- Part-way through cleaning
│   ├── processed/       <- Final, analysis-ready data
│   └── external/        <- Data from somewhere else
│
├── notebooks/           <- Jupyter notebooks for exploring
├── reports/figures/     <- Saved charts and figures
│
├── {{ cookiecutter.module_name }}/   <- Your reusable Python code
│   ├── config.py        <- File paths and logging
│   └── dataset.py       <- A worked example: loading data safely
│
├── tests/               <- Automated checks for your code
│   └── test_dataset.py  <- A worked example test
│
├── guides/              <- Beginner tutorials (start here!)
├── presentation/        <- Quarto + PowerPoint templates for sharing results
└── scripts/             <- One-off helper scripts (e.g. project setup)
```

## Sharing your results

The **[presentation/](presentation/)** folder has ready-to-fill templates for a
one-page summary and a poster, in both [Quarto](https://quarto.org) (`.qmd`)
and PowerPoint (`.pptx`) formats.
{% if cookiecutter.open_source_license != 'No license file' %}
## Licence

This project is released under the {{ cookiecutter.open_source_license }} licence. See [LICENSE](LICENSE).
{% endif %}
