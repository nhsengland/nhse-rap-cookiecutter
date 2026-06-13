# 14. Functional coding

As your analysis grows, the thing that keeps it understandable isn't cleverness —
it's **structure**. "Functional" coding here doesn't mean anything academic; it
means building your work out of small, well-named **functions** that each do one
thing. It's the single habit that most improves data code.

## Why functions

A script that's one long top-to-bottom flow is hard to read, hard to test, and
hard to reuse. Break it into functions and you get:

- **Readability** — `clean_dates(df)` tells the reader what's happening; ten
  lines of date-wrangling don't.
- **Reusability** — call it from a notebook, a script, or a test.
- **Testability** — a small function with a clear input and output is easy to
  test (see the previous two guides).

## What makes a good function

**One job, clear name.** A function should do one thing, and its name should say
what. If you need "and" to describe it (`clean_and_plot`), it's probably two
functions.

```python
# One job each — easy to read, reuse, and test.
def clean_ages(df):
    return df[df["age"].between(0, 120)]

def average_age_by_team(df):
    return df.groupby("team")["age"].mean()
```

**Inputs in, result out.** The most reliable functions take what they need as
arguments and **return** a result — rather than reaching out to global variables
or printing. Given the same input, they always give the same output. That
predictability is what makes them easy to reason about and test.

```python
# Good: everything it needs comes in; the answer comes out.
def add_tax(price, rate):
    return price * (1 + rate)

# Harder to test: depends on a global, and returns nothing useful.
TAX_RATE = 0.2
def add_tax_bad(price):
    print(price * (1 + TAX_RATE))
```

## Don't change your inputs by surprise

A function that quietly modifies the DataFrame it was handed causes
hard-to-find bugs, because the caller's data changes behind their back. Prefer
returning a **new** result and leaving the input alone:

```python
# Good: caller's df is untouched; they get a new, filtered df back.
def adults_only(df):
    return df[df["age"] >= 18]

adults = adults_only(df)   # df itself is unchanged
```

This mirrors the "never overwrite `data/raw/`" rule from the data guides — the
same instinct, applied to code.

## Build big things from small ones

Once you have small, trustworthy functions, your analysis becomes a short,
readable story of calling them in turn:

```python
df = load_dataset()
df = clean_ages(df)
summary = average_age_by_team(df)
```

Anyone can read those three lines and understand the whole pipeline — and each
step has its own test.

## Try it

Look at your busiest notebook. Find a chunk of logic that does one identifiable
thing and pull it into a named function in `{{ cookiecutter.module_name }}/`.
Make it take its data as an argument and return a result. Call it from the
notebook — and, while you're there, write a quick test for it.

➡️ Next: [Logging](15-logging.md)
