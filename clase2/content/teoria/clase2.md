# Clase 2 - Agentes y Resolución de Problemas

---

## Diapositiva 1
**Introducción**

**Inteligencia Artificial**

![Portada](img/img-003.png)

Dr. Ing. Facundo Adrián Lucianna - CEIA - FIUBA

---

## Diapositiva 2: Agentes Racionales

Portada de sección

---

## Diapositiva 3: Agentes Racionales

### Agente

![Agente](img/page3_img1.png)

---

## Diapositiva 4: Agentes Racionales

### Agente

![Secuencia de percepciones](./img/page2_img1.png)

---

## Diapositiva 5: Agentes Racionales

### Agente

![Secuencia de percepciones](./img/page2_img1.png)

> Una elección de acción de un agente en un momento dado puede depender en su conocimiento incorporado y en la secuencia completa de percepciones hasta ese instante, pero no en cualquier cosa que no haya percibido.

---

## Diapositiva 6: Agentes Racionales

### Agente

En términos matemáticos, el comportamiento del agente viene dado por la **función del agente** que mapea una percepción dada en una acción.

En principio, con tiempo infinito, podemos construir una tabla que tabule cada acción dada una secuencia de percepción.

La tabla es una caracterización externa del agente. Internamente, la **función del agente** para un agente artificial será implementada por un **programa del agente**.

Es importante mantener estas dos ideas distintas.

- La **función del agente** es una descripción matemática abstracta.
- El **programa del agente** es una implementación concreta que se ejecuta dentro de algún sistema físico.

---

## Diapositiva 7: Agentes Racionales

### Agente - Agente aspiradora

![Agente aspiradora](./img/page14_img2.png)

- **Percepción**:
  - Espacio limpio
  - Espacio sucio

- **Acciones**:
  - Mover a la izquierda
  - Mover a la derecha
  - Limpiar el espacio
  - No hacer nada

---

## Diapositiva 8: Agentes Racionales

### Agente - Agente aspiradora

La tabla (de forma parcial) de secuencia de percepción y acción:

| Secuencia de percepción | Acción |
|-------------------------|--------|
| [A, Limpio]             | Derecha |
| [A, Sucio]              | Limpiar |
| [B, Limpio]             | Izquierda |
| [B, Sucio]              | Limpiar |
| [A, Limpio], [A, Limpio] | Derecha |
| [A, Limpio], [A, Sucio] | Limpiar |
| ...                     | ... |
| [A, Limpio], [A, Limpio], [A, Limpio] | Derecha |
| [A, Limpio], [A, Limpio], [A, Sucio] | Limpiar |
| ...                     | ... |

---

## Diapositiva 9: Agentes Racionales

### Agente - Agente aspiradora

Un programa del agente para el ambiente de dos cajas, este programa implementa la tabla:

```python
def REFLEX_VACUUM_AGENT(location, status) -> Action:
    if status == "Dirty":
        return Suck
    elif location == "A":
        return Right
    else: # location == "B"
        return Left 
```

---

## Diapositiva 10: Agentes Racionales

### Medida de rendimiento

Las medidas de rendimiento incluyen los criterios que determinan el éxito en el comportamiento del agente. Estos deben ser objetivos, y en general, determinados por el diseñador.

El ejemplo de la aspiradora se puede proponer utilizar como medida de rendimiento la cantidad de suciedad limpiada en un período de 8 horas.

> Pero ojo, un agente racional puede maximizar esta medida de rendimiento limpiando la suciedad, tirando la basura al suelo, limpiándola de nuevo, y así sucesivamente.

La selección de la medida de rendimiento no es siempre fácil.

![Monkey paw](./img/page10_img1.jpeg)

---

## Diapositiva 11: Agentes Racionales

### Medida de rendimiento

Como regla general, es mejor diseñar medidas de utilidad de acuerdo con lo que se quiere para el entorno, más que de acuerdo con cómo se cree que el agente debe comportarse.

> Por ejemplo, recompensar al agente un punto por cada cuadricula limpia en cada periodo de tiempo.

Pero esto también puede llevarnos a un problema, dado que la noción de limpieza de suelo limpio está basada en un en nivel de limpieza promedio a lo largo del tiempo. Y esto se puede alcanzar:

- Haciendo una limpieza mediocre pero continua
- Limpiando en profundidad, con largos descansos.

La forma más adecuada es una cuestión filosófica.

Medida de rendimiento

![Monkey paw](./img/page10_img1.jpeg)

---

## Diapositiva 12: Agentes Racionales

### Racionalidad

La racionalidad en un momento dado depende de cuatro factores:

- La medida de rendimiento que define el criterio de éxito.
- El conocimiento previo del agente sobre el entorno.
- Las acciones que el agente puede llevar a cabo.
- La secuencia de percepciones del agente hasta este momento.

**Definición de racionalidad**

