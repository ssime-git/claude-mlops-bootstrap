"""Model evaluation utilities."""

from typing import Any

import numpy as np
import structlog
from sklearn.metrics import (
    classification_report,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)

logger = structlog.get_logger()


def evaluate_model(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    y_proba: np.ndarray | None = None,
) -> dict[str, Any]:
    """Compute evaluation metrics for fraud detection model.

    Args:
        y_true: True labels.
        y_pred: Predicted labels.
        y_proba: Predicted probabilities (optional, for AUC).

    Returns:
        Dictionary of metric names to values.
    """
    metrics: dict[str, Any] = {
        "f1": float(f1_score(y_true, y_pred)),
        "precision": float(precision_score(y_true, y_pred)),
        "recall": float(recall_score(y_true, y_pred)),
    }

    if y_proba is not None:
        metrics["auc_roc"] = float(roc_auc_score(y_true, y_proba))

    logger.info("evaluation_complete", metrics=metrics)
    logger.info("classification_report", report=classification_report(y_true, y_pred))

    return metrics
