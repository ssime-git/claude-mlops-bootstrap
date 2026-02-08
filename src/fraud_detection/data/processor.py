"""Data processing and cleaning for fraud detection pipeline."""

from pathlib import Path

import pandas as pd
import structlog

logger = structlog.get_logger()


def process_transactions(input_path: Path, output_path: Path) -> pd.DataFrame:
    """Clean and process raw transaction data.

    Args:
        input_path: Path to raw CSV file.
        output_path: Path to save processed parquet file.

    Returns:
        Processed DataFrame.
    """
    logger.info("processing_transactions", input=str(input_path))

    df = pd.read_csv(input_path)

    # Drop duplicates
    initial_rows = len(df)
    df = df.drop_duplicates()
    logger.info("dropped_duplicates", removed=initial_rows - len(df))

    # Parse timestamps
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Drop rows with null amounts
    df = df.dropna(subset=["amount"])

    # Remove negative amounts
    df = df[df["amount"] > 0]

    # Save processed data
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(output_path, index=False)
    logger.info("processing_complete", rows=len(df), output=str(output_path))

    return df
