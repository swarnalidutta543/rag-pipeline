from openai import OpenAI
from dotenv import load_dotenv
from langchain_core.documents import Document
from config import CHUNK_SIZE, CHUNK_OVERLAP
# import umap

# Load environment variables from .env file
load_dotenv()

# openai_key = os.getenv("OPENAI_API_KEY")
# client = OpenAI(api_key=openai_key)

# path = "china_revolution.txt"

# ingestion.py

# path = "china_revolution.txt"

def load_text_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    return text

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)
# split the text into smaller chunks
def split_documents(text: str) -> list[str]:
    character_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        separators=["\n\n", "\n", ". ", " ", ""], chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
    )
    chunks = character_splitter.split_text(text)
    # print(chunks[10])
    print(f"\nTotal chunks: {len(chunks)}")
    return chunks


