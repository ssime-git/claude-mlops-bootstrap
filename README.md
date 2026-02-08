# Claude Code MLOps Demo - Fraud Detection Pipeline

> Clone this repo, follow the branches in order, and master Claude Code for MLOps.

## What is this?

A **hands-on educational repository** demonstrating how Claude Code accelerates MLOps development. We build a complete fraud detection pipeline from scratch, showcasing Claude Code features at every step.

**Target audience**: Developers discovering Claude Code, Data Scientists wanting to industrialize models, MLOps Engineers seeking automation.

## Claude Code Features Covered

| Feature | Branch | What you'll learn |
|---------|--------|-------------------|
| **CLAUDE.md** | 02 | Project constitution for consistent AI behavior |
| **Hooks** | 02 | Auto quality gates (ruff, mypy) on every file write |
| **Skills** | 01-02 | Reusable patterns for MLflow, DVC, FastAPI, GE |
| **Browser tool** | 01 | Research latest docs before coding |
| **Custom commands** | 02 | `/quality-check` slash command |
| **Permission modes** | 00 | `plan`, `auto-edit`, `full-auto` |
| **GSD** | 10 | Fresh-context feature development |
| **Ralph** | 11 | Autonomous pipeline health check overnight |

## Branch Roadmap (12 branches)

```
main (this README)
│
PHASE 1: Foundation & Local Dev
├── 00-project-setup           # Structure + devcontainer + Claude Code
├── 01-research-skills         # Browser skill to research up-to-date docs
├── 02-claude-config           # CLAUDE.md + hooks + skills MLOps
├── 03-data-pipeline           # MinIO + DVC + Great Expectations
├── 04-model-training          # Training scripts + MLflow local
├── 05-api-serving             # FastAPI inference + model caching
│
PHASE 2: Production-Ready
├── 06-dockerize-all           # Docker Compose monolith
├── 07-dvc-pipeline            # Reproducible DVC pipeline
├── 08-model-registry          # MLflow Registry staging/prod + rollback
├── 09-ci-pipeline             # GitHub Actions (tests + lint)
│
PHASE 3: Automation Show-Off
├── 10-gsd-feature             # GSD for a complete new feature
├── 11-ralph-pipeline-check    # Ralph autonomous health check + remediation
└── 12-monitoring              # Prometheus + load test
```

## Getting Started

```bash
# Clone the repo
git clone https://github.com/ssime-git/claude-mlops-bootstrap.git
cd claude-mlops-bootstrap

# Start with branch 00
git checkout 00-project-setup

# Each branch has its own README with step-by-step instructions
cat README.md
```

## Tech Stack

- **Python 3.11+** (uv for env management)
- **ML**: scikit-learn, XGBoost
- **Tracking**: MLflow (experiments + model registry)
- **Versioning**: DVC (data + models) + MinIO (S3-compatible local storage)
- **Serving**: FastAPI
- **Validation**: Great Expectations
- **Containers**: Docker + Docker Compose
- **Monitoring**: Prometheus
- **CI**: GitHub Actions

## Prerequisites

- Docker Desktop
- VS Code with Dev Containers extension
- An Anthropic account (Pro, Team, or Enterprise) for Claude Code
- ~10GB disk space
