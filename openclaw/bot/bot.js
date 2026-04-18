import TelegramBot from 'node-telegram-bot-api';
import { spawn, exec } from 'child_process';
import fs from 'fs';
import path from 'path';
import http from 'http';
import dotenv from 'dotenv';

dotenv.config({ path: '../.env' });
const token = "8284033013:AAGsLnJzoAnqOI9qOpyusr0LiQsMOf7II6o";
const allowedUser = 1388349912;
const PORT = process.env.PORT || 3000;
const bot = new TelegramBot(token, { polling: { interval: 300, autoStart: true, params: { timeout: 10 } } });

let isRunning = false;
let currentChild = null;
const LOGS_DIR = '../logs';
if (!fs.existsSync(LOGS_DIR)) fs.mkdirSync(LOGS_DIR);

const runAgent = (chatId, mode = "full", provider = "local") => {
    if (isRunning) return bot.sendMessage(chatId, "⏳ Busy!");
    isRunning = true;
    const pythonPath = "/Users/vishesh_jain/.pyenv/versions/3.11.9/bin/python";
    bot.sendMessage(chatId, `🚀 **OpenClaw ${mode.toUpperCase()}** started...`);
    
    // 🔥 Updated spawn path to use common parent structure
    currentChild = spawn(pythonPath, ["../agent/main.py", "--mode", mode, "--provider", provider]);

    currentChild.stdout.on('data', (d) => process.stdout.write(d.toString()));
    currentChild.stderr.on('data', (d) => process.stderr.write(`\x1b[91m❌\x1b[0m ${d}`));

    currentChild.on('close', (code) => {
        isRunning = false;
        currentChild = null;
        bot.sendMessage(chatId, code === 0 ? "✅ Task completed! Check console for summary." : `❌ Job crashed (Code ${code})`);
    });
};

bot.on('message', (msg) => {
  const chatId = msg.chat.id;
  if (msg.from.id !== allowedUser) return;
  const text = msg.text;

  if (text === "/start") {
    bot.sendMessage(chatId, "🛠 **OpenClaw Command Center**", {
        reply_markup: {
            inline_keyboard: [
                [{ text: "🚀 Run", callback_data: 'run_local' }, { text: "🧠 Deep", callback_data: 'run_cloud' }],
                [{ text: "📊 Status", callback_data: 'status' }, { text: "💚 Health", callback_data: 'health' }]
            ]
        }
    });
  }
  
  if (text === "/health") {
      exec("ollama ps", (err, stdout) => {
          const ollamaStatus = stdout ? "OK ✅" : "OFF ❌";
          bot.sendMessage(chatId, `🕵️‍♂️ **System Health Check**\n\n- **Ollama**: ${ollamaStatus}\n- **Bot**: Running ✅\n- **Dashboard**: http://localhost:3000\n- **Agent**: Ready ✅`);
      });
  }
});

bot.on('callback_query', (query) => {
    const data = query.data;
    if (data === 'run_local') runAgent(query.message.chat.id, "full", "local");
    if (data === 'run_cloud') runAgent(query.message.chat.id, "full", "cloud");
    if (data === 'health') bot.sendMessage(query.message.chat.id, "/health");
    if (data === 'status') exec("ollama ps", (e, s) => bot.sendMessage(query.message.chat.id, `🏭 Models:\n${s}`));
    bot.answerCallbackQuery(query.id);
});

const server = http.createServer((req, res) => {
    if (req.url === '/') res.end(fs.readFileSync('../dashboard/index.html'));
    else if (req.url === '/logo.png') res.end(fs.readFileSync('../assets/logo.png'));
});

server.listen(PORT, () => {
    console.log(`Server running on ${PORT}`);
}).on("error", (err) => {
    if (err.code === "EADDRINUSE") {
        console.log("⚠️ Port 3000 already in use. Try another port.");
        process.exit(1);
    } else {
        console.error(err);
    }
});