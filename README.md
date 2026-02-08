# Branch 07: DVC Pipeline

> **Goal**: Create a reproducible DVC pipeline with containerized stages for data processing and training.

## What You'll Learn

- Defining a **DVC pipeline** (`dvc.yaml`) with stages, deps, and outputs
- Using **params.yaml** for config-driven pipelines
- Building separate Docker images for each pipeline stage
- Selective re-execution when params change

## What Changed (vs branch 06)

- Added `dvc.yaml` — pipeline definition (process → train)
- Added `params.yaml` — shared pipeline parameters
- Added `docker/Dockerfile.process` and `docker/Dockerfile.train`

## Step-by-Step

### 1. Review the pipeline

```bash
cat dvc.yaml
dvc dag
```

Expected DAG:
```
process → train
```

### 2. Run the full pipeline

```bash
dvc repro
```

### 3. Change a parameter and re-run

```bash
# Edit params.yaml: change max_depth from 6 to 8
dvc repro
# Only the 'train' stage should re-run (process is cached)
```

### 4. Check pipeline status

```bash
dvc status
```

## Expected Behavior

- `dvc repro` executes both stages (process → train)
- `dvc dag` shows the dependency graph
- Changing `params.yaml` triggers selective re-execution
- Outputs are tracked: `data/processed/`, `models/`, `metrics.json`
- `dvc status` shows clean state after successful run

## Key Files

| File | Purpose |
|------|---------|
| `dvc.yaml` | Pipeline stages definition |
| `params.yaml` | Shared hyperparameters |
| `docker/Dockerfile.process` | Container for data processing |
| `docker/Dockerfile.train` | Container for model training |

## Next Branch

→ `git checkout 08-model-registry`
