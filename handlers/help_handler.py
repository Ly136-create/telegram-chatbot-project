# handlers/help_handler.py
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Available commands:\n/start - Greet the bot\n/help - Show help info")

help_handler = CommandHandler("help", help)
