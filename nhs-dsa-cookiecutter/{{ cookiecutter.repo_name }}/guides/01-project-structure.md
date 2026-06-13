# 1. Project structure & why it matters

When you start out, it's tempting to keep everything in one folder (or one
giant notebook). It works — until it doesn't. A month later you can't remember
which file is the "real" one, where the data came from, or which chart is up to
date. A consistent structure fixes this before it becomes a problem.

## The idea

**Every kind of thing has one obvious home.** Raw data, cleaned data, code,
charts, and notebooks each live in their own folder. Once you learn the layout,
you (and your teammates) always know where to look.

## The folders in this project

| Folder | What goes here |
|--------|----------------|
| `data/raw/` | The original data, exactly as you received it. **Never edit these files.** |
| `data/interim/` | Data you're part-way through cleaning. |
| `data/processed/` | Final, tidy, analysis-ready data. |
| `data/external/` | Data from someone else (e.g. a lookup table). |
| `notebooks/` | Jupyter notebooks for exploring and experimenting. |
| `{{ cookiecutter.module_name }}/` | Reusable Python code (functions you call from notebooks). |
| `tests/` | Automated checks that your code works. |
| `reports/figures/` | Saved charts and figures. |
| `guides/` | These tutorials. |
| `presentation/` | Templates for sharing your results. |

## Two habits worth forming now

**Treat `data/raw/` as read-only.** Your raw data is the one thing you can't
recreate. If your cleaning code has a bug, you want to be able to start again
from the untouched original. So: read from `raw/`, write to `interim/` or
`processed/`, and never overwrite the raw files.

**Keep data out of git.** Data can be large, private, or both. This project's
`.gitignore` already keeps the `data/` folder out of version control — only the
empty folder structure is tracked. Your code and your data travel separately.

## Why this pays off

- **Future-you understands it.** Come back in three months and the layout still
  makes sense.
- **Others can help.** A colleague can find their way around without a tour.
- **Mistakes are reversible.** Raw data stays safe, so a bug is never a disaster.

## Try it

Open the project folder and match each item to the table above. Notice that the
data folders are empty apart from a hidden `.gitkeep` file — that's a trick to
keep an otherwise-empty folder in git. Drop a CSV into `data/raw/` and you're
ready for the [reading data safely](06-reading-data-safely.md) guide.

➡️ Next: [Understanding your project](02-understanding-your-project.md)
