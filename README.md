# Branch 01: Research Skills

> **Goal**: Use Claude Code's browser tool to research up-to-date documentation before creating MLOps skills.

## What You'll Learn

- Creating a Claude Code **skill** (`.claude/skills/`)
- Using the **browser tool** to research latest APIs
- Building a research-first workflow before coding integrations

## What Changed (vs branch 00)

- Added `.claude/skills/web-research/SKILL.md`
- Added `docs/research/` directory for research outputs

## Step-by-Step

### 1. Launch Claude Code

```bash
claude
```

### 2. Use the web-research skill

Ask Claude to research the latest APIs before creating MLOps skills:

```
> I need to research the latest APIs before creating MLOps skills.
> Use the web-research skill to:
>
> 1. Check MLflow 2.x tracking API (mlflow.org/docs)
>    - Focus on: mlflow.log_params, mlflow.log_metrics, mlflow.log_model
>    - Check for any breaking changes
>    - Save to docs/research/mlflow-latest.md
>
> 2. Check DVC 3.x commands (dvc.org/doc)
>    - Focus on: dvc add, dvc remote add, dvc pipeline
>    - Verify dvc.yaml syntax
>    - Save to docs/research/dvc-latest.md
>
> 3. Check Great Expectations 1.x (docs.greatexpectations.io)
>    - Focus on: expectation suites, data validation
>    - Check for API changes
>    - Save to docs/research/ge-latest.md
>
> 4. Check FastAPI latest (fastapi.tiangolo.com)
>    - Focus on: async patterns, Pydantic v2
>    - ML model serving patterns
>    - Save to docs/research/fastapi-latest.md
>
> 5. Search for fraud detection datasets (kaggle.com)
>    - Open source, >50k transactions
>    - Must have: amount, merchant, timestamp, label
>    - Save URLs to docs/research/datasets.md
```

### 3. Verify the results

```bash
ls -la docs/research/
cat docs/research/mlflow-latest.md
```

## Expected Behavior

- Claude uses the browser tool to navigate to official docs
- 5 research files are generated in `docs/research/`
- Each file contains current API syntax and examples
- At least 1 open-source fraud detection dataset is identified
- Research files follow the output format defined in the skill

## Key Files

| File | Purpose |
|------|---------|
| `.claude/skills/web-research/SKILL.md` | Skill definition for doc research |
| `docs/research/mlflow-latest.md` | MLflow 2.x API findings |
| `docs/research/dvc-latest.md` | DVC 3.x command findings |
| `docs/research/ge-latest.md` | Great Expectations 1.x findings |
| `docs/research/fastapi-latest.md` | FastAPI latest findings |
| `docs/research/datasets.md` | Fraud detection dataset URLs |

## Next Branch

→ `git checkout 02-claude-config`
