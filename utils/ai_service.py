import google.generativeai as genai
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

class AIService:
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-pro')
    
    async def get_ai_response(self, user_message: str) -> str:
        """Get AI response for any question"""
        try:
            # Run the synchronous call in a thread pool
            response = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: self.model.generate_content(
                    f"""You are a helpful AI assistant. Answer the user's question in a friendly, informative way.

User: {user_message}
Assistant:"""
                )
            )
            return response.text.strip()
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"

# Create a global instance
ai_service = AIService()