from telegram.ext import Application, MessageHandler, filters, CommandHandler
from utils.config import TELEGRAM_BOT_TOKEN
from handlers.start_handler import start
from handlers.help_handler import help_command
from handlers.message_handler import handle_message
from handlers.error_handler import error_handler

def main():
    # Create application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    # Handle all text messages that are not commands
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, 
        handle_message
    ))
    
    # Error handler
    application.add_error_handler(error_handler)
    
    print("🤖 AI Telegram Bot is running...")
    print("Bot can now answer all questions!")
    application.run_polling()

if __name__ == "__main__":
    main()