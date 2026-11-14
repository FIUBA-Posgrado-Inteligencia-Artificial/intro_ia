# /// script
# requires-python = ">=3.12"
# dependencies = ["shapely>=2.0"]
# ///
"""
Genera los datos de la gira a partir de las fuentes originales:

- ciudades.csv: capitales de provincia y ciudades de más de 30.000 habitantes de
  GeoNames, fusionando aglomerados, más la Base Marambio.
- provincias.geojson: límites provinciales del IGN, simplificados.

No hace falta correrlo para usar las notebooks: los archivos generados ya están en
esta carpeta. Para regenerarlos:

    uv run clase3/gira/datos/generar_datos.py
"""

import csv
import io
import json
import math
import tempfile
import urllib.request
import zipfile
from pathlib import Path

from shapely.geometry import mapping, shape

OUTPUT_DIR = Path(__file__).parent

GEONAMES_URL = "https://download.geonames.org/export/dump/AR.zip"
IGN_URL = (
    "https://wms.ign.gob.ar/geoserver/ign/ows?service=WFS&version=1.0.0"
    "&request=GetFeature&typeName=ign:provincia&outputFormat=application/json"
)

# Parámetros de selección de ciudades
MIN_POPULATION = 30_000
MERGE_DISTANCE_KM = 40

# Tolerancia de simplificación de los límites provinciales (en grados, ~1 km)
SIMPLIFY_TOLERANCE = 0.01

# Códigos de provincia de GeoNames (admin1)
PROVINCES = {
    "01": "Buenos Aires",
    "02": "Catamarca",
    "03": "Chaco",
    "04": "Chubut",
    "05": "Córdoba",
    "06": "Corrientes",
    "07": "Ciudad Autónoma de Buenos Aires",
    "08": "Entre Ríos",
    "09": "Formosa",
    "10": "Jujuy",
    "11": "La Pampa",
    "12": "La Rioja",
    "13": "Mendoza",
    "14": "Misiones",
    "15": "Neuquén",
    "16": "Río Negro",
    "17": "Salta",
    "18": "San Juan",
    "19": "San Luis",
    "20": "Santa Cruz",
    "21": "Santa Fe",
    "22": "Santiago del Estero",
    "23": "Tierra del Fuego, Antártida e Islas del Atlántico Sur",
    "24": "Tucumán",
}

# La Base Marambio no está en el archivo de Argentina de GeoNames (figura en el de
# la Antártida), así que la agregamos a mano.
# Coordenadas: 64° 14' 29" S, 56° 37' 36" O
MARAMBIO = {
    "nombre": "Base Marambio",
    "provincia": PROVINCES["23"],
    "latitud": -64.2414,
    "longitud": -56.6267,
    "poblacion": 0,
    "capital": False,
}


def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Distancia en km entre dos puntos de la Tierra, en línea recta."""
    lat1, lon1, lat2, lon2 = map(math.radians, (lat1, lon1, lat2, lon2))
    h = (
        math.sin((lat2 - lat1) / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2
    )
    return 2 * 6371 * math.asin(math.sqrt(h))


def download(url: str, destination: Path) -> Path:
    """Descarga un archivo y retorna su ruta."""
    print(f"Descargando {url}")
    with urllib.request.urlopen(url) as response:
        destination.write_bytes(response.read())
    return destination


def read_geonames(zip_path: Path) -> list:
    """Lee los lugares poblados (clase P) del archivo de GeoNames."""
    places = []
    with zipfile.ZipFile(zip_path) as zf, zf.open("AR.txt") as f:
        reader = csv.reader(
            io.TextIOWrapper(f, encoding="utf-8"),
            delimiter="\t",
            quoting=csv.QUOTE_NONE,
        )
        for row in reader:
            if row[6] != "P":
                continue
            places.append(
                {
                    "nombre": row[1],
                    "provincia": PROVINCES.get(row[10], ""),
                    "latitud": float(row[4]),
                    "longitud": float(row[5]),
                    "poblacion": int(row[14] or 0),
                    # PPLA: capital de provincia, PPLC: capital del país
                    "capital": row[7] in ("PPLA", "PPLC"),
                }
            )
    return places


def select_cities(places: list) -> list:
    """
    Selecciona las capitales y las ciudades de más de MIN_POPULATION habitantes.
    Para no tener aglomerados (por ejemplo el conurbano) con decenas de puntos
    pegados, se recorren las ciudades de mayor a menor población y se descartan las
    que están a menos de MERGE_DISTANCE_KM de una ya elegida.
    """
    chosen = [p for p in places if p["capital"]]
    for place in sorted(places, key=lambda p: -p["poblacion"]):
        if place["capital"] or place["poblacion"] < MIN_POPULATION:
            continue
        if all(
            haversine(place["latitud"], place["longitud"], c["latitud"], c["longitud"])
            > MERGE_DISTANCE_KM
            for c in chosen
        ):
            chosen.append(place)
    return chosen


def disambiguate_names(cities: list) -> None:
    """Agrega la provincia a los nombres que se repiten (por ejemplo San Vicente)."""
    names = [c["nombre"] for c in cities]
    for city in cities:
        if names.count(city["nombre"]) > 1:
            city["nombre"] = f"{city['nombre']} ({city['provincia']})"


def write_cities(cities: list, path: Path) -> None:
    fields = ["nombre", "provincia", "latitud", "longitud", "poblacion", "capital"]
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(cities)


def simplify_provinces(source: Path, destination: Path) -> None:
    """Simplifica los límites provinciales y redondea las coordenadas."""
    data = json.loads(source.read_text(encoding="utf-8"))
    features = []
    for feature in data["features"]:
        geometry = shape(feature["geometry"]).simplify(
            SIMPLIFY_TOLERANCE, preserve_topology=True
        )
        # 4 decimales son ~10 m, más que suficiente para un mapa del país
        geometry = json.loads(
            json.dumps(mapping(geometry)), parse_float=lambda x: round(float(x), 4)
        )
        features.append(
            {
                "type": "Feature",
                "properties": {"nombre": feature["properties"]["nam"]},
                "geometry": geometry,
            }
        )
    destination.write_text(
        json.dumps(
            {"type": "FeatureCollection", "features": features},
            ensure_ascii=False,
            separators=(",", ":"),
        ),
        encoding="utf-8",
    )


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)

        places = read_geonames(download(GEONAMES_URL, tmp_dir / "AR.zip"))
        cities = select_cities(places) + [MARAMBIO]
        disambiguate_names(cities)
        write_cities(cities, OUTPUT_DIR / "ciudades.csv")
        capitals = sum(c["capital"] for c in cities)
        print(f"ciudades.csv: {len(cities)} lugares ({capitals} capitales)")

        provinces = download(IGN_URL, tmp_dir / "provincias_ign.json")
        simplify_provinces(provinces, OUTPUT_DIR / "provincias.geojson")
        size = (OUTPUT_DIR / "provincias.geojson").stat().st_size / 1024
        print(f"provincias.geojson: {size:.0f} KB")


if __name__ == "__main__":
    main()
