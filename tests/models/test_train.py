"""Tests for training module."""

from pathlib import Path

from fraud_detection.models.train import load_config


def test_load_config() -> None:
    """Test that config loads correctly."""
    config = load_config()
    assert "xgboost" in config
    assert "learning_rate" in config["xgboost"]
    assert "max_depth" in config["xgboost"]
    assert "n_estimators" in config["xgboost"]
