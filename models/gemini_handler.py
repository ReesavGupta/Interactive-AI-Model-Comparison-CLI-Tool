import os
from typing import Dict, Any
from google.generativeai.client import configure
from google.generativeai.generative_models import GenerativeModel
from dotenv import load_dotenv

load_dotenv()

configure(api_key=os.getenv("GOOGLE_API_KEY"))

def query_gemini(prompt: str, model: str = "gemini-pro") -> Dict[str, Any]:
    model_obj = GenerativeModel(model)
    response = model_obj.generate_content(prompt)
    return {
        "model": model,
        "response": response.text.strip(),
        "tokens": None
    }
