import logging
from telegram import Update
from telegram.ext import ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log errors and send a friendly message"""
    logger.error(f"Exception while handling an update: {context.error}")
    
    # Send a friendly error message to user
    if update and update.effective_message:
        await update.effective_message.reply_text(
            "Sorry, I encountered an unexpected error. Please try again later."
        )