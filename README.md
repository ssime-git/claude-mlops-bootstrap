# Branch 12: Monitoring

> **Goal**: Add Prometheus monitoring to the API and run a load test to verify scalability.

## What You'll Learn

- Instrumenting a FastAPI app with **Prometheus** metrics
- Setting up a Prometheus scraping config
- Running a **load test** with Locust to verify p95 latency
- Docker Compose with monitoring stack

## What Changed (vs branch 11)

- Added `src/fraud_detection/serving/metrics.py` — Prometheus counters/histograms
- Added `monitoring/prometheus.yml` — scrape config
- Added `docker-compose.monitoring.yml` — full stack + Prometheus
- Added `tests/serving/locustfile.py` — load test

## Step-by-Step

### 1. Start the monitoring stack

```bash
docker-compose -f docker-compose.monitoring.yml up -d
```

### 2. Verify Prometheus is scraping

Open http://localhost:9090 and query:

```promql
up{job="fraud-detection-api"}
```

Should return `1`.

### 3. Generate some traffic

```bash
for i in $(seq 1 100); do
  curl -s -X POST http://localhost:8000/predict \
    -H "Content-Type: application/json" \
    -d '{"amount": '$((RANDOM % 1000))'.50, "merchant_id": "m_'$i'", "timestamp": "2026-02-08T10:30:00Z"}' &
done
wait
```

### 4. Check metrics in Prometheus

```promql
# p95 latency
histogram_quantile(0.95, rate(prediction_latency_seconds_bucket[5m]))

# Total predictions
predictions_total

# Confidence distribution
histogram_quantile(0.5, model_confidence_bucket)
```

### 5. Run the load test

```bash
uvx locust -f tests/serving/locustfile.py \
  --host http://localhost:8000 \
  --headless --users 50 --spawn-rate 5 --run-time 5m
```

### 6. Verify results

- p95 latency < 100ms
- 0 errors over 5 minutes
- Metrics visible in real-time in Prometheus

## Expected Behavior

- Prometheus scrapes API metrics every 15s
- 4 metrics are exposed: `prediction_latency_seconds`, `predictions_total`, `model_confidence`, `active_requests`
- Load test with 50 concurrent users passes (p95 < 100ms, 0 errors)
- All metrics queryable in Prometheus UI

## Key Files

| File | Purpose |
|------|---------|
| `src/fraud_detection/serving/metrics.py` | Prometheus metric definitions |
| `monitoring/prometheus.yml` | Prometheus scrape config |
| `docker-compose.monitoring.yml` | Full stack + Prometheus |
| `tests/serving/locustfile.py` | Locust load test |

## That's it!

You've completed all 12 branches. Go back to `main` for the full overview:

```bash
git checkout main
```
