import re
import random
from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters

# Function to handle message logic
async def logic_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get user text safely
    user_text = update.message.text or ""
 
    # Normalize text: lowercase + remove punctuation
    clean_text = re.sub(r'[^\w\s]', '', user_text.lower()).strip()


    greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening", "morning", "afternoon", "evening"]
    if any(greet in user_text for greet in greetings):
        responses = [
            "Hello there! 👋 I'm SmartBot.",
            "Hey! 😊 How can I help you today?",
            "Hi friend! 🤖 What brings you here?"
        ]
        await update.message.reply_text(random.choice(responses))
        return
    greetings_qa = ["how are you?","how's it going?""how do you do?","how was your day?", "how have you been?", "how are things?", "how's everything?", "how are you", "how's it going", "how do you do", "how was your day", "how have you been", "how are things", "how's everinthing"]
    if any(qa in user_text for qa in greetings_qa):
        responses = [
            "It's going well, thank you! How about you? 😊",
            "I'm doing great 😄 How about you?",
            "Fantastic! Thanks for asking 💪, How about you?"
        ]
        await update.message.reply_text(random.choice(responses))
        return

    introduction_qa = ["what is your name", "who are you", "tell me about yourself", "introduce yourself"]
    if any(intro in user_text for intro in introduction_qa):
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

# --- 🏫 PNC Information & Values ---

    # 1️⃣ Training Program (check this FIRST)
    if any(keyword in user_text for keyword in [
        "training program at pnc",
        "pnc training program",
        "tell me about training program at pnc",
        "information about training program at pnc",
        "what is training program at pnc",
        "training at pnc",
        "study program at pnc"
    ]):
        await update.message.reply_text(
            "🎓 *PNC Training Program*\n\n"
            "PNC provides a 2-year full-time *Associate Degree in Computer Science*, "
            "majoring in *Software Development*. 💻\n\n"
            "The program combines:\n"
            "• Technical and professional IT skills\n"
            "• English and soft skills\n"
            "• Personal development and employability training\n\n"
            "PNC is officially recognized by the *Ministry of Education, Youth and Sports* of Cambodia. "
            "Students graduate with both a national diploma and a *Passerelles Numériques certificate.* 🏅",
            parse_mode="Markdown"
        )
        return


    # 2️⃣ General info about PNC (now more specific)
    elif any(keyword in user_text for keyword in [
        "what is pnc",
        "tell me about pnc",
        "about pnc",
        "information about pnc",
        "pnc cambodia",
        "what does pnc do",
        "passerelles numériques cambodia",
        "passerelles numeriques cambodia"
    ]):
        await update.message.reply_text(
            "🌐 *Passerelles Numériques Cambodia (PNC)* — launched in 2005 in Phnom Penh — "
            "offers a 2-year IT training program based on a *holistic approach* combining "
            "technical skills, soft skills, and personal development. 💻\n\n"
            "While studying at PNC, students’ basic needs such as housing, food, and medical care "
            "are fully supported. 🎓",
            parse_mode="Markdown"
        )
        return


    # 3️⃣ About the main organization
    elif any(keyword in user_text for keyword in [
        "what is passerelles numériques",
        "what is passerelles numeriques",
        "passerelles numériques",
        "passerelles numeriques"
    ]):
        await update.message.reply_text(
            "🇫🇷 *Passerelles Numériques (PN)* is a French non-profit organization founded in 2005. "
            "Its mission is to enable underprivileged young people to access *education* and "
            "*skilled employment* in the fast-growing IT sector. 🌍\n\n"
            "PN operates in Cambodia, the Philippines, and Vietnam.",
            parse_mode="Markdown"
        )
        return


    # 4️⃣ Core Values
    elif any(keyword in user_text for keyword in [
        "core values of pnc",
        "pnc core values",
        "values of passerelles numériques cambodia",
        "values of pnc",
        "pnc values",
        "what are the core values of pnc"
    ]):
        await update.message.reply_text(
            "🌟 *PNC Core Values*\n\n"
            "1️⃣ *Respect* — Treat everyone with fairness, dignity, and kindness.\n"
            "2️⃣ *Responsibility* — Take ownership and always do your best.\n"
            "3️⃣ *Solidarity* — Support and help each other to grow together.\n"
            "4️⃣ *Trust* — Be honest, reliable, and transparent.\n"
            "5️⃣ *Demanding Approach* — Always strive for quality and excellence. 💪",
            parse_mode="Markdown"
        )
        return
    
    # 🏫 PNC Location / Address
    elif any(keyword in clean_text for keyword in [
    "where is pnc",
    "pnc location",
    "location of pnc",
    "pnc address",
    "address pnc"
    ]):
        await update.message.reply_text(
        "📍 Passerelles Numériques Cambodia (PNC) is located at:\n"
        "BP 511, St. 371, Phum Tropeang Chhuk (Borey Sorla),\n"
        "Sangkat Tek Thla, Khan Sen Sok, Phnom Penh, Cambodia. 🇰🇭"
        )
        return

    # 📞 Contact PNC
    elif any(keyword in clean_text for keyword in [
        "how can i contact pnc",
        "contact pnc",
        "pnc contact",
        "contact passerelles numeriques cambodia",
        "contact passerelles numeriques",
        "how to contact pnc",
        "pnc phone",
        "pnc email",
        "how to reach pnc",
        "reach pnc"
    ]):
        await update.message.reply_text(
            "📞 **Here’s how you can contact Passerelles Numériques Cambodia (PNC):**\n\n"
            "🏫 **Address:** BP 511, St. 371, Phum Tropeang Chhuk (Borey Sorla),\n"
            "Sangkat Tek Thla, Khan Sen Sok, Phnom Penh, Cambodia 🇰🇭\n\n"
            "📱 **Phone:** +855 23 99 55 00\n\n"
            "✉️ **Email:** info.cambodia@passerellesnumeriques.org\n"
            "👩‍💼 **External Relations Manager:** sreynich.leng@passerellesnumeriques.org"
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
