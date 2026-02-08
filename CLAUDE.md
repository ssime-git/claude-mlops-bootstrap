# Fraud Detection Pipeline - Claude Code Demo

## Project Context
Demo showing Claude Code capabilities for MLOps.
Focus: Code quality automation, skills usage, GSD/Ralph workflows.

## Tech Stack
Python 3.11 (uv), MLflow, DVC, MinIO, FastAPI, Docker

## Architecture Principles
1. **Monolith First** - Single container, avoid microservices complexity
2. **Minimal Files** - Max 200 lines per file, extend before creating new
3. **Config-Driven** - All params in config/*.yaml
4. **Type-Safe** - Mandatory type hints, MyPy strict

## Code Standards
- Type hints: MANDATORY (MyPy strict)
- Docstrings: Google style
- Imports: stdlib → third-party → local
- Max line length: 100
- Error handling: Always log context

## Anti-Patterns
❌ God classes (>500 lines)
❌ Mutable default arguments
❌ Bare except clauses
❌ Hardcoded config values
❌ Missing type hints

## Quality Gates (Automated)
Every Python file must pass:
1. Ruff check + format
2. MyPy strict
3. Tests (if applicable)

Hooks run automatically via .claude/settings.json

## External Docs (VERIFY FIRST)
Before implementing, check docs/research/ for latest syntax:
- MLflow → docs/research/mlflow-latest.md
- DVC → docs/research/dvc-latest.md
- Great Expectations → docs/research/ge-latest.md
- FastAPI → docs/research/fastapi-latest.md
