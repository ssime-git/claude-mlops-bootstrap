"""Load test for the fraud detection API."""

from locust import HttpUser, between, task


class FraudAPIUser(HttpUser):
    """Simulates a user hitting the fraud detection API."""

    wait_time = between(0.1, 0.5)

    @task(1)
    def health_check(self) -> None:
        """Hit the health endpoint."""
        self.client.get("/health")

    @task(10)
    def predict(self) -> None:
        """Hit the predict endpoint with a sample transaction."""
        self.client.post(
            "/predict",
            json={
                "amount": 150.50,
                "merchant_id": "m_123",
                "timestamp": "2026-02-08T10:30:00Z",
            },
        )
