# Branch 04: Model Training

> **Goal**: Create training scripts with XGBoost and full MLflow experiment tracking.

## What You'll Learn

- Training an XGBoost model for fraud detection
- Logging params, metrics, and model artifacts to **MLflow**
- Config-driven hyperparameters via `config/models.yaml`
- Using Claude Code with the **mlflow-tracking** skill

## What Changed (vs branch 03)

- Added `src/fraud_detection/models/` (train, evaluate)
- Added `config/models.yaml` — hyperparameters
- Added `tests/models/test_train.py`

## Step-by-Step

### 1. Review the config

```bash
cat config/models.yaml
```

### 2. Create training script with Claude

```bash
claude

> Using the mlflow-tracking skill (check docs/research/mlflow-latest.md),
> review src/fraud_detection/models/train.py:
> - Load data from data/processed/
> - Train XGBoost with params from config/models.yaml
> - Log params, metrics, model to MLflow
> - Use MinIO as artifact store
```

### 3. Train the model

```bash
uv run python -m fraud_detection.models.train
```

### 4. Check MLflow UI

Open http://localhost:5000 — you should see:
- An experiment named `fraud-detection`
- A run with logged params (learning_rate, max_depth, n_estimators)
- Metrics: f1, precision, recall
- Model artifact stored in MinIO

### 5. Run tests

```bash
uv run pytest tests/models/ -v
```

## Expected Behavior

- Training script runs without errors
- MLflow experiment and run are visible in the UI
- Params, metrics, and model artifact are logged
- F1 score > 0.80 on test set
- Config changes in `models.yaml` are reflected in MLflow params

## Key Files

| File | Purpose |
|------|---------|
| `src/fraud_detection/models/train.py` | XGBoost training + MLflow logging |
| `src/fraud_detection/models/evaluate.py` | Metrics computation |
| `config/models.yaml` | Hyperparameters |
| `tests/models/test_train.py` | Training tests |

## Next Branch

→ `git checkout 05-api-serving`
