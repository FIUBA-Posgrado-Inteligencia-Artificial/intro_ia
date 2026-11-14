import json
import math
import random
from datetime import date, timedelta
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from matplotlib.collections import PolyCollection
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.font_manager import FontProperties
from plotly.subplots import make_subplots

DATA_DIR = Path(__file__).parent / "datos"

# La gira siempre arranca en Buenos Aires y termina en la Base Marambio
START_CITY = "Buenos Aires"
END_CITY = "Base Marambio"

EARTH_RADIUS_KM = 6371

INSTANCES = ("capitales", "pueblo_por_pueblo")


def load_cities(instance: str = "capitales") -> pd.DataFrame:
    """
    Carga las ciudades de una de las giras.

    Args:
        instance (str, opcional): "capitales" para la Gira Federal (24 capitales más la
                                  Base Marambio) o "pueblo_por_pueblo" para la gira
                                  completa (111 lugares). Por defecto es "capitales".

    Returns:
        pd.DataFrame: Una fila por ciudad, con las columnas nombre, provincia, latitud,
                      longitud, poblacion y capital. El índice va de 0 a n-1 y es el
                      número con el que identificamos a cada ciudad en una gira.
    """
    if instance not in INSTANCES:
        raise ValueError(f"La gira debe ser una de {INSTANCES}")

    cities = pd.read_csv(DATA_DIR / "ciudades.csv")
    if instance == "capitales":
        cities = cities[cities["capital"] | (cities["nombre"] == END_CITY)]
    return cities.reset_index(drop=True)


def distance_matrix(cities: pd.DataFrame) -> np.ndarray:
    """
    Calcula la distancia en línea recta, en km, entre todos los pares de ciudades,
    usando la fórmula de haversine.

    Args:
        cities (pd.DataFrame): Ciudades de la gira.

    Returns:
        np.ndarray: Matriz de n x n donde el elemento [i, j] es la distancia entre la
                    ciudad i y la ciudad j.
    """
    lat = np.radians(cities["latitud"].to_numpy())
    lon = np.radians(cities["longitud"].to_numpy())

    # Diferencias entre todos los pares, aprovechando el broadcasting de numpy
    delta_lat = lat[:, None] - lat[None, :]
    delta_lon = lon[:, None] - lon[None, :]

    h = (
        np.sin(delta_lat / 2) ** 2
        + np.cos(lat[:, None]) * np.cos(lat[None, :]) * np.sin(delta_lon / 2) ** 2
    )
    return 2 * EARTH_RADIUS_KM * np.arcsin(np.sqrt(h))


def obtain_endpoints(cities: pd.DataFrame) -> tuple:
    """
    Retorna los índices de la ciudad donde arranca la gira y de donde termina.

    Args:
        cities (pd.DataFrame): Ciudades de la gira.

    Returns:
        tuple: (índice de Buenos Aires, índice de la Base Marambio)
    """
    names = list(cities["nombre"])
    return names.index(START_CITY), names.index(END_CITY)


def init_state(cities: pd.DataFrame) -> list:
    """
    Genera una gira al azar. Una gira es una lista con los índices de las ciudades en
    el orden en que se visitan: arranca en Buenos Aires, termina en la Base Marambio y
    en el medio pasa una única vez por cada una de las demás ciudades.

    Args:
        cities (pd.DataFrame): Ciudades de la gira.

    Returns:
        list: La gira, por ejemplo [3, 17, 5, ..., 24].
    """
    start, end = obtain_endpoints(cities)
    middle = [k for k in range(len(cities)) if k not in (start, end)]
    random.shuffle(middle)
    return [start, *middle, end]


def cost_function(tour: list, distances: np.ndarray) -> float:
    """
    Calcula la función de costo de una gira: los km totales recorridos.

    Args:
        tour (list): La gira.
        distances (np.ndarray): Matriz de distancias entre ciudades.

    Returns:
        float: Kilómetros totales de la gira.
    """
    return float(sum(distances[a, b] for a, b in zip(tour[:-1], tour[1:])))


