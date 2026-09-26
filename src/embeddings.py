import time
from google import genai
from langchain_core.embeddings import Embeddings
from .config import GEMINI_API_KEY

# --------------------------------------------------
# Cliente Gemini
# --------------------------------------------------

client = genai.Client(
    api_key=GEMINI_API_KEY
)

# --------------------------------------------------
# Adaptador de embeddings para LangChain con reintento
# --------------------------------------------------

class GeminiEmbeddings(Embeddings):

    def embed_documents(self, texts):
        for intento in range(3):
            try:
                resultado = client.models.embed_content(
                    model="gemini-embedding-001",
                    contents=texts
                )
                return [
                    embedding.values
                    for embedding in resultado.embeddings
                ]
            except Exception as e:
                if intento == 2:
                    raise e
                time.sleep(1)

    def embed_query(self, text):
        for intento in range(3):
            try:
                resultado = client.models.embed_content(
                    model="gemini-embedding-001",
                    contents=text
                )
                return resultado.embeddings[0].values
            except Exception as e:
                if intento == 2:
                    raise e
                time.sleep(1)


# --------------------------------------------------
# Instancia reutilizable
# --------------------------------------------------

gemini_embeddings = GeminiEmbeddings()