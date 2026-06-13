# 10. Keeping data & secrets safe

In health and care analytics this is the guide that matters most. Code can be
shared freely; **data and secrets cannot**. Getting this wrong — committing
patient data or a password to a public repository — is the kind of mistake that
causes real harm. The good news: a few simple habits, mostly automated for you,
keep you safe.

## The golden rule

**Your code can be public. Your data must stay private.**

These are separate things that happen to live in the same folder. Git is set up
so your code travels and your data stays put. Your job is to not accidentally
mix them.

## How this project protects you

Three layers, all already switched on:

1. **`.gitignore`** lists things git must never track — the whole `data/`
   folder, your `.env` file, and your `.venv/` environment. Run `git status`:
   you should only ever see *your own code and notebooks*, never data.
2. **`nbstripout`** (a pre-commit hook) clears the outputs from Jupyter
   notebooks before they're committed. This matters because a notebook's saved
   output can contain rows of real data.
3. **`gitleaks`** (a pre-commit hook) scans every commit for things that look
   like passwords, API keys, and tokens — and blocks the commit if it finds one.

You don't run these by hand; they run automatically once pre-commit is
installed (the setup script did that).

## Secrets go in `.env`, never in code

A **secret** is anything that proves who you are: a database password, an API
key, a connection string. The rule is simple: **never type a secret into a
`.py` file or a notebook.** Instead, put it in `.env`:

```bash
# .env  (this file is git-ignored — it never leaves your machine)
DATABASE_PASSWORD=super-secret-value
```

and read it in your code from the environment:

```python
import os
password = os.environ["DATABASE_PASSWORD"]
```

`config.py` already loads `.env` for you when your code starts, so this just
works. The secret stays on your machine; only the *name* `DATABASE_PASSWORD`
ever appears in your code.

## If a secret does slip through

Deleting a secret in a new commit is **not** enough — it's still sitting in your
git history for anyone to find. So:

1. **Treat it as compromised.** Change the password / revoke the key straight
   away. This is the important step.
2. Then clean the history (rewriting history is fiddly — ask a colleague or
   search for "remove secret from git history" / the BFG tool).

This is exactly why `gitleaks` blocks the secret *before* it's ever committed —
prevention is far easier than cleanup.

## Before you publish: the Open Code checklist

When you're ready to share your code — especially publicly — work through
[`OPEN_CODE_CHECKLIST.md`](../OPEN_CODE_CHECKLIST.md) in the project root. It's a
short, practical list that boils down to: no data, no secrets, a licence, and a
README. Working "in the open" is encouraged in health analytics, and the
checklist lets you do it safely.

## Try it

1. Run `git status`. Confirm no data files or `.env` are listed.
2. Open `.env` and add a fake secret like `TEST_KEY=abc123`. Confirm `git status`
   still doesn't show `.env` — it's protected by `.gitignore`.
3. (Optional, to see `gitleaks` work) put a realistic-looking key *in a `.py`
   file*, `git add` it, and try to commit. Watch pre-commit stop you. Then
   remove it.

➡️ Next: [What is RAP?](11-what-is-rap.md)
