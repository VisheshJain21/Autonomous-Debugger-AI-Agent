#!/bin/bash

echo "🦅 OpenClaw v3 Booting..."
echo "--------------------------------"

# Move to script directory
cd "$(dirname "$0")"

echo "🤖 Bot:        Starting"
cd bot
npm start &

cd ..

echo "🧠 Ollama:     Checking"
ollama serve &>/dev/null &

echo "🌐 Dashboard:  http://localhost:3000"
echo "--------------------------------"
