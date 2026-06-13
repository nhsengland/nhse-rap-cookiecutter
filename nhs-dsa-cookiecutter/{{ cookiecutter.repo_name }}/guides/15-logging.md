# 15. Logging

When you're exploring in a notebook, `print()` is fine. But as your code grows
into real scripts and functions, `print` becomes a blunt tool. **Logging** is
the grown-up version: messages that carry a level of importance, a timestamp,
and that you can turn up or down without deleting a single line.

This project already includes **[loguru](https://loguru.readthedocs.io/)**, a
lovely, simple logging library — and `config.py` has set it up for you.

## print vs logging

A `print` says one thing flatly. A log message also tells you **how important**
it is and **when** it happened:

```text
2026-06-13 10:24:01 | INFO     | Reading data from data/raw/example.csv
2026-06-13 10:24:01 | SUCCESS  | Loaded 2 rows and 2 columns
```

That extra context is exactly what you want when something goes wrong and you're
reading back through what happened.

## Using the logger

The logger is ready to import from `config.py`:

```python
from {{ cookiecutter.module_name }}.config import logger

logger.info("Starting the cleaning step")
logger.success("Finished — 1,240 rows written")
logger.warning("Found 3 rows with missing ages; dropping them")
logger.error("Could not connect to the database")
```

You've already seen it at work: open `{{ cookiecutter.module_name }}/dataset.py`
and you'll see `logger.info(...)` and `logger.success(...)` reporting what the
function did. That's why running the example prints those tidy status lines.

## The levels, and when to use them

Pick the level that matches the message's importance:

| Level | Use it for |
|-------|-----------|
| `debug` | Fine detail, useful only when hunting a bug. |
| `info` | Normal progress: "started X", "loaded N rows". |
| `success` | A step finished well (a loguru nicety). |
| `warning` | Something odd you handled, but the reader should know about. |
| `error` | Something failed. |

The point of levels is that you can later say "only show me warnings and above"
and all the chatty `debug`/`info` lines go quiet — without editing your code.

## Why this beats scattering `print`

- **You can dial the volume.** Turn logging up while debugging, down when it's
  running smoothly.
- **You get context for free** — timestamps and levels, every time.
- **It can go to a file.** loguru can write logs to a file as easily as to the
  screen, so you have a record of a long job: `logger.add("run.log")`.
- **It's easy to find and remove.** Stray `print` statements are noise; log
  lines are intentional.

## A simple rule of thumb

Use `print` for quick, throwaway checks in a notebook. Use `logger` in the code
that lives in `{{ cookiecutter.module_name }}/` — anything you'll run more than
once or hand to someone else.

## Try it

Open a Python shell or notebook and run:

```python
from {{ cookiecutter.module_name }}.config import logger

logger.info("Hello from the logger")
logger.warning("This one stands out in the output")
```

Notice the timestamp and level on each line. Now add a `logger.info(...)` to a
function of your own and watch it narrate what your code is doing.

➡️ Next: [Bringing in uv](16-bringing-in-uv.md)
