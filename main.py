from src.travel_ai import travel_ai


def main():

    consulta = """
    Quiero viajar 5 días a Buenos Aires.

    Somos dos personas.
    Tenemos un presupuesto medio.
    Nos interesa la gastronomía y la cultura.
    Preferimos caminar antes que utilizar transporte.
    No queremos hacer más de 3 actividades por día.

    Generá un itinerario personalizado.
    """

    respuesta = travel_ai(consulta)

    print("\n")
    print("=" * 60)
    print("TRAVELAI")
    print("=" * 60)
    print()
    print(respuesta)
    print()


if __name__ == "__main__":
    main()