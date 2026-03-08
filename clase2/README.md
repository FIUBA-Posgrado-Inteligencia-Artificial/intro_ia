# Clase 2 - Agentes y Resolución de Problemas mediante Búsqueda

<div align="center">
  <img src="content/img/fiuba.png" alt="FIUBA Logo" width="15%">
  
  **Dr. Ing. Facundo Adrián Lucianna | CEIA - FIUBA**
</div>

> [!NOTE] 
> **Nota sobre este documento:** Este archivo sirve como resumen estructurado de los contenidos de la clase. Algunos recursos mencionados (como las evaluaciones, los foros y los videos de las clases grabadas) están alojados exclusivamente en el aula virtual y no se incluyen directamente en este repositorio. Dichos elementos están marcados con el símbolo 🔒.

## Materiales obligatorios

En este segundo módulo, comenzaremos explorando el concepto de agente racional a través de dos videos:

- 📺 Clase 2.1 - Agentes (Video) 🔒 *(Solo en Campus Virtual)*

A continuación, abordaremos la resolución de problemas mediante búsqueda, explorando diversos algoritmos que nos permitirán optimizar el proceso de toma de decisiones. Los algoritmos que veremos se dividen en dos categorías:

**Algoritmos de búsqueda no informada:**
- Busqueda primero en anchura (BFS)
- Busqueda de costo uniforme (algoritmo de Dijkstra)
- Busqueda primero en profundidad (DFS)
- Busqueda de profundidad limitada
- Busqueda de profundidad limitada con profundidad iterativa

**Algoritmos de búsqueda informada:**
- Busqueda voraz (greedy) primero el mejor
- Busqueda A*

- 📺 Clase 2.2 - Resolución de problemas mediante búsqueda (Video) 🔒 *(Solo en Campus Virtual)*

Como material de apoyo, encontrarán a continuación el **material teórico** y la **presentación en formato HTML** utilizados durante esta clase.

- 📘 [Teoria clase 2](./content/teoria/README.md)
- 🌐 [Versión presentación html](./content/teoria/clase2.html)

> [!NOTE]
> **Aclaración sobre la presentación:** Para visualizar correctamente la versión HTML animada, es necesario descargar el archivo *clase2.html* a tu computadora y abrirlo con cualquier navegador web (Chrome, Firefox, Edge, etc.), ya que GitHub no previsualiza este tipo de formato.

### Consideraciones previas

Tal como vimos en el segundo video, vamos a realizar un ejercicio práctico en el que aplicaremos un algoritmo de búsqueda para resolver el problema de la Torre de Hanoi. Las siguientes recursos son necesarios para poder hacer el trabajo práctico y complementar tu aprendizaje

#### Implementación de estructuras

Primero veamos en la primera notebook la implementación de varias estructuras necesarias para poder definir el problema de la Torre de Hanoi. Dejo a continuación, un código para que usen, pero pueden optar por desarrollar su propia implementación en cualquier otro lenguaje de programación.

- 📓 [1 - Implementación de Problema de la Torre de Hanoi - Jupyter Notebook](./hanoi_tower/1-hanoi_implementation_notebook.ipynb)

#### Algoritmo de búsqueda

Una vez implementadas las estructuras necesarias para poder modelar el problema,  debemos aplicar un algoritmo de búsqueda. Para ello, primero necesitamos más estructuras tales como el árbol de búsqueda y las colas.  Una vez definidos estos, en el siguiente notebook, armaremos una implementación de Búsqueda primero en anchura. 

- 📓 [2 - Algoritmos de búsqueda - Jupyter Notebook](./hanoi_tower/2-search_hanoi_notebook.ipynb)

En este último notebook, además vimos cómo podemos medir el rendimiento del algoritmo.

De manera opcional, pueden ver la implementación de un visualizador de la solución utilizando PyGame. El siguiente notebook explica el funcionamiento de esta implementación y cómo utilizarla:

- 📓 [3 - Simulador de Torres de Hanoi - Jupyter Notebook](./hanoi_tower/3-visualization_tool.ipynb)
- 📺 [Simulador Torre de Hanoi - Inteligencia Artificial - FIUBA (YouTube)](https://youtu.be/9F8etRlu9Tg?si=mBMOVdFsfTxY-KSc)

Este simulador resulta interesante porque muestra al agente ejecutando la solución que encontró, lo que permite comprender cómo el algoritmo de búsqueda se traduce en una ejecución práctica.

Si desean experimentar con los algoritmos de búsqueda informada, necesitarán una función heurística. Pueden profundizar en el siguiente artículo

- 📘 [Funciones heurísticas - Torre de Hanoi](./content/heuristic_functions.md)

### Evaluación práctica
 
Ahora que ya tienen las herramientas necesarias, es momento de realizar la **evaluación práctica**. Asegúrense de leer detenidamente el enunciado y no duden en plantear cualquier inquietud en el foro.

- 📝 Evaluación práctica - Módulo 2 - Torre de Hanoi 🔒 *(Solo en Campus Virtual)*

Recuerden que el código que les puede servir para realizar la evaluación está en el repositorio.

- 📓 [Link al notebook de la evaluación práctica - Jupyter Notebook](./exercise/exercise_2.ipynb)
- 🔗 [Link al repositorio a código Hanoi Tower](./exercise/aima_libs/__init__.py)

## Dudas y consultas

Cualquier duda técnica o conceptual referida a esta unidad puede volcarse libremente en la sección de participación general del foro. 

- 💬 Foro de consulta - Módulo 2 🔒 *(Solo en Campus Virtual)*

## Actividades no obligatorias

Si deseas seguir profundizando en estos temas, te recomiendo leer el [capítulo 3](https://artint.info/3e/html/ArtInt3e.Ch3.html) de Artificial Intelligence: Foundations of Computational Agents de Poole y Mackworth.
