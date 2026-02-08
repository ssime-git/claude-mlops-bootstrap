---
name: fastapi-serving
description: FastAPI model serving patterns for ML inference
---

# FastAPI Serving Skill

## When to Use
- Creating prediction API endpoints
- Setting up health checks
- Serving ML models with Pydantic v2 validation

## Pattern

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Fraud Detection API")

class TransactionRequest(BaseModel):
    amount: float
    merchant_id: str
    timestamp: str

class PredictionResponse(BaseModel):
    is_fraud: bool
    confidence: float
    model_version: str

@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "healthy"}

@app.post("/predict", response_model=PredictionResponse)
async def predict(transaction: TransactionRequest) -> PredictionResponse:
    # Load cached model, run inference
    ...
```

## Important
- ALWAYS check docs/research/fastapi-latest.md for current patterns
- Use Pydantic v2 `BaseModel` for request/response schemas
- Cache model on startup with `@app.on_event("startup")` or lifespan
- Target < 100ms latency per prediction
