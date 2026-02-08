#!/bin/bash
set -e

echo "🪣 Setting up MinIO buckets..."

# Wait for MinIO to be ready
until curl -sf http://localhost:9000/minio/health/live; do
    echo "Waiting for MinIO..."
    sleep 2
done

# Install mc (MinIO client) if not present
if ! command -v mc &> /dev/null; then
    curl -sL https://dl.min.io/client/mc/release/linux-amd64/mc -o /usr/local/bin/mc
    chmod +x /usr/local/bin/mc
fi

# Configure alias
mc alias set local http://localhost:9000 minioadmin minioadmin

# Create buckets
mc mb local/dvc-storage --ignore-existing
mc mb local/mlflow --ignore-existing

echo "✅ MinIO buckets created: dvc-storage, mlflow"
