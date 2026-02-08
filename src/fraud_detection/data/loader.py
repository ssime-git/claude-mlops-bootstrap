"""Data loading utilities for fraud detection pipeline."""

from pathlib import Path

import pandas as pd
import structlog

logger = structlog.get_logger()


def load_transactions(path: Path) -> pd.DataFrame:
    """Load transaction data from CSV file.

    Args:
        path: Path to the CSV file.

    Returns:
        DataFrame with transaction data.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If required columns are missing.
    """
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")

    logger.info("loading_transactions", path=str(path))
    df = pd.read_csv(path)

    required_columns = {"amount", "merchant_id", "timestamp", "is_fraud"}
    missing = required_columns - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    logger.info("transactions_loaded", rows=len(df), columns=list(df.columns))
    return df
