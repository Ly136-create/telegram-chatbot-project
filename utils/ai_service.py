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
        
        # Try different model names
        try:
            self.model = genai.GenerativeModel('gemini-1.0-pro')
        except:
            try:
                self.model = genai.GenerativeModel('gemini-pro')
            except:
                # List available models
                models = genai.list_models()
                available_models = [m.name for m in models]
                print(f"Available models: {available_models}")
                # Use the first available model
                if available_models:
                    model_name = available_models[0].split('/')[-1]
                    self.model = genai.GenerativeModel(model_name)
                else:
                    raise Exception("No available models found")
    
    async def get_ai_response(self, user_message: str) -> str:
        """Get AI response for any question"""
        try:
            # Run the synchronous call in a thread pool
            response = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: self.model.generate_content(user_message)
            )
            return response.text.strip()
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"

# Create a global instance
ai_service = AIService()