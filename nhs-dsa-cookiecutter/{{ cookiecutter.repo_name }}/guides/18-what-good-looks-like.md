# 18. What good looks like — a checklist

You don't need to do everything perfectly. But a handful of habits separate a
project that's a pleasure to pick up from one that's a headache. Here's a
friendly checklist to glance at before you share your work or call it "done".

None of this is about being clever — it's about being kind to the next person
who opens your project (often future-you).

## The code

- [ ] **Repeated code is a function.** If you've copy-pasted something twice,
      it belongs in `{{ cookiecutter.module_name }}/` as a function.
- [ ] **Functions have clear names.** `clean_dates` tells you more than `process`.
- [ ] **Paths come from `config.py`**, not hand-typed strings scattered around.
- [ ] **No secrets in the code.** Passwords and keys live in `.env`.

## The data

- [ ] **Raw data is untouched.** You read from `data/raw/` and write elsewhere.
- [ ] **No data is committed to git.** `git status` shows only your own work.
- [ ] **You've sanity-checked it.** You've looked at `df.head()` and `df.shape`
      and the numbers make sense.

## Tests

- [ ] **The example test still passes.** Run it before you share:
{% if cookiecutter.environment_manager == 'uv' %}      `uv run pytest`.
{% else %}      `pytest` (with your environment activated).
{% endif %}
- [ ] **Your important code has at least one test.** Especially anything fiddly.

## Reproducibility

- [ ] **A colleague could recreate your environment** from `pyproject.toml`
      with a single command.
- [ ] **Figures are saved by code**, not screenshotted, so they regenerate.
- [ ] **The README explains how to run it.** Could someone get started without
      asking you?

## Version control

- [ ] **Your work is committed** in small steps with clear messages.
- [ ] **Pre-commit is on** — the tidy-up checks run automatically on each commit.

## Sharing

- [ ] **A short write-up exists.** Even a one-pager (see `presentation/`) helps
      people understand what you did and why.
- [ ] **You've removed dead ends.** Delete the experiments that went nowhere, or
      move them out of the way.

## Remember

This is a direction, not a finish line. A first project that ticks even half of
these is in great shape. Come back to this list as your project grows — each
habit gets easier the second time, and soon they're just how you work.

Well done for getting this far. 🎉

⬅️ Back to the [guides index](README.md)
