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
# Adaptador de embeddings para LangChain
# --------------------------------------------------

class GeminiEmbeddings(Embeddings):

    def embed_documents(self, texts):
        resultado = client.models.embed_content(
            model="gemini-embedding-001",
            contents=texts
        )

        return [
            embedding.values
            for embedding in resultado.embeddings
        ]

    def embed_query(self, text):
        resultado = client.models.embed_content(
            model="gemini-embedding-001",
            contents=text
        )

        return resultado.embeddings[0].values


# --------------------------------------------------
# Instancia reutilizable
# --------------------------------------------------

gemini_embeddings = GeminiEmbeddings()