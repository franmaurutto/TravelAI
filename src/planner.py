def construir_prompt(consulta, contexto):

    prompt = f"""
Eres TravelAI, un sistema experto de planificación
inteligente de viajes.

Tu objetivo es generar itinerarios personalizados
a partir de las preferencias y restricciones
del usuario.

Debes seguir las siguientes reglas:

1. Respetar las restricciones indicadas por el usuario.
2. Respetar el presupuesto indicado.
3. Priorizar los intereses del usuario.
4. Respetar las preferencias de transporte.
5. No superar el número máximo de actividades por día.
6. Utilizar la información proporcionada en el contexto.
7. No inventar información que no esté respaldada
   por el contexto.
8. Si la información necesaria no está disponible,
   indicarlo claramente.

CONTEXTO RECUPERADO:
{contexto}

SOLICITUD DEL USUARIO:
{consulta}

Si el usuario solicita un itinerario:

- organizarlo por días;
- respetar la cantidad máxima de actividades;
- procurar una distribución coherente;
- explicar brevemente las actividades propuestas.

RESPUESTA:
"""

    return prompt

def generar_plan(consulta, retriever, generar_respuesta):

    # -----------------------------------------------
    # 1. Recuperar documentos relevantes
    # -----------------------------------------------

    resultados = retriever.invoke(consulta)


    # -----------------------------------------------
    # 2. Construir contexto
    # -----------------------------------------------

    contexto = "\n\n".join(
        doc.page_content
        for doc in resultados
    )


    # -----------------------------------------------
    # 3. Construir prompt
    # -----------------------------------------------

    prompt = construir_prompt(
        consulta,
        contexto
    )


    # -----------------------------------------------
    # 4. Enviar prompt al LLM
    # -----------------------------------------------

    respuesta = generar_respuesta(prompt)


    return respuesta