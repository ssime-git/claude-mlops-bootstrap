# Branch 02: Claude Code Configuration

> **Goal**: Configure Claude Code with CLAUDE.md, automated hooks, MLOps skills, and a custom slash command.

## What You'll Learn

- Writing a **CLAUDE.md** project constitution
- Configuring **hooks** for automatic quality gates (ruff, mypy) on every file write
- Creating domain-specific **skills** (MLflow, DVC, FastAPI, Great Expectations)
- Adding a **custom slash command** (`/quality-check`)
- Setting up **pre-commit** hooks

## What Changed (vs branch 01)

- Added `CLAUDE.md` — project constitution
- Added `.claude/settings.json` — hooks configuration
- Added 4 MLOps skills in `.claude/skills/`
- Added `.claude/commands/quality-check.md` — slash command
- Added `.pre-commit-config.yaml`

## Step-by-Step

### 1. Install dev dependencies

```bash
uv add --dev ruff mypy pytest pytest-cov pre-commit
```

### 2. Read the CLAUDE.md

```bash
cat CLAUDE.md
```

This is the "constitution" that guides Claude's behavior for this project.

### 3. Test the hooks

```bash
claude

# Ask Claude to create a simple file:
> Create a simple validator: src/fraud_detection/validators.py
> Function: validate_amount(amount: float) -> bool
> Returns True if 0 < amount < 1000000
```

**Watch the hooks fire automatically:**
- ✅ Ruff check (linting)
- ✅ Ruff format (code style)
- ✅ MyPy strict (type checking)

### 4. Test a skill

```bash
claude

> Using the mlflow-tracking skill (check docs/research/mlflow-latest.md first),
> create src/fraud_detection/tracking.py with a setup_experiment() function
```

Claude should automatically reference the skill pattern and research docs.

### 5. Test the slash command

```bash
claude

/quality-check
```

### 6. Test pre-commit

```bash
uv run pre-commit run --all-files
```

## Expected Behavior

- When Claude writes any `.py` file, hooks run automatically (ruff + mypy)
- Generated code has type hints, Google-style docstrings, proper imports
- Skills are picked up automatically when relevant topics are mentioned
- `/quality-check` runs all quality gates and reports results
- Pre-commit hooks catch issues before committing

## Key Files

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Project constitution for Claude Code |
| `.claude/settings.json` | Hooks configuration (PostToolUse) |
| `.claude/skills/mlflow-tracking/SKILL.md` | MLflow tracking patterns |
| `.claude/skills/dvc-versioning/SKILL.md` | DVC versioning patterns |
| `.claude/skills/fastapi-serving/SKILL.md` | FastAPI serving patterns |
| `.claude/skills/great-expectations/SKILL.md` | Data validation patterns |
| `.claude/commands/quality-check.md` | `/quality-check` slash command |
| `.pre-commit-config.yaml` | Pre-commit hooks config |

## Next Branch

→ `git checkout 03-data-pipeline`
