# 3. Virtual environments

A **virtual environment** is a private box of Python packages that belongs to
one project. It's one of those ideas that sounds fussy until the day it saves
you hours.

## The problem it solves

Imagine two projects on your laptop. Project A needs pandas version 1, Project B
needs pandas version 2. If you install packages "globally" (for your whole
computer), these two projects fight over the same pandas — and one of them
breaks.

A virtual environment gives **each project its own packages**, at the versions
that project needs. They never interfere with each other.

## How it works here

This project lists the packages it needs in `pyproject.toml`. When you ran the
setup script, it created a virtual environment in a hidden `.venv/` folder and
installed those packages into it.

{% if cookiecutter.environment_manager == 'uv' %}This project uses **uv**, a fast, modern tool that manages the environment for
you. The two commands you'll use most:

```bash
uv sync                 # create/update the environment from pyproject.toml
uv run pytest           # run a command inside the environment
```

The lovely thing about `uv run` is that you don't have to "activate" anything —
uv finds the right environment automatically.
{% else %}This project uses **venv** and **pip**, which come built into Python. To use the
environment, you "activate" it first:

```bash
source .venv/bin/activate    # on Windows: .venv\Scripts\activate
```

Your prompt changes to show `(.venv)`. Now any `python` or `pytest` command
uses this project's packages. When you're done, type `deactivate`.

Once you're comfortable with this, there's a faster, more modern tool called
**uv** that handles environments for you. It's an optional upgrade, not
something you need now — see [Bringing in uv](16-bringing-in-uv.md) when you're
ready.
{% endif %}

## Adding a new package

When you need a new package (say, `seaborn` for nicer charts):

1. Add it to the `dependencies` list in `pyproject.toml`.
{% if cookiecutter.environment_manager == 'uv' %}2. Run `uv sync` to install it.
{% else %}2. Run `pip install -e .` (with the environment activated) to install it.
{% endif %}

Why edit the file rather than just installing it? Because `pyproject.toml` is
the **recipe** for your environment. Anyone who clones your project can recreate
the exact same setup from it. An install you did by hand and forgot to record is
an install nobody else can reproduce.

## The golden rule

**Never commit the `.venv/` folder to git.** It's large, machine-specific, and
fully recreatable from `pyproject.toml`. This project's `.gitignore` already
excludes it.

## Try it

{% if cookiecutter.environment_manager == 'uv' %}Run `uv run python -c "import pandas; print(pandas.__version__)"`. You just ran
Python inside the project's environment without activating anything.
{% else %}Activate the environment, then run
`python -c "import pandas; print(pandas.__version__)"`. Type `deactivate` and
try the same command — outside the environment, pandas may not be found. That's
the box at work.
{% endif %}

➡️ Next: [Pandas basics](04-pandas-basics.md)
