def validar_max_actividades(cantidad_actividades, max_actividades):
    """
    Verifica que la cantidad de actividades no supere
    el máximo establecido por el usuario.
    """
    if max_actividades is None:
        return True

    return cantidad_actividades <= max_actividades


def validar_dias(cantidad_dias, dias_solicitados):
    """
    Verifica que la cantidad de días generados coincida
    con la cantidad de días solicitada por el usuario.
    """
    if dias_solicitados is None:
        return True

    return cantidad_dias == dias_solicitados