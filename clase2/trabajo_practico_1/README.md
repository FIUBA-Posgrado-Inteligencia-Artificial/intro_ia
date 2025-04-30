# TP1: Algoritmos de búsqueda en Torre de Hanoi

En el módulo presentamos el problema de la Torre de Hanoi. Además, vimos diferentes algoritmos de búsqueda que nos permitieron resolver este problema. Para este trabajo práctico, deberán implementar un método de búsqueda para resolverlo con 5 discos, partiendo de un estado inicial y alcanzando un estado objetivo

![Torres Hanoi](./torres.png "Torres Hanoi")

## Tareas y preguntas a resolver:

1. ¿Cuáles son los PEAS de este problema? (Performance, Environment, Actuators, Sensors)
2. ¿Cuáles son las propiedades del entorno de trabajo?
3. En el contexto de este problema, defina los siguientes conceptos:
    - Estado
    - Espacio de estados
    - Árbol de búsqueda
    - Nodo de búsqueda
    - Objetivo
    - Acción
    - Frontera
4. Implemente algún método de búsqueda. Podés elegir cualquiera excepto búsqueda en anchura (breadth-first search), que ya fue desarrollada en clase. Sos libre de utilizar cualquiera de los algoritmos vistos, o incluso explorar nuevos.
5. ¿Cuál es la complejidad teórica en tiempo y memoria del algoritmo elegido?
6. A nivel de implementación, ¿cuánto tiempo y memoria utiliza el algoritmo? (Se recomienda ejecutarlo 10 veces y calcular el promedio y el desvío estándar de ambas métricas).
7. Si la solución óptima es de $2^k - 1$ movimientos (siendo *k* el número de discos), ¿qué tan lejos está la solución encontrada por el algoritmo implementado de esa solución óptima? (Se recomienda ejecutar al menos 10 veces y usar el promedio de los trayectos obtenidos).

### Entregables

El trabajo deberá incluir:
- Un archivo en formato `.txt`, `.pdf` o `.docx` con las respuestas teóricas.
- Los archivos con el código implementado.

Alternativamente, pueden entregar una notebook de Jupyter con todo el contenido y la solución.

Si agregan archivos `.json` para usar en el simulador, mejor aún. Pueden subir los archivos o proporcionar un enlace a un repositorio público (GitHub o GitLab) con todo el contenido. **No olviden especificar en el entregable los autores del trabajo práctico.**

#### Consideraciones

Pueden utilizar todos los recursos que consideren necesarios para resolver este trabajo. Tienen libertad para elegir el lenguaje de programación y el enfoque de implementación.

Para ahorrar tiempo, pueden utilizar el código ya implementado en Python disponible en el repositorio [hanoi_tower](https://github.com/FIUBA-Posgrado-Inteligencia-Artificial/intro_ia/tree/main/clase2/hanoi_tower). Si optan por esta alternativa, solo deberán implementar el algoritmo de búsqueda. Sin embargo, es fundamental que lean y comprendan cada parte del código existente.