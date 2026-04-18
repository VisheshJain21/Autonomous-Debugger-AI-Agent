#!/bin/bash

# 🤖 OpenClaw v3: Interactive Boot Sequence

echo -e "
\x1b[94m🦅 OpenClaw v3 Booting...\x1b[0m
--------------------------------
🤖 Bot:        Starting
🧠 Ollama:     Checking
🌐 Dashboard:  http://localhost:3000
--------------------------------
"

# 1. Setup Environment Variables
export OLLAMA_MAX_LOADED_MODELS=1
export OLLAMA_NUM_PARALLEL=1

# 2. Check and Pre-load Ollama
if ! lsof -i:11434 > /dev/null; then
    echo "⚙️ Starting Ollama daemon..."
    ollama serve &
    sleep 3
fi

# 3. Start Unified Server
cd bot && /opt/homebrew/bin/node bot.js