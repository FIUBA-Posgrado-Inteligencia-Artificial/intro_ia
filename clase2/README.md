# Clase 2 - Agentes y resolución de problemas mediante búsqueda

<div align="center">
  <img src="content/img/fiuba.png" alt="FIUBA Logo" width="15%">
  
  **Dr. Ing. Facundo Adrián Lucianna | CEIA - FIUBA**
</div>

> [!NOTE] 
> **Nota sobre este documento:** Este archivo sirve como resumen estructurado de los contenidos de la clase. Algunos recursos mencionados (como las evaluaciones, los foros y los videos de las clases grabadas) están alojados exclusivamente en el aula virtual y no se incluyen directamente en este repositorio. Dichos elementos están marcados con el símbolo 🔒.

## Materiales obligatorios

En este segundo módulo, comenzaremos explorando el concepto de **agente racional** a través de dos videos:

- 📺 Clase 2.1 - Agentes (Video) 🔒 *(Solo en Campus Virtual)*

A continuación, abordaremos la **resolución de problemas mediante búsqueda**, explorando diversos algoritmos que nos permitirán optimizar el proceso de toma de decisiones. Los algoritmos que veremos se dividen en dos categorías:

**Algoritmos de búsqueda no informada:**
1. Búsqueda primero en anchura (BFS)
2. Búsqueda de costo uniforme (Algoritmo de Dijkstra)
3. Búsqueda primero en profundidad (DFS)
4. Búsqueda de profundidad limitada
5. Búsqueda de profundidad limitada con profundidad iterativa

**Algoritmos de búsqueda informada:**
1. Búsqueda voraz (*greedy*) primero el mejor
2. Búsqueda A*

- 📺 Clase 2.2 - Resolución de problemas mediante búsqueda (Video) 🔒 *(Solo en Campus Virtual)*

Como material de apoyo, encontrarán a continuación el **material teórico** y la **presentación en formato HTML** utilizados durante esta clase.

- 📘 [Teoria clase 2](./content/teoria/README.md)
- 🌐 [Versión presentación html](./content/teoria/clase2.html)

> [!NOTE]
> **Aclaración sobre la presentación:** Para visualizar correctamente la versión HTML animada, es necesario descargar el archivo *clase2.html* a tu computadora y abrirlo con cualquier navegador web (Chrome, Firefox, Edge, etc.), ya que GitHub no previsualiza este tipo de formato.

### Consideraciones previas

Tal como vimos en el segundo video, vamos a aplicar los algoritmos de búsqueda al problema de la **Torre de Hanoi**, y después ustedes van a resolver un **Sudoku** en la evaluación práctica. Los siguientes recursos son necesarios para poder llevar a cabo el trabajo práctico y complementar su aprendizaje:

#### Implementación de estructuras

En primer lugar, veremos en la primera notebook la implementación de varias estructuras necesarias para poder definir el **problema de la Torre de Hanoi**. Este código base es el que vamos a reutilizar en el resto de las notebooks de la clase.

- 📓 [1 - Implementación de Problema de la Torre de Hanoi - Jupyter Notebook](./content/hanoi_tower/1-hanoi_implementation_notebook.ipynb)

#### Algoritmos de búsqueda

Una vez implementadas las estructuras necesarias para modelar el problema, debemos aplicar un algoritmo de búsqueda. Para ello, primero necesitamos de otras estructuras, como **el árbol de búsqueda** y **las colas**. Una vez definidos estos conceptos, en el siguiente notebook armaremos una implementación de **búsqueda primero en anchura**.

- 📓 [2 - Algoritmos de búsqueda - Jupyter Notebook](./content/hanoi_tower/2-search_hanoi_notebook.ipynb)

En este último notebook también vimos cómo medir el rendimiento del algoritmo.

Con la misma estructura, implementamos el resto de los **algoritmos de búsqueda no informada**: búsqueda primero en profundidad, de costo uniforme, de profundidad limitada y de profundidad iterativa, y los comparamos con la búsqueda primero en anchura.

- 📓 [3 - Búsqueda no informada - Jupyter Notebook](./content/hanoi_tower/3-busqueda_no_informada.ipynb)

Para los **algoritmos de búsqueda informada** necesitamos una **función heurística**, que estime cuánto falta para llegar al objetivo. Pueden profundizar sobre este tema en el siguiente recurso:

- 📘 [Funciones heurísticas - Torre de Hanoi](./content/heuristic_functions.md)

Con esa heurística, implementamos la **búsqueda voraz** y la **búsqueda A\***, y vemos por qué una heurística admisible garantiza encontrar el camino más corto.

- 📓 [4 - Búsqueda informada - Jupyter Notebook](./content/hanoi_tower/4-busqueda_informada.ipynb)

De manera opcional, pueden usar un **visualizador de la solución** hecho con **PyGame**. En el siguiente notebook se explica cómo funciona, y se puede elegir cualquiera de los algoritmos anteriores para ver la animación de la solución que encuentra:

- 📓 [5 - Simulador de Torres de Hanoi - Jupyter Notebook](./content/hanoi_tower/5-visualization_tool.ipynb)
- 📺 [Simulador Torre de Hanoi - Inteligencia Artificial - FIUBA (YouTube)](https://youtu.be/9F8etRlu9Tg?si=mBMOVdFsfTxY-KSc)

Este simulador resulta interesante porque muestra al agente ejecutando la solución que encontró, lo cual permite comprender cómo el algoritmo de búsqueda se traduce en una ejecución práctica.

### Evaluación práctica
 
Ahora que ya tienen las herramientas necesarias, es momento de realizar la **evaluación práctica**: resolver un **Sudoku** implementando un algoritmo de búsqueda. El Sudoku ya viene modelado con la misma estructura que la Torre de Hanoi, así que pueden tomar como referencia los algoritmos de las notebooks 2, 3 y 4. Asegúrense de leer detenidamente el enunciado y no duden en plantear cualquier inquietud en el **foro**.

- 📝 [Evaluación práctica - Módulo 2 - Sudoku](./exercise/README.md)

¿Es tu primera vez usando **notebooks** o **Python**? ¡No te preocupes! Si no sabés por dónde empezar con este TP, en este video te explicamos paso a paso cómo ejecutar todo.

- 📺 [Usando Jupyter por primera vez - Inteligencia Artificial - FIUBA](https://www.youtube.com/watch?v=7qXHFSwt4tw)

Recuerden que el código que les puede servir para realizar la evaluación está en el repositorio.

- 📓 [Link al notebook de la evaluación práctica - Jupyter Notebook](./exercise/exercise_2.ipynb)
- 🔗 [Link al código de la Torre de Hanoi y los algoritmos de búsqueda](./content/hanoi_tower/README.md)

Problemas ejecutando la notebook?...

- 🛠️ [Guía: cómo hacer funcionar exercise_2.ipynb](./exercise/COMO_EJECUTAR.md)

## Dudas y consultas

Cualquier duda técnica o conceptual referida a esta unidad puede volcarse libremente en la sección de participación general del **foro**. 

- 💬 Foro de consulta - Módulo 2 🔒 *(Solo en Campus Virtual)*

## Actividades no obligatorias

Si desean seguir profundizando en estos temas, les recomiendo leer el [capítulo 3](https://artint.info/3e/html/ArtInt3e.Ch3.html) del libro *Artificial Intelligence: Foundations of Computational Agents* de Poole y Mackworth.
