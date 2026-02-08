---
name: dvc-versioning
description: DVC data and model versioning patterns
---

# DVC Versioning Skill

## When to Use
- Tracking large data files (CSV, parquet)
- Versioning trained models
- Defining reproducible pipelines

## Pattern

```bash
# Track a file
dvc add data/raw/transactions.csv
git add data/raw/transactions.csv.dvc data/raw/.gitignore

# Remote storage (MinIO)
dvc remote add -d minio s3://dvc-storage
dvc remote modify minio endpointurl http://localhost:9000
dvc remote modify minio access_key_id minioadmin
dvc remote modify minio secret_access_key minioadmin

# Push/pull
dvc push
dvc pull
```

## Pipeline (dvc.yaml)

```yaml
stages:
  process:
    cmd: python -m fraud_detection.data.processor
    deps:
      - data/raw/transactions.csv
    outs:
      - data/processed/transactions_clean.parquet
```

## Important
- ALWAYS check docs/research/dvc-latest.md for current syntax
- Track files > 10MB with DVC, not git
- Use `dvc repro` to run pipelines
