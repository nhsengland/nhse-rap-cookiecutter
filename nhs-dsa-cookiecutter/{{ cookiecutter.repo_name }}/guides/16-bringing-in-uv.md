# 16. Bringing in uv

By default this project uses **venv** and **pip** — the environment tools that
ship with Python. They're reliable, universal, and a great place to learn (see
[virtual environments](03-virtual-environments.md)). Once you're comfortable
with how environments work, there's a faster, modern alternative worth knowing:
**[uv](https://docs.astral.sh/uv/)**.

This guide is an optional upgrade, not a requirement. Reach for it when pip
starts to feel slow or fiddly.

{% if cookiecutter.environment_manager == 'uv' %}> **You already chose uv when you created this project**, so it's set up and
> ready. This guide explains *why* it's nice and the handful of commands you'll
> use — think of it as the manual you didn't read yet.
{% endif %}

## What uv gives you

uv does the jobs of several tools (venv, pip, and more) in one fast program:

- **Speed.** Installing packages is dramatically faster — often seconds where
  pip took minutes.
- **No "activate" step.** `uv run <command>` finds the right environment
  automatically, so you can't forget to activate it.
- **A lockfile.** uv records the *exact* versions it installed in a `uv.lock`
  file, so a colleague gets a byte-for-byte identical environment.
- **It manages Python itself.** uv can install the Python version your project
  needs, so "it works on my machine" stops being a problem.

## Installing uv

Follow the one-line installer at <https://docs.astral.sh/uv/getting-started/installation/>.
It doesn't touch your system Python — it sits alongside it.

## Switching this project over

Your `pyproject.toml` already lists everything uv needs (the template set it up
to work with both tools). From the project folder:

```bash
uv sync          # create .venv and install everything from pyproject.toml
```

That's the equivalent of the `python -m venv` + `pip install -e ".[dev]"` you
ran before — but faster, and it writes a `uv.lock` for reproducibility.

## The commands you'll actually use

| With pip + venv | With uv |
|-----------------|---------|
| `source .venv/bin/activate` then `pytest` | `uv run pytest` |
| `source .venv/bin/activate` then `jupyter lab` | `uv run jupyter lab` |
| edit `pyproject.toml`, then `pip install -e .` | `uv add seaborn` |
| `pip install -e ".[dev]"` | `uv sync` |

The headline change: **you stop activating environments.** Prefix the command
with `uv run` and uv sorts out the rest.

## Adding a package the uv way

```bash
uv add seaborn        # installs it AND records it in pyproject.toml for you
```

No more "install it, then remember to add it to the file" — uv does both in one
step, and updates the lockfile too.

## Should you switch?

There's no rush. pip and venv will serve you perfectly well for a long time, and
understanding them makes you a better engineer. But once environments feel
familiar and you're tired of waiting for installs, uv is a small, friendly
upgrade that pays off every day.

## Try it

Install uv, run `uv sync` in this project, then `uv run pytest`. Notice you
never typed `activate` — and notice how quick it was.

➡️ Next: [Bridging to the full RAP template](17-bridging-to-the-full-rap-template.md)
