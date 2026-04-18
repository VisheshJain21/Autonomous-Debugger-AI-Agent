# 🤖 OpenClaw: Autonomous AI Coding Engine

> **Autonomous Debugging | Self-Healing Loops | Test-Driven Evolution**

OpenClaw is a product-grade autonomous agentic workflow designed to identify, patch, and verify Python codebases entirely on local infrastructure.

## 🚀 The Architecture

OpenClaw employs a **4-Stage ReAct Pipeline** powered by localized Ollama models:

1.  **🧠 Planning (Llama 3)**: Analyzes code structure and predicts potential failure points.
2.  **🔍 Debugging (Qwen 2.5 Coder)**: Generates localized patches and logic corrections.
3.  **💻 Coding (DeepSeek Coder)**: Rebuilds the codebase with the proposed fixes.
4.  **🧪 Testing (Qwen 2.5 Coder)**: Writes and executes `pytest` unit tests with strict coverage requirements.

## 🛠️ Key Features

-   **Anti-Cheat Validator**: Integrated regex engine that detects and rejects faked test results.
-   **Confidence Gate**: Only commits to Git if the test suite passes AND coverage exceeds 80%.
-   **Intelligent Loop**: Automatically feeds `pytest` failure traces back into the LLM for recursive healing.
-   **Telegram Interface**: Remote command-and-control with real-time progress updates and log auditing.

## 📦 Getting Started

### 1. Pre-requisites
- **Ollama**: Running locally with `qwen2.5-coder`, `deepseek-coder`, and `llama3`.
- **Python 3.11**: Loaded via `pyenv`.
- **Telegram Bot**: Your own Bot API token.

### 2. Boot the Engine
```bash
# Start the Telegram Bot & Remote Server
node bot.js
```

### 3. Remote Control
Message your bot:
- `/run`: Start the full autonomous fix loop.
- `/quick`: Execute a fast syntax-only patch.
- `/status`: Monitor VRAM and active models.
- `/logs`: Audit the latest AI reasoning trail.

---

*Built with ❤️ by Antigravity for the next generation of autonomous engineering.*
