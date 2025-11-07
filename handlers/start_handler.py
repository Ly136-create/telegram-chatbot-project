# handlers/start_handler.py
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
import random

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    responses = [
        "Hi! 🤖 I’m SmartBot. Type something to chat with me!",
        "Hello there! 👋 I’m SmartBot — ready to talk or help you anytime.",
        "Hey! 😊 Welcome to SmartBot. Let’s start chatting!",
        "Greetings! 🚀 I’m SmartBot, your friendly chat assistant.",
        "Welcome to SmartBot 🤖!. Type something to chat with me! "
    ]
    await update.message.reply_text(random.choice(responses))

start_handler = CommandHandler("start", start)
