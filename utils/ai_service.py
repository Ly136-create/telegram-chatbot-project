import google.generativeai as genai
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

class AIService:
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("❌ GEMINI_API_KEY not found in .env file")
        
        genai.configure(api_key=self.api_key)
        
        # Use the reliable gemini-pro model
        self.model = genai.GenerativeModel('gemini-pro')
        print("✅ AI Service initialized with gemini-pro")
    
    async def get_ai_response(self, user_message: str) -> str:
        """Get AI response for any question"""
        try:
            # Show what's being processed
            print(f"📨 User question: {user_message[:100]}...")
            
            response = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: self.model.generate_content(
                    f"""You are a helpful AI assistant. Answer the user's question clearly and helpfully.

User: {user_message}

Assistant:"""
                )
            )
            
            ai_response = response.text.strip()
            print(f"🤖 AI Response: {ai_response[:100]}...")
            return ai_response
            
        except Exception as e:
            error_msg = f"Sorry, I encountered an error: {str(e)}"
            print(f"❌ Error: {error_msg}")
            return error_msg

# Create global instance
ai_service = AIService()