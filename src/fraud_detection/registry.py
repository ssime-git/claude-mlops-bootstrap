"""MLflow Model Registry utilities with rollback support."""

from typing import Any

import mlflow
from mlflow.tracking import MlflowClient

import structlog

logger = structlog.get_logger()


def get_client(tracking_uri: str = "http://localhost:5000") -> MlflowClient:
    """Get an MLflow client instance."""
    mlflow.set_tracking_uri(tracking_uri)
    return MlflowClient(tracking_uri)


def register_model(run_id: str, model_name: str = "FraudDetector") -> str:
    """Register a model from a run.

    Args:
        run_id: MLflow run ID containing the model artifact.
        model_name: Name for the registered model.

    Returns:
        The new model version string.
    """
    model_uri = f"runs:/{run_id}/model"
    result = mlflow.register_model(model_uri, model_name)
    logger.info("model_registered", name=model_name, version=result.version)
    return str(result.version)


def promote_model(
    model_name: str = "FraudDetector",
    version: str | None = None,
    stage: str = "Staging",
) -> None:
    """Promote a model version to a stage.

    Args:
        model_name: Registered model name.
        version: Model version to promote. If None, uses latest.
        stage: Target stage (Staging or Production).
    """
    client = get_client()

    if version is None:
        versions = client.get_latest_versions(model_name)
        if not versions:
            raise ValueError(f"No versions found for model {model_name}")
        version = versions[-1].version

    client.transition_model_version_stage(
        name=model_name,
        version=version,
        stage=stage,
    )
    logger.info("model_promoted", name=model_name, version=version, stage=stage)


def rollback_model(model_name: str = "FraudDetector") -> None:
    """Rollback production model to the previous version.

    Args:
        model_name: Registered model name.

    Raises:
        ValueError: If there's no previous version to rollback to.
    """
    client = get_client()

    prod_versions = client.get_latest_versions(model_name, stages=["Production"])
    if not prod_versions:
        raise ValueError(f"No production version found for {model_name}")

    current_version = int(prod_versions[0].version)
    if current_version <= 1:
        raise ValueError("Cannot rollback: already at version 1")

    previous_version = str(current_version - 1)

    # Demote current
    client.transition_model_version_stage(
        name=model_name, version=str(current_version), stage="Archived"
    )

    # Promote previous
    client.transition_model_version_stage(
        name=model_name, version=previous_version, stage="Production"
    )

    logger.info(
        "model_rolled_back",
        name=model_name,
        from_version=current_version,
        to_version=previous_version,
    )


def get_production_model(model_name: str = "FraudDetector") -> Any:
    """Load the current production model.

    Args:
        model_name: Registered model name.

    Returns:
        The loaded model.
    """
    model_uri = f"models:/{model_name}/Production"
    model = mlflow.pyfunc.load_model(model_uri)
    logger.info("production_model_loaded", name=model_name)
    return model
