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

    # =========================================================
    # DESTINO
    # =========================================================

    destinos = {
        "buenos aires": "Buenos Aires",
        "rosario": "Rosario",
        "córdoba": "Córdoba",
        "cordoba": "Córdoba"
    }

    for nombre, destino in destinos.items():
        if nombre in texto:
            preferencias["destino"] = destino
            break

    # =========================================================
    # CANTIDAD DE DÍAS
    # =========================================================

    match = re.search(
        r"(\d+)\s*d[ií]as?",
        texto
    )

    if match:
        preferencias["dias"] = int(match.group(1))

    # =========================================================
    # CANTIDAD DE PERSONAS
    # =========================================================

    # Primero buscamos números escritos con dígitos:
    # "2 personas"
    # "somos 2 personas"
    # "viajamos 2 personas"

    match = re.search(
        r"\b(\d+)\s*personas?\b",
        texto
    )

    if match:
        preferencias["personas"] = int(match.group(1))

    else:
        # También aceptamos números escritos con palabras:
        # "dos personas"
        # "somos dos personas"
        # "viajamos tres personas"

        numeros_personas = {
            "una": 1,
            "uno": 1,
            "dos": 2,
            "tres": 3,
            "cuatro": 4,
            "cinco": 5,
            "seis": 6,
            "siete": 7,
            "ocho": 8,
            "nueve": 9,
            "diez": 10
        }

        for palabra, numero in numeros_personas.items():

            patron = rf"\b{palabra}\s+personas?\b"

            if re.search(patron, texto):
                preferencias["personas"] = numero
                break

    # =========================================================
    # PRESUPUESTO
    # =========================================================

    if re.search(r"\bpresupuesto\s+bajo\b", texto):
        preferencias["presupuesto"] = "bajo"

    elif re.search(r"\bpresupuesto\s+medio\b", texto):
        preferencias["presupuesto"] = "medio"

    elif re.search(r"\bpresupuesto\s+alto\b", texto):
        preferencias["presupuesto"] = "alto"

    # También aceptar:
    # "presupuesto moderado"

    elif re.search(r"\bpresupuesto\s+moderado\b", texto):
        preferencias["presupuesto"] = "medio"

    # =========================================================
    # INTERESES
    # =========================================================

    intereses_disponibles = {
        "gastronomía": [
            "gastronomía",
            "gastronomia",
            "comida",
            "comer",
            "restaurantes"
        ],

        "cultura": [
            "cultura",
            "cultural"
        ],

        "historia": [
            "historia",
            "histórico",
            "historico"
        ],

        "naturaleza": [
            "naturaleza",
            "naturaleza",
            "parques",
            "aire libre"
        ]
    }

    for interes, palabras in intereses_disponibles.items():

        for palabra in palabras:

            if palabra in texto:
                preferencias["intereses"].append(interes)
                break

    # =========================================================
    # TRANSPORTE
    # =========================================================

    if re.search(
        r"\b(caminar|caminando|a pie|pie)\b",
        texto
    ):
        preferencias["transporte"] = "caminar"

    elif "transporte público" in texto:
        preferencias["transporte"] = "transporte público"

    elif re.search(
        r"\b(auto|automóvil|coche)\b",
        texto
    ):
        preferencias["transporte"] = "auto"

    # =========================================================
    # MÁXIMO DE ACTIVIDADES POR DÍA
    # =========================================================

    # Ejemplos:
    # "más de 3 actividades"
    # "máximo 3 actividades"
    # "max 3 actividades"
    # "no queremos más de 3 actividades"

    match = re.search(
    r"(?:m[aá]ximo|max|m[aá]s de|hasta)"
    r"(?:\s+\w+){0,4}\s+(\d+)\s*actividades?",
    texto
)

    if match:
        preferencias["max_actividades_dia"] = int(
            match.group(1)
        )

    return preferencias