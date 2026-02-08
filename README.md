# Branch 06: Dockerize All

> **Goal**: Containerize the full stack (API + MinIO + MLflow) with Docker Compose.

## What You'll Learn

- Writing a production **Dockerfile** with uv
- Composing services with **Docker Compose** (API, MinIO, MLflow)
- Using `.dockerignore` to keep images lean

## What Changed (vs branch 05)

- Added `Dockerfile` — production image with multi-stage uv install
- Added `docker-compose.yml` — full production stack
- Added `.dockerignore`

## Step-by-Step

### 1. Build the image

```bash
docker-compose build
```

### 2. Start the full stack

```bash
docker-compose up -d
```

### 3. Test the API in container

```bash
curl http://localhost:8000/health
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"amount": 42.0, "merchant_id": "m_1", "timestamp": "2026-02-08T12:00:00Z"}'
```

### 4. Check services

```bash
curl http://localhost:9001  # MinIO console
curl http://localhost:5000  # MLflow UI
```

### 5. View logs

```bash
docker-compose logs -f api
```

## Expected Behavior

- `docker-compose build` completes without errors
- API is accessible at http://localhost:8000
- MinIO console at http://localhost:9001
- MLflow UI at http://localhost:5000
- `/predict` endpoint works end-to-end through containers
- Image size is reasonable (< 500MB)

## Key Files

| File | Purpose |
|------|---------|
| `Dockerfile` | Production image (python:3.11-slim + uv) |
| `docker-compose.yml` | Full stack: API + MinIO + MLflow |
| `.dockerignore` | Exclude dev files from image |

## Next Branch

→ `git checkout 07-dvc-pipeline`
