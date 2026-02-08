"""Pydantic v2 schemas for the fraud detection API."""

from pydantic import BaseModel, Field


class TransactionRequest(BaseModel):
    """Input schema for fraud prediction."""

    amount: float = Field(..., gt=0, description="Transaction amount")
    merchant_id: str = Field(..., description="Merchant identifier")
    timestamp: str = Field(..., description="Transaction timestamp (ISO 8601)")


class PredictionResponse(BaseModel):
    """Output schema for fraud prediction."""

    is_fraud: bool = Field(..., description="Whether the transaction is fraudulent")
    confidence: float = Field(..., ge=0, le=1, description="Model confidence score")
    model_version: str = Field(..., description="Model version used for prediction")


class HealthResponse(BaseModel):
    """Health check response."""

    status: str = Field(..., description="Service status")
    model_loaded: bool = Field(..., description="Whether the model is loaded")
