"""
AI Pipeline configuration module.
"""
import os
from dotenv import load_dotenv

load_dotenv()

API_BASE = os.getenv("LITELLM_API_BASE", "https://api.openai.com/v1")

def get_config():
    return {
        "api_base": API_BASE,
        "forward_headers": True,
    }
