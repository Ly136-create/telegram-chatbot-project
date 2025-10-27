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
    
    #  # PNC informations
    # if "pnc" in user_text or "passerelles numériques Cambodia" in user_text or "what is pnc" in user_text or "tell me about pnc" in user_text or "information about pnc" in user_text or "about pnc" in user_text or "pnc Cambodia" in user_text or "Passerelles Numériques Cambodia" in user_text:
    #     await update.message.reply_text(
    #         "Launched in 2005 in Phnom Penh, Passerelles Numériques Cambodia (PNC) offers a 2-year  IT training program in IT, based on a holistic approach including technical skills and professional development (or soft skills). While at PNC, the basic needs of our students (housing, food, medical care) are covered."
    #     )
    #     return

    # elif "passerelles numériques" in user_text or "What is passerelles numériques" in user_text or "passerelles numeriques" in user_text or "what is passerelles numeriques?" in user_text:
    #     await update.message.reply_text(
    #         "Passerelles Numériques is French non-profit organization, created in 2005, witch intends to enable the most under priviliged young people access to higher education and skilled employment in the promising sector of Inormation Technology (IT)."
    #     )
    #     return
    
    # elif "What is training program at pnc?" in user_text or "training program at pnc" in user_text or "tell me about training program at pnc" in user_text or "information about training program at pnc" in user_text or "training program pnc" in user_text:
    #     await update.message.reply_text(
    #         "Paserelles numeriques has implelemented an innovative and comprehensive training program in each of its centers, focused on long-term employability. An associate degree in Computer Sience, passerelles numeriques in Cambodia (PNC) offers a 2-year full time training in IT with a major in software Development, meeting the needs of local companies in the IT industry, for underprivileged Cambodian youths. PNC is registered with the Cambodian Ministry of Education, Youth and Sports. At the end of the training, students receive an Assocciate Computer Sience with a major in software Development, as well as a Passerelles Numériques certificate. Throughout their traning, students benefit from a comprehensive professional and technical skills training, and strong support for their professional integration. They also participate in extra-curricular and personal development activities."
    #     )
    #     return
    
    #  # --- 🏫 PNC Values ---
    # elif "What are the core values of PNC?" in user_text or "core values of pnc" in user_text or "PNC core values" in user_text or "values of passerelles numériques Cambodia" in user_text or "values of pnc" in user_text:
    #     await update.message.reply_text(
    #         "Passerelles Numériques Cambodia (PNC) — like all Passerelles Numériques centers — is guided by five strong core values that shape the behavior, mindset, and teamwork of every student and staff member.Here are the PNC core values:"
    #         "1.Respec: We treat everyone with kindness, fairness, and dignity. Respect is the foundation of teamwork and good communication."
    #     )
    #     return

    # --- 🏫 PNC Information and Values ---
    if any(keyword in user_text for keyword in [
        "pnc",
        "passerelles numériques cambodia",
        "passerelles numeriques cambodia",
        "what is pnc",
        "tell me about pnc",
        "information about pnc",
        "about pnc",
        "pnc cambodia"
    ]):
        await update.message.reply_text(
            "🌐 *Passerelles Numériques Cambodia (PNC)*  launched in 2005 in Phnom Penh  "
            "offers a 2-year IT training program based on a *holistic approach* combining "
            "technical skills, soft skills, and personal development. 💻\n\n"
            "While studying at PNC, students’ basic needs such as housing, food, and medical care "
            "are fully supported. 🎓",
            parse_mode="Markdown"
        )
        return

    elif any(keyword in user_text for keyword in [
        "passerelles numériques",
        "passerelles numeriques",
        "what is passerelles numériques",
        "what is passerelles numeriques"
    ]):
        await update.message.reply_text(
            "🇫🇷 *Passerelles Numériques (PN)* is a French non-profit organization* founded in 2005.* "
            "Its mission is to enable underprivileged young people to access *education* and "
            "*skilled employment* in the fast-growing IT sector. 🌍\n\n"
            "PN operates in Cambodia, the Philippines, and Vietnam.",
            parse_mode="Markdown"
        )
        return

    elif any(keyword in user_text for keyword in [
        "training program at pnc",
        "pnc training program",
        "information about training program at pnc",
        "tell me about training program at pnc",
        "what is training program at pnc"
    ]):
        await update.message.reply_text(
            "🎓 *PNC Training Program*\n\n"
            "PNC provides a 2-year full-time *Associate Degree in Computer Science*, "
            "majoring in *Software Development*. 💻\n\n"
            "The curriculum focuses on:\n"
            "• Technical and professional skills\n"
            "• English and soft skills\n"
            "• Personal development and employability\n\n"
            "PNC is officially recognized by the *Ministry of Education, Youth and Sports* of Cambodia. "
            "Students graduate with both a national diploma and a *Passerelles Numériques certificate.* 🏅",
            parse_mode="Markdown"
        )
        return

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
            "5️⃣ *Demanding Approach* — Always strive for quality and excellence. 💪\n\n"
            "These values guide how every student and staff member at PNC behaves, learns, "
            "and collaborates each day. 🤝",
            parse_mode="Markdown"
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