def obtain_moves(n: int) -> list:
    """
    Retorna todos los movimientos 2-opt posibles para una gira de n ciudades. Un
    movimiento (i, j) invierte el tramo de la gira que va de la posición i a la j.
    Nunca se mueven la primera ni la última posición, para que la gira siga
    arrancando en Buenos Aires y terminando en la Base Marambio.

    Args:
        n (int): Cantidad de ciudades de la gira.

    Returns:
        list: Lista de tuplas (i, j) con 1 <= i < j <= n - 2.
    """
    return [(i, j) for i in range(1, n - 2) for j in range(i + 1, n - 1)]


def two_opt(tour: list, i: int, j: int) -> list:
    """
    Aplica un movimiento 2-opt: invierte el tramo de la gira entre las posiciones i y
    j (inclusive).

    Args:
        tour (list): La gira.
        i (int): Posición donde empieza el tramo.
        j (int): Posición donde termina el tramo.

    Returns:
        list: Nueva gira. La gira original no se modifica.
    """
    return tour[:i] + tour[i : j + 1][::-1] + tour[j + 1 :]


def delta_cost(tour: list, i: int, j: int, distances: np.ndarray) -> float:
    """
    Calcula cuánto cambia el costo al aplicar el movimiento 2-opt (i, j), sin armar
    la nueva gira. Al invertir un tramo, solo cambian los dos tramos de avioneta de
    sus bordes: el resto de la gira se recorre igual, aunque al revés.

    Args:
        tour (list): La gira.
        i (int): Posición donde empieza el tramo.
        j (int): Posición donde termina el tramo.
        distances (np.ndarray): Matriz de distancias entre ciudades.

    Returns:
        float: Diferencia de km entre la nueva gira y la actual. Si es negativa, el
               movimiento acorta la gira.
    """
    # Antes: ... a -> b ... c -> d ...   Después: ... a -> c ... b -> d ...
    a, b = tour[i - 1], tour[i]
    c, d = tour[j], tour[j + 1]
    return float(distances[a, c] + distances[b, d] - distances[a, b] - distances[c, d])


def return_neib_states(tour: list) -> list:
    """
    Retorna todas las giras vecinas de la gira actual, es decir, las que se obtienen
    con un movimiento 2-opt.

    Args:
        tour (list): La gira.

    Returns:
        list: Lista de giras vecinas.
    """
    return [two_opt(tour, i, j) for i, j in obtain_moves(len(tour))]


def random_move(n: int) -> tuple:
    """
    Retorna un movimiento 2-opt al azar para una gira de n ciudades.

    Args:
        n (int): Cantidad de ciudades de la gira.

    Returns:
        tuple: (i, j) con 1 <= i < j <= n - 2.
    """
    i, j = sorted(random.sample(range(1, n - 1), 2))
    return i, j


def random_neib_state(tour: list) -> list:
    """
    Retorna una única gira vecina elegida al azar, sin generar a todas las vecinas.

    Args:
        tour (list): La gira.

    Returns:
        list: Una gira vecina.
    """
    return two_opt(tour, *random_move(len(tour)))


def format_km(km: float) -> str:
    """Formatea una distancia al estilo argentino, por ejemplo 14.155 km."""
    return f"{km:,.0f} km".replace(",", ".")


# ---------------------------------------------------------------------------------
# Visualización
#
# Cada mapa tiene dos versiones:
# - Estática (por defecto), dibujada con matplotlib. Es liviana y se ve en GitHub.
# - Interactiva (interactive=True), con plotly: permite hacer zoom y ver el nombre y
#   la fecha de cada ciudad al pasar el mouse. Es pesada, porque guarda el mapa
#   completo dentro de la notebook.
# ---------------------------------------------------------------------------------

# Capitales muy cercanas entre sí: ubicamos sus nombres para que no se superpongan.
# Los valores son (posición en plotly, alineación horizontal y vertical en matplotlib)
TEXT_POSITIONS = {
    "Resistencia": ("middle left", "right", "center"),
    "Corrientes": ("middle right", "left", "center"),
    "Santa Fe": ("middle left", "right", "center"),
    "Paraná": ("middle right", "left", "center"),
    "Buenos Aires": ("top right", "left", "bottom"),
    "La Plata": ("bottom right", "left", "top"),
    "Salta": ("bottom right", "left", "top"),
    "San Salvador de Jujuy": ("top right", "left", "bottom"),
}
DEFAULT_TEXT_POSITION = ("middle right", "left", "center")

