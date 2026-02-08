# Branch 10: GSD Feature

> **Goal**: Use GSD (Get-Shit-Done) to add a complete geo-anomaly detection feature with fresh-context agents.

## What You'll Learn

- Using **GSD** for structured feature development
- Fresh-context agent spawning (no context rot)
- Comparing GSD vs manual development (time, quality, commits)

## What Changed (vs branch 09)

- Added `.planning/` directory (GSD creates its plan here)
- Added `docs/gsd-metrics.md` — metrics tracking template

## Step-by-Step

### 1. Start GSD

```bash
claude
/gsd:new-project
```

### 2. Answer the GSD interview

```
> What: Add geographic anomaly detection
> Requirements:
>   - Geohashing for location clustering
>   - Flag unusual locations per user
>   - Integrate with MLflow tracking
>   - <100ms latency
```

GSD will create a plan in `.planning/` with tasks.

### 3. Execute the plan

```bash
/gsd:execute-plan
```

GSD spawns fresh-context agents for each task:
- **Task 1**: GeoHasher utility class
- **Task 2**: GeoAnomalyDetector model
- **Task 3**: Integration with feature pipeline
- **Task 4**: MLflow experiment logging
- **Task 5**: Tests (target coverage > 80%)

### 4. Measure metrics

Fill in `docs/gsd-metrics.md` with:
- Time: GSD vs how long it would take manually
- Quality: test coverage, lint errors, type errors
- Commits: atomic (GSD) vs chaotic (manual)

### 5. Review the generated code

```bash
# Check what GSD created
git diff --stat HEAD
uv run pytest tests/ -v
```

## Expected Behavior

- GSD creates a structured plan in `.planning/`
- Each task is executed by a fresh-context agent (no context rot)
- Generated code passes all quality gates (ruff, mypy, pytest)
- Commits are atomic and well-described
- New geo-anomaly feature integrates with existing pipeline

## Key Files

| File | Purpose |
|------|---------|
| `.planning/` | GSD planning directory (auto-generated) |
| `docs/gsd-metrics.md` | Metrics comparison template |

## Next Branch

→ `git checkout 11-ralph-pipeline-check`
