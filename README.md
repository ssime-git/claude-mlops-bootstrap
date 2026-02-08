# Branch 11: Ralph Pipeline Check

> **Goal**: Use Ralph for autonomous pipeline health check, remediation, and model retraining.

## What You'll Learn

- Setting up **Ralph** (frankbria version) for autonomous tasks
- Writing task definitions that require **judgment** (not just scripting)
- Running overnight health checks with fresh context per iteration
- Autonomous model retraining with comparison logic

## What Changed (vs branch 10)

- Added `scripts/ralph/pipeline_health_check.md` — health check task
- Added `scripts/ralph/retrain_model.md` — retraining task
- Added `scripts/ralph/setup.sh` — Ralph installation
- Added `docs/reports/` — health report output directory

## Why Ralph (not a script)?

The health check task is **open-ended and requires judgment**:
- If data validation fails → investigate *which* rules broke and *why*
- If API is slow → profile and suggest optimization
- If DVC is stale → decide which stages to re-run

A script would just report pass/fail. Ralph investigates and remediates.

## Step-by-Step

### 1. Install Ralph

```bash
bash scripts/ralph/setup.sh
```

### 2. Run the health check (overnight)

```bash
ralph-setup --task scripts/ralph/pipeline_health_check.md
ralph --monitor --max-iterations 50
```

### 3. Check the report in the morning

```bash
cat docs/reports/health_*.md
```

### 4. Run retraining (if recommended by health check)

```bash
ralph-setup --task scripts/ralph/retrain_model.md
ralph --monitor --max-iterations 50
```

### 5. Verify results

```bash
# Check MLflow for new model versions
open http://localhost:5000
# Check if new model was promoted to staging
uv run python scripts/promote_model.py --stage staging
```

## Expected Behavior

- Health check runs all 5 verification steps autonomously
- Issues are **investigated**, not just reported (e.g., "column X has 3% nulls because...")
- Remediation is attempted when possible (reprocess data, restart service)
- Health report is generated in `docs/reports/health_{date}.md`
- Retraining compares new model F1 with current production
- New model registered only if it's better
- Fresh context per iteration (no context rot)

## Key Files

| File | Purpose |
|------|---------|
| `scripts/ralph/pipeline_health_check.md` | Health check + remediation task |
| `scripts/ralph/retrain_model.md` | Retraining task |
| `scripts/ralph/setup.sh` | Ralph installation script |
| `docs/reports/` | Health report output directory |

## Next Branch

→ `git checkout 12-monitoring`
