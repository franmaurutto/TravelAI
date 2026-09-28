import re

from .rules import validar_max_actividades, validar_dias


def contar_dias(itinerario):
    """
    Cuenta los días diferentes del itinerario.

    Busca formatos como:
    Día 1
    Día 2
    Día 3

    Se utiliza el número del día para evitar contar
    nuevamente las menciones que aparecen en consejos
    o explicaciones posteriores.
    """

    patron = r"\bDía\s+(\d+)\b"

    coincidencias = re.findall(
        patron,
        itinerario,
        flags=re.IGNORECASE
    )

    dias = {int(numero) for numero in coincidencias}

    return len(dias)


def contar_actividades_por_dia(itinerario):
    """
    Cuenta aproximadamente las actividades de cada día.

    Se consideran como actividades las líneas que comienzan
    con un guion o una viñeta.
    """

    lineas = itinerario.splitlines()

    actividades_por_dia = {}
    dia_actual = None

    for linea in lineas:
        linea = linea.strip()

        # Detectar encabezado del día
        match = re.match(
            r"^Día\s+(\d+)",
            linea,
            flags=re.IGNORECASE
        )

        if match:
            dia_actual = int(match.group(1))
            actividades_por_dia[dia_actual] = 0
            continue

        # Contar actividades
        if dia_actual is not None:
            if linea.startswith("-") or linea.startswith("•"):
                actividades_por_dia[dia_actual] += 1

    return actividades_por_dia


def validar_itinerario(itinerario, preferencias):
    """
    Valida que el itinerario generado respete
    las restricciones principales del usuario.
    """

    errores = []

    # -------------------------
    # Validación de días
    # -------------------------

    dias_generados = contar_dias(itinerario)
    dias_solicitados = preferencias.get("dias")

    if not validar_dias(dias_generados, dias_solicitados):
        errores.append(
            f"Se solicitaron {dias_solicitados} días, "
            f"pero se generaron {dias_generados}."
        )

    # -------------------------
    # Validación de actividades
    # -------------------------

    actividades_por_dia = contar_actividades_por_dia(itinerario)

    max_actividades = preferencias.get(
        "max_actividades_dia"
    )

    if max_actividades is not None:

        for dia, cantidad in actividades_por_dia.items():

            if not validar_max_actividades(
                cantidad,
                max_actividades
            ):
                errores.append(
                    f"El día {dia} tiene {cantidad} actividades "
                    f"y el máximo permitido es "
                    f"{max_actividades}."
                )

    # -------------------------
    # Resultado
    # -------------------------

    if errores:
        return {
            "valido": False,
            "errores": errores
        }

    return {
        "valido": True,
        "errores": []
    }