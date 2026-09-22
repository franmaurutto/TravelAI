from .retriever import crear_retriever
from .llm import generar_respuesta
from .planner import generar_plan
from .user_preferences import extraer_preferencias


print("1. Creando retriever...")
retriever = crear_retriever(k=4)
print("2. Retriever creado.")


def travel_ai(consulta):

    print("3. Extrayendo preferencias...")

    preferencias = extraer_preferencias(consulta)

    print("4. Preferencias extraídas:")
    print(preferencias)

    print("5. Generando plan...")

    respuesta = generar_plan(
        consulta,
        preferencias,
        retriever,
        generar_respuesta
    )

    print("6. Plan generado.")

    return respuesta

# from .retriever import crear_retriever
# from .llm import generar_respuesta
# from .planner import generar_plan
# from .user_preferences import extraer_preferencias


# # Crear retriever
# retriever = crear_retriever(k=4)


# def travel_ai(consulta):

#     # 1. Extraer preferencias
#     preferencias = extraer_preferencias(consulta)

#     # 2. Generar itinerario
#     respuesta = generar_plan(
#         consulta,
#         preferencias,
#         retriever,
#         generar_respuesta
#     )

#     return respuesta