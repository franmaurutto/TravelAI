from src.rules import validar_max_actividades, validar_dias


print("TEST DE REGLAS")
print("=" * 50)


# ---------------------------------------------------------
# TEST 1 — Máximo de actividades
# ---------------------------------------------------------

assert validar_max_actividades(3, 3) is True
assert validar_max_actividades(2, 3) is True
assert validar_max_actividades(4, 3) is False

print("✓ validar_max_actividades funciona correctamente")


# ---------------------------------------------------------
# TEST 2 — Cantidad de días
# ---------------------------------------------------------

assert validar_dias(3, 3) is True
assert validar_dias(2, 3) is False

print("✓ validar_dias funciona correctamente")


print("=" * 50)
print("✓ Todos los tests de reglas pasaron.")