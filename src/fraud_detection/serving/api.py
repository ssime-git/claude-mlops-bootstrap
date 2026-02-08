"""FastAPI application for fraud detection inference."""

from contextlib import asynccontextmanager
from typing import AsyncGenerator

import structlog
from fastapi import FastAPI, HTTPException

from fraud_detection.serving.inference import (
    get_model_version,
    is_model_loaded,
    load_model,
    predict,
)
from fraud_detection.serving.schemas import (
    HealthResponse,
    PredictionResponse,
    TransactionRequest,
)

logger = structlog.get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Load model on startup."""
    try:
        load_model()
    except Exception as e:
        logger.warning("model_load_failed_at_startup", error=str(e))
    yield


app = FastAPI(title="Fraud Detection API", lifespan=lifespan)


@app.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    """Health check endpoint."""
    return HealthResponse(status="healthy", model_loaded=is_model_loaded())


@app.post("/predict", response_model=PredictionResponse)
async def predict_fraud(transaction: TransactionRequest) -> PredictionResponse:
    """Predict whether a transaction is fraudulent."""
    if not is_model_loaded():
        raise HTTPException(status_code=503, detail="Model not loaded")

    features = {"amount": transaction.amount}
    is_fraud, confidence = predict(features)

    return PredictionResponse(
        is_fraud=is_fraud,
        confidence=confidence,
        model_version=get_model_version(),
    )
