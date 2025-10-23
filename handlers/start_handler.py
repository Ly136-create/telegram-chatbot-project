from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = """
🤖 Welcome to SmartBot!

I'm an AI-powered chatbot that can help you with:
• Answering any questions
• Providing information
• Having conversations
• And much more!

Just send me a message and I'll respond!
    """
    await update.message.reply_text(welcome_text)