# Con más ciudades que esto, los nombres se superponen y no se escriben
MAX_CITIES_WITH_NAMES = 30

TOUR_COLORS = ("#c0392b", "#2980b9", "#27ae60", "#8e44ad")
LAND_COLOR = "#f4f1ea"
BORDER_COLOR = "#9a9a9a"
OCEAN_COLOR = "#dbe9f4"
SOURCE_NOTE = "FUENTE: Instituto Geográfico Nacional de la República Argentina"

# Encuadre del mapa: del norte argentino hasta la Base Marambio. Usamos una proyección
# transversa de Mercator centrada en el meridiano 64° O, que deforma poco al país.
CENTRAL_MERIDIAN = -64
LATITUDE_RANGE = (-66, -21.5)
LONGITUDE_RANGE = (-75, -52)

# Tamaño de cada mapa: en pulgadas para matplotlib y en píxeles para plotly
STATIC_MAP_SIZE = (5, 9)
INTERACTIVE_MAP_SIZE = (560, 1000)


def _load_provinces() -> dict:
    """Límites provinciales oficiales del IGN, en formato GeoJSON."""
    return json.loads((DATA_DIR / "provincias.geojson").read_text(encoding="utf-8"))


def _tour_markers(cities: pd.DataFrame, tour: list) -> list:
    """
    Separa las ciudades de una gira según cómo se dibujan: ciudades comunes,
    capitales, la ciudad donde arranca (■) y donde termina (▼).

    Returns:
        list: Lista de tuplas (ciudades, símbolo en plotly, símbolo en matplotlib,
              tamaño, si siempre se escribe el nombre). Cada grupo de ciudades
              incluye la columna fecha: la posición de la ciudad en la gira.
    """
    route = cities.loc[tour].assign(fecha=range(1, len(tour) + 1))
    is_start = route["fecha"] == 1
    is_end = route["fecha"] == len(tour)
    is_middle = ~is_start & ~is_end
    return [
        (route[is_middle & ~route["capital"]], "circle", "o", 6, False),
        (route[is_middle & route["capital"]], "star", "*", 10, False),
        (route[is_start], "square", "s", 11, True),
        (route[is_end], "triangle-down", "v", 14, True),
    ]


# --- Versión estática (matplotlib) -------------------------------------------------


def _project(lon: np.ndarray, lat: np.ndarray) -> tuple:
    """Proyección transversa de Mercator (esférica) centrada en CENTRAL_MERIDIAN."""
    lon = np.radians(np.asarray(lon, dtype=float) - CENTRAL_MERIDIAN)
    lat = np.radians(np.asarray(lat, dtype=float))
    b = np.clip(np.cos(lat) * np.sin(lon), -0.999999, 0.999999)
    x = 0.5 * np.log((1 + b) / (1 - b))
    y = np.arctan2(np.tan(lat), np.cos(lon))
    return x, y


def _draw_provinces(ax: plt.Axes) -> None:
    """Dibuja las provincias y fija el encuadre del mapa."""
    polygons = []
    for feature in _load_provinces()["features"]:
        geometry = feature["geometry"]
        parts = (
            [geometry["coordinates"]]
            if geometry["type"] == "Polygon"
            else geometry["coordinates"]
        )
        for polygon in parts:
            # Solo el contorno exterior: no hay lagos ni huecos que valga la pena ver
            lon, lat = np.array(polygon[0]).T
            polygons.append(np.column_stack(_project(lon, lat)))

    ax.add_collection(
        PolyCollection(
            polygons, facecolor=LAND_COLOR, edgecolor=BORDER_COLOR, linewidth=0.4
        )
    )
    # En esta proyección los paralelos se curvan, así que el encuadre se calcula
    # proyectando todo el borde del rectángulo de latitudes y longitudes
    lon_grid, lat_grid = np.meshgrid(
        np.linspace(*LONGITUDE_RANGE, 50), np.linspace(*LATITUDE_RANGE, 50)
    )
    frame_x, frame_y = _project(lon_grid, lat_grid)
    ax.set_xlim(frame_x.min(), frame_x.max())
    ax.set_ylim(frame_y.min(), frame_y.max())
    ax.set_facecolor(OCEAN_COLOR)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])


