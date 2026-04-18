#!/bin/bash

# 🤖 OpenClaw v2 One-Command Boot Script

echo "🚀 Booting OpenClaw Autonomous Engine..."

# 1. Setup Environment Variables for Speed
export OLLAMA_MAX_LOADED_MODELS=1
export OLLAMA_NUM_PARALLEL=1

# 2. Check and Pre-load Ollama if needed
if ! pgrep -x "ollama" > /dev/null
then
    echo "⚙️ Starting Ollama daemon..."
    ollama serve &
    sleep 5
fi

# 3. Ensure Models are available
echo "📦 Checking models..."
ollama run qwen2.5-coder "hello" > /dev/null 2>&1 &

# 4. Start the Unified Server (Telegram + Dashboard)
echo "🌍 Starting Server & Dashboard..."
/opt/homebrew/bin/node bot.js
