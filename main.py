import os
import threading
import random
from flask import Flask
import telebot

TOKEN = os.environ.get("BOT_TOKEN", "PASTE_YOUR_TOKEN_HERE")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Running!"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Welcome! Bot is LIVE ✅\n\nSend /signal to get a trading signal\nSend /help for commands")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(message, "Commands:\n/start - Start bot\n/signal - Get signal\n/help - Help")

@bot.message_handler(commands=['signal'])
def signal(message):
    pairs = ["EUR/USD", "GBP/USD", "USD/JPY", "BTC/USD", "GOLD"]
    pair = random.choice(pairs)
    direction = random.choice(["CALL 🟢 UP", "PUT 🔴 DOWN"])
    time = random.choice(["1 MIN", "2 MIN", "5 MIN"])
    msg = f"📈 SIGNAL\n\nPair: {pair}\nDirection: {direction}\nTimeframe: {time}\n\n⚠️ Trade with risk management"
    bot.reply_to(message, msg)

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    print("Bot Started...")
    bot.infinity_polling()
