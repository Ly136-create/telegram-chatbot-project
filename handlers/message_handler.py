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

    if "how are you" in user_text or "how's it going" in user_text or "how do you do" in user_text or"How was your day" in user_text:
        responses = [
            "It's going well, thank you! How about you? 😊",
            "I'm doing great 😄 How about you?",
            "All systems online 🚀 Feeling awesome!",
            "Fantastic! Thanks for asking 💪"
        ]
        await update.message.reply_text(random.choice(responses))
        return

    if "your name" in user_text or "who are you" in user_text or "what's your name" in user_text or "tell me about yourself" in user_text or "tell your name" in user_text:
        responses = [
            "I'm SmartBot 🤖, your friendly assistant!",
            "People call me SmartBot — nice to meet you!",
            "SmartBot at your service! ⚡",
            "I'm here to assist you with anything you need!",
            "I'm SmartBot, created to help you out!",
            "I'm SmartBot."
        ]
        await update.message.reply_text(random.choice(responses))
        return
    
     # PNC informations
    if "pnc" in user_text or "passerelles numériques Cambodia" in user_text or "what is pnc" in user_text or "tell me about pnc" in user_text or "information about pnc" in user_text or "about pnc" in user_text or "pnc Cambodia" in user_text or "Passerelles Numériques Cambodia" in user_text:
        await update.message.reply_text(
            "Launched in 2005 in Phnom Penh, Passerelles Numériques Cambodia (PNC) offers a 2-year  IT training program in IT, based on a holistic approach including technical skills and professional development (or soft skills). While at PNC, the basic needs of our students (housing, food, medical care) are covered."
        )
        return

    if "passerelles numériques" in user_text or "What is passerelles numériques" in user_text or "paserelles numeriques" in user_text or "what is passereles numeriques?" in user_text:
        await update.message.reply_text(
            "Passerelles Numériques is French non-profit organization, created in 2005, witch intends to enable the most under priviliged young people access to higher education and skilled employment in the promising sector of Inormation Technology (IT)."
        )
        return
    
    # Help information
    if "help" in user_text:
        await update.message.reply_text(
            "Here's what I can do:\n"
            "• Say hello or hi 👋\n"
            "• Ask how I am 😄\n"
            "• Ask my name 🤖\n"
            "• Soon I'll answer questions about PNC! 🎓"
        )
        return
    
    # Fallback response
    fallback_responses = [
        "Hmm 🤔 I'm not sure what you mean. Try typing /help.",
        "Sorry, I didn't get that 😅",
        "Could you say that another way? 💡"
    ]
    await update.message.reply_text(random.choice(fallback_responses))


# ✅ Add this line at the very end:
logic_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, logic_reply)
