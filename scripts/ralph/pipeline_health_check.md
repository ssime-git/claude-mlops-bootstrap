# Pipeline Health Check & Remediation

Verify the entire fraud detection pipeline works end-to-end.
Investigate and fix any issues found.

## Checks to Perform
1. Data pipeline: run Great Expectations suite on latest data
   - If validation fails → investigate which columns/rules broke
   - Attempt fix (reprocess data) or report unfixable issues
2. Model health: load production model from MLflow registry
   - Verify model loads without error
   - Run prediction on 100 sample transactions
   - If latency > 100ms → investigate bottleneck
3. API serving: hit /health and /predict endpoints
   - If down → check logs, identify root cause
   - If slow → profile and suggest optimization
4. DVC pipeline: verify `dvc status` shows no changed deps
   - If stale → run `dvc repro` for affected stages
5. Generate health report in docs/reports/health_{date}.md
   - Summary of all checks
   - Issues found + actions taken
   - Recommendations for next steps

Output <promise>HEALTH_CHECK_COMPLETE</promise> when all checks done.
