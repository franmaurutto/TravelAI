from src.llm import generar_respuesta


print("1. Probando Gemini...")

respuesta = generar_respuesta(
    "Respondé únicamente: OK"
)

print("2. Gemini respondió:")
print(respuesta)