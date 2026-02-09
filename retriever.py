# retriever.py

from config import TOP_K, SIMILARITY_THRESHOLD
from vectorstore import get_collection

# query = "pointers on the influence of japan in china?"

def retrieve_context(query: str) -> str:
    collection = get_collection()
    results = collection.query(
        query_texts=[query],
        n_results=TOP_K
    )

    retrieved_documents = results["documents"][0]
    
    # scores = results["distances"][0]

    # filtered_docs = [
    #     doc for doc, score in zip(retrieved_documents, scores)
    #     if score < SIMILARITY_THRESHOLD
    # ]

    return "\n\n".join(retrieved_documents)

context = retrieve_context(query)

# print(context)
