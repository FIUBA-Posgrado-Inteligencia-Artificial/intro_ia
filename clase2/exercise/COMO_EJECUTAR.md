# 🛠️ Guía: cómo hacer funcionar `exercise_2.ipynb`

**Inteligencia Artificial - CEIA - FIUBA**

Si al ejecutar la primera celda del notebook les aparece este error:

```text
ModuleNotFoundError: No module named 'aima_libs'
```

no está roto el notebook: les falta la carpeta `aima_libs`. Esta guía explica por qué pasa y cómo solucionarlo.

---

## 🔍 ¿Por qué pasa esto?

La primera celda del notebook hace:

```python
from aima_libs.hanoi_states import ProblemHanoi, StatesHanoi
from aima_libs.tree_hanoi import NodeHanoi
```

`aima_libs` **no es un paquete de PyPI**: no se instala con `pip install aima_libs` (si lo intentan, o no existe, o van a instalar algo que no tiene nada que ver). Es una carpeta con código de la cátedra que vive **al lado del notebook**, en el repositorio.

Cuando descargan solamente el archivo `exercise_2.ipynb` (por ejemplo con el botón *Download raw file* de GitHub), se llevan el notebook pero no la carpeta que necesita. Python busca `aima_libs` en la carpeta desde donde se levantó el kernel y no la encuentra.

La estructura que tiene que quedar es esta:

```text
mi_carpeta_de_trabajo/
├── exercise_2.ipynb          <- el notebook que completan
└── aima_libs/                <- la carpeta que falta
    ├── __init__.py           <- archivo vacío, pero TIENE que estar
    ├── aima.py
    ├── hanoi_states.py
    └── tree_hanoi.py
```

> [!IMPORTANT]
> `aima_libs` tiene que estar en la **misma carpeta** que el notebook, no una carpeta más arriba ni adentro de otra subcarpeta.

---

## ✅ Solución 1 (recomendada): clonar el repositorio completo

Es la opción más simple y la que menos problemas trae, porque se llevan todo el material de la materia y con la estructura correcta.

```bash
git clone https://github.com/FIUBA-Posgrado-Inteligencia-Artificial/intro_ia.git
cd intro_ia/clase2/exercise
```

Ahí adentro ya están `exercise_2.ipynb` y `aima_libs/`. Abren Jupyter desde esa carpeta y listo:

```bash
jupyter lab
```

Si no tienen `git` instalado, pueden bajar el repo como ZIP desde GitHub (botón verde **Code → Download ZIP**), descomprimirlo y entrar a `clase2/exercise`.

---

## ✅ Solución 2: descargar los archivos desde el navegador

Si ya tienen el notebook en una carpeta propia y no quieren clonar todo el repositorio, pueden bajar los archivos que faltan uno por uno desde GitHub. No hace falta usar la consola ni tener `git` instalado.

### Paso 1: crear la carpeta `aima_libs`

Al lado de su `exercise_2.ipynb`, creen una carpeta nueva y llámenla exactamente **`aima_libs`** (todo en minúscula, con guion bajo). En Windows: clic derecho → *Nuevo* → *Carpeta*. En macOS: clic derecho → *Nueva carpeta*.

### Paso 2: entrar a la carpeta en GitHub

Abran este link en el navegador:

🔗 **https://github.com/FIUBA-Posgrado-Inteligencia-Artificial/intro_ia/tree/main/clase2/exercise/aima_libs**

Van a ver los 4 archivos que necesitan:

- `__init__.py`
- `aima.py`
- `hanoi_states.py`
- `tree_hanoi.py`

### Paso 3: descargar cada archivo

Para **cada uno** de los 4 archivos, repitan esto:

1. Hagan clic en el nombre del archivo para abrirlo.
2. Arriba a la derecha del recuadro con el código hay un grupo de botones. Busquen el ícono de **descarga** (una flecha hacia abajo), cuyo cartelito dice **Download raw file**.
3. El navegador va a bajar el archivo a su carpeta de *Descargas*.
4. Vuelvan atrás con la flecha del navegador y sigan con el siguiente archivo.

