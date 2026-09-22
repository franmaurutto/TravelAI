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


print("PREFERENCIAS EXTRAÍDAS")
print("======================")

for clave, valor in preferencias.items():
    print(f"{clave}: {valor}")