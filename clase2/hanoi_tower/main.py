from hanoi_states import StatesHanoi  # Importa la clase StatesHanoi del módulo hanoi_states
from tree_hanoi import ProblemHanoi  # Importa la clase ProblemHanoi del módulo tree_hanoi
from search import (  # Importa las funciones de búsqueda del módulo search
    breadth_first_tree_search,
    breadth_first_tree_search_with_memory
)


def main():
    """
    Función principal que resuelve el problema de la Torre de Hanoi y genera los JSON para el simulador.
    """
    # Define el estado inicial y el estado objetivo del problema
    initial_state = StatesHanoi([5, 4, 3, 2, 1], [], [], max_disks=5)
    goal_state = StatesHanoi([], [], [5, 4, 3, 2, 1], max_disks=5)

    # Crea una instancia del problema de la Torre de Hanoi
    problem_hanoi = ProblemHanoi(initial=initial_state, goal=goal_state)

    # Resuelve el problema utilizando búsqueda en anchura
    # Esta forma de búsqueda es muy ineficiente, por lo que si deseas probarlo, usa 3 discos o si querés esperar
    # un poco más, 4 discos, pero 5 discos no finaliza nunca.
    # last_node = breadth_first_tree_search(problem_hanoi)

    # Resuelve el problema utilizando búsqueda en anchura, pero con memoria que recuerda caminos ya recorridos.
    last_node = breadth_first_tree_search_with_memory(problem_hanoi)

    # Imprime la longitud del camino de la solución encontrada
    print(f'Longitud del camino de la solución: {last_node.state.accumulated_cost}')

    # Genera los JSON para el simulador
    last_node.generate_solution_for_simulator()


# Sección de ejecución del programa
if __name__ == "__main__":
    main()
