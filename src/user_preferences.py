import re


def extraer_preferencias(consulta):

    texto = consulta.lower()

    preferencias = {
        "destino": None,
        "dias": None,
        "personas": None,
        "presupuesto": None,
        "intereses": [],
        "transporte": None,
        "max_actividades_dia": None
    }

    # -------------------------------------------------
    # DESTINO
    # -------------------------------------------------

    destinos = [
        "Buenos Aires",
        "Rosario",
        "Córdoba"
    ]

    for destino in destinos:
        if destino.lower() in texto:
            preferencias["destino"] = destino
            break

    # -------------------------------------------------
    # CANTIDAD DE DÍAS
    # -------------------------------------------------

    match = re.search(
        r"(\d+)\s*d[ií]as?",
        texto
    )

    if match:
        preferencias["dias"] = int(match.group(1))

    # -------------------------------------------------
    # CANTIDAD DE PERSONAS
    # -------------------------------------------------

    match = re.search(
        r"(\d+)\s*personas?",
        texto
    )

    if match:
        preferencias["personas"] = int(match.group(1))

    # -------------------------------------------------
    # PRESUPUESTO
    # -------------------------------------------------

    if "presupuesto bajo" in texto:
        preferencias["presupuesto"] = "bajo"

    elif "presupuesto medio" in texto:
        preferencias["presupuesto"] = "medio"

    elif "presupuesto alto" in texto:
        preferencias["presupuesto"] = "alto"

    # -------------------------------------------------
    # INTERESES
    # -------------------------------------------------

    intereses_disponibles = [
        "gastronomía",
        "cultura",
        "historia",
        "naturaleza"
    ]

    for interes in intereses_disponibles:

        if interes in texto:
            preferencias["intereses"].append(interes)

    # -------------------------------------------------
    # TRANSPORTE
    # -------------------------------------------------

    if "caminar" in texto:
        preferencias["transporte"] = "caminar"

    elif "transporte público" in texto:
        preferencias["transporte"] = "transporte público"

    elif "auto" in texto or "automóvil" in texto:
        preferencias["transporte"] = "auto"

    # -------------------------------------------------
    # MÁXIMO DE ACTIVIDADES
    # -------------------------------------------------

    match = re.search(
        r"m[aá]s de (\d+)\s*actividades?",
        texto
    )

    if match:
        preferencias["max_actividades_dia"] = int(
            match.group(1)
        )

    return preferencias