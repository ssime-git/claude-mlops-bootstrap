"""Model inference logic with caching."""

from typing import Any

import mlflow
import numpy as np
import structlog

logger = structlog.get_logger()

_model: Any = None
_model_version: str = "unknown"


def load_model(tracking_uri: str = "http://localhost:5000") -> None:
    """Load production model from MLflow registry on startup.

    Args:
        tracking_uri: MLflow tracking server URI.
    """
    global _model, _model_version  # noqa: PLW0603

    mlflow.set_tracking_uri(tracking_uri)
    model_uri = "models:/FraudDetector/Production"

    logger.info("loading_model", uri=model_uri)
    _model = mlflow.pyfunc.load_model(model_uri)
    _model_version = model_uri.split("/")[-1]
    logger.info("model_loaded", version=_model_version)


def predict(features: dict[str, float]) -> tuple[bool, float]:
    """Run fraud prediction on a single transaction.

    Args:
        features: Transaction features as a dict.

    Returns:
        Tuple of (is_fraud, confidence).

    Raises:
        RuntimeError: If model is not loaded.
    """
    if _model is None:
        raise RuntimeError("Model not loaded. Call load_model() first.")

    input_data = np.array([[features.get("amount", 0.0)]])
    prediction = _model.predict(input_data)
    confidence = float(prediction[0]) if isinstance(prediction[0], float) else 0.5

    is_fraud = confidence > 0.5
    return is_fraud, confidence


def get_model_version() -> str:
    """Return the currently loaded model version."""
    return _model_version


def is_model_loaded() -> bool:
    """Check if a model is currently loaded."""
    return _model is not None
