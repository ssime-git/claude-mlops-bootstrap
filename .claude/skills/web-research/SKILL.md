---
name: web-research
description: Research latest documentation and APIs before implementing integrations
---

# Web Research Skill

Use browser to search and extract current documentation.

## When to Use
- Before creating new skills (verify latest API)
- Before implementing third-party integrations
- When you need current best practices

## Pattern
1. Navigate to official documentation
2. Search for specific API/command
3. Extract syntax and examples
4. Save to docs/research/[topic].md

## Sites to Check
- MLflow: https://mlflow.org/docs/latest/
- DVC: https://dvc.org/doc
- Great Expectations: https://docs.greatexpectations.io/
- FastAPI: https://fastapi.tiangolo.com/
- Datasets: https://www.kaggle.com/datasets

## Output Format

Save findings as:

```markdown
# [Tool] Latest API (YYYY-MM-DD)

## Key Changes from Training Data
- Change 1
- Change 2

## Current Syntax
\```python
# Example code
\```

## References
- [Official docs link]
```
