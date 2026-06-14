# 11. What is RAP?

Everything you've learned so far — a tidy structure, environments, git, tests,
keeping data safe — isn't just "good coding". In health and care analytics it
has a name: **RAP**, short for **Reproducible Analytical Pipelines**.

This short guide explains what RAP is, why it matters, and the **levels** you can
aim for. Think of it as the "why" behind this whole template.

## What RAP means

A **Reproducible Analytical Pipeline** is analysis built so that **the same code,
run on the same data, always produces the same result** — with as little manual,
point-and-click work as possible.

Contrast that with the old way: download a file, do some clicks in a spreadsheet,
copy a number into a document, screenshot a chart. Every manual step is a chance
for an unrecorded mistake, and nobody — including future-you — can reliably
reproduce it.

RAP replaces those manual steps with **code that is version-controlled, tested,
documented, and shareable**. The payoff:

- **Trust** — results can be checked and reproduced by others.
- **Time saved** — re-running next quarter is one command, not a day of clicking.
- **Transparency** — the method is open for anyone to inspect (see
  [keeping data & secrets safe](10-keeping-data-and-secrets-safe.md) for how code
  can be open while data stays private).

This template is a gentle on-ramp to RAP: it bakes the good habits in from day
one, so you're already working the RAP way without having to think about it.

## The levels of RAP

RAP isn't all-or-nothing. The NHS RAP Community of Practice defines three
**levels**, so teams can improve step by step rather than all at once.

### 🥉 Baseline RAP — the minimum standard

- Data produced by code in an open-source language (Python, R, SQL).
- Code is version controlled (git).
- A README explains how to reproduce the work.
- Code has been peer reviewed.
- Code is published openly, linked to the publication.

### 🥈 Silver RAP — best practice

Everything in Baseline, plus:

- Outputs produced by code with minimal manual steps.
- Well documented — user guidance, structure, and docstrings.
- A standard directory layout.
- Reusable **functions** (and/or classes) where appropriate.
- Agreed coding standards followed.
- A **testing** framework.
- **Dependency** information recorded.
- **Logging** so you can confirm outputs are as expected.
- Data handled and output in a **tidy** data format.

### 🥇 Gold RAP — analysis as a product

Everything in Silver, plus:

- Code is fully **packaged**.
- Tests run automatically via **CI/CD**.
- Runs on a schedule or event-based trigger.
- Changes signposted with a changelog or releases.

## Where this template sits

You might notice how much of **Baseline** and **Silver** this little project
already sets you up for: version control, a README, a standard layout, reusable
functions, tests, dependency management in `pyproject.toml`, and logging. By
working through these guides you're not just learning to code — you're learning
to do **Silver-level RAP**.

The remaining guides ([tests](12-writing-a-first-test.md),
[functional coding](14-functional-coding.md), [logging](15-logging.md)) deepen
exactly these habits, and the final guide,
[bridging to the full RAP template](17-bridging-to-the-full-rap-template.md),
shows how to step up towards Gold.

## Learn more

- [What is RAP? — RAP Community of Practice](https://nhsdigital.github.io/rap-community-of-practice/introduction_to_RAP/what_is_RAP/)
- [Levels of RAP](https://nhsdigital.github.io/rap-community-of-practice/introduction_to_RAP/levels_of_RAP/)

➡️ Next: [Writing your first test](12-writing-a-first-test.md)
