"""Loading data — a worked example.

This is real, working code (not a placeholder). It shows one good-practice
pattern for reading a CSV file safely:

* take a clear input (a file path),
* check the file actually exists before trying to read it,
* return a tidy pandas DataFrame,
* log what happened so you can see it working.

There is a matching test in ``tests/test_dataset.py``. Run it with ``pytest``
and watch it pass — then change this code and watch the test tell you what
broke. That feedback loop is the whole point.
"""

from pathlib import Path

import pandas as pd
from loguru import logger

from {{ cookiecutter.module_name }}.config import RAW_DATA_DIR


def load_dataset(path: Path | None = None) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame.

    Args:
        path: Path to the CSV file. If omitted, defaults to
            ``data/raw/example.csv`` inside the project.

    Returns:
        The file's contents as a pandas DataFrame.

    Raises:
        FileNotFoundError: If the file does not exist. Catching this early,
            with a clear message, is much friendlier than a confusing error
            from deep inside pandas.
    """
    if path is None:
        path = RAW_DATA_DIR / "example.csv"
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(
            f"Could not find a data file at: {path}\n"
            "Put your CSV in the data/raw/ folder, or pass the correct path."
        )

    logger.info(f"Reading data from {path}")
    df = pd.read_csv(path)
    logger.success(f"Loaded {len(df)} rows and {len(df.columns)} columns")
    return df
