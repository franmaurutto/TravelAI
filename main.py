from src.travel_ai import travel_ai


def main():
    # Consulta de prueba realista
    consulta = (
        "Hola! Quiero viajar a Buenos Aires por 3 días. "
        "Me interesa mucho la gastronomía y la cultura. "
        "Prefiero caminar, con presupuesto medio y no hacer más de 3 actividades por día."
    )

    itinerario_final = travel_ai(consulta)

    print("\n" + "=" * 60)
    print("📋 ITINERARIO GENERADO POR TRAVELAI:")
    print("=" * 60)
    print(itinerario_final)


if __name__ == "__main__":
    main()