> En cada posible secuencia de percepciones, un agente racional deberá seleccionar aquella acción que supuestamente maximice su medida de rendimiento, basándose en las evidencias aportadas por la secuencia de percepciones y en el conocimiento que el agente mantiene almacenado.

---

## Diapositiva 13: Agentes Racionales

### Racionalidad

¿La función de la aspiradora es racional?

```python
def REFLEX_VACUUM_AGENT(location, status) -> Action:
    if status == "Dirty":
        return Suck
    elif location == "A":
        return Right
    else: # location == "B"
        return Left 
```

---

## Diapositiva 14: Agentes Racionales

### Racionalidad

¿La función de la aspiradora es racional?

```python
def REFLEX_VACUUM_AGENT(location, status) -> Action:
    if status == "Dirty":
        return Suck
    elif location == "A":
        return Right
    else: # location == "B"
        return Left 
```

![Agente aspiradora](./img/page14_img2.png)

---

## Diapositiva 15: Agentes Racionales

### Racionalidad

*¿La función de la aspiradora es racional?* **Depende**

Asumamos lo siguiente:

- Damos un punto por rendimiento por cada espacio limpio en un tiempo de
vida de 10000 pasos
- Se conoce la geografía del ambiente a “a priori”, pero no la distribución de
suciedad. El espacio una vez que se limpia, se mantiene. Y el movimiento de izquierda y derecha siempre asegura el movimiento correcto.
- Solo tenemos tres acciones disponibles: Derecha, Izquierda y Limpiar.
- El agente siempre percibe correctamente su ubicación y si el piso está sucio.

Bajo estas circunstancias el agente es **racional**.

![Monkey paw](./img/page10_img1.jpeg)

---

## Diapositiva 16: Agentes Racionales

### Racionalidad

*¿La función de la aspiradora es racional?* **Depende**

Pero cambiando un poco las condiciones para que el mismo sea **irracional**:

*Agregamos una medida de penalización de un punto por cada movimiento. Esta función del agente lo deja oscilando.*

- Una solución mejor es para a la aspiradora cuando termina de aspirar, algo que implica memoria.
- Si el piso se puede volver a ensuciar, se puede realizar rutinas de chequeo.
- Si la geografía no se encuentra, el agente necesita explorar mediante algún *algoritmo de búsqueda*.

---

## Diapositiva 17: Agentes Racionales

### Especificación del entorno de trabajo

En el ejemplo de racionalidad de una agente aspiradora, hubo que especificar las medidas de rendimiento, el entorno, y los actuadores y sensores del agente.

Todo ello forma lo que se llama el entorno de trabajo, cuya denominación es **PEAS**:

- Sensors
- Actuators
- Environment
- Performance

---

## Diapositiva 18: Agentes Racionales

### Especificación del entorno de trabajo

| Agente | Performance | Environment | Actuators | Sensors |
|---|---|---|---|---|
| Sistema de diagnóstico medico | Paciente sano, reducir costos | Paciente, personal del hospital | Display de preguntas, test, diagnosis y tratamientos | Pantalla táctil/entrada por voz |
| Sistema de análisis de imágenes de satélite | Categorización correcta de objetos, terreno | Satélite en órbita, enlace, clima | Visualización de categorización de escenas | Cámara digital de alta resolución |
| Robot levanta piezas | Porcentaje de piezas en contenedores correctos | Cinta transportadora con piezas, Contenedores | Brazo y mano articulados | Sensores de cámara, táctiles y de ángulo articular |

---

## Diapositiva 19: Agentes Racionales

### Propiedades del entorno de trabajo

Veamos algunas dimensiones que podemos categorizar a los entornos:

- Totalmente observable vs. parcialmente observable
- Deterministas vs. Estocástico
- Episódico vs. Secuencial
- Estático vs. Dinámico
- Discreto vs. Continuo
- Agente individual vs. Multiagente (competitivo o cooperativo)

---

## Diapositiva 20: Agentes Racionales

### Propiedades del entorno de trabajo

**Totalmente observable vs. parcialmente observable**

![Totalmente observable vs. parcialmente observable](./img/page20_img2.jpeg)

---

## Diapositiva 21: Agentes Racionales

### Propiedades del entorno de trabajo

Veamos algunas dimensiones que podemos categorizar a los entornos:

- Totalmente observable vs. parcialmente observable
- Deterministas vs. Estocástico
- Episódico vs. Secuencial
- Estático vs. Dinámico
- Discreto vs. Continuo
- Agente individual vs. Multiagente (competitivo o cooperativo)

---

## Diapositiva 21: Agentes Racionales

### Propiedades del entorno de trabajo

**Episódico vs. Secuencial**

![Episódico vs. Secuencial](./img/page22_img2.jpeg)

---

## Diapositiva 23: Agentes Racionales

### Propiedades del entorno de trabajo

Veamos algunas dimensiones que podemos categorizar a los entornos:

