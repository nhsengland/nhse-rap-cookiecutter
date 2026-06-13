# NHS DSA Cookiecutter

A lightweight, **beginner-focused** [cookiecutter](https://cookiecutter.readthedocs.io/)
template for your first real data-science project. It gives you a tidy project
layout, a friendly starter module, a worked example test, and — the part that
makes it different — a **`guides/` folder of short tutorials** that teach the
good habits the structure is built around.

It's a slimmed-down cousin of the
[NHS RAP cookiecutter](https://github.com/nhsengland/nhse-rap-cookiecutter):
same good bones, but with the governance and admin depth removed and learning
material put front and centre. If you're building a production pipeline, use the
RAP template. If you're finding your feet, start here.

## What you get

A generated project contains:

- **Sensible folders** — `data/{raw,interim,processed,external}`, `notebooks/`,
  `reports/figures/`.
- **A small, friendly module** — `config.py` (paths + logging) and a worked
  `dataset.py` example for loading data safely.
- **A worked example test** in `tests/`.
- **`guides/`** — 18 beginner tutorials in three parts: *understand your
  project* (structure & file tour), *basic skills* (environments, pandas,
  notebooks → modules, reading data, plotting, git, GitHub, keeping data safe,
  and an intro to **RAP** and its levels), and *going further* (writing tests,
  functional coding, logging, bringing in uv, and bridging to the full RAP
  template).
- **`presentation/`** — Quarto (`.qmd`) and PowerPoint (`.pptx`) templates for a
  one-page summary and a poster.
- **An Open Code checklist** (`OPEN_CODE_CHECKLIST.md`) to run through before
  sharing code publicly.
- **Sensible tooling** — `pyproject.toml` with **pip + venv** as the default
  environment manager (uv optional), and a light `.pre-commit-config.yaml`
  (ruff + nbstripout + whitespace fixes + **gitleaks** secret-scanning).
- **A short, readable setup script** (`scripts/setup_project.py`) you can learn
  from — it does `git init`, installs the environment, turns on pre-commit, and
  makes your first commit.

## Quick start

You can generate a project in two ways.

**With the installed CLI:**

```bash
pip install nhs-dsa-cookiecutter      # or: uv tool install nhs-dsa-cookiecutter
nhs-dsa-template
```

**With cookiecutter directly:**

```bash
cookiecutter gh:nhsengland/nhs-dsa-cookiecutter
```

You'll be asked a handful of questions:

| Prompt | Meaning | Default |
|--------|---------|---------|
| `project_name` | A human-friendly name | *My Data Science Project* |
| `author_name` | Your name | *Your Name* |
| `description` | One line about the project | — |
| `python_version_number` | Python version to target | *3.11* |
| `environment_manager` | `pip+venv` or `uv` | *pip+venv* |
| `open_source_license` | `MIT`, `Apache-2.0`, or none | *MIT* |

The `repo_name` and `module_name` are derived from `project_name` automatically.

Once generated, follow the new project's README — its first step is to run
`python scripts/setup_project.py`.

## Developing this template

```bash
uv sync --extra dev          # install dev dependencies
uv run pytest                # run the bake + no-leftover-marker test suite
```

The tests bake the template with several prompt combinations and assert that no
unrendered Jinja markers or staging files are left behind.

## Licence

Released under the [MIT License](LICENSE).
