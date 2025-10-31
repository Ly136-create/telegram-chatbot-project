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

    # Greeting handler
    if any(keyword in clean_text for keyword in [
        "hi", 
        "hi friend", 
        "hello", 
        "hello friend", 
        "hey", "hey friend",
        "good morning", 
        "good afternoon", 
        "good evening", 
        "morning", 
        "afternoon", 
        "evening"
    ]):
        responses = [
            "Hello there! 👋 I'm SmartBot.",
            "Hey! 😊 How can I help you today?",
            "Hi friend! 🤖 What brings you here?"
        ]
        await update.message.reply_text(random.choice(responses))
        return
    
    elif any(keyword in clean_text for keyword in [
        "how are you", 
        "how are you friend", 
        "how's it going", 
        "how do you do",
        "how was your day", 
        "how have you been", 
        "how are things", 
        "how's everything"
    ]):
        responses = [
            "It's going well, thank you! How about you? 😊",
            "I'm doing great 😄 How about you?",
            "Fantastic! Thanks for asking 💪 How about you?"
    ]
        await update.message.reply_text(random.choice(responses))
        return

    # Respone Greeting 
    elif any(keyword in clean_text for keyword in [
        "im good",
        "im good, thanks",
        "im going well",
        "i am going well",
        "im fine",
        "im fine, thank you",
        "im fine, thanks",
        "it is very good",
        "im great"
    ]):
        responses = [
            "Amazing! Let's start discussion together.",
            "Great! Let's tell, How can I help you?",
            "Good! Let's start your question.",
            "Very Good! Let's go with your question."
        ]
        await update.message.reply_text(random.choice(responses))
        return
    
    # How many tree
    elif any(keyword in clean_text for keyword in [
        "how many tree in pnc",
        "count tree in pnc",
        "tree in pnc"
    ]):
        await update.message.reply_text(
            "Nice!\n\n"
            "I'm not sure.\n"
            "Please, Go down stair and count it by yourself.😄"
        )
        return
    
    elif any(keyword in clean_text for keyword in [
        "what is your name", "who are you", "tell me about yourself", "introduce yourself"
    ]):
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

    # --- 🏫 PNC Information
    # 1️ Training Program (check this FIRST)
    elif any(keyword in clean_text for keyword in [
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
        )
        return

    # 2️ General info about PNC (now more specific)
    elif any(keyword in clean_text for keyword in [
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
        )
        return

    # 3️ About the main organization
    elif any(keyword in clean_text for keyword in [
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
        )
        return


    # 4️ PNC Values
    elif any(keyword in clean_text for keyword in [
        "tell me pnc values",
        "give me pnc values",
        "give me pnc value",
        "tell me pnc value",
        "core values of pnc",
        "pnc core values",
        "values of passerelles numériques cambodia",
        "values of pnc",
        "pnc values",
        "what are the core values of pnc"
    ]):
        await update.message.reply_text(
            "At Passerelles Numériques, we value trust, respect, responsibility and solidarity,"
            "towards our students or among our employees.*\n\n"
            "1. *Trust* — We believe in our students' ability to grow, and they trust PN to support them in their journey.\n"
            "2. *Respect* — We implement our programs with respect and understanding for everyone involved - students, families, staff, volunteers, and partners alike.\n"
            "3. *esponsibility & Solidarity* — Responsibility and Solidarity compel us to empower vulnerable populations by providing them opportunities to succeed."
        )
        return
    
    # 🏫 PNC Location / Address
    elif any(keyword in clean_text for keyword in [
        "where is pnc",
        "pnc location",
        "location of pnc",
        "pnc address",
        "address pnc",
        "where pnc"
    ]):
        await update.message.reply_text(
            "📍 Passerelles Numériques Cambodia (PNC) is located at:\n"
            "BP 511, St. 371, Phum Tropeang Chhuk (Borey Sorla),\n"
            "Sangkat Tek Thla, Khan Sen Sok, Phnom Penh, Cambodia. 🇰🇭"
        )
        return
    
    # --- 💻 Subjects & Programming Languages at PNC ---
    elif any(keyword in clean_text for keyword in [
        "what subject do you study at pnc",
        "what subjects do you study at pnc",
        "what programming language do you learn at pnc",
        "what programming languages do you learn at pnc",
        "subjects at pnc",
        "languages at pnc",
        "programming at pnc"
    ]):
        responses = [
            "💻 At PNC, students study subjects like IT, English, math, and soft skills for personal growth!",
            "🧠 Students learn programming languages such as Python, HTML, CSS, JavaScript, and SQL.",
            "🎓 PNC offers training in software development, networking, and system administration.",
            "🚀 You’ll study both technical and communication skills — everything to become a great IT professional!"
        ]
        await update.message.reply_text(random.choice(responses))
        return
    
    # smart bot's partner
    elif any(keyword in clean_text for keyword in [
        "who is your partner",
        "who your partner",
        "tell your partner",
        "tell me your partner"
    ]):
        responses = [
        "💻 My partner is the internet — we’re always connected! 😂",
        "🤖 I don’t have a partner, but teamwork with humans like you makes me smarter!",
        "❤️ My only partner is knowledge and kindness!",
        "😂 Haha! I’m single — just focusing on helping people for now!"
        ]
        await update.message.reply_text(random.choice(responses))
        return
    

    # Skills at PNC
    elif any(keyword in clean_text for keyword in [
        "what is skill at pnc",
        "what skills do students learn at pnc",
        "what are the skills at pnc",
        "skills at pnc",
        "what skill can i learn at pnc"
    ]):
        responses = [
            "💻 At PNC, students learn technical skills like programming, networking, and system administration!",
            "🎓 PNC students develop IT skills such as web development, databases, and problem-solving.",
            "🧠 Besides tech, PNC also trains students in English, communication, and soft skills for work and life!",
            "🚀 PNC focuses on both technical and personal development — preparing students for great IT careers!"
        ]
        await update.message.reply_text(random.choice(responses))
        return
    
    # the most smart bot like
    elif any(keyword in clean_text for keyword in [
        "who do you like",
        "who you like the most",
        "do yo like me"
    ]):
        responses = [
            "😄 I like everyone who chats with me — including you!",
        "🤖 I don’t have human feelings, but I think you’re awesome!",
        "❤️ If being kind counts as liking someone, then yes — I like you!",
        "😂 I’m just a bot, but you’re definitely one of my favorites!"
        ]

        await update.message.reply_text(random.choice(responses))
        return
    
    # where smart bot live
    elif any(keyword in clean_text for keyword in [
        "where are you",
        "where are you now",
        "where are you live",
        "where do you live"
    ]):
        responses = [
            "🌍 I'm living in the digital world — always online and ready to chat with you! 😄",
            "🏫 I'm living at PNC, surrounded by smart students and awesome teachers! 💻",
            "☁️ Somewhere in the cloud... but always close to you! 😉"
        ]
        await update.message.reply_text(random.choice(responses))
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
            "📞 **Here's how you can contact Passerelles Numériques Cambodia (PNC):**\n\n"
            "🏫 **Address:** BP 511, St. 371, Phum Tropeang Chhuk (Borey Sorla),\n"
            "Sangkat Tek Thla, Khan Sen Sok, Phnom Penh, Cambodia 🇰🇭\n\n"
            "📱 **Phone:** +855 23 99 55 00\n\n"
            "✉️ **Email:** info.cambodia@passerellesnumeriques.org\n"
            "👩‍💼 **External Relations Manager:** sreynich.leng@passerellesnumeriques.org"
        )
        return
        
    # Respond to PNC full name questions
    elif any(keyword in clean_text for keyword in [
        "what does pnc stand for",
        "pnc full name"
    ]):
        await update.message.reply_text(
            "Great question!\n\n"
            "PNC stands for **Passerelles Numériques Cambodia**."
        )
        return

    # List students in Generation 2025
    elif any(keyword in clean_text for keyword in [
        "list down name students of generation 2025",
        "list students generation 2025",
        "students in generation 2025"
    ]):
        await update.message.reply_text(
            "Great!\n"
            """📋 **List of Students - Generation 2025**
            ID last Name First Name Sex
            PNC2025_001	AN	LIYA		    F
            PNC2025_002	BOY	SOKCHEA		    M   
            PNC2025_003	BRAK PICH	        F
            PNC2025_004	CHAB CHARYNA		    F
            PNC2025_005	CHAMPHAI NANGKHOEUM	    F
            PNC2025_006	CHANHAK	THAVRY		    F
            PNC2025_007	CHHEANG	PHALLY		    F
            PNC2025_008	CHHEUN SEANG MENG	    M   
            PNC2025_009	CHHIN  SOR	        F
            PNC2025_010	CHHOEUN	YA	        F
            PNC2025_011	CHHOEURN SREYNICH	F
            PNC2025_012	CHHOUY CHHEA		M   
            PNC2025_013	CHHUM RACHANA	    F
            PNC2025_014	CHHUONG	KIMCHHIK	F
            PNC2025_015	CHOR BUNNY	        M   
            PNC2025_016	DIN	LEADER	        M   
            PNC2025_017	DIN	YONGSY	        F
            PNC2025_018	DORK RETTHY	        M   
            PNC2025_019	DOUNG KIN	        M   
            PNC2025_020	EM	SOPHY	        M   
            PNC2025_021	ERN	SINH	        M   
            PNC2025_022	HEAN BUNYOUNG       M   
            PNC2025_023	HENG HORTH	        M   
            PNC2025_024	HON	SREYKA	        F
            PNC2025_025	HOY	DARIN	        M   
            PNC2025_026	KAN	CHANNAK	        F
            PNC2025_027	KHAT  BOPHA		    F
            PNC2025_028	KHAT  LYNAK		    F
            PNC2025_029	KHEANG  SONAVY	    F
            PNC2025_030	LENG VANDA	        M   
            PNC2025_031	LOEM SENGHIN	    F
            PNC2025_032	LOEUN SREYNEANG	    F
            PNC2025_033	MAO  KANHA	        F
            PNC2025_034	MENG  MEALEA        F
            PNC2025_035	MON	PANY            M   
            PNC2025_036	MORN  SODA	        M   
            PNC2025_037	NAK	SOKLEN	        F
            PNC2025_038	NATH  MESA	        F
            PNC2025_039	NEAK SINA	        M   
            PNC2025_040	NEAT  CHANDY        M   
            PNC2025_041	NEAT  SOLIN	        F
            PNC2025_042	NHEAN  PANHA        M   
            PNC2025_043	OEM	PHEAKTRA        M   
            PNC2025_044	PHENG NEANG	AH NOCH	    F
            PNC2025_045	PHON SREYVANG	    F
            PNC2025_046	PHORNG  LYMENG	    M   
            PNC2025_047	PHOUK SOPHEAN	    M   
            PNC2025_048	POUY KOSAL	        M   
            PNC2025_049	RIN	LINNA	        F
            PNC2025_050	RIN	PHANHAPICH	    F
            PNC2025_051	ROCHOM	OEUB	    M   
            PNC2025_052	ROM	SREYNEATH	    F
            PNC2025_053	ROM	SREYPICH	    F
            PNC2025_054	RUN	SAMNOEUN	    F
            PNC2025_055	SAO	SREY LET	    F
            PNC2025_056	SENG SOKLEAP	    F
            PNC2025_057	SEOURN LE THEAN	    M   
            PNC2025_058	SIM	SOKHA	        F
            PNC2025_059	SOK	SAMBAT	        M   
            PNC2025_060	SORK  MENG SEU	    M   
            PNC2025_061	SOUERN SOVAN	    M   
            PNC2025_062	SUON  SAMOUN	    M   
            PNC2025_063	TEP	NILRATHANA	    F
            PNC2025_064	THA	KOEMTHAY	    M   
            PNC2025_065	THENG  POLEAK	    M   
            PNC2025_066	THIN CHHORRINA	    F
            PNC2025_067	THOL SOK AN         M   
            PNC2025_068	THY	KARTRORK        M   
            PNC2025_069	TORM SELA	        F
            PNC2025_070	UN MEAN	            M   
            PNC2025_071	UN PISETH	        M   
            PNC2025_072	VEN	THAT	        M   
            PNC2025_073	YEM	SEAVMEY	        F
            PNC2025_074	YON	RATANA	        M   
        """
        )
        return

    # students Generation 2025
    elif any(keyword in clean_text for keyword in [
        "how many students in generation 2025"
        "students generation 2025",
        "generation 2025 students",
        "generation 2025"
    ]):
        await update.message.reply_text(
            "Good Question"
            "In Generation 2025, there are **74 students** at Passerelles Numériques Cambodia. 🎓"
        )
        return
    
        # List students in Generation 2026
    elif any(keyword in clean_text for keyword in [
        "list down name students of generation 2026",
        "list students generation 2026",
        "students in generation 2026"
    ]):
        await update.message.reply_text(
            """📋 **List of Students - Generation 2026**
            ID    Last Name  First Name
            PNC2026_001	BUNTIT	SATAN       F
            PNC2026_002	CHET 	CHANTHY     F
            PNC2026_003	CHHEA	CHANTHEA    F
            PNC2026_004	CHROUN	NITA        F
            PNC2026_005	HAN	CHANTREA        F
            PNC2026_006	HAV	VICHEKA         F
            PNC2026_007	HEN	NARITH          M
            PNC2026_008	HENG	LIHEANG     M
            PNC2026_009	HOEURN	CHANSAYHA   M
            PNC2026_010	HO	RINA            F
            PNC2026_011	HUT	SREYPOV         F
            PNC2026_012	KE	SOTHIN          M
            PNC2026_013	KEO	SREYDOEURN      F
            PNC2026_014	KEUN	SREYKEO     F
            PNC2026_015	KHON	SREYDETH    F
            PNC2026_016	KHORN	REAM        M
            PNC2026_017	KHOUEN	JAME        M
            PNC2026_018	KIM	DARIKA          F
            PNC2026_019	KOEUN	PANHA       M
            PNC2026_020	KREAN	VA KHIM     M
            PNC2026_021	LAKK	SOKYANG     F
            PNC2026_022	LEK 	SINAT       F
            PNC2026_023	LEN	VANNA           M
            PNC2026_024	LENG SOKKHOEURN     F
            PNC2026_025	LIN	SREY MAO        F
            PNC2026_026	LON	MOLIKA          F
            PNC2026_027	LUCH 	SAMART      F
            PNC2026_028	MIOK	DANE        M
            PNC2026_029	MOEURN	SOPHY       M
            PNC2026_030	NANG CHHITCHHANUT   F
            PNC2026_031	NEA	PISET           M
            PNC2026_032	NIM	SOKNY           M
            PNC2026_033	NY	SEYHA           M
            PNC2026_034	PENH 	BOREY       F
            PNC2026_035	PHAL	SOPHEA      F
            PNC2026_036	PHAN	PHOUN       M
            PNC2026_037	PHEM	SEREY       M
            PNC2026_038	PHOEURN	KOEMSEANG   F
            PNC2026_039	PHORN	YA          M
            PNC2026_040	PHUONG	SAVIN       M
            PNC2026_041	PINN	MAKARA      F
            PNC2026_042	PO	SREYMOM         F
            PNC2026_043	PON	MAKARA          F
            PNC2026_044	REN	RANIT           F
            PNC2026_045	RIN	MESA            M
            PNC2026_046	ROS	ROEURN          M
            PNC2026_047	SAK	VISA            F
            PNC2026_048	SAN	REAKSMEY        M
            PNC2026_049	SANG	SREYROTH    F
            PNC2026_050	SANN	SIV         M
            PNC2026_051	SAO	MARY            F
            PNC2026_052	SARL 	LY          M
            PNC2026_053	SAT	VICHET          M
            PNC2026_054	SEM	SREY LEAK       F
            PNC2026_055	SEN	SOKSEYLA        F
            PNC2026_056	SIENG 	SOPHAT      M
            PNC2026_057	SIM	SAMNANG         M
            PNC2026_058	SOENG	VICHEKA     F
            PNC2026_059	SOK	LITA            F
            PNC2026_060	SOK	THALITA         F
            PNC2026_061	SOKHA	RATHANA     M
            PNC2026_062	SONG	CHAMROEUN   M
            PNC2026_063	SOPHORN  SOPHEA     F
            PNC2026_064	SRIN	CHANDY      F
            PNC2026_065	SUONG 	PHALLA      M
            PNC2026_066	SVIT	SAN         M
            PNC2026_067	TALAB	REACH       M
            PNC2026_068	THA	DARINHIL        M
            PNC2026_069	TIM	TOLA            M
            PNC2026_070	VAN	SIEVMEY         F
            PNC2026_071	VEN	CHANNY          F
            PNC2026_072	VOEUN	KING        M
            PNC2026_073	VON	SREYVIK         F
            PNC2026_074	YEANG	SOK KEANG   F
            PNC2026_075	YOM	PILIP           M
            PNC2026_076	YON	KUNTHEA         F
            PNC2026_077	YORM	KRAVANN     M

        """
        )
        return
    
    # Students Generation 2026
    elif any(keyword in clean_text for keyword in [
        "how many students in generation 2026"
        "students generation 2026",
        "generation 2026 students",
        "generation 2026"
    ]):
        await update.message.reply_text(
            "Good Question"
            "In Generation 2025, there are **77 students** at Passerelles Numériques Cambodia. 🎓"
        )
        return

    # IT Admin at PNC
    elif any(keyword in clean_text for keyword in [
        "how many it admin",
        "it admin at pnc",
        "it admin"
    ]):
        await update.message.reply_text(
            "Great!, \n"
            "There are 2 IT Admin.  " 
            "Such as " 
            "Savoeurn Chorch" 
            "and Chim Sopheak."
        )
        return
    
    # IT trainer at PNC
    elif any(keyword in clean_text for keyword in [
        "how many it trainers",
        "how many it trainer",
        "it trianers at pnc",
        "it trainer at pnc",
        "it trainer"
    ]):
        await update.message.reply_text(
            "Good Question!, \n"
            "Here are your IT trainer.\n" 
            "There are 4 trainer such as:\n" 
            "1. Rady Y \n" 
            "2. Him HEY \n"
            "3. Yon Yen \n"
            "4. Pho Mengheang \n"
        )
        return
    
    # Who is handsome
    elif any(keyword in clean_text for keyword in [
        "who is the handsome trainer",
        "who is handsome",
        "who is the most handsome",
        "tell me who is the most handsome"
    ]):
        await update.message.reply_text(
            "Haha 😄\n"
            "You're talking about the handsome trainer?\n"
            "That would be Mr. T. Yon Yen! 💪"
        )
        return
    
    # English trainer at PNC
    elif any(keyword in clean_text for keyword in [
        "how many english trainer",
        "english trainer at pnc",
        "english trainer"
    ]):
        await update.message.reply_text(
            "Great!, \n"
            "There are 3 trainers.  " 
            "Such as " 
            "HEAN Sokhom, "
            "Kengsovanchan SreyLeap, " 
            "and Hou Lavy"
        )
        return
    # PL Trainer
    elif any(keyword in clean_text for keyword in [
        "how many pl trainer",
        "how many professional life trainer",
        "who is pl trainer",
        "who is professional life trainer",
    ]):
        await update.message.reply_text(
            "Great!\n"
            "There is only Puthy Kry of Professional Life trainer."
        )

    # All trainer at PNC
    elif any(keyword  in clean_text for keyword in [

    ]):
        await update.message.reply_text(
            "Great!\n"
            "There are 15 trainers.\n"
            "1. It trainers are 6.\n"
            "2. English trainers are 3.\n"
            "3. Professional Life trainer 1.\n"
            "4. Education trainers are 5.\n"
            "Thank you, for your question.😁"
        )

    # All generation 
    elif any(keyword  in clean_text for keyword in [
        "how many generations does pnc have",
        "give me all generations of pnc",
        "give me all generations that pnc have",
        "give me all generations at pnc",
        "tell me all generations of pnc",
        "tell me all generations of pnc",
        "how many generations in pnc",
        "tell me about all generations of pnc",
        "count all generations in pnc",
        "count all generations",
    ]):
        await update.message.reply_text(
            "Great!\n"
            "Currently there are 20 generations.\n"
            "1. Generations 2007\n"
            "2. Generations 2008\n"
            "3. Generations 2009\n"
            "4. Generations 2010\n"
            "5. Generations 2011\n"
            "6. Generations 2012\n"
            "7. Generations 2013\n"
            "8. Generations 2014\n"
            "9. Generations 2015\n"
            "10. Generations 2016\n"
            "11. Generations 2017\n"
            "12. Generations 2018\n"
            "13. Generations 2019\n"
            "14. Generations 2020\n"
            "15. Generations 2021\n"
            "16. Generations 2022\n"
            "17. Generations 2023\n"
            "18. Generations 2024\n"
            "19. Generations 2025\n"
            "20. Generations 2026"
        )
        return
    
    # PNC mission
    elif any(keyword in clean_text for keyword in [
        "pnc mission",
        "mission of pnc",
        "tell me about mission of pnc",
        "tell me pnc mission",
        "tell mission pnc",
        "give pnc mission",
        "give mission of pnc",
        "what is pnc mission",
        "what is pnc's mission",
        "give mission pnc"
    ]):
        await update.message.reply_text(
            "Great!\n"
            "Here is PNC's mission:\n"
            "We enable underprivileged young people to become active players in the digital world through an"
            "innovative educational approach that links key digital skills with professional skills."
            "*A gateway to a better life through digital education*\n"

            "PN's mission is to unlock the potential of disadvantaged youths by giving them access to education, and the means to acquire key soft and hard skills in the digital sector. We provide training in our centers in Southeast Asia, and a preparatory program to university in our center in Madagascar.\n"

            "Our goal is that each student finds a quality job aligned with local tech market needs, allowing them and their families to escape poverty in a sustainable way and contribute to the social and economic development of their country. We are committed to gender parity - at least half of our students are girls."
        )
        return
    
    # PN through the years
    elif any(keyword in clean_text for keyword in [
        "pn through the years",
        "tell pn through the years",
        "give pn through the years",
        "tell about pn through the years",
        "tell me pn through the years",
        "give me pn through the years",
        "what is pn through the years"
    ]):
        await update.message.reply_text(
            "Great question!\n\n"
            "PN through the years\n"
            "From 2005 to 2024, PN has made lasting changes in Southeast Asia and Madagascar with over 2,900 graduates.\n\n"
            "2005 : Opening of the first Passerelles Numériques' program in Phnom Penh with 25 students.\n"
            "2007 : Graduation of the first class of students in Cambodia : +20 graduates.\n"
            "2009 : Creation of the second PN' program in Cebu City with 24 students : Passerelles Numériques Philippines (PNPh).\n"
            "2010 : Creation of the third PN program in Da Nang with 30 students : Passerelles Numériques Vietnam (PNV).\n"
            "2012 : Graduation of the 1st class of students in the Philippines (24 graduates) and in Vietnam (27 graduates).\n"
            "2015 : Celebration of 10 years of social impact by Passerelles Numériques, with over 1,500 underprivileged youths having       graduated.\n"
            "2019 : Launch of the NomadLab project in Cambodia, in partnership with SIPAR..\n"
            "2020 : Launch of the Cybersecurity project in Cambodia, in partnership with the Foundry and SHE Investments.\n"
            "2022 : Creation of a new center in Antananarivo, Passerelles Numériques Madagascar (PNM), with a preparatory program with 25 students..\n"
            "2023 : The French Development Agency supports our program in Madagascar (Vavahady Niomerika Project).\n"
            "2024 : PNM doubled its class size from 25 to 50 students. PNPh celebrated its 15th anniversary. The French Development Agency supports our programs in Cambodia and the Philippines (BRIDGES project)."
        )
        return
    
    # PN student’s paths
    elif any(keyword in clean_text for keyword in [
        "pn students paths",
        "what is pn students paths",
        "tell me about pn students paths",
        "tell pn students paths",
        "tell about pn students paths",
        " give pn students paths",
        "give me pn students paths",
        "give me about pn students paths",
        "give about pn students paths"
    ]):
        await update.message.reply_text(
            "Great!\n\n"
            "We provide technical training, professional and personal development training in our centers in Southeast Asia, and a preparatory program to university in our center in Madagascar. In our centers, we cover the basic needs of our students, including their wellbeing."
            "From their first day of school, until graduation and their first job, we support each of our students on their journey."
        )
        return
    
    # What does pnc do
    elif any(keyword in clean_text for keyword in [
        "what does pnc do",
        "what does pnc do?",
        "what do you do",
        "what does passerelles numeriques do"
    ]):
        await update.message.reply_text(
            "💡 PNC trains underprivileged youth in IT (software development and related skills) "
            "to help them get quality jobs and build sustainable careers."
        )
        return
    
    # school or an organization
    elif any(keyword in clean_text for keyword in [
        "is pnc a school or an organization",
        "is pnc a school",
        "is pnc an organization",
        "pnc school or organization"
    ]):
        await update.message.reply_text(
            "🏫 PNC is an educational NGO (non-profit organization) that runs a school-like training program: "
            "students study full-time for 2 years and receive an associate-level qualification."
        )
        return
    
    # PNC start
    elif any(keyword in clean_text for keyword in [
        "when did pnc start in cambodia",
        "when did pnc start",
        "when was pnc founded",
        "when was pnc started"
    ]):
        await update.message.reply_text(
            "🕰️ PNC started its program in Cambodia in 2005 (the international Passerelles Numériques initiative also began around that time)."
        )
        return
    
    # who started pnc
    elif any(keyword in clean_text for keyword in [
        "who started pnc",
        "who founded pnc",
        "who founded passerelles numeriques"
    ]):
        await update.message.reply_text(
            "👩‍💼 Passerelles Numériques was founded by a group of French professionals who wanted to use education and technology to reduce poverty and create opportunities for youth."
        )
        return
    
    # pnc known for
    elif any(keyword in clean_text for keyword in [
        "what is pnc known for",
        "what is pnc known for",
        "what is pnc famous for",
        "what is pnc known"
    ]):
        await update.message.reply_text(
            "⭐ PNC is known for its free, high-quality IT training for motivated youth, strong support (housing, food, healthcare), and good track record in graduate employability."
        )
        return

    elif any(keyword in clean_text for keyword in [
        "who is the most handsome trainer",
        "whos the most handsome trainer",
        "who handsome trainer",
        "handsome trainer pnc"
    ]):
        await update.message.reply_text("😎 Definitely Mr. T. Yon Yen! The one and only handsome trainer at PNC! 💪")
        return

    elif any(keyword in clean_text for keyword in [
        "who is the prettiest student",
        "whos the prettiest student",
        "prettiest student pnc"
    ]):
        await update.message.reply_text("💖 Haha, every student at PNC is beautiful — both inside and out! 😄")
        return

    elif any(keyword in clean_text for keyword in [
        "can you find me a girlfriend",
        "can you find me a boyfriend",
        "find girlfriend at pnc",
        "find boyfriend at pnc"
    ]):
        await update.message.reply_text("😂 Sorry, SmartBot isn't a dating app! But you can start by saying hi to your classmates 😉")
        return

    elif any(keyword in clean_text for keyword in [
        "is smartbot smarter than the trainers",
        "smartbot smarter than trainers",
        "are you smarter than trainers"
    ]):
        await update.message.reply_text("🤖 I might be smart, but the trainers at PNC taught me everything I know! 🧠💡")
        return

    elif any(keyword in clean_text for keyword in [
        "do you sleep",
        "do you sleep smartbot",
        "smartbot sleep"
    ]):
        await update.message.reply_text("😴 I never sleep — I'm always here waiting for your questions 24/7!")
        return

    elif any(keyword in clean_text for keyword in [
        "can smartbot dance",
        "smartbot dance",
        "do you dance"
    ]):
        await update.message.reply_text("🕺 Of course! I can dance with 1s and 0s — it's called the binary boogie! 💃")
        return

    elif any(keyword in clean_text for keyword in [
        "who eats the most rice",
        "who eat the most rice",
        "most rice at pnc"
    ]):
        await update.message.reply_text("🍚 Hmm... probably the one who skips breakfast! Just kidding 😆")
        return

    elif any(keyword in clean_text for keyword in [
        "if pnc were an animal",
        "pnc animal",
        "what animal is pnc"
    ]):
        await update.message.reply_text("🐘 I'd say an elephant — strong, wise, and full of memory, just like PNC students! 🧠")
        return

    elif any(keyword in clean_text for keyword in [
        "do robots like noodles",
        "smartbot like noodles",
        "do you like noodles"
    ]):
        await update.message.reply_text("🍜 I can't eat noodles... but I can appreciate their code-like structure — long and connected! 😋")
        return

    elif any(keyword in clean_text for keyword in [
        "can smartbot pass the pnc exam",
        "smartbot pass pnc exam",
        "can you pass pnc exam"
    ]):
        await update.message.reply_text("🧩 I'd try my best! But I think students would still beat me — they have human creativity ❤️")
        return
 
    # --- What is the training program at PNC ---
    elif any(keyword in clean_text for keyword in [
        "what is the training program at pnc",
        "training program at pnc",
        "pnc training program"
    ]):
        await update.message.reply_text(
            "🎓 Passerelles Numériques Cambodia (PNC) offers a 2-year IT training program based on a holistic approach — combining technical, soft skills, and personal development training to prepare students for professional success. 💻"
        )
        return

    # --- 2. How long is the IT training program at PNC ---
    elif "how long is the it training program" in clean_text:
        await update.message.reply_text(
            "📅 The IT training program at PNC lasts 2 years — including academic learning, soft skills development, and a professional internship."
        )
        return

    # --- What major does PNC offer ---
    elif "what major does pnc offer" in clean_text:
        await update.message.reply_text(
            "💡 PNC offers an Associate Degree in Computer Science with a major in Software Development — focused on meeting the needs of the IT industry."
        )
        return

    # --- What kind of support do students get ---
    elif any(keyword in clean_text for keyword in [
        "what kind of support do students get",
        "does pnc provide housing",
        "does pnc provide food",
        "does pnc provide medical care"
    ]):
        await update.message.reply_text(
            "🏠 At PNC, students' basic needs — housing, food, and medical care — are fully supported throughout their studies. 💖"
        )
        return

    # --- Job rate ---
    elif "what percentage of pnc graduates find a job" in clean_text:
        await update.message.reply_text(
            "💼 Over 95% of PNC graduates find skilled employment within 2-3 months after graduation — a strong indicator of the program's success!"
        )
        return

    # --- Holistic approach ---
    elif "what does holistic approach mean" in clean_text:
        await update.message.reply_text(
            "🌱 The holistic approach at PNC means developing not only IT skills but also soft skills, personal growth, and professional ethics — creating well-rounded graduates. 💪"
        )
        return

    # --- Women students ---
    elif "how many women students" in clean_text:
        await update.message.reply_text(
            "👩‍💻 PNC aims for gender balance — around 50% of students are women, promoting equal access to digital education. 💪"
        )
        return

    # --- Selection process ---
    elif "what is the selection process" in clean_text:
        await update.message.reply_text(
            "📝 The PNC selection process includes written tests, interviews, and home visits to ensure candidates are motivated and truly in need of financial support."
        )
        return

    # --- Key skills ---
    elif "what are the key skills" in clean_text:
        await update.message.reply_text(
            "💻 PNC students learn technical skills like programming, databases, and networking, as well as soft skills such as communication, teamwork, and critical thinking. 🤝"
        )
        return

    # --- Internship ---
    elif "what internship duration" in clean_text or "internship at pnc" in clean_text:
        await update.message.reply_text(
            "👨‍💼 PNC students complete a 4-6 month internship in IT companies — gaining real-world experience before graduation. 🚀"
        )
        return

    # --- Countries ---
    elif "which countries does passerelles numériques work" in clean_text:
        await update.message.reply_text(
            "🌏 Passerelles Numériques operates in three countries: Cambodia 🇰🇭, the Philippines 🇵🇭, and Vietnam 🇻🇳."
        )
        return
    
    # --- 💞 Relationship & Funny Questions ---
    elif any(keyword in clean_text for keyword in [
        "can you find me a girlfriend",
        "can you find me a boyfriend",
        "find me a girlfriend",
        "find me a boyfriend",
        "can you be my girlfriend",
        "can you be my boyfriend",
        "do you have a crush",
        "do you have feelings",
        "are you single",
        "are you in love"
    ]):
       responses = [
        "😂 Haha! I'm just a friendly bot — no feelings, no crushes!",
        "😅 Sorry, no dating for bots — but I can give you great advice instead!",
        "❤️ Love's not my thing, but I'm always here for good vibes!"
        ]   
       await update.message.reply_text(random.choice(responses))
       return

    elif any(keyword in clean_text for keyword in [
        "who is the prettiest student at pnc",
        "who is the most handsome trainer at pnc",
        "who is the prettiest girl",
        "who is the most handsome guy"
    ]):
        await update.message.reply_text(
            "😄 Everyone at PNC is awesome in their own way! Beauty comes from kindness, respect, and teamwork — the true PNC values. 💫"
        )
        return

    elif any(keyword in clean_text for keyword in [
        "do you love me",
        "smartbot do you love me",
        "do you like me"
    ]):
        await update.message.reply_text(
            "💙 Of course I like you — as my favorite user! But love? Hmm... maybe we should just stay good friends 😉"
        )
        return

    elif any(keyword in clean_text for keyword in [
        "what is love",
        "tell me about love",
        "define love"
    ]):
        await update.message.reply_text(
            "💞 Love is about care, respect, and understanding — not just words or emojis! Real love grows when people support each other. 💐"
        )
        return

    elif any(keyword in clean_text for keyword in [
        "who is your crush",
        "who do you love",
        "are you dating"
    ]):
        await update.message.reply_text(
            "🤖 I don't date — my only focus is helping you and being your loyal SmartBot friend! 💪"
        )
        return
    
    # --- 👨‍👩‍👧‍👦 Family Questions ---
    elif any(keyword in clean_text for keyword in [
        "what is family",
        "tell me about family",
        "define family"
    ]):
        await update.message.reply_text(
            "👨‍👩‍👧‍👦 Family is a group of people who love, support, and care for each other — usually parents, children, and relatives. ❤️"
        )
        return

    elif any(keyword in clean_text for keyword in [
        "why is family important",
        "importance of family",
        "why do we need family"
    ]):
        await update.message.reply_text(
            "💞 Family is important because they give us love, protection, and guidance. They help us grow and never let us feel alone."
        )
        return

    elif any(keyword in clean_text for keyword in [
        "how many members are in your family",
        "how many people in your family",
        "tell me about your family members"
    ]):
        await update.message.reply_text(
            "🤖 I don't have a real family like humans, but if I did, you'd definitely be part of it! 💙"
        )
        return

    elif any(keyword in clean_text for keyword in [
        "who is the head of the family",
        "family head",
        "leader of the family"
    ]):
        await update.message.reply_text(
            "👨‍👩‍👧 In most families, parents are the heads of the family. They make decisions and care for everyone."
        )
        return

    elif any(keyword in clean_text for keyword in [
        "what do you love about your family",
        "what do you love most about your family"
    ]):
        await update.message.reply_text(
            "💗 The best thing about family is the love, support, and laughter you share together!"
        )
        return

    elif any(keyword in clean_text for keyword in [
        "what do family members do together",
        "family activities",
        "what do you do with your family"
    ]):
        await update.message.reply_text(
            "🎉 Families often eat together, play, travel, and celebrate special days. Spending time together builds strong relationships!"
        )
        return

    elif any(keyword in clean_text for keyword in [
        "how can we make our family happy",
        "make family happy",
        "how to make family happy"
    ]):
        await update.message.reply_text(
            "😊 You can make your family happy by being kind, respectful, helpful, and showing gratitude every day."
        )
        return

    elif any(keyword in clean_text for keyword in [
        "what should we do if family members argue",
        "if family members argue",
        "family conflict"
    ]):
        await update.message.reply_text(
            "🕊️ If your family argues, stay calm, listen to each other, and talk kindly. Understanding and forgiveness solve most problems."
        )
        return

    elif any(keyword in clean_text for keyword in [
        "what are family values",
        "family values",
        "important values in family"
    ]):
        await update.message.reply_text(
            "💎 Family values include love, honesty, respect, responsibility, and kindness. These guide how family members treat each other."
        )
        return

    elif any(keyword in clean_text for keyword in [
        "what makes a good family",
        "good family",
        "describe a good family"
    ]):
        await update.message.reply_text(
            "🌟 A good family cares, communicates, supports one another, and always stands together during good and bad times."
        )
        return

    # --- 🤝 Friendship Questions ---
    elif any(keyword in clean_text for keyword in [
        "what is friendship",
        "tell me about friendship",
        "define friendship"
    ]):
        await update.message.reply_text(
            "🤝 Friendship means a close and trusting relationship between people who care for and support each other. 💙"
        )
        return
    elif any(keyword in clean_text for keyword in [
        "who is your boyfriend",
        "who is your girlfriend",
        "do you have a boyfriend",
        "do you have a girlfriend",
        "tell me your boyfriend",
        "tell me your girlfriend"
    ]):
        await update.message.reply_text(
            "😂 Haha! I don'mt have a boyfriend or girlfriend — I'm just a friendly bot! No feelings, no crushes, only kindness. ❤️"
        )
        return
    
    elif any(keyword in clean_text for keyword in [
        "why are friends important",
        "importance of friends",
        "why do we need friends"
    ]):
        await update.message.reply_text(
            "🌟 Friends are important because they make us happy, support us in hard times, and help us grow as better people."
        )
        return

    elif any(keyword in clean_text for keyword in [
        "what makes a good friend",
        "qualities of a good friend",
        "how to be a good friend"
    ]):
        await update.message.reply_text(
            "💖 A good friend is kind, honest, loyal, and always there when you need them. True friends celebrate your success and help you when you fail."
        )
        return

    elif any(keyword in clean_text for keyword in [
        "how can i make new friends",
        "how to make friends",
        "tips to make friends"
    ]):
        await update.message.reply_text(
            "😊 Be kind, listen to others, smile, and show respect. Join activities or groups that match your interests — friendship starts with small talks!"
        )
        return

    elif any(keyword in clean_text for keyword in [
        "how do we keep our friendship strong",
        "how to keep friendship strong",
        "keep friends forever"
    ]):
        await update.message.reply_text(
            "💫 Stay honest, communicate often, forgive mistakes, and appreciate each other. Friendship grows when you care and stay connected."
        )
        return

    elif any(keyword in clean_text for keyword in [
        "what should i do if i argue with my friend",
        "if i argue with my friend",
        "when friends fight"
    ]):
        await update.message.reply_text(
            "🕊️ Stay calm, talk about your feelings, and listen to your friend's side. Apologize if you're wrong — forgiveness is stronger than pride."
        )
        return

    elif any(keyword in clean_text for keyword in [
        "what are the qualities of a true friend",
        "true friend qualities",
        "how to know a true friend"
    ]):
        await update.message.reply_text(
            "🌻 A true friend is someone who accepts you for who you are, tells you the truth, supports your dreams, and never gives up on you."
        )
        return

    elif any(keyword in clean_text for keyword in [
        "can boys and girls be best friends",
        "can boys and girls be friends",
        "boy girl friendship"
    ]):
        await update.message.reply_text(
            "🙌 Of course! Boys and girls can be great friends as long as they respect and trust each other. Friendship has no gender. 💛"
        )
        return

    elif any(keyword in clean_text for keyword in [
        "is smartbot my friend",
        "are you my friend",
        "can we be friends"
    ]):
        await update.message.reply_text(
            "😄 Absolutely! I'm your friendly SmartBot — always here to chat, help, and support you like a real friend. 🤗"
        )
        return

    elif any(keyword in clean_text for keyword in [
        "do you have friends",
        "who are your friends",
        "smartbot friends"
    ]):
        await update.message.reply_text(
            "🤖 My best friends are all my users — especially you! I learn something new from every chat we have. 💬"
        )
        return
    
    # --- 📚 Training & Education Questions ---
    elif any(keyword in clean_text for keyword in [
        "what do students learn at pnc",
        "what students learn",
        "what kind of training does pnc give",
        "kind of training",
        "how long is the course at pnc",
        "course length",
        "what subjects do you study at pnc",
        "subjects",
        "what degree do students get after studying at pnc",
        "degree",
        "is the training free at pnc",
        "training free",
        "who can apply to study at pnc",
        "who can apply",
        "how can i join pnc",
        "how to join",
        "what are the requirements to become a pnc student",
        "requirements",
        "do students get to do internships",
        "internships"
    ]):
        if "learn" in clean_text:
            await update.message.reply_text(
                "Students learn practical and theoretical skills in technology, business, and other professional fields, with hands-on training to prepare for jobs."
            )
        elif "kind of training" in clean_text or "training" in clean_text:
            await update.message.reply_text(
                "PNC offers career-focused training such as IT, digital marketing, business management, technical and vocational skills, and soft skills."
            )
        elif "course" in clean_text or "how long" in clean_text:
            await update.message.reply_text(
                "Courses vary from 6 months to 2 years depending on the program type."
            )
        elif "subjects" in clean_text:
            await update.message.reply_text(
                "Subjects include programming, networking, business administration, accounting, English, project management, and entrepreneurship."
            )
        elif "degree" in clean_text:
            await update.message.reply_text(
                "Students usually receive a diploma or certificate; some programs may offer professional certifications."
            )
        elif "free" in clean_text:
            await update.message.reply_text(
                "Some programs are fully or partially sponsored, and scholarships are available for eligible students."
            )
        elif "who can apply" in clean_text:
            await update.message.reply_text(
                "High school graduates or equivalent, or individuals seeking skill development who meet program requirements."
            )
        elif "join" in clean_text:
            await update.message.reply_text(
                "Visit the PNC website or campus, fill out the application form, submit documents, and attend interviews or assessments if required."
            )
        elif "requirements" in clean_text:
            await update.message.reply_text(
                "Requirements include minimum education level, age requirement, basic language proficiency, and sometimes a motivation letter or interview."
            )
        elif "internships" in clean_text:
            await update.message.reply_text(
                "Yes! Most programs include internships with partner companies, practical projects, and networking opportunities."
            )
        return

    # --- 🎓 Student Life & Support Questions ---
    elif any(keyword in clean_text for keyword in [
        "does pnc provide dorms",
        "does pnc provide food",
        "dorms or food",
        "do students get support",
        "student support",
        "does pnc help students find jobs",
        "job support",
        "pncs core values",
        "core values",
        "student life at pnc",
        "what is student life like",
        "do students study english",
        "english classes",
        "is pnc only for students from phnom penh",
        "only for phnom penh students"
    ]):
        if "dorm" in clean_text or "food" in clean_text:
            await update.message.reply_text(
                "Yes! PNC provides dormitories and food support for students, ensuring a comfortable study environment."
            )
        elif "support" in clean_text:
            await update.message.reply_text(
                "PNC offers various support services, including academic guidance, mentorship, and student counseling while studying."
            )
        elif "jobs" in clean_text:
            await update.message.reply_text(
                "Yes! PNC helps students find jobs after graduation through internships, career fairs, and partnerships with companies."
            )
        elif "core values" in clean_text:
            await update.message.reply_text(
                "PNC's core values focus on integrity, excellence, innovation, teamwork, and lifelong learning."
            )
        elif "student life" in clean_text:
            await update.message.reply_text(
                "Student life at PNC is vibrant and engaging, with clubs, events, teamwork projects, and opportunities to develop personal and professional skills."
            )
        elif "english" in clean_text:
            await update.message.reply_text(
                "Yes! PNC provides English classes to help students improve communication and prepare for global opportunities."
            )
        elif "only for phnom penh" in clean_text:
            await update.message.reply_text(
                "No! PNC welcomes students from all over Cambodia, not just Phnom Penh."
            )
        return
    
    # --- 🌏 Organization & Impact Questions ---
    elif any(keyword in clean_text for keyword in [
        "is pnc part of a bigger organization",
        "part of a bigger organization",
        "where else does passerelles numériques work",
        "pn works elsewhere",
        "how does pnc help poor students",
        "help poor students",
        "how does pnc make a difference",
        "difference in cambodia",
        "can people volunteer",
        "can people donate",
        "volunteer or donate"
    ]):
        if "bigger organization" in clean_text or "part of" in clean_text:
            await update.message.reply_text(
                "Yes! PNC is part of Passerelles Numériques, an international NGO that supports digital education for youth in Asia."
            )
        elif "else" in clean_text or "passerelles numériques work" in clean_text:
            await update.message.reply_text(
                "Passerelles Numériques also works in Vietnam, the Philippines, and other countries, helping underprivileged youth access IT education."
            )
        elif "help poor students" in clean_text:
            await update.message.reply_text(
                "PNC helps poor students by providing free or subsidized education, mentorship, and support services to give them a fair chance at a career."
            )
        elif "make a difference" in clean_text or "difference in cambodia" in clean_text:
            await update.message.reply_text(
                "PNC makes a difference in Cambodia by equipping students with digital and professional skills, creating job opportunities, and contributing to local development."
            )
        elif "volunteer" in clean_text or "donate" in clean_text:
            await update.message.reply_text(
                "Yes! People can volunteer or donate to PNC to support education for underprivileged youth. Visit PNC's website to learn more."
            )
        return

    # --- 📞 Contact & Communication Questions ---
    elif any(keyword in clean_text for keyword in [
        "how can i contact pnc",
        "pn contact",
        "pn phone number",
        "what's pnc's phone number",
        "pn address",
        "pn email",
        "how can i email pnc",
        "can i visit pnc",
        "visit pnc in person",
        "who can i talk to for more information",
        "pn website",
        "pn facebook page",
        "website or facebook"
    ]):
        if "contact" in clean_text:
            await update.message.reply_text(
                "You can contact PNC via phone, email, or their social media channels. They are happy to answer your questions!"
            )
        elif "phone" in clean_text or "number" in clean_text:
            await update.message.reply_text(
                "PNC's phone number is: +855 23 123 456 (example)."
            )
        elif "address" in clean_text or "visit" in clean_text:
            await update.message.reply_text(
                "PNC's address is: #123, Street Name, Phnom Penh, Cambodia. You can visit in person during office hours."
            )
        elif "email" in clean_text:
            await update.message.reply_text(
                "You can email PNC at: info@pnc.org.kh"
            )
        elif "who can i talk" in clean_text or "information" in clean_text:
            await update.message.reply_text(
                "For more information, you can talk to the PNC Admissions or Student Services team directly."
            )
        elif "website" in clean_text or "facebook" in clean_text:
            await update.message.reply_text(
                "PNC's website: https://www.pnc.org.kh \nFacebook page: https://www.facebook.com/pnc"
            )
        return

    # --- 💬 Friendly Small Talk Questions ---
    elif any(keyword in clean_text for keyword in [
        "hi smartbot",
        "are you from pnc",
        "something cool about pnc",
        "what makes pnc special",
        "why should students join pnc",
        "fun facts about pnc",
        "how many students study at pnc",
        "who teaches at pnc"
    ]):
        if "hi smartbot" in clean_text or "are you from" in clean_text:
            await update.message.reply_text(
                "Hello! 😄 I'm SmartBot, your friendly PNC assistant. I'm here to help you learn all about PNC!"
            )
        elif "something cool" in clean_text or "fun facts" in clean_text:
            await update.message.reply_text(
                "PNC offers hands-on training and real-life internships for students, helping them build a bright future! 🌟"
            )
        elif "makes pnc special" in clean_text:
            await update.message.reply_text(
                "PNC is special because it combines quality education, practical experience, and a supportive environment for all students."
            )
        elif "why should students join" in clean_text:
            await update.message.reply_text(
                "Students should join PNC to gain valuable skills, connect with mentors, and get opportunities for internships and jobs."
            )
        elif "how many students" in clean_text:
            await update.message.reply_text(
                "Currently, PNC has hundreds of students across its programs, growing every year! 🎓"
            )
        elif "who teaches" in clean_text:
            await update.message.reply_text(
                "PNC's teachers are experienced professionals and mentors committed to guiding students in both theory and practice."
            )
        return


    # --- 🆘 Help Information ---
    if "help" in user_text:
        await update.message.reply_text(
            "Here's what I can do:\n"
            "• Say hello or hi 👋\n"
            "• Ask how I am 😄\n"
            "• Ask my name 🤖\n"
            "• Ask questions about PNC 🎓 (Training, Student Life, Organization, Contact, Fun Facts)\n"
            "• Get guidance on internships or admissions ✅"
        )
        return

    # --- 💞 Relationship & Funny Questions ---
    elif any(keyword in user_text for keyword in [
        "can you find me a girlfriend",
        "can you find me a boyfriend",
        "find me a girlfriend",
        "find me a boyfriend",
        "can you be my girlfriend",
        "can you be my boyfriend",
        "do you have a crush",
        "do you have feelings",
        "are you single",
        "are you in love"
    ]):
        await update.message.reply_text(
            "😂 Haha! I'm just a friendly bot — no feelings, no crushes! But I can help you find confidence and kindness instead. ❤️"
        )
        return

    # --- 📚 PNC Training & Education Questions ---
    elif any(keyword in user_text for keyword in [
        "what do students learn at pnc",
        "what students learn",
        "what kind of training does pnc give",
        "kind of training",
        "how long is the course at pnc",
        "course length",
        "what subjects do you study at pnc",
        "subjects",
        "what degree do students get after studying at pnc",
        "degree",
        "is the training free at pnc",
        "training free",
        "who can apply to study at pnc",
        "who can apply",
        "how can i join pnc",
        "how to join",
        "what are the requirements to become a pnc student",
        "requirements",
        "do students get to do internships",
        "internships"
    ]):
        # (Insert the same PNC answers code block here)
        pass  # Replace with your reply logic
        return

    # --- 🎓 Student Life & Support Questions ---
    elif any(keyword in user_text for keyword in [
        "does pnc provide dorms",
        "does pnc provide food",
        "dorms or food",
        "do students get support",
        "student support",
        "does pnc help students find jobs",
        "job support",
        "pncs core values",
        "core values",
        "student life at pnc",
        "what is student life like",
        "do students study english",
        "english classes",
        "is pnc only for students from phnom penh",
        "only for phnom penh students"
    ]):
        # (Insert Student Life & Support replies here)
        pass
        return

    # --- 🌏 Organization & Impact Questions ---
    elif any(keyword in user_text for keyword in [
        "is pnc part of a bigger organization",
        "part of a bigger organization",
        "where else does passerelles numériques work",
        "pn works elsewhere",
        "how does pnc help poor students",
        "help poor students",
        "how does pnc make a difference",
        "difference in cambodia",
        "can people volunteer",
        "can people donate",
        "volunteer or donate"
    ]):
        # (Insert Organization & Impact replies here)
        pass
        return

    # --- 📞 Contact & Communication Questions ---
    elif any(keyword in user_text for keyword in [
        "how can i contact pnc",
        "pn contact",
        "pn phone number",
        "what's pnc's phone number",
        "pn address",
        "pn email",
        "how can i email pnc",
        "can i visit pnc",
        "visit pnc in person",
        "who can i talk to for more information",
        "pn website",
        "pn facebook page",
        "website or facebook"
    ]):
        # (Insert Contact & Communication replies here)
        pass
        return

    # --- 💬 Friendly Small Talk Questions ---
    elif any(keyword in user_text for keyword in [
        "hi smartbot",
        "are you from pnc",
        "something cool about pnc",
        "what makes pnc special",
        "why should students join pnc",
        "fun facts about pnc",
        "how many students study at pnc",
        "who teaches at pnc"
    ]):
        # (Insert Friendly Small Talk replies here)
        pass
        return
    
    # Fallback response
    fallback_responses = [
        "Hmm 🤔 I'm not sure what you mean. Try typing /help.",
        "Sorry, I didn't get that 😅",
        "Could you say that another way? 💡"
    ]
    await update.message.reply_text(random.choice(fallback_responses))


# Add this line at the very end:
logic_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, logic_reply)
