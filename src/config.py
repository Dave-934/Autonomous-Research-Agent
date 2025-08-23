import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")

# Sanity checks
for key, value in {
    "OPENAI_API_KEY": OPENAI_API_KEY,
    "SERPER_API_KEY": SERPER_API_KEY,
    "PINECONE_API_KEY": PINECONE_API_KEY,
    "PINECONE_INDEX": PINECONE_INDEX,
}.items():
    if not value:
        raise ValueError(f"Missing {key} in .env")
# Note: PINECONE_ENV is not needed since we use a direct host URL.