def _draw_tour(ax: plt.Axes, cities: pd.DataFrame, tour: list, color: str) -> None:
    """Dibuja la ruta de la gira y sus ciudades."""
    route = cities.loc[tour]
    x, y = _project(route["longitud"], route["latitud"])
    ax.plot(x, y, color=color, linewidth=1.2, zorder=2)

    show_names = len(tour) <= MAX_CITIES_WITH_NAMES
    for group, _, symbol, size, always_named in _tour_markers(cities, tour):
        x, y = _project(group["longitud"], group["latitud"])
        ax.scatter(x, y, marker=symbol, s=size**2 / 2, color=color, zorder=3)
        if not (show_names or always_named):
            continue
        for name, xi, yi in zip(group["nombre"], x, y):
            _, ha, va = TEXT_POSITIONS.get(name, DEFAULT_TEXT_POSITION)
            offset = 0.006 if ha == "left" else -0.006
            ax.text(xi + offset, yi, name, fontsize=6, ha=ha, va=va, zorder=4)


def _plot_static(cities: pd.DataFrame, tours: dict, distances: np.ndarray) -> None:
    width, height = STATIC_MAP_SIZE
    fig, axes = plt.subplots(
        1, len(tours), figsize=(width * len(tours), height), squeeze=False
    )
    for ax, (title, tour), color in zip(axes[0], tours.items(), TOUR_COLORS):
        _draw_provinces(ax)
        _draw_tour(ax, cities, tour, color)
        km = format_km(cost_function(tour, distances))
        ax.set_title(f"{title}: {km}" if title else km)
    fig.text(0.5, 0.01, SOURCE_NOTE, ha="center", fontsize=7)
    fig.tight_layout(rect=(0, 0.02, 1, 1))
    plt.show()


# --- Versión interactiva (plotly) --------------------------------------------------


def _provinces_trace() -> go.Choropleth:
    geojson = _load_provinces()
    names = [feature["properties"]["nombre"] for feature in geojson["features"]]
    return go.Choropleth(
        geojson=geojson,
        locations=names,
        featureidkey="properties.nombre",
        z=[0] * len(names),
        colorscale=[[0, LAND_COLOR], [1, LAND_COLOR]],
        showscale=False,
        marker_line_color=BORDER_COLOR,
        marker_line_width=0.6,
        hoverinfo="skip",
    )


def _tour_traces(cities: pd.DataFrame, tour: list, color: str) -> list:
    route = cities.loc[tour]
    traces = [
        go.Scattergeo(
            lat=route["latitud"],
            lon=route["longitud"],
            mode="lines",
            line={"width": 2, "color": color},
            hoverinfo="skip",
            showlegend=False,
        )
    ]

    show_names = len(tour) <= MAX_CITIES_WITH_NAMES
    for group, symbol, _, size, always_named in _tour_markers(cities, tour):
        if group.empty:
            continue
        names = show_names or always_named
        traces.append(
            go.Scattergeo(
                lat=group["latitud"],
                lon=group["longitud"],
                mode="markers+text" if names else "markers",
                text=group["nombre"] if names else None,
                textposition=[
                    TEXT_POSITIONS.get(name, DEFAULT_TEXT_POSITION)[0]
                    for name in group["nombre"]
                ],
                textfont={"size": 9},
                marker={"size": size, "color": color, "symbol": symbol},
                hovertext=[
                    f"Fecha {row.fecha}: {row.nombre} ({row.provincia})"
                    for row in group.itertuples()
                ],
                hoverinfo="text",
                showlegend=False,
            )
        )
    return traces


