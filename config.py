import os
from dotenv import load_dotenv

# load .env 
load_dotenv()

# API Keys and Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
VECTOR_DB_FOLDER = os.getenv("VECTOR_DB_FOLDER", "vector_db")
MODEL_NAME = os.getenv("MODEL_NAME", "sentence-transformers/all-MiniLM-L6-v2")
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")