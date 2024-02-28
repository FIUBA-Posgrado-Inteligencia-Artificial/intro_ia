from collections import deque
import tree_hanoi


def breadth_first_tree_search(problem: tree_hanoi.ProblemHanoi) -> tree_hanoi.NodeHanoi:
    """
    Realiza una búsqueda en anchura para encontrar una solución a un problema de Hanoi.

    Parameters:
        problem (tree_hanoi.ProblemHanoi): El problema de la Torre de Hanoi a resolver.

    Returns:
        tree_hanoi.NodeHanoi: El nodo que contiene la solución encontrada.
    """
    node = None
    frontier = deque([tree_hanoi.NodeHanoi(problem.initial)])  # Creamos una cola FIFO con el nodo inicial
    while frontier:
        node = frontier.popleft()  # Extraemos el primer nodo de la cola
        if problem.goal_test(node.state):  # Comprobamos si hemos alcanzado el estado objetivo
            return node
        frontier.extend(node.expand(problem))  # Agregamos a la cola todos los nodos sucesores del nodo actual

    return node


def breadth_first_tree_search_with_memory(problem: tree_hanoi.ProblemHanoi) -> tree_hanoi.NodeHanoi:
    """
    Realiza una búsqueda en anchura para encontrar una solución y memoria para evitar estados repetidos.

    Parameters:
        problem (tree_hanoi.ProblemHanoi): El problema de la Torre de Hanoi a resolver.

    Returns:
        tree_hanoi.NodeHanoi: El nodo que contiene la solución encontrada.
    """
    big_list_of_states = []  # Lista para almacenar los hashes de los estados visitados
    node = None
    frontier = deque([tree_hanoi.NodeHanoi(problem.initial)])  # Creamos una cola FIFO con el nodo inicial
    counter = 0
    while frontier:
        node = frontier.popleft()  # Extraemos el primer nodo de la cola
        if hash(node) in big_list_of_states:  # Comprobamos si el estado ya ha sido visitado
            continue
        big_list_of_states.append(hash(node))  # Agregamos el hash del estado a la lista de estados visitados
        counter += 1

        if problem.goal_test(node.state):  # Comprobamos si hemos alcanzado el estado objetivo
            return node
        frontier.extend(node.expand(problem))  # Agregamos a la cola todos los nodos sucesores del nodo actual

    return node
