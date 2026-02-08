# 001. Tech Stack Selection

Date: 2026-02-08

## Status

Accepted

## Context

We need a tech stack for a fraud detection MLOps demo that is:
- Simple enough to reproduce in ~10 days
- Credible for production use
- Fully local (no cloud dependencies)

## Decision

- **Python 3.11** with **uv** for environment management
- **scikit-learn + XGBoost** for ML models
- **MLflow** for experiment tracking and model registry
- **DVC** for data/model versioning
- **MinIO** for S3-compatible local storage
- **FastAPI** for model serving
- **Great Expectations** for data validation
- **Docker Compose** for containerization (monolith)
- **Prometheus** for monitoring
- **GitHub Actions** for CI

## Consequences

- No cloud vendor lock-in
- Everything runs locally via Docker Compose
- Easy to extend to cloud later (MinIO → S3, etc.)