- Totalmente observable vs. parcialmente observable
- Deterministas vs. Estocástico
- Episódico vs. Secuencial
- Estático vs. Dinámico
- Discreto vs. Continuo
- Agente individual vs. Multiagente (competitivo o cooperativo)

---

## Diapositiva 24:Agentes Racionales

### Propiedades del entorno de trabajo

**Discreto vs. Continuo**

![Discreto vs. Continuo](./img/page24_img2.jpeg)

---

## Diapositiva 25: Agentes Racionales

### Propiedades del entorno de trabajo

Veamos algunas dimensiones que podemos categorizar a los entornos:

- Totalmente observable vs. parcialmente observable
- Deterministas vs. Estocástico
- Episódico vs. Secuencial
- Estático vs. Dinámico
- Discreto vs. Continuo
- Agente individual vs. Multiagente (competitivo o cooperativo)

---

## Diapositiva 26: Agentes Racionales

### Propiedades del entorno de trabajo

**Agente individual vs. Multiagente (competitivo o cooperativo)**

Veamos algunas dimensiones que podemos categorizar a los entornos:

![Agente individual vs. Multiagente ](./img/page26_img2.jpeg)

---

## Diapositiva 27: Programa de los agentes

Portada de sección

---

## Diapositiva 28: Programa de los agentes

Veamos diferentes programas de agentes:

- Agentes reactivos simples
- Agentes reactivos basados en modelos
- Agentes basados en objetivos
- Agentes basados en utilidad
- Agentes que aprenden

---

## Diapositiva 29: Programa de los agentes

### Agentes reactivos simples

```python
def simple_reflex_agent_program(rules, interpret_input):

    def program(percept):
        state = interpret_input(percept)
        rule = rule_match(state, rules)
        action = rule.action
        return action
    
    return program
```

![Agentes reactivos simples](./img/page29_img1.png)

---

## Diapositiva 30: Programa de los agentes

### Agentes reactivos basados en modelos

```python
def model_based_reflex_agent_program(rules, update_state, model):
    def program(percept):
        program.state = update_state(program.state, 
                                     program.action, 
                                     percept, 
                                     model)
        rule = rule_match(program.state, rules)
        action = rule.action
        program.action = action
        
        return action
    
    program.state = program.action = None
    
    return program
```

![Agentes reactivos basados en modelos](./img/page30_img1.png)

---

## Diapositiva 31: Programa de los agentes

### Agentes basados en objetivos

![Agentes basados en objetivos](./img/page31_img1.png)

---

## Diapositiva 32: Programa de los agentes

### Agentes basados en utilidad

![Agentes basados en objetivos](./img/page32_img1.png)

---

## Diapositiva 33: Programa de los agentes

### Agentes que aprenden

![Agentes que aprenden](./img/page33_img1.png)

---

## Diapositiva 34: Resolución de problemas mediante búsqueda

Portada de sección

---

## Diapositiva 35: Resolución de problemas mediante búsqueda

### Agentes de resolución de problemas

Cuando la acción correcta a tomar no es inmediatamente obvia, un agente puede necesitar planificar con anticipación: considerar una secuencia de acciones que formen un camino hacia un estado objetivo. A dicho agente se le llama **agente de resolución de problemas** y el proceso computacional que lleva a cabo se llama **búsqueda**.

Para estos métodos de búsquedas, se considera sólo los entornos más simples: *episódico, de agente único, totalmente observable, determinista, estático, discreto y conocido*.

Dado estas condiciones, el agente puede llevar un proceso de 4 fases:

- **Formulación de objetivo**: El agente adopta el objetivo basado en la situación actual y la medida de rendimiento del agente.
- **Formulación del problema**: El agente diseña una descripción de los estados y acciones necesarias para alcanzar el objetivo: un modelo abstracto de la parte relevante del entorno.
- **Búsqueda**: Antes de realizar cualquier acción en el mundo real, el agente simula secuencias de acciones en su modelo, buscando hasta encontrar una secuencia de acciones que alcance el objetivo. Esta secuencia se llama solución.
- **Ejecución**: El agente ahora puede ejecutar las acciones de la solución, de a un paso por vez.

---

## Diapositiva 36: Resolución de problemas mediante búsqueda

### Problemas de búsquedas y soluciones

Un problema de búsqueda puede ser definido formalmente como:
- Un conjunto de estados posibles en los que puede estar el entorno, llamado **espacio de estados**.
- El **estado inicial** en que el agente comienza.
- Un set de uno o más **estados objetivos**.
- Las **acciones** disponibles al agente. Dado un estado `s`, `ACTIONS(s)` retorna un numero finito de acciones que puede ejecutarse en `s`. Decimos que cada una de estas acciones es *aplicable* en `s`.
- Un **modelo de transición**, que describe lo que hace cada acción. `RESULT(s,a)` devuelve el estado que resulta de realizar la acción `a` en el estado `s`.
- Una **función de costo de acción** (`ACTION-COST(s, a, s’)`) que nos devuelva un número que denote el costo de aplicar una acción `a` a un estado `s` para llegar al estado `s’`.
- Una secuencia de acción forma un **camino**, y una **solución** es el camino del estado inicial a un estado objetivo.
- Si asumimos el costo es aditivo y positivo, el costo total es la suma del costo de cada acción. **Una solución óptima** es aquella que el costo es **mínimo**.

