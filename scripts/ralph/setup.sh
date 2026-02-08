#!/bin/bash
set -e

echo "🤖 Setting up Ralph (frankbria version)..."

if [ ! -d "$HOME/ralph" ]; then
    git clone https://github.com/frankbria/ralph-claude-code "$HOME/ralph"
    cd "$HOME/ralph" && ./install.sh
    cd -
else
    echo "Ralph already installed at ~/ralph"
fi

echo "✅ Ralph ready"
echo "Usage:"
echo "  ralph-setup --task scripts/ralph/pipeline_health_check.md"
echo "  ralph --monitor --max-iterations 50"
