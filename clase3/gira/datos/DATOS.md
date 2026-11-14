# Datos de la gira

Esta carpeta contiene los datos que usan las notebooks de la gira de **Los Auténticos
Descendentes**. Fueron generados con el script `generar_datos.py` el **11 de noviembre
de 2026**.

## `ciudades.csv`

Los 111 lugares de la gira:

- Las **24 capitales**: las 23 capitales de provincia más la Ciudad Autónoma de Buenos
  Aires (columna `capital = True`). Forman la instancia fácil de la gira.
- **86 ciudades** de más de 30.000 habitantes. Para evitar que los aglomerados urbanos
  (como el conurbano bonaerense o el Gran Rosario) aparezcan como decenas de puntos
  pegados, se recorrieron las ciudades de mayor a menor población y se descartaron las
  que estaban a menos de 40 km de una ya elegida.
- La **Base Marambio** (Antártida Argentina), agregada a mano porque GeoNames la incluye
  en el archivo de la Antártida y no en el de Argentina. Es el final obligado de la
  gira.

Cuando un nombre se repite (por ejemplo, San Vicente), se le agrega la provincia entre
paréntesis.

| Columna | Descripción |
|---|---|
| `nombre` | Nombre de la localidad |
| `provincia` | Provincia a la que pertenece |
| `latitud`, `longitud` | Coordenadas en grados decimales (WGS84) |
| `poblacion` | Población según GeoNames |
| `capital` | `True` si es capital de provincia o la Ciudad Autónoma de Buenos Aires |

> ⚠️ La columna `poblacion` se usó solo para elegir las ciudades. Algunas cifras de
> GeoNames no son precisas (por ejemplo, la de Ituzaingó, Corrientes), así que no
> deben tomarse como datos oficiales. Para cifras oficiales, consultar el censo del
> INDEC.

**Fuente**: [GeoNames](https://www.geonames.org/), archivo
[`AR.zip`](https://download.geonames.org/export/dump/AR.zip). Licencia
[Creative Commons Atribución 4.0](https://creativecommons.org/licenses/by/4.0/).
Coordenadas de la Base Marambio: 64° 14' 29" S, 56° 37' 36" O.

## `provincias.geojson`

Límites de las 24 jurisdicciones, incluida la provincia de Tierra del Fuego, Antártida
e Islas del Atlántico Sur con el sector antártico y las Islas Malvinas. Se usa para
dibujar el mapa.

Los límites originales (112 MB) se simplificaron con una tolerancia de 0,01° (~1 km) y
las coordenadas se redondearon a 4 decimales, lo que deja un archivo de ~420 KB. Esta
simplificación es suficiente para un mapa del país completo, pero no para trabajos de
detalle.

**FUENTE: Instituto Geográfico Nacional de la República Argentina**. Capa `provincia`
del servicio WFS del IGN, descargada el 11 de noviembre de 2026. Uso sujeto a los
[términos y condiciones del IGN](https://www.ign.gob.ar/descargas/tyc1.html). Este
material no está patrocinado ni respaldado por el IGN.

## `fuentes/Anton-Regular.ttf`

Tipografía que se usa en el cartel de la gira. Se incluye en el repositorio para que el
cartel se vea igual en cualquier computadora.

**Fuente**: [Anton](https://fonts.google.com/specimen/Anton), de The Anton Project
Authors, descargada de Google Fonts. Licencia
[SIL Open Font License 1.1](https://openfontlicense.org/), cuyo texto completo está en
`fuentes/OFL.txt`.

## Distancias

Las distancias entre ciudades se calculan en línea recta sobre la superficie de la
Tierra (fórmula de *haversine*). No son distancias por ruta: la banda viaja en
avioneta clandestina.

## Cómo regenerar los datos

Desde la raíz del repositorio:

```bash
uv run clase3/gira/datos/generar_datos.py
```

El script declara sus propias dependencias, así que `uv` las instala en un entorno
aislado, sin modificar el del proyecto.
