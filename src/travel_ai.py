from .retriever import crear_retriever
from .llm import generar_respuesta
from .planner import generar_plan
from .user_preferences import extraer_preferencias
from .validator import validar_itinerario


retriever = crear_retriever(k=4)


def travel_ai(consulta):

    # -------------------------
    # 1. Extraer preferencias
    # -------------------------

    print("\n3. Extrayendo preferencias...")

    preferencias = extraer_preferencias(consulta)

    print("\n4. Preferencias extraídas:")

    for clave, valor in preferencias.items():
        print(f"   {clave}: {valor}")

    # -------------------------
    # 2. Generar itinerario
    # -------------------------

    print("\n5. Generando plan...")

    respuesta = generar_plan(
        consulta,
        preferencias,
        retriever,
        generar_respuesta
    )

    # -------------------------
    # 3. Validar itinerario
    # -------------------------

    print("   → Validando itinerario...")

    validacion = validar_itinerario(
        respuesta,
        preferencias
    )

    # -------------------------
    # 4. Mostrar resultado
    # -------------------------

    if validacion["valido"]:

        print("   → ✓ Itinerario válido.")

    else:

        print("   → ⚠ El itinerario no cumple todas las reglas.")

        for error in validacion["errores"]:
            print(f"      - {error}")

    return respuesta