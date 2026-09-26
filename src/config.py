import os
from pathlib import Path
from dotenv import load_dotenv


# --------------------------------------------------
# Rutas del proyecto
# --------------------------------------------------

PROJECT_PATH = Path(__file__).resolve().parent.parent

RAG_PATH = PROJECT_PATH / "rag"

VECTORSTORE_PATH = PROJECT_PATH / "vectorstore"


# --------------------------------------------------
# Variables de entorno
# --------------------------------------------------

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEOAPIFY_API_KEY = os.getenv("GEOAPIFY_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("No se encontró GEMINI_API_KEY. Verificá el archivo .env")

if not GEOAPIFY_API_KEY:
    raise ValueError("No se encontró GEOAPIFY_API_KEY. Verificá el archivo .env")


# --------------------------------------------------
# Configuración del modelo
# --------------------------------------------------

GEMINI_MODEL = "gemini-3.6-flash"