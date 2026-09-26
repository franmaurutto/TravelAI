from .retriever import crear_retriever
from .llm import generar_respuesta
from .planner import generar_plan
from .user_preferences import extraer_preferencias

print("1. Inicializando base vectorial y Retriever...")
retriever = crear_retriever(k=4)
print("2. Retriever listo.")


def travel_ai(consulta: str):
    """
    Función principal de TravelAI:
    1. Extrae las preferencias del usuario (NLP / Reglas).
    2. Consulta la base de conocimiento (RAG).
    3. Consulta la API externa (Geoapify Lugares y Rutas).
    4. Genera el itinerario personalizado usando Gemini.
    """
    print("\n" + "=" * 50)
    print("🚀 INICIANDO PLANIFICACIÓN CON TRAVELAI")
    print("=" * 50)
    print(f"Consulta: \"{consulta}\"\n")

    print("3. Extrayendo preferencias y restricciones...")
    preferencias = extraer_preferencias(consulta)
    print("4. Preferencias extraídas:")
    for k, v in preferencias.items():
        print(f"   • {k}: {v}")

    print("\n5. Generando plan (RAG + Geoapify + Gemini)...")
    respuesta = generar_plan(
        consulta=consulta,
        preferencias=preferencias,
        retriever=retriever,
        generar_respuesta=generar_respuesta
    )

    print("\n6. ✅ Plan generado exitosamente.")
    return respuesta