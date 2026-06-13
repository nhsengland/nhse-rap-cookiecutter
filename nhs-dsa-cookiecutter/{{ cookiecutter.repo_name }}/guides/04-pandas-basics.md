# 4. Pandas basics

**pandas** is the workhorse library for data in Python. It gives you the
**DataFrame** — a table with named columns, a bit like a spreadsheet you can
control with code. Almost every data project starts here.

This guide is a five-minute tour of the handful of operations you'll use again
and again. Run the snippets in a notebook (`notebooks/`) as you read.

## Getting some data to play with

```python
import pandas as pd

df = pd.DataFrame(
    {
        "name": ["Ada", "Grace", "Alan", "Edith"],
        "age": [36, 45, 41, 28],
        "team": ["A", "A", "B", "B"],
    }
)
```

`df` is now a DataFrame with four rows and three columns.

## Looking at your data first

Before doing anything, *look* at it. These four are your constant companions:

```python
df.head()      # the first few rows
df.shape       # (rows, columns) — e.g. (4, 3)
df.info()      # column names, types, and how many values are missing
df.describe()  # quick stats (mean, min, max…) for the number columns
```

Building the habit of peeking first catches a huge number of mistakes early.

## Picking out columns and rows

```python
df["age"]                 # one column
df[["name", "age"]]       # several columns (note the double brackets)

df[df["age"] > 40]        # only the rows where age is over 40
df[df["team"] == "A"]     # only team A
```

That `df[df["age"] > 40]` pattern — "give me the rows where a condition is
true" — is called **filtering**, and you'll use it constantly.

## Making a new column

```python
df["age_in_5_years"] = df["age"] + 5
```

pandas applies the `+ 5` to every row at once — no loop needed. Doing things to
a whole column at a time is the pandas way, and it's much faster than looping.

## Grouping and summarising

One of pandas' superpowers is answering "for each group, what's the…?":

```python
df.groupby("team")["age"].mean()
```

This reads almost like English: *group by team, take the age column, and give me
the mean for each group.* Swap `.mean()` for `.sum()`, `.count()`, `.max()`, and
so on.

## Reading and writing files

In real projects your data comes from a file. Use the project's paths from
`config.py` (see [reading data safely](06-reading-data-safely.md)):

```python
from {{ cookiecutter.module_name }}.config import RAW_DATA_DIR, PROCESSED_DATA_DIR

df = pd.read_csv(RAW_DATA_DIR / "example.csv")     # read
df.to_csv(PROCESSED_DATA_DIR / "cleaned.csv", index=False)  # write
```

Remember the golden rule from earlier guides: **read from `raw/`, write to
`processed/`** — never overwrite your original data.

## Try it

With the `df` from the top of this guide:

1. Filter to just team B and print it.
2. Add a column `is_senior` that is `True` when `age` is 40 or over
   (`df["age"] >= 40`).
3. Use `groupby` to find the average age per team.

When your settled pandas code starts repeating, that's your cue for the next
guide.

➡️ Next: [From notebooks to modules](05-notebooks-to-modules.md)
