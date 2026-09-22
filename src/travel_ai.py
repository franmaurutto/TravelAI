from .retriever import crear_retriever
from .llm import generar_respuesta
from .planner import generar_plan


# --------------------------------------------------
# Crear retriever
# --------------------------------------------------

retriever = crear_retriever(k=4)


# --------------------------------------------------
# Función principal de TravelAI
# --------------------------------------------------

def travel_ai(consulta):

    respuesta = generar_plan(
        consulta,
        retriever,
        generar_respuesta
    )

    return respuesta