def _plot_interactive(cities: pd.DataFrame, tours: dict, distances: np.ndarray) -> None:
    titles = []
    for title, tour in tours.items():
        km = format_km(cost_function(tour, distances))
        titles.append(f"{title}: {km}" if title else km)

    fig = make_subplots(
        rows=1,
        cols=len(tours),
        specs=[[{"type": "geo"}] * len(tours)],
        subplot_titles=titles,
    )
    for col, (tour, color) in enumerate(zip(tours.values(), TOUR_COLORS), start=1):
        fig.add_trace(_provinces_trace(), row=1, col=col)
        for trace in _tour_traces(cities, tour, color):
            fig.add_trace(trace, row=1, col=col)

    fig.update_geos(
        projection_type="transverse mercator",
        projection_rotation={"lon": CENTRAL_MERIDIAN},
        center={"lat": sum(LATITUDE_RANGE) / 2, "lon": CENTRAL_MERIDIAN},
        lataxis_range=list(LATITUDE_RANGE),
        lonaxis_range=list(LONGITUDE_RANGE),
        showcountries=False,
        showland=False,
        showcoastlines=False,
        showocean=True,
        oceancolor=OCEAN_COLOR,
        showframe=False,
    )
    width, height = INTERACTIVE_MAP_SIZE
    fig.update_layout(
        height=height,
        width=width * len(tours),
        margin={"l": 0, "r": 0, "t": 50, "b": 20},
        annotations=[
            *fig.layout.annotations,
            {
                "text": SOURCE_NOTE,
                "x": 0.5,
                "y": 0,
                "xref": "paper",
                "yref": "paper",
                "showarrow": False,
                "font": {"size": 9},
            },
        ],
    )
    fig.show()


# --- Funciones públicas ------------------------------------------------------------


def plot_tour(
    cities: pd.DataFrame,
    tour: list,
    distances: np.ndarray,
    title: str = "",
    interactive: bool = False,
) -> None:
    """
    Dibuja una gira sobre el mapa de Argentina. Si la gira tiene pocas ciudades, se
    escriben sus nombres. El inicio se marca con ■, el final con ▼ y las capitales
    con ★.

    Args:
        cities (pd.DataFrame): Ciudades de la gira.
        tour (list): La gira.
        distances (np.ndarray): Matriz de distancias, para mostrar los km totales.
        title (str, opcional): Título del mapa. A continuación se agregan los km.
        interactive (bool, opcional): Si es True, genera un mapa interactivo con
                                      plotly, donde al pasar el mouse se ve el nombre
                                      y la fecha de cada ciudad. Por defecto es False:
                                      una imagen estática, liviana, que se ve en GitHub.
    """
    plot_tours(cities, {title: tour}, distances, interactive=interactive)


def plot_tours(
    cities: pd.DataFrame, tours: dict, distances: np.ndarray, interactive: bool = False
) -> None:
    """
    Dibuja varias giras lado a lado, para compararlas.

    Args:
        cities (pd.DataFrame): Ciudades de la gira.
        tours (dict): Diccionario {título: gira}. Admite hasta 4 giras.
        distances (np.ndarray): Matriz de distancias, para mostrar los km totales.
        interactive (bool, opcional): Si es True, genera mapas interactivos con plotly.
                                      Por defecto es False: imagen estática.
    """
    if len(tours) > len(TOUR_COLORS):
        raise ValueError(f"Se pueden comparar hasta {len(TOUR_COLORS)} giras")

    if interactive:
        _plot_interactive(cities, tours, distances)
    else:
        _plot_static(cities, tours, distances)


# ---------------------------------------------------------------------------------
# Cartel de la gira
#
# Imita los carteles de recitales impresos sobre cartulina con fondo degradé: el
# nombre de la banda bien grande, el disco que presentan y todas las fechas.
# ---------------------------------------------------------------------------------

BAND_NAME = ("LOS AUTÉNTICOS", "DESCENDENTES")
# En Anton las comillas « » se ven como <<, así que usamos las inglesas
ALBUM_NAME = "“AFTER ANNEALING”"
TOUR_NAME = "GIRA MÍNIMO GLOBAL"

