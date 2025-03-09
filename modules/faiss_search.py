import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from config import VECTOR_DB_FOLDER, MODEL_NAME

# FAISS Model Loading
print(" Model ve FAISS veritabanı yükleniyor...")
model = SentenceTransformer(MODEL_NAME)
index = faiss.read_index(f"{VECTOR_DB_FOLDER}/vector_database.faiss")

# Uploading Texts
with open(f"{VECTOR_DB_FOLDER}/texts.txt", "r", encoding="utf-8") as f:
    texts = [line.strip() for line in f.readlines()]

def clean_text(text):
    """Removes unnecessary characters, resulting in smoother text."""
    return text.replace("\n", " ").replace("  ", " ").strip()

def search_faiss(query, top_k=3):
    """Searches FAISS and returns the most relevant text."""
    print(f" FAISS içinde arama yapılıyor: {query}")
    
    query_vector = np.array([model.encode(query)]).astype('float32')
    D, I = index.search(query_vector, k=top_k)

    results = [{"text": clean_text(texts[i]), "score": float(D[0][j])} for j, i in enumerate(I[0])]

    return " ".join([res["text"] for res in results])
