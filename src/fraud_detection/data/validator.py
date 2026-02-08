"""Data validation using Great Expectations."""

from pathlib import Path
from typing import Any

import pandas as pd
import structlog

logger = structlog.get_logger()

EXPECTATIONS_DIR = Path("great_expectations/expectations")


def validate_transactions(df: pd.DataFrame) -> dict[str, Any]:
    """Validate transaction data against the fraud suite.

    Args:
        df: DataFrame with transaction data.

    Returns:
        Validation results dict with success flag and details.
    """
    logger.info("validating_transactions", rows=len(df))

    results: dict[str, Any] = {"success": True, "checks": []}

    # Amount checks
    amount_positive = bool((df["amount"] > 0).all())
    results["checks"].append({"name": "amount_positive", "passed": amount_positive})

    amount_bounded = bool((df["amount"] < 1_000_000).all())
    results["checks"].append({"name": "amount_bounded", "passed": amount_bounded})

    # Null checks
    merchant_not_null = bool(df["merchant_id"].notna().all())
    results["checks"].append({"name": "merchant_not_null", "passed": merchant_not_null})

    timestamp_not_null = bool(df["timestamp"].notna().all())
    results["checks"].append({"name": "timestamp_not_null", "passed": timestamp_not_null})

    results["success"] = all(c["passed"] for c in results["checks"])

    if results["success"]:
        logger.info("validation_passed", checks=len(results["checks"]))
    else:
        failed = [c["name"] for c in results["checks"] if not c["passed"]]
        logger.warning("validation_failed", failed_checks=failed)

    return results
