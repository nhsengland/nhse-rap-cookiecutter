# Open Code Checklist

Working "in the open" — publishing your analysis code so others can read, reuse,
and check it — is a core part of good practice in health and care analytics. It
makes your work more transparent, more reproducible, and more useful to others.

But **open code is not the same as open data.** The single most important rule is
that your *code* can be public while your *data* stays private. This checklist
helps you publish safely.

> New to this? Read **[guides/10 — keeping data & secrets safe](guides/10-keeping-data-and-secrets-safe.md)**
> first. This file is the checklist; that guide explains the "why".

## Before you make a repository public

Work through these. If you can't tick a box, fix it before you publish.

### No data, no secrets

- [ ] **No data files are committed.** Run `git ls-files | grep -i -E '\.csv|\.xlsx|\.parquet|\.db'` —
      it should return nothing. The `.gitignore` already excludes `data/`.
- [ ] **No patient-level or person-identifiable data anywhere** — not in code,
      not in notebook outputs, not in test fixtures, not in commit history.
- [ ] **Notebook outputs are cleared.** The `nbstripout` pre-commit hook does
      this for you, but double-check — outputs can contain real data.
- [ ] **No secrets.** No passwords, API keys, connection strings, or tokens in
      the code. They belong in `.env` (which is git-ignored). The `gitleaks`
      pre-commit hook scans for these automatically.
- [ ] **No secrets in your git *history*.** A secret you committed last week is
      still there even if you delete it today. If you find one, treat it as
      compromised: rotate it, then clean the history (ask for help — it's fiddly).
- [ ] **No internal-only details** that shouldn't be public — server names,
      internal URLs, file paths that reveal infrastructure, colleagues' personal
      contact details.

### It can be understood and reused

- [ ] **There's a README** that says what the project does and how to run it.
- [ ] **There's an open licence** (this template offers MIT or Apache-2.0). Code
      without a licence can't legally be reused by others.
- [ ] **The code runs from a clean clone.** A colleague could follow the README,
      create the environment from `pyproject.toml`, and run it.
- [ ] **Comments and names are professional** — no rude words, no half-finished
      "TODO: this is rubbish" notes you wouldn't want the world to read.

### It's good enough to stand behind

- [ ] **The example/important code has tests**, and they pass.
- [ ] **Pre-commit is installed and passing**, so style and secret checks run on
      every commit.
- [ ] **You have permission to publish.** Check your organisation's policy and,
      if in doubt, ask your manager or information-governance team first.

## A note on proportion

You don't need a perfect, polished repository to work in the open — you need a
*safe* one. The "no data, no secrets" section is non-negotiable. The rest is
about being a good citizen, and it gets easier every time.

## Learn more

- [NHS England — RAP community of practice](https://nhsdigital.github.io/rap-community-of-practice/)
- [The Goldacre Review — *Better, broader, safer*](https://www.goldacrereview.org/) (the case for open code in health data)
- [choosealicense.com](https://choosealicense.com/) — pick an open licence
