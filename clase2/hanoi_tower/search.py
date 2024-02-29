from collections import deque
import tree_hanoi
import hanoi_states


def breadth_first_tree_search(problem: hanoi_states.ProblemHanoi):
    """
    Realiza una búsqueda en anchura para encontrar una solución a un problema de Hanoi.
    Esta función no chequea si un estado se visito, por lo que puede entrar en Loop infinitos muy fácilmente. No
    usarla con más de 3 discos.

    Parameters:
        problem (hanoi_states.ProblemHanoi): El problema de la Torre de Hanoi a resolver.

    Returns:
        tree_hanoi.NodeHanoi: El nodo que contiene la solución encontrada.
    """
    frontier = deque([tree_hanoi.NodeHanoi(problem.initial)])  # Creamos una cola FIFO con el nodo inicial
    while frontier:
        node = frontier.popleft()  # Extraemos el primer nodo de la cola
        if problem.goal_test(node.state):  # Comprobamos si hemos alcanzado el estado objetivo
            return node
        frontier.extend(node.expand(problem))  # Agregamos a la cola todos los nodos sucesores del nodo actual

    return None


def breadth_first_graph_search(problem: hanoi_states.ProblemHanoi, display: bool = False):
    """
    Realiza una búsqueda en anchura para encontrar una solución a un problema de Hanoi. Pero ahora si recuerda si ya
    paso por un estado e ignora seguir buscando en ese nodo para evitar recursividad.

    Parameters:
        problem (hanoi_states.ProblemHanoi): El problema de la Torre de Hanoi a resolver.
        display (bool, optional): Muestra un mensaje de cuantos caminos se expandieron y cuantos quedaron sin expandir.
                                  Por defecto es False.

    Returns:
        tree_hanoi.NodeHanoi: El nodo que contiene la solución encontrada.
    """

    frontier = deque([tree_hanoi.NodeHanoi(problem.initial)])  # Creamos una cola FIFO con el nodo inicial

    explored = set()  # Este set nos permite ver si ya exploramos un estado para evitar repetir indefinidamente
    while frontier:
        node = frontier.popleft()  # Extraemos el primer nodo de la cola

        # Agregamos nodo al set. Esto evita guardar duplicados, porque set nunca tiene elementos repetidos, esto sirve
        # porque heredamos el método __eq__ en tree_hanoi.NodeHanoi de aima.Node
        explored.add(node.state)

        if problem.goal_test(node.state):  # Comprobamos si hemos alcanzado el estado objetivo
            if display:
                print(len(explored), "caminos se expandieron y", len(frontier), "caminos quedaron en la frontera")
            return node
        # Agregamos a la cola todos los nodos sucesores del nodo actual que no haya visitados
        frontier.extend(child for child in node.expand(problem)
                        if child.state not in explored and child not in frontier)

    return None

