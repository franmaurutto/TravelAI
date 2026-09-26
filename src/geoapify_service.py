import requests
from src.config import GEOAPIFY_API_KEY

# Coordenadas centrales de las ciudades soportadas
COORDENADAS_DESTINOS = {
    "buenos aires": {"lat": -34.6037, "lon": -58.3816},
    "cordoba": {"lat": -31.4201, "lon": -64.1888},
    "córdoba": {"lat": -31.4201, "lon": -64.1888},
    "rosario": {"lat": -32.9468, "lon": -60.6393},
}

# Mapeo corregido con categorías oficiales de Geoapify
MAPEO_CATEGORIAS = {
    "gastronomía": "catering.restaurant,catering.cafe",
    "cultura": "entertainment.culture,entertainment.museum",
    "historia": "heritage,tourism.sights",
    "naturaleza": "leisure.park,natural"
}


def buscar_lugares_geoapify(destino: str, intereses: list = None, limite: int = 6):
    """
    Consulta la API de Geoapify para obtener lugares reales (con coords) según destino e intereses.
    """
    if not destino:
        return []

    destino_clave = destino.lower().strip()
    coords = COORDENADAS_DESTINOS.get(destino_clave)

    if not coords:
        print(f"⚠️ Destino '{destino}' no tiene coordenadas configuradas.")
        return []

    categorias_seleccionadas = []
    if intereses:
        for interes in intereses:
            cat = MAPEO_CATEGORIAS.get(interes.lower())
            if cat:
                categorias_seleccionadas.append(cat)

    if categorias_seleccionadas:
        categorias_str = ",".join(categorias_seleccionadas)
    else:
        categorias_str = "tourism.sights,catering.restaurant"

    url = "https://api.geoapify.com/v2/places"
    params = {
        "categories": categorias_str,
        "filter": f"circle:{coords['lon']},{coords['lat']},8000",
        "limit": limite,
        "apiKey": GEOAPIFY_API_KEY
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        lugares = []
        for feature in data.get("features", []):
            prop = feature.get("properties", {})
            nombre = prop.get("name")
            direccion = prop.get("formatted")
            lat = prop.get("lat")
            lon = prop.get("lon")

            if nombre and lat and lon:
                lugares.append({
                    "nombre": nombre,
                    "direccion": direccion,
                    "lat": lat,
                    "lon": lon
                })

        return lugares

    except Exception as e:
        print(f"⚠️ Error al consultar Geoapify Places: {e}")
        return []


def calcular_ruta(origen_lat: float, origen_lon: float, destino_lat: float, destino_lon: float, modo: str = "walk"):
    """
    Calcula distancia (en km/metros) y tiempo estimado entre 2 puntos usando Routing API.
    Modos soportados: 'walk' (a pie), 'drive' (auto), 'bicycle' (bici).
    """
    url = "https://api.geoapify.com/v1/routing"

    params = {
        "waypoints": f"{origen_lat},{origen_lon}|{destino_lat},{destino_lon}",
        "mode": modo,
        "apiKey": GEOAPIFY_API_KEY
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        feature = data["features"][0]
        prop = feature.get("properties", {})

        distancia_metros = prop.get("distance", 0)
        tiempo_segundos = prop.get("time", 0)

        distancia_km = round(distancia_metros / 1000, 2)
        tiempo_minutos = round(tiempo_segundos / 60)

        return {
            "distancia_km": distancia_km,
            "distancia_metros": distancia_metros,
            "tiempo_minutos": tiempo_minutos,
            "modo": modo
        }

    except Exception as e:
        print(f"⚠️ Error al calcular la ruta en Geoapify: {e}")
        return None