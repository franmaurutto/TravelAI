from google import genai

from .config import (
    GEMINI_API_KEY,
    GEMINI_MODEL
)


# --------------------------------------------------
# Cliente Gemini
# --------------------------------------------------

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# --------------------------------------------------
# Función para generar respuestas
# --------------------------------------------------

def generar_respuesta(prompt):

    respuesta = client.interactions.create(
        model=GEMINI_MODEL,
        input=prompt
    )

    return respuesta.output_text