# Tipografía Anton (licencia SIL Open Font License, ver datos/fuentes/OFL.txt)
POSTER_FONT = DATA_DIR / "fuentes" / "Anton-Regular.ttf"
POSTER_INK = "#161616"
# Colores del fondo, de abajo hacia arriba, con la posición donde empieza cada uno
POSTER_GRADIENT = [
    (0.0, "#1fc94f"),
    (0.2, "#c9e83a"),
    (0.34, "#ffe03d"),
    (0.6, "#ffd23d"),
    (0.76, "#ff6a5c"),
    (0.86, "#ff2e8a"),
    (1.0, "#ff2e8a"),
]
POSTER_SIZE = (11, 17)  # pulgadas, el tamaño de un cartel tabloide

# Fecha del primer show. El año solo sirve para calcular los días de la semana: en el
# cartel no aparece.
FIRST_SHOW = date(2025, 3, 7)

# Cómo se mueve la banda: al día siguiente de cada show, la avioneta despega a las
# 08:00. Si llega a la próxima ciudad antes de las 20:00, la banda toca esa misma
# noche. Si llega más tarde, toca al día siguiente.
PLANE_SPEED_KMH = 180
DEPARTURE_HOUR = 8
SHOW_HOUR = 20
HOURS_PER_DAY = 24

WEEKDAYS = ("LUN", "MAR", "MIÉ", "JUE", "VIE", "SÁB", "DOM")
MONTHS = (
    "ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"
)  # fmt: skip

# Cantidad de columnas del listado de fechas según la cantidad de shows
MAX_SHOWS_ONE_COLUMN = 12
MAX_SHOWS_TWO_COLUMNS = 50
MAX_DATE_FONT_SIZE = 24

# Zona del cartel (en fracción de la altura) que ocupa el listado de fechas
DATES_TOP = 0.585
DATES_BOTTOM = 0.105


def flight_hours(tour: list, distances: np.ndarray) -> float:
    """
    Calcula las horas de vuelo de una gira, con la avioneta a PLANE_SPEED_KMH.

    Args:
        tour (list): La gira.
        distances (np.ndarray): Matriz de distancias entre ciudades.

    Returns:
        float: Horas de vuelo totales.
    """
    return cost_function(tour, distances) / PLANE_SPEED_KMH


def tour_dates(tour: list, distances: np.ndarray) -> list:
    """
    Calcula la fecha de cada show de la gira. Al día siguiente de cada show, la
    avioneta despega a las 08:00 rumbo a la próxima ciudad. Si llega antes de las
    20:00, la banda toca esa misma noche; si llega más tarde, toca al día siguiente.

    Args:
        tour (list): La gira.
        distances (np.ndarray): Matriz de distancias entre ciudades.

    Returns:
        list: Lista con la fecha (datetime.date) de cada show, en orden.
    """
    dates = [FIRST_SHOW]
    for a, b in zip(tour[:-1], tour[1:]):
        # Hora de llegada, contando desde la medianoche del día en que despega
        arrival = DEPARTURE_HOUR + distances[a, b] / PLANE_SPEED_KMH
        # Si llega después del horario del show, se pasa al día siguiente. Un vuelo
        # muy largo puede llevar más de un día
        late_days = max(0, math.ceil((arrival - SHOW_HOUR) / HOURS_PER_DAY))
        dates.append(dates[-1] + timedelta(days=1 + late_days))
    return dates


def format_date(day: date) -> str:
    """Formatea una fecha como en los carteles, por ejemplo VIE 7 MAR."""
    return f"{WEEKDAYS[day.weekday()]} {day.day} {MONTHS[day.month - 1]}"


def _poster_text(
    ax: plt.Axes, x: float, y: float, text: str, size: float, **kwargs
) -> None:
    """Escribe un texto del cartel con la tipografía Anton."""
    font = FontProperties(fname=POSTER_FONT, size=size)
    kwargs = {"ha": "center", "va": "center", "color": POSTER_INK, **kwargs}
    ax.text(x, y, text, fontproperties=font, **kwargs)


