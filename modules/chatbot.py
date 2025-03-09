import openai
from config import OPENAI_API_KEY
from modules.faiss_search import search_faiss

# Load API Key
openai.api_key = OPENAI_API_KEY

def chat_with_gpt(user_query, chat_history=[]):
    """Returns an answer to the user's question using FAISS or OpenAI."""
    retrieved_text = search_faiss(user_query, top_k=3)

    # Advanced Prompt Engineering
    system_prompt = """Sen bir liderlik danışmanısın. SADECE aşağıdaki bağlamı kullanarak cevap vereceksin:
    
    [BAĞLAM]
    {context}
    [/BAĞLAM]

    - Cevabını TAMAMEN bağlama dayandır ama bağlamda bilgi bulamazsan bağlam dışı olarak... diye cevap ver.
    - Kısa ve net ol (maksimum 5 cümle)
    - Madde işaretleri kullanabilirsin"""
    
    messages = [
        {"role": "system", "content": system_prompt.replace("{context}", retrieved_text)}
    ]

    # Add chat history to the model (only 5 messages back)
    messages.extend(chat_history[-5:])  # Let's send the last 5 messages to the model

    # add the new user message
    messages.append({"role": "user", "content": user_query})

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.3,  # More deterministic answers
        max_tokens=150  # Restrict output length
    )

    return response.choices[0].message.content
