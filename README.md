# Branch 05: API Serving

> **Goal**: Build a FastAPI inference API with model caching on startup and Pydantic v2 validation.

## What You'll Learn

- Building a **FastAPI** prediction API
- **Pydantic v2** request/response schemas
- Model caching on startup via **lifespan** context manager
- Using Claude Code with the **fastapi-serving** skill

## What Changed (vs branch 04)

- Added `src/fraud_detection/serving/` (api, schemas, inference)
- Added `config/serving.yaml` — API configuration
- Added `tests/serving/test_api.py`

## Step-by-Step

### 1. Review the API code

```bash
cat src/fraud_detection/serving/api.py
cat src/fraud_detection/serving/schemas.py
```

### 2. Start the API in dev mode

```bash
uv run uvicorn fraud_detection.serving.api:app --reload
```

### 3. Test the health endpoint

```bash
curl http://localhost:8000/health
# Expected: {"status": "healthy", "model_loaded": true}
```

### 4. Test a prediction

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"amount": 150.50, "merchant_id": "m_123", "timestamp": "2026-02-08T10:30:00Z"}'

# Expected: {"is_fraud": false, "confidence": 0.12, "model_version": "Production"}
```

### 5. Use Claude to enhance

```bash
claude

> Using the fastapi-serving skill, review the API and suggest improvements
> for production readiness (error handling, logging, etc.)
```

### 6. Run tests

```bash
uv run pytest tests/serving/ -v
```

## Expected Behavior

- API starts and loads model from MLflow on startup
- `GET /health` returns 200 with model status
- `POST /predict` returns fraud prediction with confidence score
- Invalid input (negative amount, missing fields) returns 422 validation error
- If model is not loaded, `/predict` returns 503
- Response time < 100ms per prediction

## Key Files

| File | Purpose |
|------|---------|
| `src/fraud_detection/serving/api.py` | FastAPI app with lifespan |
| `src/fraud_detection/serving/schemas.py` | Pydantic v2 request/response models |
| `src/fraud_detection/serving/inference.py` | Model loading + prediction logic |
| `config/serving.yaml` | API config (host, port, workers) |
| `tests/serving/test_api.py` | API endpoint tests |

## Next Branch

→ `git checkout 06-dockerize-all`
