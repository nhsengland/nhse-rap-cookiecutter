"""Configuration module for {{ cookiecutter.project_name }}.

This module provides project-wide configuration including:
- Directory paths for data, models, and reports
- Environment variable loading from .env files
- Logger configuration with tqdm integration

Attributes:
    PROJ_ROOT: Root directory of the project.
    DATA_DIR: Base directory for all data storage.
    RAW_DATA_DIR: Directory for original, immutable data.
    INTERIM_DATA_DIR: Directory for intermediate transformed data.
    PROCESSED_DATA_DIR: Directory for final, canonical datasets.
    EXTERNAL_DATA_DIR: Directory for data from third-party sources.
    MODELS_DIR: Directory for trained model files.
    REPORTS_DIR: Directory for generated reports.
    FIGURES_DIR: Directory for generated figures and plots.
"""

from pathlib import Path

from dotenv import load_dotenv
from loguru import logger

# Load environment variables from .env file if it exists
load_dotenv()

# Paths
PROJ_ROOT = Path(__file__).resolve().parents[1]
logger.info(f"PROJ_ROOT path is: {PROJ_ROOT}")

DATA_DIR = PROJ_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

MODELS_DIR = PROJ_ROOT / "models"

REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# If tqdm is installed, configure loguru with tqdm.write
# https://github.com/Delgan/loguru/issues/135
try:
    from tqdm import tqdm

    logger.remove(0)
    logger.add(lambda msg: tqdm.write(msg, end=""), colorize=True)
except ModuleNotFoundError:
    pass
