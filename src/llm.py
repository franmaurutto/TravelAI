from google import genai

from .config import (
    GEMINI_API_KEY,
    GEMINI_MODEL
)


client = genai.Client(
    api_key=GEMINI_API_KEY,
    http_options={
        "timeout": 60001
    }
)


def generar_respuesta(prompt):

    try:

        print("      → Llamando a Gemini...")

        respuesta = client.interactions.create(
            model=GEMINI_MODEL,
            input=prompt
        )

        print("      → Respuesta recibida de Gemini.")

        return respuesta.output_text

    except Exception as e:

        print("\n      ❌ Error al comunicarse con Gemini:")
        print(f"      {e}")

        raise RuntimeError(
            "No se pudo obtener una respuesta de Gemini. "
            "Revisá la cuota, la API key y el estado del servicio."
        ) from e