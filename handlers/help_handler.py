from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
🆘 Help Guide

I'm an AI chatbot powered by Google Gemini. I can:

• Answer any questions you have
• Help with research and information
• Assist with learning and explanations
• Have friendly conversations

Just type your question or message, and I'll respond!

Commands:
/start - Start the bot
/help - Show this help message
    """
    await update.message.reply_text(help_text)