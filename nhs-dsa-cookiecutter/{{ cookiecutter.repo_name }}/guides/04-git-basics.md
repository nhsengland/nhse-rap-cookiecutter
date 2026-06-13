# 4. Git basics

**Git** is a tool that saves snapshots of your project over time. Think of it as
an unlimited, labelled undo history: you can always go back to how things were,
see what changed and when, and share your work with others.

## The three commands you'll use constantly

```bash
git status      # what has changed since the last snapshot?
git add .       # stage your changes, ready to be saved
git commit -m "Describe what changed"   # save a snapshot (a "commit")
```

A **commit** is one saved snapshot with a short message describing it. The
setup script already made your first commit for you.

## Make a commit, step by step

1. Change something — edit a file, add a notebook.
2. See what changed:

   ```bash
   git status
   ```

3. Stage the changes you want to save:

   ```bash
   git add .
   ```

4. Save the snapshot with a clear message:

   ```bash
   git commit -m "Add chart of patient ages"
   ```

That's the whole loop. Do it often.

## What makes a good commit

- **Small and focused.** One change per commit. "Clean the date column" is
  better than "lots of stuff". If something breaks later, small commits make it
  easy to find which change caused it.
- **A message that finishes the sentence "This commit will…"** —
  *"…add a test for load_dataset"*, *"…fix the off-by-one in the row count"*.
- **Committed often.** A commit is a save point. More save points, less risk.

## What not to commit

Some things should never go into git:

- **Data** — it can be large or sensitive. (Already handled by `.gitignore`.)
- **Secrets** — passwords and API keys. Put those in `.env`, which is ignored.
- **Your virtual environment** — the `.venv/` folder. (Also ignored.)

This project's `.gitignore` takes care of all three. When you run `git status`,
you should only ever see *your own work* listed.

## Going further

Once you're comfortable, the natural next steps are **branches** (working on a
change in isolation) and **pushing** to a remote like GitHub (backing up and
sharing your work). You don't need them on day one — but `add`, `commit`, and
clear messages will serve you well from the very start.

## Try it

Add a line to this project's README, then run `git status`, `git add .`, and
`git commit -m "Tweak the README"`. Run `git log --oneline` to see your commit
sitting in the history next to the initial one.

➡️ Next: [Writing your first test](05-writing-a-first-test.md)
