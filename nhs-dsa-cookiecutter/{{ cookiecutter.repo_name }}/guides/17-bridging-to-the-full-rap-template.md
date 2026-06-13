# 17. Bridging to the full RAP template

This template is the **beginner's on-ramp**. It deliberately keeps things small
and friendly so you can learn the habits without being overwhelmed. Once those
habits feel natural, there's a bigger sibling waiting for you: the
**[NHS RAP cookiecutter](https://github.com/nhsengland/nhse-rap-cookiecutter)** —
the template for production-grade Reproducible Analytical Pipelines.

This guide explains what the full template adds, and how to step up when you're
ready.

## You're already most of the way there

If you've worked through these guides, you're comfortably doing **Baseline** and
much of **Silver** RAP (see [what is RAP?](11-what-is-rap.md)): version control,
a README, a standard layout, reusable functions, tests, dependency management,
and logging. That's a genuinely strong foundation — most of the journey is
behind you.

## What the full RAP template adds

The full template is aimed at teams shipping analysis on a schedule, so it layers
on the heavier machinery this one leaves out:

- **Continuous integration (CI/CD).** Tests and checks run automatically on every
  push (e.g. GitHub Actions) — a key step towards **Gold** RAP. Here you run
  `pytest` yourself; there it runs for you, every time.
- **Packaging for distribution.** Set up to be built and shared as a proper,
  installable package.
- **Deeper documentation tooling.** Generated docs, contribution guides, and
  templates for issues and pull requests.
- **Governance & admin scaffolding.** The organisational paperwork a published
  NHS pipeline needs — which we stripped out here to keep things light.
- **More configuration.** More prompts and options to fit a wider range of
  production setups.

## How to make the jump

You don't migrate a project file-by-file. Instead, **start your next, more
serious project from the full template**:

```bash
cookiecutter gh:nhsengland/nhse-rap-cookiecutter
```

Everything you've learned here carries straight over — the folder layout, the
config/paths pattern, tests, logging, and pre-commit are the same ideas, just
with more around them. You'll recognise the shape immediately.

## A sensible path

1. **Finish a project or two with this template.** Let the habits settle.
2. **Read [what is RAP?](11-what-is-rap.md)** and aim to tick every Silver box.
3. **Add CI to a project** — even a single GitHub Action that runs your tests is
   a real taste of Gold RAP.
4. **Start your next big piece of work from the full template**, and lean on the
   [RAP Community of Practice](https://nhsdigital.github.io/rap-community-of-practice/)
   for guidance.

There's no rush, and no wasted effort: every habit in this template is a habit
the full one expects. You've been building towards it all along.

➡️ Next: [What good looks like](18-what-good-looks-like.md)
