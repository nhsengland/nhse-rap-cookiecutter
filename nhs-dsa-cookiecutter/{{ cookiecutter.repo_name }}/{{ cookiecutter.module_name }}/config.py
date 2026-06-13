"""Project configuration: file paths and logging.

Import the paths from here instead of writing file locations by hand. That way
your code works the same on your laptop, a colleague's machine, or a server —
no matter where the project folder lives.

    from {{ cookiecutter.module_name }}.config import RAW_DATA_DIR, logger

    logger.info("Loading data...")
    df = pd.read_csv(RAW_DATA_DIR / "my_data.csv")
"""

from pathlib import Path

from dotenv import load_dotenv
from loguru import logger

# Load any variables defined in the .env file (e.g. API keys) so they are
# available via os.environ. Safe to call even if there is no .env file.
load_dotenv()

# PROJ_ROOT is the top of the project. `parents[1]` means "two folders up from
# this file": config.py -> {{ cookiecutter.module_name }}/ -> project root.
PROJ_ROOT = Path(__file__).resolve().parents[1]

# Data folders. Keep raw data read-only and write everything you create
# into interim/ or processed/.
DATA_DIR = PROJ_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"             # original, untouched data
INTERIM_DATA_DIR = DATA_DIR / "interim"     # part-way through cleaning
PROCESSED_DATA_DIR = DATA_DIR / "processed" # final, analysis-ready data
EXTERNAL_DATA_DIR = DATA_DIR / "external"   # data from someone else

# Where reports and figures go.
REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

logger.info(f"Project root is: {PROJ_ROOT}")
