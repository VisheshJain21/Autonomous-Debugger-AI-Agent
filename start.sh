#!/bin/bash

# 🦅 OpenClaw: Unified Startup Engine
# ----------------------------------
# This script initializes the Ollama daemon and boots the bot/dashboard.

# 1. Configuration & Paths
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CORE_DIR="$PROJECT_ROOT/core"
SERVER_DIR="$PROJECT_ROOT/server"
ACTIVITY_LOG="$PROJECT_ROOT/logs/activity.json"

# Add common local paths
export PATH=$PATH:/opt/homebrew/bin:/usr/local/bin

# 0. Kill existing instances on port 3000
lsof -ti:3000 | xargs kill -9 2>/dev/null || true

echo -e "
\x1b[94m🦅 OpenClaw System Booting...\x1b[0m
----------------------------------
🤖 Environment:  $(basename "$PROJECT_ROOT")
🌐 Dashboard:    http://localhost:3000
🧠 Status:       Checking dependencies...
----------------------------------
"

# 2. Dependency Check: Ollama
OLLAMA_BIN=$(which ollama || find /Applications/Ollama.app/Contents/Resources/ollama -type f 2>/dev/null | head -n 1)

if [ ! -z "$OLLAMA_BIN" ]; then
    export PATH="$(dirname "$OLLAMA_BIN"):$PATH"
fi

if ! lsof -i:11434 > /dev/null; then
    echo "⚙️ Starting Ollama daemon..."
    if [ ! -z "$OLLAMA_BIN" ]; then
        "$OLLAMA_BIN" serve &>/dev/null &
        sleep 5
    else
        echo "❌ ERROR: Ollama binary not found. Please install from https://ollama.com"
        exit 1
    fi
else
    echo "✅ Ollama is already active."
fi

# 3. Environment Setup
export OLLAMA_MAX_LOADED_MODELS=1
export OLLAMA_NUM_PARALLEL=1

# 4. Launch Bot & Dashboard
echo "🤖 Launching Command Center..."
cd "$SERVER_DIR" && npm start
