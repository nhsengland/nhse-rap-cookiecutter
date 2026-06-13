"""A worked example test for `load_dataset`.

This is a complete, passing test you can learn from. It shows the classic
"arrange, act, assert" shape:

1. Arrange: create a tiny CSV file to read.
2. Act: call the function we want to test.
3. Assert: check we got back what we expected.

`tmp_path` is a built-in pytest fixture that gives you a fresh temporary
folder, so the test never touches your real data. Run all tests with:

    pytest

The guide in ``guides/05-writing-a-first-test.md`` walks through this in detail.
"""

import pytest

from {{ cookiecutter.module_name }}.dataset import load_dataset


def test_load_dataset_reads_rows_and_columns(tmp_path):
    """A small CSV is loaded into a DataFrame with the right shape."""
    # Arrange: write a tiny CSV with 2 columns and 2 rows of data.
    csv_path = tmp_path / "example.csv"
    csv_path.write_text("name,age\nAda,36\nGrace,45\n")

    # Act: load it.
    df = load_dataset(csv_path)

    # Assert: we got the columns and rows we expect.
    assert list(df.columns) == ["name", "age"]
    assert len(df) == 2
    assert df.loc[0, "name"] == "Ada"


def test_load_dataset_missing_file_gives_clear_error(tmp_path):
    """Asking for a file that doesn't exist raises a helpful error."""
    missing = tmp_path / "does_not_exist.csv"

    # `pytest.raises` checks that the expected error is raised.
    with pytest.raises(FileNotFoundError):
        load_dataset(missing)
