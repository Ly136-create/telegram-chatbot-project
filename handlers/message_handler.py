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
        "hi", "hi friend", "hello", "hello friend", "hey", "hey friend",
        "good morning", "good afternoon", "good evening", "morning", "afternoon", "evening"
    ]):
        responses = [
            "Hello there! 👋 I'm SmartBot.",
            "Hey! 😊 How can I help you today?",
            "Hi friend! 🤖 What brings you here?"
        ]
        await update.message.reply_text(random.choice(responses))
        return
    
    
    elif any(keyword in clean_text for keyword in [
    "how are you", "how are you friend", "how's it going", "how do you do",
    "how was your day", "how have you been", "how are things", "how's everything"
    ]):
        responses = [
        "It's going well, thank you! How about you? 😊",
        "I'm doing great 😄 How about you?",
        "Fantastic! Thanks for asking 💪 How about you?"
    ]
        await update.message.reply_text(random.choice(responses))
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
            "**Great question!**\n\n"
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
    # students Generation 2026
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
    
    # Who handsome 
    elif any(keyword in clean_text for keyword in [
        "who is the handsome trainner",
        "who is handsome",
        "who is the most handsome",
        "tell me who the most handsome"
    ]):
        await update.message.reply_text(
        "Amazing!, \n"
        "Here is your handsome trainer.\n" 
        "He's name is T.Yon Yen. 😄" 
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
            "20. Generations 2026\n"
            "Do you have any question?😁"
        )
        return

    # Help informations
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
