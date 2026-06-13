# 6. Reading data safely

Loading a data file is the very first step of almost every project — and it's
where a surprising number of confusing errors come from. This guide shows how to
read data in a way that fails *clearly* when something's wrong, instead of
leaving you puzzled.

## Use paths from `config.py`, not hand-typed strings

It's tempting to write:

```python
df = pd.read_csv("data/raw/example.csv")
```

This breaks the moment you run your code from a different folder, because
`"data/raw/..."` is relative to wherever you happen to be. Instead, this project
defines the locations once, in `{{ cookiecutter.module_name }}/config.py`:

```python
from {{ cookiecutter.module_name }}.config import RAW_DATA_DIR

df = pd.read_csv(RAW_DATA_DIR / "example.csv")
```

`RAW_DATA_DIR` is an *absolute* path worked out from the project's location, so
it's correct no matter where you run from. The `/` joins paths in a way that
works on Windows, macOS, and Linux alike.

## Check the file exists before reading it

If you call `pd.read_csv` on a missing file, you get a long, intimidating error.
A friendlier approach is to check first and raise a clear message. That's exactly
what `load_dataset` in `{{ cookiecutter.module_name }}/dataset.py` does:

```python
if not path.exists():
    raise FileNotFoundError(
        f"Could not find a data file at: {path}\n"
        "Put your CSV in the data/raw/ folder, or pass the correct path."
    )
```

Now the error tells you the *what* and the *how-to-fix*, not just the *where it
blew up*.

## Walk through it end to end

1. Create a small CSV. In a terminal, from the project folder:

   ```bash
   printf "name,age\nAda,36\nGrace,45\n" > data/raw/example.csv
   ```

2. Open a notebook (or a Python shell) and load it:

   ```python
   from {{ cookiecutter.module_name }}.dataset import load_dataset

   df = load_dataset()          # uses data/raw/example.csv by default
   df.head()
   ```

   You'll see the loguru log lines ("Reading data from…", "Loaded 2 rows…") and
   then your table.

3. Now try a file that doesn't exist:

   ```python
   load_dataset("data/raw/nope.csv")
   ```

   Instead of a cryptic pandas error, you get the clear `FileNotFoundError`
   message above. That's the whole point.

## A few more safe-loading habits

- **Peek before you trust.** After loading, run `df.head()`, `df.shape`, and
  `df.info()` to confirm the data looks the way you expect.
- **Don't overwrite raw data.** Read from `data/raw/`, and write any cleaned
  version to `data/processed/`.
- **Keep secrets out of code.** If loading data needs a password or API key, put
  it in `.env` (see `config.py`, which loads it for you) — never hard-code it.

➡️ Next: [Making your first plot](07-making-a-first-plot.md)
