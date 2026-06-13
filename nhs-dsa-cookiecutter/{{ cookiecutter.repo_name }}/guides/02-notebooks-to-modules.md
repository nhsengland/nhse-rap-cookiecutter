# 2. From notebooks to modules

Notebooks are wonderful for exploring: you run a cell, see the result, tweak it,
run again. But notebooks have a weakness — code in a notebook is hard to reuse,
hard to test, and easy to run in the wrong order. The fix is to move your
*settled* code into a Python module.

## Notebooks vs modules

- A **notebook** (`notebooks/explore.ipynb`) is your workbench: messy,
  experimental, full of half-finished ideas. That's fine — that's its job.
- A **module** (`{{ cookiecutter.module_name }}/dataset.py`) is your toolbox:
  tidy, reusable functions you trust.

The skill is knowing when to move something from the workbench to the toolbox.

## A good rule of thumb

**When you copy-paste a chunk of code for the second time, turn it into a
function and move it into the module.** Repetition is the signal.

## A worked example

Say your notebook keeps loading a CSV like this:

```python
import pandas as pd
df = pd.read_csv("data/raw/example.csv")
```

This project already moved that into a reusable function in
`{{ cookiecutter.module_name }}/dataset.py`:

```python
def load_dataset(path=None):
    ...
    return pd.read_csv(path)
```

Now, from any notebook, you can simply write:

```python
from {{ cookiecutter.module_name }}.dataset import load_dataset

df = load_dataset("data/raw/example.csv")
```

The benefits stack up:

- **One source of truth.** Fix a bug once, and every notebook gets the fix.
- **It can be tested.** See [writing your first test](05-writing-a-first-test.md).
- **Notebooks stay readable.** They show *what* you're doing, not the plumbing.

## Importing your own code into a notebook

Because this project is installed into your environment (the setup script ran
`uv sync` or `pip install -e .`), you can import your module from anywhere —
no fiddling with file paths. If you add a new function to the module while a
notebook is open, restart the notebook kernel to pick it up.

## Try it

1. Open a notebook in `notebooks/`.
2. Import and call `load_dataset` as shown above.
3. Add a second function to `dataset.py` — say, one that returns only the rows
   where a column is above some value — and call it from the notebook too.

➡️ Next: [Virtual environments](03-virtual-environments.md)
