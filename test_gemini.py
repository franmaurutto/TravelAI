from src.llm import generar_respuesta


print("1. Iniciando prueba de Gemini...")

respuesta = generar_respuesta(
    "Respondé únicamente con la palabra OK."
)

print("2. Gemini respondió:")
print(respuesta)