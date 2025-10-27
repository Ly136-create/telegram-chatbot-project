# handlers/start_handler.py
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! 🤖 I’m SmartBot. Type something to chat with me.")

start_handler = CommandHandler("start", start)