> [!TIP]
> Si en vez del ícono de descarga usan el botón **Raw**, se les va a abrir el código en una pestaña. Desde ahí pueden guardarlo con `Ctrl + S` (o `Cmd + S` en Mac), pero presten atención a que se guarde con el nombre y la extensión correctos (ver la advertencia de más abajo).

### Paso 4: mover los archivos a `aima_libs`

Vayan a su carpeta de *Descargas*, seleccionen los 4 archivos y muévanlos (cortar y pegar, o arrastrar) adentro de la carpeta `aima_libs` que crearon en el Paso 1.

Al terminar tiene que quedar así:

```text
mi_carpeta_de_trabajo/
├── exercise_2.ipynb
└── aima_libs/
    ├── __init__.py
    ├── aima.py
    ├── hanoi_states.py
    └── tree_hanoi.py
```

> [!WARNING]
> Tres detalles que suelen fallar acá:
> - **No se olviden de `__init__.py`.** En GitHub se ve vacío (pesa 0 bytes) y por eso muchos lo saltean, pero es justamente el archivo que le dice a Python que `aima_libs` es un paquete. Sin él, el import falla igual.
> - **Ojo con las extensiones en Windows.** A veces el navegador guarda `aima.py` como `aima.py.txt`. Para darse cuenta, activen *Vista → Mostrar → Extensiones de nombre de archivo* en el Explorador de Windows y verifiquen que los 4 terminen en `.py`. Si alguno quedó con `.txt`, renómbrenlo.
> - **No creen una carpeta dentro de otra.** Si les queda `aima_libs/aima_libs/aima.py`, no va a funcionar. Los `.py` van directamente adentro de `aima_libs`.

---

## ✅ Solución 3: trabajar en Google Colab

Si no quieren instalar nada localmente, en Colab pueden bajar las dependencias desde la primera celda. Agreguen **una celda nueva al principio del notebook** con esto:

```python
!wget -q -N -P aima_libs https://raw.githubusercontent.com/FIUBA-Posgrado-Inteligencia-Artificial/intro_ia/main/clase2/exercise/aima_libs/__init__.py
!wget -q -N -P aima_libs https://raw.githubusercontent.com/FIUBA-Posgrado-Inteligencia-Artificial/intro_ia/main/clase2/exercise/aima_libs/aima.py
!wget -q -N -P aima_libs https://raw.githubusercontent.com/FIUBA-Posgrado-Inteligencia-Artificial/intro_ia/main/clase2/exercise/aima_libs/hanoi_states.py
!wget -q -N -P aima_libs https://raw.githubusercontent.com/FIUBA-Posgrado-Inteligencia-Artificial/intro_ia/main/clase2/exercise/aima_libs/tree_hanoi.py
```

> [!IMPORTANT]
> **Esa celda es solo para que puedan trabajar, no forma parte de la entrega.** Antes de entregar el notebook, bórrenla: la consigna pide completar únicamente las secciones indicadas, sin agregar contenido adicional.

Otra opción en Colab es clonar el repo completo:

```python
!git clone https://github.com/FIUBA-Posgrado-Inteligencia-Artificial/intro_ia.git
%cd intro_ia/clase2/exercise
```

Y desde ahí abrir el notebook con **Archivo → Abrir cuaderno → GitHub / Subir**.

---

## 🧪 Cómo verificar que quedó bien

Antes de arrancar con el ejercicio, corran esto en una celda temporal del notebook:

```python
import os

print("Carpeta actual:", os.getcwd())
print("Contenido:", sorted(os.listdir()))
print("aima_libs:", sorted(os.listdir("aima_libs")))
```

Tienen que ver `exercise_2.ipynb` y `aima_libs` en el contenido de la carpeta actual, y los 4 archivos `.py` adentro de `aima_libs`. Si eso da bien, la celda de imports del notebook debería correr sin errores:

