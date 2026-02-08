# Architecture

## Overview

Fraud detection pipeline with a monolith-first approach.

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Raw Data   │───▶│  Processing │───▶│  Training   │
│  (DVC)      │    │  (GE valid) │    │  (MLflow)   │
└─────────────┘    └─────────────┘    └─────────────┘
                                            │
                                            ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Monitoring │◀───│  API        │◀───│  Registry   │
│  (Prometheus│    │  (FastAPI)  │    │  (MLflow)   │
└─────────────┘    └─────────────┘    └─────────────┘
```

## Principles

1. **Monolith First** — single container, no microservices
2. **Minimal Files** — max 200 lines per file
3. **Config-Driven** — all params in `config/*.yaml`
4. **Type-Safe** — mandatory type hints, MyPy strict

## Storage

- **MinIO** — S3-compatible local storage for artifacts
- **DVC** — data and model versioning backed by MinIO
- **MLflow** — experiment tracking and model registry
