from telegram import Update
from telegram.ext import ContextTypes
from utils.ai_service import ai_service

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    
    # Don't process commands
    if user_message.startswith('/'):
        return
    
    # Show typing action
    await update.message.chat.send_action(action="typing")
    
    try:
        # Get AI response for any question
        ai_response = await ai_service.get_ai_response(user_message)
        
        # Send response back to user
        await update.message.reply_text(ai_response)
        
    except Exception as e:
        await update.message.reply_text(f"Sorry, I'm having trouble right now. Please try again later. Error: {str(e)}")