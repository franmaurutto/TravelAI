from src.validator import validar_itinerario


print("TEST DEL VALIDATOR")
print("=" * 50)


preferencias = {
    "dias": 3,
    "max_actividades_dia": 3
}


# ---------------------------------------------------------
# TEST 1 — Itinerario válido
# ---------------------------------------------------------

itinerario_valido = """
Día 1
- Actividad 1
- Actividad 2

Día 2
- Actividad 1
- Actividad 2
- Actividad 3

Día 3
- Actividad 1
"""


resultado = validar_itinerario(
    itinerario_valido,
    preferencias
)


assert resultado["valido"] is True
assert resultado["errores"] == []


print("✓ Detecta correctamente un itinerario válido.")


# ---------------------------------------------------------
# TEST 2 — Demasiadas actividades
# ---------------------------------------------------------

itinerario_invalido = """
Día 1
- Actividad 1
- Actividad 2
- Actividad 3
- Actividad 4

Día 2
- Actividad 1

Día 3
- Actividad 1
"""


resultado = validar_itinerario(
    itinerario_invalido,
    preferencias
)


assert resultado["valido"] is False
assert len(resultado["errores"]) > 0


print("✓ Detecta correctamente un exceso de actividades.")


print("=" * 50)
print("✓ Todos los tests del validator pasaron.")