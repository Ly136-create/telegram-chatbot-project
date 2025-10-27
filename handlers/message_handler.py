# handlers/message_handler.py
from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters

async def logic_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip().lower()

    if "hello" in user_text or "hi" in user_text:
        await update.message.reply_text("Hello there! 👋 I'm SmartBot.")
    elif "how are you" in user_text:
        await update.message.reply_text("I'm doing great 😄 How about you?")
    elif "your name" in user_text:
        await update.message.reply_text("I'm SmartBot 🤖, nice to meet you!")
    elif "help" in user_text:
        await update.message.reply_text("You can say 'hello', 'how are you', or ask my name.")
    else:
        await update.message.reply_text("Hmm 🤔 I don’t understand. Try typing /help.")

logic_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, logic_reply)
