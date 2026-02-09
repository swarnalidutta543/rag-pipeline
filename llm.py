from dotenv import load_dotenv
from openai import OpenAI
from config import LLM_MODEL
load_dotenv()
import os


openai_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key = openai_key)



def generate_answer(prompt: str) -> str:
    response = client.responses.create(
        model=LLM_MODEL,
        input=prompt
    )

    return response.output_text

#     response = client.responses.create(
#         model="gpt-4.1-mini",
#         input=prompt
#     )

#     return response.output_text

# answer = generate_response(query, retrieved_documents)
# print(answer)