def _draw_poster_header(ax: plt.Axes) -> None:
    """Dibuja la parte de arriba del cartel: banda, disco y nombre de la gira."""
    _poster_text(ax, 0.5, 0.932, BAND_NAME[0], 86)
    _poster_text(ax, 0.5, 0.852, BAND_NAME[1], 100)
    # Las notas musicales y las estrellas no están en Anton: usan la tipografía
    # por defecto de matplotlib
    ax.text(0.5, 0.79, "♪ ♫ ♪", ha="center", va="center", fontsize=28)
    _poster_text(ax, 0.5, 0.752, "PRESENTAN SU NUEVO DISCO", 30)
    _poster_text(ax, 0.5, 0.699, ALBUM_NAME, 64)
    _poster_text(ax, 0.5, 0.639, TOUR_NAME, 40)
    ax.text(0.5, 0.606, "★   ★   ★   ★   ★", ha="center", va="center", fontsize=16)


def _draw_poster_dates(ax: plt.Axes, names: list, dates: list) -> None:
    """Dibuja el listado de fechas en una, dos o tres columnas."""
    n = len(names)
    if n <= MAX_SHOWS_ONE_COLUMN:
        columns = 1
    elif n <= MAX_SHOWS_TWO_COLUMNS:
        columns = 2
    else:
        columns = 3
    rows = math.ceil(n / columns)

    row_height = (DATES_TOP - DATES_BOTTOM) / rows
    # Altura de cada renglón en puntos tipográficos, para elegir el tamaño de letra
    row_points = row_height * ax.get_position().height * POSTER_SIZE[1] * 72
    size = min(MAX_DATE_FONT_SIZE, 0.72 * row_points)

    column_width = 1 / columns
    for k, (name, day) in enumerate(zip(names, dates)):
        column, row = divmod(k, rows)
        x = column * column_width
        y = DATES_TOP - (row + 0.5) * row_height
        # La fecha alineada a la derecha y la ciudad a la izquierda de una línea
        # imaginaria, así todas las ciudades de una columna quedan alineadas
        middle = x + 0.36 * column_width
        _poster_text(ax, middle - 0.006, y, format_date(day), size, ha="right")
        _poster_text(ax, middle + 0.006, y, name.upper(), size * 0.92, ha="left")


def plot_poster(
    cities: pd.DataFrame, tour: list, distances: np.ndarray, footer: str = ""
) -> None:
    """
    Dibuja el cartel de la gira, con todas las fechas en el orden de la gira. Las
    fechas se calculan con tour_dates(), según cuánto tarda la avioneta en llegar a
    cada ciudad.

    Args:
        cities (pd.DataFrame): Ciudades de la gira.
        tour (list): La gira.
        distances (np.ndarray): Matriz de distancias entre ciudades.
        footer (str, opcional): Texto que se agrega al pie del cartel, por ejemplo,
                                el algoritmo con el que se armó la gira.
    """
    fig = plt.figure(figsize=POSTER_SIZE, facecolor="white")
    # Un pequeño margen blanco, como el borde de la cartulina
    ax = fig.add_axes((0.025, 0.015, 0.95, 0.97))
    ax.set_axis_off()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    background = LinearSegmentedColormap.from_list("cartel", POSTER_GRADIENT)
    ax.imshow(
        np.linspace(0, 1, 512)[:, None],
        cmap=background,
        origin="lower",
        aspect="auto",
        extent=(0, 1, 0, 1),
    )

    _draw_poster_header(ax)
    names = cities.loc[tour, "nombre"].tolist()
    _draw_poster_dates(ax, names, tour_dates(tour, distances))

    km = format_km(cost_function(tour, distances)).upper()
    hours = flight_hours(tour, distances)
    _poster_text(
        ax, 0.5, 0.068, f"EN AVIONETA CLANDESTINA · {km} · {hours:.0f} HS DE VUELO", 30
    )
    if footer:
        _poster_text(ax, 0.5, 0.028, footer.upper(), 16)
    plt.show()
