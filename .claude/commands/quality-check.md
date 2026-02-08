# Quality Check

Run all quality gates on the project.

## Steps
1. Run ruff check on all Python files: `uvx ruff check src/ tests/`
2. Run ruff format check: `uvx ruff format --check src/ tests/`
3. Run mypy strict: `uvx mypy --strict src/`
4. Run pytest: `uv run pytest tests/ -v`
5. Report results summary