---

## Diapositiva 37: Torre de Hanoi

Portada de sección

![Torre de Hanoi](./img/page37_img1.jpeg)

---

## Diapositiva 38: Torre de Hanoi

Pongámonos místicos…

> Cuenta la leyenda que unos brahmanes en un templo de Benarés han estado realizando el movimiento de la "Torre Sagrada de Brahma” sin parar desde hace siglos, la torre está formada por sesenta y cuatro discos de oro, y los movimientos obedecen a las siguientes místicas reglas:
> 1. Sólo se puede mover un disco a la vez.
> 2. Cada movimiento consiste en recoger el disco superior de una de las pilas y colocarlo encima de otra pila o sobre una varilla vacía.
> 3. Ningún disco podrá colocarse encima de un disco que sea más pequeño que él.
> Una vez que finalicen la torre, va a llegar el fin del mundo.

![Templo mistico de Benarés](./img/page38_img1.jpeg)

---

## Diapositiva 39: Torre de Hanoi

![Torre de Hanoi](./img/page37_img1.jpeg)

La Torre de Hanói es un rompecabezas inventado en 1883 por el matemático francés **Édouard Lucas**.

El rompecabezas comienza con los discos apilados en una varilla en orden de tamaño decreciente, el más pequeño en la parte superior, aproximándose así a una forma cónica.

El objetivo del rompecabezas es mover toda la pila a una de las otras barras, con las reglas de la leyenda:

1. Sólo se puede mover un disco a la vez.
2. Cada movimiento consiste en recoger el disco superior de una de las pilas y colocarlo encima de otra pila o sobre una varilla vacía.
3. Ningún disco podrá colocarse encima de un disco que sea más pequeño que él.

---

## Diapositiva 40: Torre de Hanoi

### Resolviendo este problema usando IA

Este problema es un típico problema para aplicar métodos de búsquedas. Podemos crear un agente que pueda resolver este problema.

Limitemos a 5 discos, *salvo que quieran usar 64 discos como los brahmanes*.

El agente puede percibir cuantos discos y en qué orden hay en cada varilla. Además, puede tomar cualquier disco que se encuentre en la parte superior y moverlo a cualquier otra varilla que este permitido moverlo.

---

## Diapositiva 41: Torre de Hanoi

### Resolviendo este problema usando IA

Definamos el problema con las características que vimos:

**Espacio de estados**: Para 5 discos, tenemos $3^5 = 243$ posibles estados.


![Estado inicial](./img/page41_img1.png)

![Estado final](./img/page41_img2.png)

![Estado 1](./img/page41_img3.png)

![Estado 2](./img/page41_img4.png)

---

## Diapositiva 42: Torre de Hanoi

### Resolviendo este problema usando IA

Definamos el problema con las características que vimos:

**Estado inicial:**:

![Estado inicial](./img/page41_img1.png)

**Estado objetivo**: Para simplificar, vamos a tener un solo estado objetivo de los dos posibles.

![Estado final](./img/page41_img2.png)

---

## Diapositiva 43: Torre de Hanoi

### Resolviendo este problema usando IA

Definamos el problema con las características que vimos:

- **Acciones**: `ACTIONS(s)`, por ejemplo, para el siguiente estado, tenemos las siguientes acciones:

| Disco | Acción |
|---|---|
| -- | No hacer nada |
| Amarillo | Mover a la varilla derecha |
| Verde | Mover a la varilla del medio |
| Verde | Mover a la varilla derecha |


![Imagen de la diapositiva 43](./img/page43_img1.png)

---

## Diapositiva 44: Torre de Hanoi

### Resolviendo este problema usando IA

Definamos el problema con las características que vimos:

- **Modelo de transición**: `RESULT(s,a)`,  por ejemplo:

| Disco | Acción |
|---|---|
| -- | No hacer nada |
| Amarillo | Mover a la varilla derecha |
| Verde | Mover a la varilla del medio |
| **Verde** | **Mover a la varilla derecha** |

*Antes*:
![Estado anterior](./img/page41_img3.png)   

*Después* al aplicar la acción *Disco Verde - Mover a la varilla derecha*:
![Estado posterior](./img/page44_img2.png)

---

## Diapositiva 45: Torre de Hanoi

### Resolviendo este problema usando IA

Definamos el problema con las características que vimos:

- **Función de costo de acción** (`ACTION-COST(s, a, s’)`). Mover un disco de una varilla a otra, siempre que sea un movimiento permitido, cuesta lo mismo, que podemos definir como 1.


---

