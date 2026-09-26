from langchain_chroma import Chroma

from .config import VECTORSTORE_PATH
from .embeddings import gemini_embeddings


def cargar_vectorstore():

    vectorstore = Chroma(
        persist_directory=str(VECTORSTORE_PATH),
        embedding_function=gemini_embeddings
    )

    return vectorstore