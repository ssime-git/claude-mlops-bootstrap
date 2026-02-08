---
name: mlflow-tracking
description: MLflow experiment tracking patterns for fraud detection pipeline
---

# MLflow Tracking Skill

## When to Use
- Setting up experiment tracking
- Logging params, metrics, and models
- Querying experiment results

## Pattern

```python
import mlflow

# Setup
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("fraud-detection")

# Run
with mlflow.start_run(run_name="xgboost-v1"):
    mlflow.log_params({"learning_rate": 0.1, "max_depth": 6})
    mlflow.log_metrics({"f1": 0.86, "precision": 0.89, "recall": 0.83})
    mlflow.sklearn.log_model(model, "model")
```

## Important
- ALWAYS check docs/research/mlflow-latest.md for current API before implementing
- Use `mlflow.set_tracking_uri()` to point to local MLflow server
- Log ALL hyperparameters and metrics
- Use `mlflow.sklearn.log_model()` or `mlflow.xgboost.log_model()` for auto-serialization
