
import os
import streamlit as st

from ingestion import load_text_file, split_documents
from vectorstore import get_collection, add_documents
from retriever import retrieve_context
from prompt import build_prompt
from llm import generate_answer
from helper_utils import join_docs
from config import CHROMA_PATH


# Streamlit page config
st.set_page_config(
    page_title="RAG Question Answering",
    layout="wide"
)

st.title("📘The Great Wall-E")
st.caption("RAG Question Answering System on Chinese Revolution")
import streamlit as st
import base64

def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}

        /* TRANSLUCENT BLACK BOXES */
        .overlay-box {{
            background-color: rgba(0, 0, 0, 0.75); /* translucent black */
            padding: 25px;
            border-radius: 12px;
            color: #ffffff;
            font-size: 16px;
            line-height: 1.8;
            margin-top: 20px;
            margin-bottom: 20px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.8);
        }}

        h3 {{
            color: #f5f5f5;
            margin-bottom: 15px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
set_background("china.png")

# Index document ONCE

@st.cache_resource
def index_fixed_document():
    """
    Index the fixed document only once.
    This prevents re-indexing on every Streamlit rerun.
    """
    collection = get_collection()

    # If collection already has data, skip indexing
    if collection.count() > 0:
        return collection

    docs = load_text_file("china_revolution.txt")
    chunks = split_documents(docs)
    add_documents(collection, chunks)


# Run indexing
index_fixed_document()
# Question answering UI
st.header("Find out interesting facts about the Chinese Revolution!")

query= st.text_input(
    "Enter your question:",
    placeholder="e.g. When did the Chinese Revolution begin?"
)

if st.button("Answer"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        context = retrieve_context(query)
        prompt = build_prompt(context, query)
        answer = generate_answer(prompt)
        st.markdown(
            f"""
            <div class="overlay-box">
                <h3>Answer</h3>
                {answer}
            </div>
            """,
            unsafe_allow_html=True
        )

        # # with st.expander(" Retrieved Context"):
        # #     for i, doc in enumerate(context.split("\n\n")[:5], 1):
        # #         st.markdown(f"** {i}**")
        # #         st.write(doc[:1000])
        


