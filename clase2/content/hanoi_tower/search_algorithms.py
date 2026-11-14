"""
Algoritmos de búsqueda para la Torre de Hanoi. Son las mismas implementaciones que se
explican paso a paso en las notebooks 2, 3 y 4, para poder reutilizarlas, por ejemplo,
con el visualizador.

Todas las funciones reciben la cantidad de discos y devuelven una tupla con el último
nodo de la solución (o None si no la encuentran) y un diccionario con métricas.
"""

from aima_libs.aima import PriorityQueue
from aima_libs.hanoi_states import ProblemHanoi, StatesHanoi
from aima_libs.tree_hanoi import NodeHanoi


def create_problem(number_disks: int = 5) -> ProblemHanoi:
    """Crea el problema de la Torre de Hanoi con todos los discos en la primera
    varilla, y el objetivo de llevarlos a la tercera."""
    list_disks = list(range(number_disks, 0, -1))
    initial_state = StatesHanoi(list_disks, [], [], max_disks=number_disks)
    goal_state = StatesHanoi([], [], list_disks, max_disks=number_disks)
    return ProblemHanoi(initial=initial_state, goal=goal_state)


def _metrics(node, node_explored: int, states_visited: int, frontier_size: int):
    """Arma el diccionario de métricas de una búsqueda."""
    return {
        "solution_found": node is not None,
        "nodes_explored": node_explored,
        "states_visited": states_visited,
        "nodes_in_frontier": frontier_size,
        "max_depth": node.depth if node else None,
        "cost_total": node.state.accumulated_cost if node else None,
    }


def breadth_first_search(number_disks: int = 5) -> tuple:
    """Búsqueda primero en anchura: cola FIFO."""
    problem = create_problem(number_disks)
    frontier = [NodeHanoi(problem.initial)]
    explored = set()
    node_explored = 0

    while frontier:
        node = frontier.pop()
        node_explored += 1
        explored.add(node.state)
        if problem.goal_test(node.state):
            return node, _metrics(node, node_explored, len(explored), len(frontier))
        for next_node in node.expand(problem):
            if next_node.state not in explored:
                frontier.insert(0, next_node)

    return None, _metrics(None, node_explored, len(explored), 0)


def depth_first_search(number_disks: int = 5) -> tuple:
    """Búsqueda primero en profundidad: cola LIFO."""
    problem = create_problem(number_disks)
    frontier = [NodeHanoi(problem.initial)]
    explored = set()
    node_explored = 0

    while frontier:
        node = frontier.pop()
        node_explored += 1
        explored.add(node.state)
        if problem.goal_test(node.state):
            return node, _metrics(node, node_explored, len(explored), len(frontier))
        for next_node in node.expand(problem):
            if next_node.state not in explored:
                frontier.append(next_node)

    return None, _metrics(None, node_explored, len(explored), 0)


def best_first_search(number_disks: int, priority) -> tuple:
    """Búsqueda primero el mejor: expande siempre el nodo de la frontera con menor
    valor de `priority`, una función que recibe un nodo."""
    problem = create_problem(number_disks)
    frontier = PriorityQueue(order="min", f=priority)
    frontier.append(NodeHanoi(problem.initial))
    explored = set()
    node_explored = 0

    while len(frontier) != 0:
        _, node = frontier.pop()
        if node.state in explored:
            continue
        node_explored += 1
        explored.add(node.state)
        if problem.goal_test(node.state):
            return node, _metrics(node, node_explored, len(explored), len(frontier))
        for next_node in node.expand(problem):
            if next_node.state not in explored:
                frontier.append(next_node)

    return None, _metrics(None, node_explored, len(explored), 0)


def uniform_cost_search(number_disks: int = 5) -> tuple:
    """Búsqueda de costo uniforme: la prioridad es g(n)."""
    return best_first_search(number_disks, lambda node: node.path_cost)


def depth_limited_search(number_disks: int = 5, limit: int = 31) -> tuple:
    """Búsqueda primero en profundidad que no expande nodos a más de `limit` pasos
    del inicio."""
    problem = create_problem(number_disks)
    frontier = [NodeHanoi(problem.initial)]
    best_depth = {problem.initial: 0}  # Menor profundidad a la que vimos cada estado
    node_explored = 0

    while frontier:
        node = frontier.pop()
        node_explored += 1
        if problem.goal_test(node.state):
            return node, _metrics(node, node_explored, len(best_depth), len(frontier))
        if node.depth < limit:
            for next_node in node.expand(problem):
                if next_node.depth < best_depth.get(next_node.state, limit + 1):
                    best_depth[next_node.state] = next_node.depth
                    frontier.append(next_node)

    return None, _metrics(None, node_explored, len(best_depth), 0)


def iterative_deepening_search(number_disks: int = 5, max_limit: int = 200) -> tuple:
    """Búsqueda de profundidad limitada con límites cada vez más grandes."""
    total_explored = 0
    for limit in range(max_limit + 1):
        node, metrics = depth_limited_search(number_disks, limit)
        total_explored += metrics["nodes_explored"]
        if metrics["solution_found"]:
            metrics["nodes_explored"] = total_explored
            return node, metrics
    return None, _metrics(None, total_explored, 0, 0)


def misplaced_disks(state: StatesHanoi) -> int:
    """Heurística: cantidad de discos que no están en su posición correcta en la
    tercera varilla."""
    correct = 0
    for expected_disk, disk in zip(range(state.number_of_disks, 0, -1), state.rods[2]):
        if disk != expected_disk:
            break
        correct += 1
    return state.number_of_disks - correct


def greedy_search(number_disks: int = 5) -> tuple:
    """Búsqueda voraz: la prioridad es h(n)."""
    return best_first_search(number_disks, lambda node: misplaced_disks(node.state))


def a_star_search(number_disks: int = 5) -> tuple:
    """Búsqueda A*: la prioridad es f(n) = g(n) + h(n)."""
    return best_first_search(
        number_disks, lambda node: node.path_cost + misplaced_disks(node.state)
    )


# Los algoritmos disponibles, por nombre
ALGORITHMS = {
    "BFS": breadth_first_search,
    "DFS": depth_first_search,
    "Costo uniforme": uniform_cost_search,
    "Profundidad iterativa": iterative_deepening_search,
    "Voraz": greedy_search,
    "A*": a_star_search,
}