## Diapositiva 46: Torre de Hanoi

### Grafo de estados

![Grafo de estados](./img/page46_img1.png)

---

## Diapositiva 47: Algortimos de búsqueda

Portada de sección

---

## Diapositiva 48: Algortimos de búsqueda

### Árbol de búsqueda

Un algoritmo de búsqueda toma un **problema de búsqueda** como entrada y retorna una **solución**, o una indicación de falla.

Vamos a considerar únicamente, a modo de cortar un tema inmenso, a solo aquello que superponen un **árbol de búsqueda** sobre el **grafo de espacios de estados**. La idea es buscar un camino que llegue al estado objetivo.

Cada **nodo** del árbol corresponde a un **estado** y las **aristas** corresponde a una **acción**.

Importante, el árbol **NO** es el grafo de estados. El grafo describe todo el set de estados, y las acciones que llevan de un lado a otro.

El árbol describe el camino entre estos estados, para alcanzar el objetivo.

---

## Diapositiva 49: Algortimos de búsqueda

### Árbol de búsqueda

![Árbol de búsqueda](./img/page49_img1.png)

---

## Diapositiva 50: Algortimos de búsqueda

### Árbol de búsqueda

La frontera separa dos regiones del grafo, aquella que ya fue explorada por el algoritmo y aquella que no.

![Frontera](./img/page50_img1.png)

---

## Diapositiva 51: Algortimos de búsqueda

### Árbol de búsqueda – Estructura de datos

Para poder aplicar los algoritmos, debemos definir la estructura de datos para hacer seguimiento del árbol. Los **nodos** del árbol son representados con los siguientes componentes:

- `STATE`: El estado, del espacio de estados, que corresponde el nodo.
- `NODE PARENT`: El nodo en el árbol de búsqueda que ha generado al nodo.
- `ACTION`: La acción que se aplicará al padre para generar el nodo.
- `PATH-COST`: El costo `g(n)` de un camino desde el nodo inicial al nodo.

---

## Diapositiva 52: Algortimos de búsqueda

### Árbol de búsqueda – Estructura de datos

Necesitamos una estructura para la frontera. Seleccionamos una **cola**, porque las operaciones en la frontera son:

- `IS-EMPTY(FRONTIER)`: Retorna `True` si no hay nodos en la frontera.
- `POP(FRONTIER)`: Quita el primer nodo en la cola.
- `TOP(FRONTIER)`: Devuelve, pero no quita al primer nodo en la cola
- `ADD(FRONTIER)`: Inserta el nodo en su correspondiente lugar de la cola

---

## Diapositiva 53: Algortimos de búsqueda

### Árbol de búsqueda – Estructura de datos

Tres tipos de colas se usan en los algoritmos, los cuales nos pueden dar diferentes tipos de resultados:

- Una **cola FIFO** (primero entra, primero sale) que toma los nodos
en el mismo modo que se agregan.

![cola FIFO](./img/page53_img1.png)

- Una **cola LIFO** (último en salir, sale primero… o **stack**) quita el
nodo más reciente.

![cola LIFO](./img/page53_img2.png)

- Una **cola prioritaria** que primer quita nodos con el mínimo costo
de acuerdo con una función de evaluación `f`.

![cola prioritaria](./img/page53_img3.png)

---

## Diapositiva 54: Algortimos de búsqueda

### Midiendo el rendimiento

Para poder evaluar a los algoritmos de búsquedas, debemos usar un criterio para elegir:

- **Completitud**: ¿El algoritmo garantiza encontrar una solución cuando hay una, y correctamente informar cuando no lo haya?
- **Optimización**: ¿encuentra la estrategia la solución óptima, es decir el camino más corto?
- **Complejidad de tiempo**: Cuando tiempo le lleva encontrar la solución.
- **Complejidad de espacio**: Cuanta memoria es necesaria para la búsqueda

---

## Diapositiva 55: Algortimos de búsqueda

Hay múltiples algoritmos de búsqueda, los que veremos hoy son:

- **Algoritmos de búsqueda no informada**
    - **Búsqueda primero en anchura**
    - **Búsqueda de costo uniforme o algoritmo de Dijkstra**
    - **Búsqueda primero en profundidad**
    - **Búsqueda de profundidad limitada**
    - **Búsqueda de profundidad limitada con profundidad iterativa**
- **Algoritmos de búsqueda informada**
    - **Búsqueda voraz (greedy) primero el mejor**
    - **Búsqueda A\***

---

## Diapositiva 56: Algortimos de búsqueda no informada

Portada de sección

---

## Diapositiva 57: Algortimos de búsqueda no informada

### Búsqueda primero en anchura

Es una estrategia sencilla en la que se expande primero el nodo raíz, a continuación, se expanden todos los sucesores del nodo raíz, después sus sucesores, etc. Complejidad: `O(bd+1)`

![arbol_anchura](./img/achura1.png)

Cola FIFO:

