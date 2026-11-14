# Evaluación práctica - Módulo 3 - Aproximando la FIUBA con triángulos

## 📋 Descripción del problema
En este ejercicio deberán implementar el algoritmo de **Simulated Annealing** para aproximar una foto de la Facultad de Ingeniería usando solamente **100 triángulos** semitransparentes.

Cada triángulo tiene una posición, un color y una transparencia. El objetivo es encontrar los valores que hacen que la imagen formada por los triángulos se parezca lo más posible a la foto. Es un **problema de optimización**: no hay una solución exacta que encontrar, sino una función de costo que queremos hacer lo más chica posible.

En el notebook ya están implementadas la representación del problema, la función de costo, la generación de vecinos y el algoritmo de gradiente descendente. Ustedes deberán implementar Simulated Annealing, elegir sus parámetros y comparar los resultados con los de gradiente descendente.

---

## 🛠️ Instrucciones de Entrega
A continuación, se deja el enlace al notebook que deben completar para resolver el ejercicio.

> [!IMPORTANT]
> Es **obligatorio** completar únicamente las secciones indicadas en el notebook, sin agregar contenido adicional.

🔗 **[Notebook a completar](aproximando_la_fiuba.ipynb)**

> [!NOTE]
> El notebook necesita el archivo `fiuba.jpg`, que está en esta misma carpeta. Cada ejecución de los algoritmos tarda alrededor de medio minuto.

---

## 📷 Créditos de la imagen
[Foto de la Facultad de Ingeniería de la Universidad de Buenos Aires](https://commons.wikimedia.org/wiki/File:Facultad_de_Ingenier%C3%ADa_Universidad_de_Buenos_Aires_(FIUBA).jpg), de Gobonobo, publicada en Wikimedia Commons bajo la licencia [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
