"""Prometheus metrics instrumentation for the fraud detection API."""

from prometheus_client import Counter, Gauge, Histogram

prediction_latency = Histogram(
    "prediction_latency_seconds",
    "Time spent processing prediction requests",
    buckets=[0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5, 1.0],
)

predictions_total = Counter(
    "predictions_total",
    "Total number of predictions",
    ["outcome"],
)

model_confidence = Histogram(
    "model_confidence",
    "Distribution of model confidence scores",
    buckets=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
)

active_requests = Gauge(
    "active_requests",
    "Number of active prediction requests",
)