![cola_anchura](./img/cola_achura1.png)

---

## Diapositiva 58: Algortimos de búsqueda no informada

### Búsqueda primero en anchura

Es una estrategia sencilla en la que se expande primero el nodo raíz, a continuación, se expanden todos los sucesores del nodo raíz, después sus sucesores, etc. Complejidad: `O(bd+1)`

![arbol_anchura](./img/achura1.png)

Cola FIFO:

![cola_anchura](./img/cola_achura2.png)

---

## Diapositiva 59: Algortimos de búsqueda no informada

### Búsqueda primero en anchura

Es una estrategia sencilla en la que se expande primero el nodo raíz, a continuación, se expanden todos los sucesores del nodo raíz, después sus sucesores, etc. Complejidad: `O(bd+1)`

![arbol_anchura](./img/achura2.png)

Cola FIFO:

![cola_anchura](./img/cola_achura3.png)

---

## Diapositiva 60: Algortimos de búsqueda no informada

### Búsqueda primero en anchura

Es una estrategia sencilla en la que se expande primero el nodo raíz, a continuación, se expanden todos los sucesores del nodo raíz, después sus sucesores, etc. Complejidad: `O(bd+1)`

![arbol_anchura](./img/achura3.png)

Cola FIFO:

![cola_anchura](./img/cola_achura4.png)

---

## Diapositiva 61: Algortimos de búsqueda no informada

### Búsqueda primero en anchura

Es una estrategia sencilla en la que se expande primero el nodo raíz, a continuación, se expanden todos los sucesores del nodo raíz, después sus sucesores, etc. Complejidad: `O(bd+1)`

![arbol_anchura](./img/achura4.png)

Cola FIFO:

![cola_anchura](./img/cola_achura5.png)

---

## Diapositiva 62: Algortimos de búsqueda no informada

### Búsqueda de costo uniforme o algoritmo de Dijkstra

En vez de expandir el nodo más superficial, la búsqueda de costo uniforme expande el nodo con el camino de costo más pequeño. **Si todos los costos son iguales, es idéntico a la búsqueda primero en anchura.**

Para que funcione todos los caminos deben tener un costo positivo y mayor que cero, sino puede entrar en bucles infinitos.

Este método de búsqueda expande los caminos más cortos y luego los más grandes.

---

## Diapositiva 63: Algortimos de búsqueda no informada

### Búsqueda de costo uniforme o algoritmo de Dijkstra

![grafo Dijkstra](./img/dgrafo1.png)

Cola prioritaria

![cola Dijkstra](./img/dcola1.png)

Árbol

![arbol Dijkstra](./img/darbol1.png)
---

## Diapositiva 64: Algortimos de búsqueda no informada

### Búsqueda de costo uniforme o algoritmo de Dijkstra

![grafo Dijkstra](./img/dgrafo2.png)

Cola prioritaria

![cola Dijkstra](./img/dcola2.png)

Árbol

![arbol Dijkstra](./img/darbol2.png)

---

## Diapositiva 65: Algortimos de búsqueda no informada

### Búsqueda de costo uniforme o algoritmo de Dijkstra

![grafo Dijkstra](./img/dgrafo3.png)

Cola prioritaria

![cola Dijkstra](./img/dcola3.png)

Árbol

![arbol Dijkstra](./img/darbol3.png)

---

## Diapositiva 66: Algortimos de búsqueda no informada

### Búsqueda de costo uniforme o algoritmo de Dijkstra

![grafo Dijkstra](./img/dgrafo4.png)

Cola prioritaria

![cola Dijkstra](./img/dcola4.png)

Árbol

![arbol Dijkstra](./img/darbol4.png)

---

## Diapositiva 67: Algortimos de búsqueda no informada

### Búsqueda de costo uniforme o algoritmo de Dijkstra

![grafo Dijkstra](./img/dgrafo5.png)

Cola prioritaria

![cola Dijkstra](./img/dcola5.png)

Árbol

![arbol Dijkstra](./img/darbol5.png)

---

## Diapositiva 68: Algortimos de búsqueda no informada

### Búsqueda de costo uniforme o algoritmo de Dijkstra

![grafo Dijkstra](./img/dgrafo6.png)

Cola prioritaria

![cola Dijkstra](./img/dcola6.png)

Árbol

![arbol Dijkstra](./img/darbol6.png)

---

## Diapositiva 69: Algortimos de búsqueda no informada

### Búsqueda de costo uniforme o algoritmo de Dijkstra

![grafo Dijkstra](./img/dgrafo7.png)

Cola prioritaria

![cola Dijkstra](./img/dcola6.png)

Árbol

![arbol Dijkstra](./img/darbol6.png)

---

## Diapositiva 70: Algortimos de búsqueda no informada

### Búsqueda primero en profundidad

Expande el nodo más profundo en la frontera actual del árbol de búsqueda. Cuando esos nodos se expanden, son quitados de la frontera, así entonces la búsqueda **retrocede** al siguiente nodo más superficial.

