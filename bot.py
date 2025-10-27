# bot.py
from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN
from handlers.start_handler import start_handler
from handlers.help_handler import help_handler
from handlers.message_handler import logic_handler

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add handlers
    app.add_handler(start_handler)
    app.add_handler(help_handler)
    app.add_handler(logic_handler)

    print("🤖 SmartBot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()