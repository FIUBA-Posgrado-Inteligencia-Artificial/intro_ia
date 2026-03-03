[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

# 🧠 Inteligencia Artificial (CEIA - FIUBA)

¡Bienvenido al repositorio oficial de la materia! Aquí encontrarás todo el material de clases, incluyendo presentaciones, ejercicios prácticos y notebooks interactivos.

> 📝 **Nota:** Para revisar los criterios de aprobación de la materia, por favor consulta el [documento correspondiente](CriteriosAprobacion.md).

---

## 📂 Organización del Repositorio

El material está estructurado por clases de la siguiente manera:

```text
📁 clase#
 ├── 📄 README.md
 ├── 📁 teoria/
 ├── 📁 ejercicios/
 └── 📁 jupyter_notebooks/
```

---

## 🛠️ Requerimientos y Herramientas

Para aprovechar el contenido, asegúrate de contar con el siguiente entorno de trabajo:

### 🐍 Entorno Python
- **Python:** >=3.11
- **Librerías principales:** Numpy, Pandas, SciPy, Matplotlib, Seaborn, Scikit-Learn, Pygame
- **Consolas interactivas:** IPython, Jupyter Notebook

### 💻 IDEs Recomendados
- Visual Studio Code
- Cursor / Google Antigravity / Windsurf
- PyCharm Community Edition
- Google Colab

### 📦 Gestión de Dependencias (Elige una opción)

<details>
<summary><strong>Opción 1: uv (Recomendado)</strong></summary>

Este repositorio contiene un archivo `pyproject.toml` para instalar las dependencias súper rápido usando [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```
</details>

<details>
<summary><strong>Opción 2: Conda</strong></summary>

Si prefieres usar Conda/Anaconda, proveemos el archivo `env_anaconda_shareable.yml`. Puedes crear el entorno y activarlo con:

```bash
conda env create -f env_anaconda_shareable.yml
conda activate ia_env
```
</details>

---

## 📚 Temario por Clases

| Clase | Temas Principales | Link |
| :---: | :--- | :---: |
| **01** | Introducción a la Materia • Inteligencia Artificial • Python | [🔗 Ver Clase](clase1/README.md) |
| **02** | Agente de resolución de problemas • Agente racional • Resolución mediante búsqueda | [🔗 Ver Clase](clase2/README.md) |
| **03** | Problemas de optimización • Algoritmos de búsqueda Local • Búsqueda en espacios continuos | [🔗 Ver Clase](clase3/README.md) |
| **04** | Aprendizaje Automático • Formas de aprendizaje • Aprendizaje supervisado | [🔗 Ver Clase](clase4/README.md) |
| **05** | Regresión Lineal (simple y múltiple) • Regresión Ridge y Lasso | [🔗 Ver Clase](clase5/README.md) |
| **06** | Conceptos de Clasificación • Regresión logística • Clasificador bayesiano ingenuo | [🔗 Ver Clase](clase6/README.md) |
| **07** | Aprendizaje por Refuerzo • Proceso de decisión de Márkov • Ecuación de Bellman | [🔗 Ver Clase](clase7/README.md) |

---

## 📖 Bibliografía Recomendada

⭐ **Libro Principal:**
- *Artificial Intelligence: A Modern Approach* - Stuart Russell, Peter Norvig (Ed. Pearson)

**Otros recursos útiles:**
- *Artificial Intelligence Basics: A Non-Technical Introduction* - Tom Taulli (Ed. Apress)
- *Artificial Intelligence For Dummies* - John Paul Mueller, Luca Massaron
- *[An Introduction to Statistical Learning](https://www.statlearning.com/)* - Gareth James (Ed. Springer)
- *[Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)* - Jake VanderPlas
- *The Elements of Statistical Learning* - Trevor Hastie (Ed. Springer)

---

## 📄 Licencia

Esta obra está bajo una [Licencia Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
