# Implementación de Torre de Hanoi

Este código presenta la implementación del problema de la torre de Hanoi desarrollada en Python (>=3.8), tal como fue vista en clase. Aquí daremos una breve introducción de lo que hay en cada archivo. Aunque el código se puede usar sin entender la implementación exacta de cada parte, se invita al alumno a ver el código para ayudarlo en su aprendizaje de Python.

La implementación está separada en varios archivos:

- `main.py`: El script principal donde se genera el problema y se resuelve mediante un método de búsqueda
- `hanoi_states.py`: Libreria que contiene el problema de Hanoi y la definición del problema, de la clase que se usa 
para guardar los estados y la clase que se usa para guardar las acciones.
- `tree_hanoi.py`: Libreria que contiene los elementos necesarios para la construcción del arbol de búsqueda 
(únicamente la clase que permite construir los nodos)
- `search.py`: Libreria que contiene los algoritmos de búsqueda. Aquí solo se encuentra la implementación de búsqueda 
en anchura primero vista en clase.
- `aima.py`: Libreria con código del libro Artificial Intelligence: A Modern Approach - Stuart Russell, Peter Norvig. 
Usamos a las clases definidas aquí como padre de las clases definidas para el problema de Hanoi. El repositorio origen 
es [https://github.com/aimacode/aima-python](https://github.com/aimacode/aima-python)

## Definición de algunas clases y funciones:

### hanoi_states.py
#### StatesHanoi

Representa un estado posible de ubicación de discos de la Torre de Hanoi.

```Python
class StatesHanoi:
    """
    # Argumentos
        rod1 (Lista): Discos en la primera varilla.
        rod2 (Lista): Discos en la segunda varilla.
        rod3 (Lista): Discos en la tercera varilla.
        max_disks (int): Máximo número de discos permitidos, por defecto es 5.
        cost (float): Costo asociado al estado, el costo es cuantos movimientos de discos se efectuaron hasta llegar a este estado, por defecto es 0.
    
    # Atributos
        self.rods = [rod1, rod2, rod3]
        self.number_of_disks = max_disks
        self.number_of_pegs = 3
        self.accumulated_cost = cost
    """
    def get_last_disk_rod(number_rod):
        """
        Obtiene el último disco de una varilla específica.
        """

    def check_valid_disk_in_rod(number_rod, disk):
        """
        Comprueba si es válido colocar un disco en una varilla específica.
        """

    def put_disk_in_rod(number_rod, disk):
        """
        Coloca un disco en una varilla específica.
        """
        
    def accumulate_cost(cost):
        """
        Acumula el costo asociado al estado.
        """
        
    def get_state_dict():
        """
        Obtiene una representación del estado de Hanoi como un diccionario.
        """
```

Ejemplo de uso,

```Python
initial_state = StatesHanoi([5, 4, 3, 2, 1], [], [], max_disks=5)
```

Esta clase además tiene implementado diferentes operadores que nos permiten trabajar con la clase:

```Python
# Podemos imprimir un objeto de la clase
print(state)
# Imprime: HanoiState: 5 4 3 | 2 | 1

# Podemos comparar si dos estados son iguales (son iguales si los discos están en las mismas posiciones, sin importar 
# el costo)
state1 == state2 

# Podemos ver si un estado es mayor al otro, para ello tiene en cuenta el costo acumulado
state1 < state2

# Podemos obtener el hash del objeto
hash(state)
```

#### ActionHanoi

Representa una acción en el problema de la Torre de Hanoi.

```Python
class ActionHanoi:
    """
    # Argumentos
        disk (int): Número del disco.
        rod_input (int): Índice de la varilla de entrada.
        rod_out (int): Índice de la varilla de salida.
    
    # Atributos
        self.disk = disk
        self.rod_input = rod_input
        self.rod_out = rod_out
        self.action_dict # Diccionario con la acción
        self.cost # Valor del costo de realizar la acción
    """
    def execute(StatesHanoi):
        """
        Ejecuta la acción en un estado de Hanoi dado.
        """
```

Ejemplo de uso,

```Python
initial_state = StatesHanoi([5, 4, 3, 2, 1], [], [], max_disks=5)
# Imprime: HanoiState: 5 4 3 2 1 | |
print(initial_state)

action = ActionHanoi(disk=1, rod_input=1, rod_out=2)

new_state = action.execute(initial_state)

# Imprime: HanoiState: 5 4 3 2 | 1 |
print(new_state)
```

#### ProblemHanoi

Clase que define el problema de la Torre de Hanoi. Hereda de la clase aima.Problem.

```Python
class ProblemHanoi(aima.Problem):
    """
    # Argumentos
        initial (StatesHanoi): El estado inicial del problema.
        goal (StatesHanoi): El estado objetivo del problema.
    
    # Atributos
        self.initial (StatesHanoi): El estado inicial del problema.
        self.goal (StatesHanoi): El estado objetivo del problema.
    """
    def actions(StatesHanoi):
        """
        Devuelve una lista con todas las acciones posibles que se pueden ejecutar desde un estado dado.
        """
    def result(StatesHanoi, ActionHanoi):
        """
        Calcula el nuevo estado después de aplicar una acción.
        """
    def path_cost(self, _, StatesHanoi, ActionHanoi, _):
        """
        Calcula el costo del camino.
        """
    def goal_test(StatesHanoi):
        """
        Revisa si el estado es el estado objetivo
        """
```

Ejemplo de uso,

```Python
initial_state = StatesHanoi([5, 4, 3, 2, 1], [], [], max_disks=5)
goal_state = StatesHanoi([], [], [5, 4, 3, 2, 1], max_disks=5)

problem_hanoi = ProblemHanoi(initial=initial_state, goal=goal_state)

all_actions_from_intial = problem_hanoi.actions(initial_state)
next_state = problem_hanoi.result(initial_state, all_actions_from_intial[0])

# Imprime 1
print(problem_hanoi.path_cost(initial_state, all_actions_from_intial[0]))

# Imprime False
print(problem_hanoi.goal_test(next_state))
```

### tree_hanoi.py
#### NodeHanoi

Clase que define un nodo en el arbol de búsqueda para la Torre de Hanoi. Hereda de la clase aima.Node.

```Python
class NodeHanoi(aima.Node):
    """
    # Argumentos
        state (StatesHanoi): Estado del nodo.
        parent (StatesHanoi | None): Nodo padre.
        action (StatesHanoi | None): Acción realizada para llegar a este nodo.
            
    # Atributos
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost # Costo acumulado para llegar a este nodo
        self.depth # Profundidad del arbol en que se encuentra el nodo
    """
    def child_node(ProblemHanoi, ActionHanoi):
        """
        Genera el nodo hijo a partir de una acción.
        """
        
    def path():
        """
        Retorna una lista con todos los nodos que forma parte del trayecto del root a este nodo.
        """

    def generate_solution_for_simulator(initial_state_file, sequence_file):
        """
        Genera los archivos JSON para el simulador de la Torre de Hanoi. Para obtener el estado inicial, encuentra 
        quien es el root del arbol, y para la secuencia obtiene el listado de acciones desde el root hasta este nodo.
        """
```

Ejemplo de uso,

```Python
initial_state = StatesHanoi([5, 4, 3, 2, 1], [], [], max_disks=5)
goal_state = StatesHanoi([], [], [5, 4, 3, 2, 1], max_disks=5)
problem_hanoi = ProblemHanoi(initial=initial_state, goal=goal_state)

# Creamos el nodo raíz
initial_node = NodeHanoi(state=initial_state, parent=None, action=None)

action = ActionHanoi(disk=1, rod_input=1, rod_out=2)

# Creamos el siguiente nodo, este tiene como padre al nodo raíz. Tiene un costo de 1 (se movio un disco desde el 
# principio y el path es initial_node -> next_node
next_node = initial_node.child(problem_hanoi, action)
```

### search.py
#### breadth_first_graph_search

Implementación del algoritmo de búsqueda en anchura primero para encontrar una solución al problema de Hanoi. Esta 
función recuerda si ya paso por un estado e ignora seguir buscando en ese nodo para evitar recursividad.

Para entender como es el algoritmo, ver la clase teórica.

Ejemplo de uso,

```Python
initial_state = StatesHanoi([5, 4, 3, 2, 1], [], [], max_disks=5)
goal_state = StatesHanoi([], [], [5, 4, 3, 2, 1], max_disks=5)
problem_hanoi = ProblemHanoi(initial=initial_state, goal=goal_state)

# Aplicamos la búsqueda
breadth_first_graph_search(problem_hanoi)
```
