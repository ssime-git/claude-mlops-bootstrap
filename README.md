# Branch 00: Project Setup

> **Goal**: Set up the project structure, devcontainer with Claude Code and GSD pre-installed, and local services (MinIO + MLflow).

## What You'll Learn

- How to structure an MLOps project with `uv`
- Setting up a devcontainer with Claude Code ready to use
- Authenticating Claude Code inside a container
- Running MinIO (S3-compatible) and MLflow locally via Docker Compose

## Prerequisites

- Docker Desktop running
- VS Code with the Dev Containers extension
- An Anthropic account (Pro, Team, or Enterprise)

## Step-by-Step

### 1. Open in devcontainer

```bash
# VS Code: Cmd/Ctrl + Shift + P → "Reopen in Container"
# Wait for post-create.sh to complete (~3 minutes)
```

### 2. Authenticate Claude Code (first time only)

```bash
claude login
# → Opens a browser link for OAuth
# → Requires an Anthropic Pro, Team, or Enterprise account
# → Token is persisted in ~/.claude/ for future sessions
```

> **Note**: The browser tool is built into Claude Code natively. No separate browser agent install needed.

### 3. Verify the installation

```bash
claude --version     # Claude Code 2.x
gsd --version        # get-shit-done-cc
uv --version         # uv 0.x
python --version     # Python 3.11.x
```

### 4. Verify services

```bash
curl http://localhost:9003  # MinIO console
curl http://localhost:5001  # MLflow UI
```

### 5. Test Claude Code

```bash
claude --permission-mode plan

# Inside Claude:
> Read the project structure and summarize what you see
```

### 6. Test GSD

```bash
claude
/gsd:help
```

## Expected Behavior

- devcontainer starts without errors
- Claude Code is installed and authenticated (`claude login`)
- GSD is available globally
- MinIO console accessible on http://localhost:9003
- MLflow UI accessible on http://localhost:5001
- Python 3.11 + uv are functional
- `claude --permission-mode plan` opens Claude in plan mode

## Project Structure

```
fraud-detection/
├── README.md
├── .gitignore
├── pyproject.toml
├── .python-version
├── .devcontainer/
│   ├── devcontainer.json
│   ├── Dockerfile
│   ├── docker-compose.dev.yml
│   └── post-create.sh
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
