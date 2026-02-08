# Branch 09: CI Pipeline

> **Goal**: Set up GitHub Actions for automated testing, linting, and Docker image builds.

## What You'll Learn

- Configuring **GitHub Actions** for CI on pull requests
- Automated quality gates: ruff, mypy, pytest
- Docker image build and smoke test on merge to main

## What Changed (vs branch 08)

- Added `.github/workflows/ci.yml` — lint + test on PR
- Added `.github/workflows/docker-build.yml` — build + smoke test on merge

## Step-by-Step

### 1. Review the workflows

```bash
cat .github/workflows/ci.yml
cat .github/workflows/docker-build.yml
```

### 2. Test CI locally (simulate what GitHub Actions does)

```bash
uvx ruff check src/
uvx ruff format --check src/
uvx mypy --strict src/
uv run pytest tests/ -v --tb=short
```

### 3. Test Docker build locally

```bash
docker build -t fraud-detection:test .
docker run -d --name test-api -p 8000:8000 fraud-detection:test
sleep 5
curl -f http://localhost:8000/health
docker stop test-api && docker rm test-api
```

### 4. Push and verify

```bash
# Create a PR to trigger CI
git push origin 09-ci-pipeline
# Open PR on GitHub → watch CI run
```

## Expected Behavior

- `ci.yml` runs on every pull request: ruff check, ruff format, mypy, pytest
- `docker-build.yml` runs on push to main: builds image, starts container, hits /health
- All checks pass on the current codebase
- Failed checks block PR merge

## Key Files

| File | Purpose |
|------|---------|
| `.github/workflows/ci.yml` | Lint + test on PR |
| `.github/workflows/docker-build.yml` | Build + smoke test on merge |

## Next Branch

→ `git checkout 10-gsd-feature`
