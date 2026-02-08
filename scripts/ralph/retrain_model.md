# Model Retraining Task

Retrain fraud detection model on latest data.

## Requirements
1. Load latest processed data from DVC
2. Train XGBoost with params from config/models.yaml
3. Compare F1 score with current production model
4. If better: register new version, promote to staging
5. If worse: investigate why (data drift? feature issue?)
6. Log comparison metrics to MLflow

Output <promise>RETRAIN_COMPLETE</promise> when done.