No encuentra la solución más eficiente, pero consume muy poca memoria `O(bm)`, y el tiempo es proporcional a la cantidad de estados

---

## Diapositiva 71: Algortimos de búsqueda no informada

### Búsqueda primero en profundidad

![arbol primero en profundidad](./img/profundida1.png)

Cola LIFO:

![cola primero en profundidad](./img/cola_profundida1.png)

---

## Diapositiva 72: Algortimos de búsqueda no informada

### Búsqueda primero en profundidad

![arbol primero en profundidad](./img/profundida2.png)

Cola LIFO:

![cola primero en profundidad](./img/cola_profundida2.png)

---

## Diapositiva 73: Algortimos de búsqueda no informada

### Búsqueda primero en profundidad

![arbol primero en profundidad](./img/profundida3.png)

Cola LIFO:

![cola primero en profundidad](./img/cola_profundida3.png)

---

## Diapositiva 74: Algortimos de búsqueda no informada

### Búsqueda primero en profundidad

![arbol primero en profundidad](./img/profundida4.png)

Cola LIFO:

![cola primero en profundidad](./img/cola_profundida4.png)

---

## Diapositiva 75: Algortimos de búsqueda no informada

### Búsqueda primero en profundidad

![arbol primero en profundidad](./img/profundida5.png)

Cola LIFO:

![cola primero en profundidad](./img/cola_profundida5.png)

---

## Diapositiva 76: Algortimos de búsqueda no informada

### Búsqueda primero en profundidad

![arbol primero en profundidad](./img/profundida6.png)

Cola LIFO:

![cola primero en profundidad](./img/cola_profundida6.png)

---

## Diapositiva 77: Algortimos de búsqueda no informada

### Búsqueda de profundidad limitada

Para los casos de árboles muy grandes o infinitos, se puede limitar la búsqueda en profundidad hasta un cierto nivel. Por ejemplo, si elegimos una profundidad de 2, se llegaría hasta los nodos B y C.

Esto restringe que tan profundo avanza, pero la dificultad está en que se debe elegir la profundidad.

Complejidad en tiempo `O(bl)` y en memoria `O(bl)`

---

## Diapositiva 78: Algortimos de búsqueda no informada

### Búsqueda de profundidad limitada (Limite 2)

![arbol primero en profundidad](./img/profundida1.png)

Cola LIFO:

![cola primero en profundidad](./img/cola_profundida1.png)

---

## Diapositiva 79: Algortimos de búsqueda no informada

### Búsqueda de profundidad limitada (Limite 2)

![arbol primero en profundidad](./img/profundida2.png)

Cola LIFO:

![cola primero en profundidad](./img/cola_profundida2.png)

---

## Diapositiva 80: Algortimos de búsqueda no informada

### Búsqueda de profundidad limitada (Limite 2)

![arbol primero en profundidad](./img/profundiad_lim1.png)

Cola LIFO:

![cola primero en profundidad](./img/cola_profundiad_lim1.png)

---

## Diapositiva 81: Algortimos de búsqueda no informada

### Búsqueda de profundidad limitada (Limite 2)

![arbol primero en profundidad](./img/profundiad_lim2.png)

Cola LIFO:

![cola primero en profundidad](./img/cola_profundida1.png)

---

## Diapositiva 82: Algortimos de búsqueda no informada

### Búsqueda de profundidad limitada con profundidad iterativa

Esta búsqueda es una estrategia que se realiza aumentando la profundidad iterativamente hasta alcanzar la solución. Se parte de un límite de 0, 1, …

> La profundidad iterativa es el método de búsqueda no informada preferido cuando hay un espacio grande de búsqueda y no se conoce la profundidad de la solución.

---

## Diapositiva 83: Algortimos de búsqueda no informada

### Búsqueda de profundidad limitada con profundidad iterativa

Límite = 0

![limite 0](./img/prof_iterativa1.png)

Límite = 1

![limite 1](./img/prof_iterativa2.png)

Límite = 2

![limite 2](./img/prof_iterativa3.png)

---

## Diapositiva 84: Algortimos de búsqueda informada

Portada de la sección

---

## Diapositiva 85: Algortimos de búsqueda informada

### Función heurística

Si tuviéramos alguna forma de saber que tan lejos estamos del objetivo, podríamos hacer una búsqueda más eficiente de la solución más que probar diferentes caminos. 

> El problema es que, para saber la distancia, debemos resolver el problema primero.

Entonces, una forma que podemos resolver esto es usar una estimación que llamamos **función heurística**:

`h(n) = costo estimado del camino más barato del estado del nodo n al estado objetivo`

![serpiente que se muerde la cola](./img/page83_img1.jpeg)

---

## Diapositiva 86: Algortimos de búsqueda informada

### Búsqueda voraz (greedy) primero el mejor

