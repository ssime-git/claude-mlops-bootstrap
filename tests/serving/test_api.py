"""Tests for the FastAPI application."""

from fastapi.testclient import TestClient

from fraud_detection.serving.api import app

client = TestClient(app)


def test_health_endpoint() -> None:
    """Test health check returns 200."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_predict_without_model() -> None:
    """Test predict returns 503 when model is not loaded."""
    response = client.post(
        "/predict",
        json={"amount": 100.0, "merchant_id": "m_1", "timestamp": "2026-02-08T10:00:00Z"},
    )
    assert response.status_code == 503
