from src.user_preferences import extraer_preferencias


consulta = """
Quiero viajar 5 días a Buenos Aires.

Somos dos personas.
Tenemos un presupuesto medio.
Nos interesa la gastronomía y la cultura.
Preferimos caminar antes que utilizar transporte.
No queremos hacer más de 3 actividades por día.
"""


preferencias = extraer_preferencias(consulta)


print("TEST DE PREFERENCIAS")
print("=" * 50)

print(preferencias)


assert preferencias["destino"] == "Buenos Aires"
assert preferencias["dias"] == 5
assert preferencias["personas"] == 2
assert preferencias["presupuesto"] == "medio"
assert "gastronomía" in preferencias["intereses"]
assert "cultura" in preferencias["intereses"]
assert preferencias["transporte"] == "caminar"
assert preferencias["max_actividades_dia"] == 3


print("=" * 50)
print("✓ Todas las preferencias fueron extraídas correctamente.")