#!/bin/bash

# 🚀 OpenClaw: Developer Suite
# ---------------------------
# Integrated lifecycle management with real-time log monitoring.

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CORE_DIR="$PROJECT_ROOT/core"
SERVER_DIR="$PROJECT_ROOT/server"
ACTIVITY_LOG="$PROJECT_ROOT/logs/activity.json"

echo "🔥 Launching OpenClaw Developer Suite..."

# 1. Start Ollama if not active
OLLAMA_BIN=$(which ollama || find /Applications/Ollama.app/Contents/Resources/ollama -type f 2>/dev/null | head -n 1)

if ! lsof -i:11434 > /dev/null; then
  echo "⚙️ Starting Ollama daemon..."
  if [ ! -z "$OLLAMA_BIN" ]; then
    "$OLLAMA_BIN" serve &>/dev/null &
    sleep 5
  else
    echo "❌ ERROR: Ollama binary not found."
    exit 1
  fi
fi

# 2. Start Bot in background
echo "🤖 Starting Bot Server..."
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
cd "$SERVER_DIR" && node bot.js &

# 3. Monitor Decision Logs in Real-time
echo "💡 Live Monitoring active. Watching for autonomous decisions..."
sleep 2

if [ -f "$ACTIVITY_LOG" ]; then
    tail -f "$ACTIVITY_LOG"
else
    echo "⏳ Waiting for first run to generate logs at: $ACTIVITY_LOG"
    # Wait for file to exist then tail
    while [ ! -f "$ACTIVITY_LOG" ]; do sleep 1; done
    tail -f "$ACTIVITY_LOG"
fi
