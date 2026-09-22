def construir_prompt(consulta, preferencias, contexto):

    prompt = f"""
Eres TravelAI, un sistema experto de planificación
inteligente de viajes.

Tu objetivo es generar un itinerario personalizado.

PREFERENCIAS EXTRAÍDAS DEL USUARIO:

Destino:
{preferencias.get("destino")}

Cantidad de días:
{preferencias.get("dias")}

Cantidad de personas:
{preferencias.get("personas")}

Presupuesto:
{preferencias.get("presupuesto")}

Intereses:
{preferencias.get("intereses")}

Transporte preferido:
{preferencias.get("transporte")}

Máximo de actividades por día:
{preferencias.get("max_actividades_dia")}


REGLAS:

1. Respetar las restricciones indicadas por el usuario.
2. Respetar el presupuesto.
3. Priorizar los intereses.
4. Respetar el transporte preferido.
5. No superar el máximo de actividades por día.
6. Utilizar solamente información respaldada por el contexto.
7. No inventar lugares, actividades o datos.
8. Si falta información, indicarlo.


CONTEXTO RECUPERADO:

{contexto}


SOLICITUD ORIGINAL:

{consulta}


Genera un itinerario organizado por días.

Cada día debe tener como máximo la cantidad
de actividades indicada por el usuario.

RESPUESTA:
"""

    return prompt


def generar_plan(consulta, preferencias, retriever, generar_respuesta):

    print("   → Buscando información en el RAG...")

    resultados = retriever.invoke(consulta)

    print(
        f"   → RAG recuperó {len(resultados)} documentos."
    )

    contexto = "\n\n".join(
        doc.page_content
        for doc in resultados
    )

    print("   → Construyendo prompt...")

    prompt = construir_prompt(
        consulta,
        preferencias,
        contexto
    )

    print("   → Enviando solicitud a Gemini para generar itinerario...")

    respuesta = generar_respuesta(prompt)

    print("   → Gemini generó el itinerario.")

    return respuesta