```python
from aima_libs.hanoi_states import ProblemHanoi, StatesHanoi
from aima_libs.tree_hanoi import NodeHanoi

print("Todo OK ✅")
```

(Acuérdense de borrar estas celdas de prueba antes de entregar.)

---

## 🐍 Entorno de Python

El material está pensado para **Python 3.11 o superior** (nosotros usamos 3.12). Para este ejercicio en particular no hacen falta librerías externas: `aima_libs` usa solo la biblioteca estándar. Igual, conviene tener armado el entorno de la materia.

En la clase 1 explicamos tres formas de armarlo, según cuánto se quieran meter:

**👶 Modo Bebé — Google Colab.** No instalan nada: trabajan desde el navegador. Es la vía más rápida si el entorno local les está dando dolores de cabeza (ver la [Solución 3](#-solución-3-trabajar-en-google-colab) de arriba para traer `aima_libs` a Colab).

- 🛠️ [Herramientas de desarrollo - Modo Bebé 👶](../../clase1/content/modo_baby.md)

**🙂 Modo Novato — Anaconda (recomendado).** Es la opción recomendada para la materia. Desde la raíz del repositorio:

```bash
conda env create -f env_anaconda_shareable.yml
conda activate ia_env
jupyter lab
```

- 🛠️ [Herramientas de desarrollo - Modo Novato 🙂](../../clase1/content/modo_novato.md)

**👹 Modo Gore — uv.** Para quienes quieran usar herramientas más modernas. El repositorio ya trae `pyproject.toml` y `uv.lock`, así que desde la raíz:

```bash
uv sync
uv run jupyter lab
```

- 🛠️ [Herramientas de desarrollo - Modo Gore 👹](../../clase1/content/modo_gore.md)

> [!NOTE]
> El notebook usa `tuple[NodeHanoi, dict]` como anotación de tipo. Eso requiere Python 3.9+; con versiones anteriores van a ver un `TypeError` en la definición de la función.

---

## 🧯 Otros errores frecuentes

| Error / síntoma | Causa probable | Solución |
| :--- | :--- | :--- |
| `ModuleNotFoundError: No module named 'aima_libs'` | Falta la carpeta, o Jupyter se abrió desde otra carpeta | Verificar con `os.getcwd()` que estén parados donde está el notebook y que `aima_libs` esté al lado |
| `ModuleNotFoundError: No module named 'aima_libs.hanoi_states'` | Bajaron `__init__.py` pero falta alguno de los otros `.py` | Chequear que estén los 4 archivos |
| Los archivos están pero igual falla | Los archivos quedaron con extensión `.py.txt`, o `aima_libs` quedó anidada (`aima_libs/aima_libs/...`) | Renombrar / reacomodar según la estructura de arriba |
| Cambié un archivo de `aima_libs` y el notebook sigue usando la versión vieja | Python cachea los módulos ya importados | Reiniciar el kernel (**Kernel → Restart**) y volver a correr |
| `NameError: name 'NodeHanoi' is not defined` | No corrieron la celda de imports | Ejecutar las celdas en orden, de arriba hacia abajo |
| Se cuelga o tarda muchísimo en `search_algorithm(number_disks=5)` | El algoritmo entró en un ciclo (revisitando estados) | Llevar un registro de estados ya visitados; probar primero con `number_disks=3` |
| Aparece una carpeta `__pycache__` | Es normal: son los `.pyc` que genera Python | Ignorarla, no hace falta entregarla |

---

## 📦 Qué entregar

Solo el notebook `exercise_2.ipynb` completo, con:

- Su nombre en la primera celda markdown.
- Únicamente las secciones indicadas completadas, sin celdas extra (acordarse de borrar las celdas de descarga o de verificación que hayan agregado).
- Las celdas ejecutadas, de modo que se vean las métricas y la solución en la salida.

No hace falta entregar `aima_libs` ni `__pycache__`.
