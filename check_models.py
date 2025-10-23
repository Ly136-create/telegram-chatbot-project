import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

print("🔍 Checking ALL available models...")

try:
    models = genai.list_models()
    
    print("📋 Available Models:")
    print("=" * 50)
    
    for i, model in enumerate(models, 1):
        model_name = model.name
        generation_methods = model.supported_generation_methods
        print(f"{i}. {model_name}")
        print(f"   Methods: {generation_methods}")
        print()
        
    print("=" * 50)
    
    # Check specifically for flash models
    flash_models = [m for m in models if 'flash' in m.name.lower()]
    if flash_models:
        print("🎉 Flash models found!")
        for model in flash_models:
            print(f"   ✅ {model.name}")
    else:
        print("❌ No flash models found in your account")
        
except Exception as e:
    print(f"❌ Error: {e}")