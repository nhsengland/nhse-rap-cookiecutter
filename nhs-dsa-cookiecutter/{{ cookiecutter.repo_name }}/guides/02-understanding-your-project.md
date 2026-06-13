# 2. Understanding your project

This project didn't appear by magic — it was generated from a **template**
(a "cookiecutter") that answered a few questions about you and your project and
then filled in all the files. This guide is a quick tour of the pieces that make
it tick, so nothing feels like a black box.

## What "generated from a template" means

When the project was created, you (or someone) answered prompts like
*project name*, *author*, and *which Python version*. The template took those
answers and stamped them into every file. That's why the README already has your
project's name, and the code folder is named after your project — you didn't
type any of that by hand.

You don't need the template again to work on your project. From here on, this is
just **your** project: ordinary files you can edit freely.

## The key files, and what each one is for

| File | What it does |
|------|--------------|
| `pyproject.toml` | The project's **recipe**: its name, the Python version, and the list of packages it needs. The single source of truth for your environment. |
| `.pre-commit-config.yaml` | A list of small automatic checks that run every time you commit (formatting, secret-scanning, clearing notebook outputs). |
| `.gitignore` | The list of things git should **ignore** — your data, your `.env`, your virtual environment. |
| `.env` | Your private settings and secrets. Never committed. `config.py` reads it for you. |
| `README.md` | The front page: what the project is and how to run it. |
| `OPEN_CODE_CHECKLIST.md` | A safety checklist to run through before sharing the code publicly. |

## The code folder

The folder named after your project (e.g. `{{ cookiecutter.module_name }}/`) is
your **Python package** — the reusable code you'll write. It starts with two
small, worked examples:

- **`config.py`** works out where your project lives on disk and gives you ready-
  made paths like `RAW_DATA_DIR` and `FIGURES_DIR`. It also sets up logging and
  loads your `.env`. Using it means you never hand-type fragile file paths.
- **`dataset.py`** is a worked example of loading data safely — the kind of
  function you'll write a lot of.

## The helper script

`scripts/setup_project.py` is the script you run once at the start. It's
deliberately short and commented: it starts git, builds your environment,
installs the packages, switches on pre-commit, and makes your first commit.
Open it — every line is a command you could have typed yourself. Reading it is
the fastest way to understand what "setting up a project" actually involves.

## Try it

Open `pyproject.toml` and find the `dependencies` list. Every package your
project can `import` is named there. Now open `{{ cookiecutter.module_name }}/config.py`
and find `RAW_DATA_DIR`. These two files — the recipe and the paths — are the
backbone you'll lean on in every later guide.

➡️ Next: [Virtual environments](03-virtual-environments.md)
