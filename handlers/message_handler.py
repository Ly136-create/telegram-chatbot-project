# handlers/message_handler.py
import random
from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters

async def logic_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower().strip()

    greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening", "morning", "afternoon", "evening"]
    if any(greet in user_text for greet in greetings):
        responses = [
            "Hello there! 👋 I'm SmartBot.",
            "Hey! 😊 How can I help you today?",
            "Hi friend! 🤖 What brings you here?"
        ]
        await update.message.reply_text(random.choice(responses))
        return

    if "how are you" in user_text:
        responses = [
            "I'm doing great 😄 How about you?",
            "All systems online 🚀 Feeling awesome!",
            "Fantastic! Thanks for asking 💪"
        ]
        await update.message.reply_text(random.choice(responses))
        return

    if "your name" in user_text or "who are you" in user_text:
        responses = [
            "I'm SmartBot 🤖, your friendly assistant!",
            "People call me SmartBot — nice to meet you!",
            "SmartBot at your service! ⚡"
        ]
        await update.message.reply_text(random.choice(responses))
        return

    if "help" in user_text:
        await update.message.reply_text(
            "Here’s what I can do:\n"
            "• Say hello or hi 👋\n"
            "• Ask how I am 😄\n"
            "• Ask my name 🤖\n"
            "• Soon I’ll answer questions about PNC! 🎓"
        )
        return

    fallback_responses = [
        "Hmm 🤔 I’m not sure what you mean. Try typing /help.",
        "Sorry, I didn’t get that 😅",
        "Could you say that another way? 💡"
    ]
    await update.message.reply_text(random.choice(fallback_responses))


# ✅ Add this line at the very end:
logic_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, logic_reply)
