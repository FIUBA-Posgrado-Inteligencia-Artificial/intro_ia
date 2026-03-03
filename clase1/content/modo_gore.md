# Modo Gore 👹

Si sos un hábil programador o sentís que ya tenés suficientes conocimientos como para animarte a algo más personalizado, veamos qué opciones de instalación tenés. Ahora vamos a ver cómo armar un entorno de programación en Python orientado a propósitos generales, es decir, algo similar a lo que haría un desarrollador Python en su día a día.

> [!NOTE]
> Se puede usar Anaconda perfectamente como entorno de desarrollo, y de hecho es ampliamente utilizado en ciencia de datos. Incluso AWS usa Anaconda en _[SageMaker](https://aws.amazon.com/es/sagemaker/)_ para construir herramientas profesionales. Acá simplemente mostramos otras alternativas para quienes quieran animarse a meterse más a fondo en el rabbit hole.

📌 Al igual que en el **modo novato**, necesitamos tres cosas básicas:

1. Tener instalada al menos una versión de Python
2. Un sistema de gestión de paquetes
3. Herramientas para crear entornos virtuales

---

### 🐍 Instalar Python

Dependiendo de tu sistema operativo, tenés varias opciones para instalar Python:

* Descargarlo desde la página oficial de [Python](https://www.python.org/), donde se pueden elegir distintas versiones.
* Usar el gestor de paquetes del sistema (en Linux o Windows con [WSL](https://learn.microsoft.com/es-es/windows/wsl/install)), o [Homebrew](https://brew.sh/) en macOS. Por ejemplo, Ubuntu incluye Python en su [repositorio deadsnakes](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa) y Arch Linux a través de [AUR](https://aur.archlinux.org/packages/python).
* Usar un gestor de versiones de Python, como:
  * [pyenv](https://github.com/pyenv/pyenv) para Linux/macOS **_(recomendado)_**
  * [pyenv-win](https://github.com/pyenv-win/pyenv-win) para Windows

---

### 📦 Gestión de paquetes o librerías

[pip](https://pypi.org/) es el sistema de gestión de paquetes oficial de Python, utilizado para instalar y administrar paquetes desde el repositorio [PyPI](https://pypi.org/). Desde hace años, Python ya incluye pip por defecto.

También existen otros gestores que vale la pena conocer:

* [Poetry](https://python-poetry.org/)
* [Mamba](https://github.com/mamba-org/mamba)
* [PDM](https://pdm-project.org/en/latest/)
* Entre otros

---

### 🧪 Entornos virtuales

Para crear entornos virtuales también hay múltiples opciones. La más clásica y popular es [virtualenv](https://virtualenv.pypa.io/en/latest/) (o el módulo nativo `venv`), aunque hay otras herramientas interesantes:

* [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
* [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

---

### ✨ La alternativa moderna: uv

Una herramienta muy popular en el desarrollo moderno con Python es **[uv](https://docs.astral.sh/uv/)**.

> _uv es una herramienta extremadamente rápida para la gestión de dependencias y el empaquetado de proyectos en Python, escrita en Rust. Es una alternativa a herramientas como pip, pip-tools y virtualenv, optimizada para la velocidad, que se encarga de instalar, actualizar y gestionar las librerías que tu proyecto necesita de manera eficiente._

Para iniciar un nuevo proyecto:

```bash
uv init test-project
```

También se puede indicar qué versión de Python se desea usar:

```bash
uv init test-project --python 3.11
```

Esto generará una estructura básica de proyecto que incluye:

* `.python-version`: contiene la versión de Python especificada.
* `README.md`: archivo Markdown con una descripción del proyecto.
* `hello.py` / `main.py`: script de ejemplo que actúa como punto de entrada.
* `pyproject.toml`: archivo de configuración estándar para proyectos Python.

Dado que es común que un sistema ya tenga instalada una versión de Python, uv permite detectar las versiones disponibles. Sin embargo, también podés dejar que uv se encargue de instalar una versión específica. **uv** primero intentará encontrar una instalación existente de la versión solicitada. Si no la encuentra, puede instalarla automáticamente.

También podés instalar versiones de Python manualmente usando `uv python`:

* `uv python install 3.12.3` - Instala una versión específica
* `uv python install 3.12` - Instala la última versión disponible de la rama 3.12
* `uv python install ">=3.8,<3.10"` - Instala una versión que cumpla con esa restricción
* `uv python install 3.9 3.10 3.11` - Instala múltiples versiones

> [!WARNING]
> **Nota:** Las versiones de Python disponibles pueden estar "congeladas" por la versión de uv. Si necesitás una versión de Python muy reciente, asegurate de tener [uv actualizado](https://docs.astral.sh/uv/getting-started/installation/#updating-uv).

Toda la configuración del proyecto —metadatos, dependencias, y ajustes de herramientas— se guarda en `pyproject.toml`, el estándar moderno definido por [PEP 621](https://packaging.python.org/en/latest/specifications/pyproject-toml/#pyproject-toml-spec). Ahí se registran cosas como:

* El nombre del proyecto
* La versión requerida de Python
* Las dependencias del proyecto
* Configuraciones específicas de uv (y otras herramientas, como ruff o pytest)

Por ejemplo, para agregar una dependencia con uv, lo ideal es usar:

```bash
uv add matplotlib
```

Esto actualizará automáticamente `pyproject.toml` y bloqueará las versiones en `uv.lock`. El `uv.lock` es el archivo de bloqueo que garantiza que todas las dependencias se instalen en las mismas versiones exactas, lo que hace el entorno reproducible en cualquier máquina.

> [!TIP]
> En el [repositorio de esta materia](https://github.com/FIUBA-Posgrado-Inteligencia-Artificial/intro_ia) se incluye un `pyproject.toml` y un `uv.lock` con todas las dependencias necesarias para el curso. Para instalar todo y configurarlo _automágicamente_, simplemente corré el comando:
> 
> ```bash
> uv sync
> ```

Y esto es solo la punta del iceberg. uv es una herramienta muy poderosa (¡podés ejecutar scripts sin instalar dependencias manualmente con `uv run`!). Pero como sos un usuario _hardcore_, [no vas a tener problema en leer la documentación oficial](https://docs.astral.sh/uv/) 😉.
