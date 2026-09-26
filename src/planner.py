from src.geoapify_service import buscar_lugares_geoapify, calcular_ruta


def construir_prompt(consulta, preferencias, contexto_rag, lugares_api, info_rutas):
    # Formatear la lista de lugares reales
    texto_lugares = ""
    if lugares_api:
        texto_lugares = "\n".join(
            f"- {l['nombre']} (Dirección: {l.get('direccion', 'Ubicación céntrica')})"
            for l in lugares_api
        )
    else:
        texto_lugares = "No se obtuvieron lugares específicos de la API."

    # Formatear estimaciones de tiempo/distancia
    texto_rutas = info_rutas if info_rutas else "Distancias caminables en la zona."

    prompt = f"""
Eres TravelAI, un sistema experto de planificación inteligente de viajes y turismo.
Tu objetivo es generar un itinerario de viaje personalizado, detallado, realista y justificado.

PREFERENCIAS Y RESTRICCIONES DEL VIAJERO:
- Destino: {preferencias.get("destino", "No especificado")}
- Cantidad de días: {preferencias.get("dias", 1)}
- Cantidad de personas: {preferencias.get("personas", 1)}
- Presupuesto: {preferencias.get("presupuesto", "medio")}
- Intereses principales: {', '.join(preferencias.get("intereses", []))}
- Transporte preferido: {preferencias.get("transporte", "caminar")}
- Máximo de actividades por día: {preferencias.get("max_actividades_dia", 3)}

REGLAS OBLIGATORIAS:
1. Respetar estrictamente la cantidad de días solicitados ({preferencias.get("dias", 1)} días).
2. Cada día debe contener COMO MÁXIMO {preferencias.get("max_actividades_dia", 3)} actividades principales.
3. Incorporar los LUGARES REALES obtenidos por la API externa y ubicarlos en los días correspondientes según afinidad.
4. Usar la información de TIEMPOS Y DISTANCIAS para aconsejar al usuario sobre los traslados.
5. Emplear el CONTEXTO RAG para contextualizar cultural e históricamente cada barrio y parada.
6. Organizar cada día en tres turnos claros: Mañana, Tarde y Noche (respetando el límite de actividades).
7. Para cada parada indicar: Nombre del lugar, dirección estimada, qué hacer y por qué se recomienda.

CONOCIMIENTO EXPERTO DE LA CIUDAD (RAG):
{contexto_rag}

LUGARES REALES VERIFICADOS (API GEOAPIFY PLACES):
{texto_lugares}

DATOS DE TRASLADO Y RUTAS (API GEOAPIFY ROUTING):
{texto_rutas}

SOLICITUD ORIGINAL DEL USUARIO:
"{consulta}"

Genera una respuesta cordial y estructurada con el itinerario completo:
"""
    return prompt


def generar_plan(consulta, preferencias, retriever, generar_respuesta):
    print("\n   [1/4] 📚 Consultando base de conocimiento RAG...")
    resultados = retriever.invoke(consulta)
    contexto_rag = "\n\n".join(doc.page_content for doc in resultados)

    print("   [2/4] 📍 Obteniendo lugares reales vía Geoapify Places...")
    lugares_api = buscar_lugares_geoapify(
        destino=preferencias.get("destino"),
        intereses=preferencias.get("intereses", []),
        limite=6
    )

    print("   [3/4] 🗺️ Calculando estimaciones de rutas con Geoapify Routing...")
    info_rutas = ""
    if len(lugares_api) >= 2:
        modo_transporte = "drive" if preferencias.get("transporte") == "auto" else "walk"
        ruta = calcular_ruta(
            lugares_api[0]["lat"], lugares_api[0]["lon"],
            lugares_api[1]["lat"], lugares_api[1]["lon"],
            modo=modo_transporte
        )
        if ruta:
            info_rutas = (
                f"Traslado estimado entre '{lugares_api[0]['nombre']}' y '{lugares_api[1]['nombre']}': "
                f"{ruta['tiempo_minutos']} min ({ruta['distancia_km']} km) en modo {ruta['modo']}."
            )

    print("   [4/4] 🤖 Generando itinerario experto con Gemini...")
    prompt = construir_prompt(consulta, preferencias, contexto_rag, lugares_api, info_rutas)
    respuesta = generar_respuesta(prompt)

    return respuesta