import json
import aima
import hanoi_states


class ProblemHanoi(aima.Problem):
    """
    Clase que define el problema de la Torre de Hanoi.

    Attributes:
        initial (hanoi_states.StatesHanoi): El estado inicial del problema.
        goal (hanoi_states.StatesHanoi): El estado objetivo del problema.
    """

    def __init__(self, initial: hanoi_states.StatesHanoi, goal: hanoi_states.StatesHanoi):
        """
        Inicializa el problema de la Torre de Hanoi.

        Args:
            initial (hanoi_states.StatesHanoi): El estado inicial del problema.
            goal (hanoi_states.StatesHanoi): El estado objetivo del problema.
        """
        super().__init__(initial=initial, goal=goal)

    def actions(self, state: hanoi_states.StatesHanoi):
        """
        Devuelve todas las acciones posibles que se pueden ejecutar desde un estado dado.

        Args:
            state (hanoi_states.StatesHanoi): Estado actual de la Torre de Hanoi.

        Returns:
            list: Lista con todas las acciones posibles.
        """
        actions_list = []
        for i in range(3):
            for j in range(3):
                disk = state.get_last_disk_rod(i, peek=True)
                if disk:
                    if state.check_valid_disk_in_rod(j, disk):
                        actions_list.append(hanoi_states.ActionHanoi(disk, i, j))
                else:
                    break

        return actions_list

    def result(self, state: hanoi_states.StatesHanoi, action: hanoi_states.ActionHanoi):
        """
        Calcula el nuevo estado después de aplicar una acción.

        Args:
            state (hanoi_states.StatesHanoi): Estado actual de la Torre de Hanoi.
            action (hanoi_states.ActionHanoi): Acción a aplicar.

        Returns:
            hanoi_states.StatesHanoi: Nuevo estado después de aplicar la acción.
        """
        return action.execute(state)

    def path_cost(self, c, state1, action, state2):
        """
        Calcula el costo del camino.

        Args:
            c: Costo acumulado hasta el estado actual (No utilizado, pero necesario por la herencia)
            state1 (hanoi_states.StatesHanoi): Estado inicial.
            action (hanoi_states.ActionHanoi): Acción realizada.
            state2 (hanoi_states.StatesHanoi): Estado resultante después de la acción. (No utilizado, pero necesario
            por la herencia)

        Returns:
            float: Costo total del camino.
        """
        return state1.accumulated_cost + action.cost


class NodeHanoi(aima.Node):
    """
    Clase que define un nodo en el arbol de búsqueda para la Torre de Hanoi.
    """

    def __init__(self, state, parent=None, action=None):
        """
        Inicializa un nodo en el espacio de búsqueda.

        Args:
            state: Estado del nodo.
            parent: Nodo padre.
            action: Acción realizada para llegar a este nodo.
        """
        super().__init__(state, parent=parent, action=action)
        self.path_cost = state.accumulated_cost

    def child_node(self, problem, action):
        """
        Genera el nodo hijo a partir de una acción.

        Args:
            problem: Problema de la Torre de Hanoi.
            action: Acción a aplicar.

        Returns:
            NodeHanoi: Nodo hijo generado.
        """
        next_state = problem.result(self.state, action)
        next_node = NodeHanoi(next_state, parent=self, action=action)
        return next_node

    def generate_solution_for_simulator(self, initial_state_file="./initial_state.json",
                                        sequence_file="./sequence.json"):
        """
        Genera los archivos JSON para el simulador de la Torre de Hanoi.

        Args:
            initial_state_file (str): Ruta del archivo JSON para el estado inicial.
            sequence_file (str): Ruta del archivo JSON para la secuencia de movimientos.
        """
        list_solution = self.path()

        with open(initial_state_file, "w") as file:
            initial_state = list_solution[0].state.get_state_dict()
            json.dump(initial_state, file)

        with open(sequence_file, "w") as file:
            sequence = [node.action.action_dict for node in list_solution[1:]]
            json.dump(sequence, file, indent=2)
