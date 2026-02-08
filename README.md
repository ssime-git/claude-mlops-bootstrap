# Branch 00: Project Setup

> **Goal**: Set up the project structure, install Claude Code and GSD, and start local services (MinIO + MLflow).

## What You'll Learn

- How to structure an MLOps project with `uv`
- Installing and configuring Claude Code
- Running MinIO (S3-compatible) and MLflow locally via Docker Compose

## Prerequisites

- Docker installed
- Python 3.11+ and [uv](https://docs.astral.sh/uv/)
- Node.js 18+ (for Claude Code and GSD)
- An Anthropic account (Pro, Team, or Enterprise)

## Step-by-Step

### 1. Install tools

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install Claude Code
npm install -g @anthropic-ai/claude-code

# Install GSD
npm install -g get-shit-done-cc
```

### 2. Set up the project

```bash
git clone https://github.com/ssime-git/claude-mlops-bootstrap.git
cd claude-mlops-bootstrap
git checkout 00-project-setup
uv sync
```

### 3. Start services (MinIO + MLflow)

```bash
docker compose -f docker-compose.claude.yml up -d minio mlflow
```

Verify:
- MinIO console: http://localhost:9003 (login: minioadmin / minioadmin)
- MLflow UI: http://localhost:5001

### 4. Authenticate Claude Code (first time only)

```bash
claude login
# → Opens a browser link for OAuth
# → Requires an Anthropic Pro, Team, or Enterprise account
# → Token is persisted in ~/.claude/ for future sessions
```

### 5. Verify the installation

```bash
claude --version     # Claude Code 2.x
gsd --version        # get-shit-done-cc
uv --version         # uv 0.x
python --version     # Python 3.11.x
```

### 6. Test Claude Code

```bash
claude --permission-mode plan

# Inside Claude:
> Read the project structure and summarize what you see
```

### 7. Test GSD

```bash
claude
/gsd:help
```

### 8. Stop services (when done)

```bash
docker compose -f docker-compose.claude.yml down
```

## Alternative: Run Claude Code in a container

If you prefer a containerized setup (no local install needed):

```bash
# Set your API key
export ANTHROPIC_API_KEY=sk-ant-...

# Run Claude Code in a container with MinIO + MLflow
docker compose -f docker-compose.claude.yml run --rm claude
```

This uses the official Anthropic Claude Code image (`Dockerfile.claude`).

## Expected Behavior

- Claude Code is installed and authenticated (`claude login`)
- GSD is available globally
- MinIO console accessible at http://localhost:9003
- MLflow UI accessible at http://localhost:5001
- Python 3.11 + uv are functional
- `claude --permission-mode plan` opens Claude in plan mode

## Project Structure

```
fraud-detection/
├── README.md
├── .gitignore
├── pyproject.toml
├── .python-version
├── docker-compose.claude.yml
├── Dockerfile.claude
├── docs/
│   ├── CONTRIBUTING.md
│   ├── ARCHITECTURE.md
│   └── decisions/
│       └── 001-tech-stack.md
├── src/
│   └── fraud_detection/
│       └── __init__.py
└── tests/
    └── __init__.py
```

## Next Branch

→ `git checkout 01-research-skills`
