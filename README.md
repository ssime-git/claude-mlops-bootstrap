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

### 1. Start services on the host

Before opening the devcontainer, start MinIO and MLflow on the host machine:

```bash
docker compose -f .devcontainer/docker-compose.dev.yml up -d
```

Verify they are running:

```bash
curl http://localhost:9003  # MinIO console
curl http://localhost:5001  # MLflow UI
```

### 2. Open in devcontainer

```bash
# VS Code/Windsurf: Cmd/Ctrl + Shift + P → "Reopen in Container"
# Wait for post-create.sh to complete (~3 minutes)
```

> The devcontainer connects to MinIO and MLflow running on the host via `host.docker.internal`.

### 3. Authenticate Claude Code (first time only)

```bash
claude login
# → Opens a browser link for OAuth
# → Requires an Anthropic Pro, Team, or Enterprise account
# → Token is persisted in ~/.claude/ for future sessions
```

> **Note**: The browser tool is built into Claude Code natively. No separate browser agent install needed.

### 4. Verify the installation

```bash
claude --version     # Claude Code 2.x
gsd --version        # get-shit-done-cc
uv --version         # uv 0.x
python --version     # Python 3.11.x
```

### 5. Verify services from inside the devcontainer

The services run on the host. From inside the devcontainer, access them via `host.docker.internal`:

```bash
# MinIO API
curl http://host.docker.internal:9002
# MinIO console (open in browser on host: http://localhost:9003)
# Login: minioadmin / minioadmin

# MLflow UI (open in browser on host: http://localhost:5001)
curl http://host.docker.internal:5001
```

Test MinIO with Python:

```python
import boto3

s3 = boto3.client(
    "s3",
    endpoint_url="http://host.docker.internal:9002",
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin",
)
s3.list_buckets()  # Should return empty list
```

Test MLflow:

```python
import mlflow

mlflow.set_tracking_uri("http://host.docker.internal:5001")
mlflow.search_experiments()  # Should return default experiment
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

On the host:

```bash
docker compose -f .devcontainer/docker-compose.dev.yml down
```

## Expected Behavior

- Services (MinIO, MLflow) start on the host without port conflicts
- devcontainer starts without errors
- Claude Code is installed and authenticated (`claude login`)
- GSD is available globally
- MinIO reachable from devcontainer at `host.docker.internal:9002` (API) / `:9003` (console)
- MLflow reachable from devcontainer at `host.docker.internal:5001`
- MinIO console accessible in browser at http://localhost:9003
- MLflow UI accessible in browser at http://localhost:5001
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
