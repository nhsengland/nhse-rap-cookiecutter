# 13. Writing good tests

[Writing your first test](12-writing-a-first-test.md) showed the mechanics:
arrange, act, assert. This guide is about writing tests that are genuinely
*useful* — the difference between a test that catches real bugs and one that
just makes the green number go up.

## Test behaviour, not implementation

A good test checks **what** a function should do, not **how** it does it. Test
the inputs and outputs you care about; stay out of the internal details.

```python
# Good: checks the promised behaviour.
assert load_dataset(csv_path).shape == (2, 2)

# Fragile: breaks if you rename an internal variable, even when nothing's wrong.
assert load_dataset.__code__.co_varnames[0] == "path"
```

If a small, harmless refactor breaks your test, the test was checking the wrong
thing.

## Test the unhappy paths

Beginners test the case where everything goes right. The bugs live where things
go *wrong*. For every function, ask: what should happen with bad input?

```python
import pytest

def test_missing_file_raises_clearly():
    with pytest.raises(FileNotFoundError):
        load_dataset("does/not/exist.csv")
```

`pytest.raises` says "I *expect* this to fail in this specific way." A function
that fails clearly and predictably is a well-behaved one.

## One behaviour per test, with a name that says what it checks

A test name is documentation. When it fails, the name alone should tell you
what broke:

```python
def test_load_dataset_keeps_all_columns(): ...
def test_load_dataset_skips_blank_rows(): ...
```

Better than one giant `test_load_dataset` that checks ten things — when it
fails, you'd have no idea which of the ten broke.

## Cover the edge cases

The bugs hide at the boundaries. For each function, jot down the awkward cases
and write a quick test for each:

- **Empty** input — an empty DataFrame, an empty list.
- **One** item — code that assumes "many" often trips on exactly one.
- **Duplicates**, **missing values** (`NaN`), **unexpected types**.
- The **boundary** itself — if a rule is "age ≥ 40", test 39, 40, and 41.

## Don't repeat yourself: fixtures and parametrize

When several tests need the same starting data, a **fixture** builds it once:

```python
import pandas as pd
import pytest

@pytest.fixture
def people():
    return pd.DataFrame({"name": ["Ada", "Grace"], "age": [36, 45]})

def test_has_two_people(people):
    assert len(people) == 2
```

When you want to run the *same* test over many inputs, **parametrize** it
instead of copy-pasting:

```python
@pytest.mark.parametrize("age,expected", [(39, False), (40, True), (41, True)])
def test_is_senior(age, expected):
    assert (age >= 40) == expected
```

One test, three cases, no duplication.

## Run them often

{% if cookiecutter.environment_manager == 'uv' %}```bash
uv run pytest
```
{% else %}```bash
pytest      # with your environment activated
```
{% endif %}

Tests are only a safety net if you actually use them. Run them after every
meaningful change, and always before you push.

## Try it

Take the example test in `tests/test_dataset.py` and add: (1) an edge-case test
for an empty CSV, and (2) a parametrized test covering two or three inputs. Run
pytest and watch them all pass.

➡️ Next: [Functional coding](14-functional-coding.md)
