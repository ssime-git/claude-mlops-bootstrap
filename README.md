# Branch 03: Data Pipeline

> **Goal**: Set up MinIO + DVC for data versioning, Great Expectations for validation, and build the data loading/processing pipeline.

## What You'll Learn

- Configuring **DVC** with MinIO as S3-compatible remote storage
- Creating a **Great Expectations** validation suite
- Building data loading, validation, and processing modules
- Using Claude Code with the **dvc-versioning** and **great-expectations** skills

## What Changed (vs branch 02)

- Added `data/raw/` and `data/processed/` directories
- Added `src/fraud_detection/data/` (loader, validator, processor)
- Added `great_expectations/expectations/fraud_suite.json`
- Added `scripts/setup_minio.sh`

## Step-by-Step

### 1. Setup MinIO buckets

```bash
bash scripts/setup_minio.sh
# Creates: dvc-storage, mlflow buckets
```

### 2. Download a dataset

```bash
# Use the dataset identified in branch 01 research
curl -o data/raw/transactions.csv [URL_FROM_DOCS_RESEARCH_DATASETS]
```

### 3. Initialize DVC with MinIO

```bash
dvc init
dvc remote add -d minio s3://dvc-storage
dvc remote modify minio endpointurl http://localhost:9000
dvc remote modify minio access_key_id minioadmin
dvc remote modify minio secret_access_key minioadmin
```

### 4. Track raw data

```bash
dvc add data/raw/transactions.csv
git add data/raw/transactions.csv.dvc .dvc/
```

### 5. Use Claude to enhance the pipeline

```bash
claude

> Using the great-expectations skill, enhance src/fraud_detection/data/validator.py
> to use the fraud_suite.json expectation suite.
> Then run the full pipeline: load → validate → process
```

### 6. Run the pipeline

```bash
uv run python -m fraud_detection.data.processor
dvc add data/processed/transactions_clean.parquet
```

## Expected Behavior

- MinIO buckets `dvc-storage` and `mlflow` are created
- DVC is initialized with MinIO as remote
- Raw data is tracked by DVC (`.dvc` file created)
- Great Expectations suite validates: amount > 0, amount < 1M, no null merchant_id
- Processed parquet file is generated in `data/processed/`

## Key Files

| File | Purpose |
|------|---------|
| `scripts/setup_minio.sh` | Create MinIO buckets |
| `src/fraud_detection/data/loader.py` | Load CSV data |
| `src/fraud_detection/data/validator.py` | Validate with GE rules |
| `src/fraud_detection/data/processor.py` | Clean and process data |
| `great_expectations/expectations/fraud_suite.json` | Validation rules |

## Next Branch

→ `git checkout 04-model-training`
