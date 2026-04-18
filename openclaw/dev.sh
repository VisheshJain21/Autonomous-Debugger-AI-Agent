#!/bin/bash

# 🚀 OpenClaw Dev Mode: Monitoring & Orchestration

echo "🔥 Launching OpenClaw Developer Suite..."

# 1. Start Ollama if not active
if ! lsof -i:11434 > /dev/null; then
  echo "⚙️ Starting Ollama daemon..."
  ollama serve &
  sleep 3
fi

# 2. Start Bot in background (from bot directory)
echo "🤖 Starting Bot Server..."
cd bot && /opt/homebrew/bin/node bot.js &

# 3. Monitor Decision Logs in Real-time
echo "💡 Live Monitoring active. Watching for autonomous decisions..."
sleep 2
cd .. && tail -f logs/decision_log.json
