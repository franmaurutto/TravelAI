from src.geoapify_service import buscar_lugares_geoapify, calcular_ruta

print("==================================================")
print("1. Buscando lugares reales en Buenos Aires...")
print("==================================================")

lugares = buscar_lugares_geoapify("Buenos Aires", ["gastronomía", "cultura"], limite=2)

if len(lugares) >= 2:
    lugar1 = lugares[0]
    lugar2 = lugares[1]

    print(f"\n📍 ORIGEN:")
    print(f"   • Lugar:     {lugar1['nombre']}")
    print(f"   • Dirección: {lugar1['direccion']}")

    print(f"\n📍 DESTINO:")
    print(f"   • Lugar:     {lugar2['nombre']}")
    print(f"   • Dirección: {lugar2['direccion']}")

    print("\n--------------------------------------------------")
    print("2. Calculando ruta a pie (walk)...")
    print("--------------------------------------------------")
    ruta_caminando = calcular_ruta(
        lugar1["lat"], lugar1["lon"],
        lugar2["lat"], lugar2["lon"],
        modo="walk"
    )

    if ruta_caminando:
        print(f"   🚶 A pie:")
        print(f"      - Tiempo estimado: {ruta_caminando['tiempo_minutos']} min")
        print(f"      - Distancia:       {ruta_caminando['distancia_km']} km ({ruta_caminando['distancia_metros']} metros)")

    print("\n--------------------------------------------------")
    print("3. Calculando ruta en auto (drive)...")
    print("--------------------------------------------------")
    ruta_auto = calcular_ruta(
        lugar1["lat"], lugar1["lon"],
        lugar2["lat"], lugar2["lon"],
        modo="drive"
    )

    if ruta_auto:
        print(f"   🚗 En auto:")
        print(f"      - Tiempo estimado: {ruta_auto['tiempo_minutos']} min")
        print(f"      - Distancia:       {ruta_auto['distancia_km']} km ({ruta_auto['distancia_metros']} metros)")

    print("\n==================================================")

else:
    print("⚠️ No se encontraron suficientes lugares para calcular una ruta.")