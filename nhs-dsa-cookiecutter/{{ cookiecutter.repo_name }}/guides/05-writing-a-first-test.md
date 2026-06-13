# 5. Writing your first test

A **test** is a small piece of code that checks your *other* code does what you
expect. Instead of eyeballing a result and hoping, you write down the answer you
expect once — and then the computer checks it for you, every time, forever.

## Why bother?

- **Confidence.** You can change your code and instantly know if you broke
  something.
- **A safety net.** Six months from now, a test catches the mistake you'd
  otherwise have shipped.
- **Documentation.** A good test shows exactly how a function is meant to be used.

## The worked example in this project

Open `tests/test_dataset.py`. It tests the `load_dataset` function from
[reading data safely](06-reading-data-safely.md). Here's the heart of it:

```python
def test_load_dataset_reads_rows_and_columns(tmp_path):
    # Arrange: write a tiny CSV to a temporary folder.
    csv_path = tmp_path / "example.csv"
    csv_path.write_text("name,age\nAda,36\nGrace,45\n")

    # Act: call the function we're testing.
    df = load_dataset(csv_path)

    # Assert: check we got what we expected.
    assert list(df.columns) == ["name", "age"]
    assert len(df) == 2
```

Every test follows the same three-beat rhythm:

1. **Arrange** — set up the situation (here, a small CSV file).
2. **Act** — run the thing you want to test.
3. **Assert** — state what *should* be true. If it isn't, the test fails.

## A couple of things to notice

- **`assert`** is plain Python. `assert len(df) == 2` means "I expect this to be
  true; shout if it isn't."
- **`tmp_path`** is a gift from pytest: a fresh temporary folder for each test.
  Using it means your test never touches your real data and cleans up after
  itself.
- **Test the unhappy path too.** The second test checks that asking for a
  missing file raises a clear error. Code that fails *well* is good code.

## Run the tests

{% if cookiecutter.environment_manager == 'uv' %}```bash
uv run pytest
```
{% else %}```bash
pytest      # with your environment activated
```
{% endif %}

You'll see something like `2 passed`. Green means good.

## Watch a test fail (on purpose)

This is the best way to understand tests. In `dataset.py`, temporarily break
something — for example, make `load_dataset` return `df.head(1)` instead of
`df`. Re-run the tests. You'll see a clear failure explaining that 1 row was
returned where 2 were expected. Now undo your change and watch it pass again.
That red-then-green loop is what testing feels like in real work.

## Try it

Add a third test that checks the first person's name is `"Ada"`:

```python
assert df.loc[0, "name"] == "Ada"
```

Run pytest and watch it pass.

➡️ Next: [Reading data safely](06-reading-data-safely.md)
