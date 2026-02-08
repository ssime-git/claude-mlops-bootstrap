FROM python:3.11-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Install dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen

# Copy code
COPY . .

CMD ["uv", "run", "uvicorn", "fraud_detection.serving.api:app", "--host", "0.0.0.0", "--workers", "2"]
