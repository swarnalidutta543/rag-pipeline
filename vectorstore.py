from importlib.resources import path
import chromadb
from chromadb.utils import embedding_functions
from config import EMBEDDING_MODEL, CHROMA_COLLECTION, CHROMA_PATH
from ingestion import split_documents, load_text_file


def get_collection():
    client = chromadb.Client(
        chromadb.config.Settings(
            persist_directory=CHROMA_PATH
        )
    )

    embedding_function = embedding_functions.OpenAIEmbeddingFunction(
        model_name=EMBEDDING_MODEL
    )

    collection = client.get_or_create_collection(
        name=CHROMA_COLLECTION,
        embedding_function=embedding_function,
        metadata={"hnsw:space": "cosine"} 
    )

    return collection


def add_documents(collection, chunks: list[str]):
    collection.add(
        documents=chunks,
        ids=[f"chunk_{i}" for i in range(len(chunks))]
    )
    return f"Added {len(chunks)} chunks."

path = "china_revolution.txt"
add_documents(get_collection(), split_documents(load_text_file(path)))


