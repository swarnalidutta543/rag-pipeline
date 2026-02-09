# prompt.py
from retriever import retrieve_context 

def build_prompt(context: str, question: str) -> str:
    return f"""
        You are a strict question-answering assistant.

        ONLY answer the question if the answer is clearly supported
        by the context below.
        If you answer, the response MUST be between 500 and 1000 words.
        If the question is unrelated to the context,
        or the answer is not present, reply EXACTLY with:
        "I am sorry. I lack sufficient information to answer your question."

        Do NOT use outside knowledge.
        Do NOT guess.
        

        Context:
        {context}

        Question:
        {question}

        Answer:
        """
 
