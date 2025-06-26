import os
from typing import Dict, Any
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def query_openai(prompt: str, model: str = "gpt-3.5-turbo") -> Dict[str, Any]:
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )

    msg = response.choices[0].message.content

    if msg is None:
        msg = ""
    else:
        msg = msg.strip()

    token_usage = response.usage.total_tokens if response.usage else 0

    return {
        "model" : model,
        "response" : msg,
        "token_usage" : token_usage
    }    
