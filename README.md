# Branch 08: Model Registry

> **Goal**: Set up MLflow Model Registry with staging/production stages and a rollback strategy.

## What You'll Learn

- Registering models in **MLflow Model Registry**
- Promoting models through stages (Staging → Production)
- Implementing a **rollback strategy** (revert to previous version)
- CLI tooling for model lifecycle management

## What Changed (vs branch 07)

- Added `src/fraud_detection/registry.py` — register, promote, rollback, load
- Added `scripts/promote_model.py` — CLI for model promotion

## Step-by-Step

### 1. Register the best model

```bash
uv run python scripts/promote_model.py --stage staging
```

### 2. Test the staging model

```bash
# Verify the model works in staging
curl http://localhost:8000/health
```

### 3. Promote to production

```bash
uv run python scripts/promote_model.py --stage production
```

### 4. Simulate a rollback

```bash
# If something goes wrong:
uv run python scripts/promote_model.py --rollback
```

### 5. Verify in MLflow UI

Open http://localhost:5000 → Models tab:
- See registered model "FraudDetector"
- See version history with stage transitions
- Verify rollback moved previous version to Production

## Expected Behavior

- Model is registered in MLflow Registry
- Promotion from Staging → Production works
- Rollback demotes current version to Archived, promotes N-1 to Production
- API automatically picks up the new production model
- All transitions are logged with structlog

## Key Files

| File | Purpose |
|------|---------|
| `src/fraud_detection/registry.py` | Register, promote, rollback, load |
| `scripts/promote_model.py` | CLI for model lifecycle |

## Next Branch

→ `git checkout 09-ci-pipeline`
