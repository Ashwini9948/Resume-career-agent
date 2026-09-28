import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.5-flash")

# LangChain Google integrations expect GOOGLE_API_KEY; Gemini SDKs commonly use GEMINI_API_KEY.
os.environ.setdefault("GOOGLE_API_KEY", GEMINI_API_KEY or "")

if not GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is missing. Copy .env.example to .env and add your key."
    )