Esta búsqueda trata de expandir el nodo **con el valor más bajo de `h(n)`** (el nodo que parece más cerca del objetivo), alegando que probablemente conduzca rápidamente a una solución.

Esta estrategia no siempre asegura que se encuentre el mejor camino, pero nos permite llegar más rápido a la solución que las búsquedas no informadas.

---

## Diapositiva 87: Algortimos de búsqueda informada

### Búsqueda voraz (greedy) primero el mejor

![grafo greedy](./img/grafo_greedy1.png)

Cola prioritaria

![cola greedy](./img/dcola1.png)

Árbol

![arbol greedy](./img/arbol_greedy1.png)

---

## Diapositiva 88: Algortimos de búsqueda informada

### Búsqueda voraz (greedy) primero el mejor

![grafo greedy](./img/grafo_greedy2.png)

Cola prioritaria

![cola greedy](./img/cola_greedy1.png)

Árbol

![arbol greedy](./img/arbol_greedy2.png)

---

## Diapositiva 89: Algortimos de búsqueda informada

### Búsqueda voraz (greedy) primero el mejor

![grafo greedy](./img/grafo_greedy3.png)

Cola prioritaria

![cola greedy](./img/cola_greedy2.png)

Árbol

![arbol greedy](./img/arbol_greedy3.png)

---

## Diapositiva 90: Algortimos de búsqueda informada

### Búsqueda voraz (greedy) primero el mejor

![grafo greedy](./img/grafo_greedy4.png)

Cola prioritaria

![cola greedy](./img/cola_greedy3.png)

Árbol

![arbol greedy](./img/arbol_greedy4.png)

---

## Diapositiva 91: Algortimos de búsqueda informada

### Búsqueda voraz (greedy) primero el mejor

![grafo greedy](./img/grafo_greedy5.png)

Cola prioritaria

![cola greedy](./img/dcola1.png)

Árbol

![arbol greedy](./img/arbol_greedy5.png)

---

## Diapositiva 90: ALGORITMOS DE BÚSQUEDA INFORMADA

Búsqueda A*

Esta búsqueda no solo usa la función heurística, sino también utiliza el costo del camino tomado para llegar al nodo:

f(nodo) = costo(nodo) + h(nodo)

Si todos los costos son >0, se asegura que la búsqueda es completa. Encontrar la solución más eficiente depende de si

la función heurística nunca sobreestima el costo de llegar al resultado (admisible).

Además, si la función heurística es consistente:

h(nodo1) < costo(nodo1, acción, nodo2) + h(nodo2)

Entonces A* cada nodo al que llegue siempre va a ser el camino más optimo.

nodo1

nodo2

nodo3

h(nodo1)

h(nodo2)

costo(nodo1, acción, nodo2)


---

## Diapositiva 91: ALGORITMOS DE BÚSQUEDA INFORMADA

Búsqueda A*

A

B

C

D

F

99

E

211

80

146

97

138

101

253

193

176

100

160

273

275

386

277

310

Cola prioritaria

Árbol

A


---

## Diapositiva 92: ALGORITMOS DE BÚSQUEDA INFORMADA

Búsqueda A*

A

B

C

D

F

99

E

211

80

146

97

138

101

253

193

176

100

160

273

275

386

277

310

B

275

C

273

Cola prioritaria

Árbol

A

B

C


---

## Diapositiva 93: ALGORITMOS DE BÚSQUEDA INFORMADA

Búsqueda A*

A

B

C

D

F

99

E

211

80

146

97

138

101

253

193

176

100

160

273

275

386

277

310

B

275

E

386

D

277

Cola prioritaria

Árbol

A

B

C

E

D


---

## Diapositiva 94: ALGORITMOS DE BÚSQUEDA INFORMADA

Búsqueda A*

A

B

C

D

F

99

E

211

80

146

97

138

101

253

193

176

100

160

273

275

386

277

310

F

310

E

386

D

277

Cola prioritaria

Árbol

A

B

C

F

E

D


---

## Diapositiva 95: ALGORITMOS DE BÚSQUEDA INFORMADA

Búsqueda A*

A

B

C

D

F

99

E

211

80

146

97

138

101

253

193

176

100

160

273

275

386

277

310

278

F

310

E

386

F

278

Cola prioritaria

Árbol

A

B

C

F

E

D

F

E


---

## Diapositiva 96: ALGORITMOS DE BÚSQUEDA INFORMADA

Búsqueda A*

A

B

C

D

F

99

E

211

80

146

97

138

101

253

193

176

100

160

273

275

386

277

310

278

F

310

E

386

F

278

Cola prioritaria

Árbol

A

B

C

F

E

D

F

E


---

## Diapositiva 97: ALGORITMOS DE BÚSQUEDA INFORMADA

Búsqueda A*

A

B

C

D

F

99

E

211

80

146

97

138

101

253

193

176

100

160

273

275

386

277

310

278

Árbol

A

B

C

F

E

D

F

E


