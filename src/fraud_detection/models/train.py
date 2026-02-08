"""XGBoost training script with MLflow tracking."""

from pathlib import Path
from typing import Any

import mlflow
import pandas as pd
import structlog
import yaml
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

logger = structlog.get_logger()

CONFIG_PATH = Path("config/models.yaml")
DATA_PATH = Path("data/processed/transactions_clean.parquet")


def load_config() -> dict[str, Any]:
    """Load model hyperparameters from config file."""
    with open(CONFIG_PATH) as f:
        config: dict[str, Any] = yaml.safe_load(f)
    return config


def train_model() -> None:
    """Train XGBoost model and log to MLflow."""
    config = load_config()
    xgb_params = config["xgboost"]

    logger.info("loading_data", path=str(DATA_PATH))
    df = pd.read_parquet(DATA_PATH)

    feature_cols = [c for c in df.columns if c not in ("is_fraud", "timestamp", "merchant_id")]
    x = df[feature_cols]
    y = df["is_fraud"]

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42, stratify=y
    )

    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment("fraud-detection")

    with mlflow.start_run(run_name="xgboost-baseline"):
        mlflow.log_params(xgb_params)

        logger.info("training_model", params=xgb_params)
        model = XGBClassifier(**xgb_params, random_state=42)
        model.fit(x_train, y_train)

        y_pred = model.predict(x_test)

        metrics = {
            "f1": float(f1_score(y_test, y_pred)),
            "precision": float(precision_score(y_test, y_pred)),
            "recall": float(recall_score(y_test, y_pred)),
        }
        mlflow.log_metrics(metrics)
        mlflow.xgboost.log_model(model, "model")

        logger.info("training_complete", metrics=metrics)


if __name__ == "__main__":
    train_model()
