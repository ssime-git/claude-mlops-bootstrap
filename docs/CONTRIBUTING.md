# Contributing

## Branch Structure

This repo uses thematic branches. Each branch builds on the previous one.

## Code Standards

- Type hints: mandatory (MyPy strict)
- Docstrings: Google style
- Imports: stdlib → third-party → local
- Max line length: 100
- Error handling: always log context

## Quality Gates

Every Python file must pass:
1. `uvx ruff check --fix`
2. `uvx ruff format`
3. `uvx mypy --strict`
4. `uv run pytest` (if tests exist)
