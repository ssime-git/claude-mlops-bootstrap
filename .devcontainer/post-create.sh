#!/bin/bash
set -e

echo "🔧 Installing uv..."
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.cargo/env

echo "🔧 Installing Claude Code..."
curl -fsSL https://code.claude.com/install.sh | sh
# NOTE: Run `claude login` manually after first start to authenticate
# with your Pro/Team account. Token persists in ~/.claude/.

echo "🔧 Installing GSD globally..."
npm install -g get-shit-done-cc

echo "🔧 Setting up Python environment..."
uv sync

echo "🔧 Installing pre-commit hooks..."
uv run pre-commit install

echo "✅ Development environment ready!"
echo "   - Claude Code: $(claude --version 2>/dev/null || echo 'not yet installed')"
echo "   - GSD: $(gsd --version 2>/dev/null || echo 'not yet installed')"
echo "   - uv: $(uv --version)"
echo "   - Python: $(python --version)"
echo ""
echo "⚠️  Run 'claude login' to authenticate (first time only)"
