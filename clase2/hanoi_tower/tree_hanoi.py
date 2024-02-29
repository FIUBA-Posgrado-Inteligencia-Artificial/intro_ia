import json
import aima
import hanoi_states


class NodeHanoi(aima.Node):
    """
    Clase que define un nodo en el arbol de búsqueda para la Torre de Hanoi.
    """

    def __init__(self, state: hanoi_states.StatesHanoi, parent=None, action=None):
        """
        Inicializa un nodo en el espacio de búsqueda.

        Args:
            state (hanoi_states.StatesHanoi): Estado del nodo.
            parent (hanoi_states.StatesHanoi | None): Nodo padre.
            action (hanoi_states.ActionHanoi | None): Acción realizada para llegar a este nodo.
        """
        super().__init__(state, parent=parent, action=action)
        self.path_cost = state.accumulated_cost

    def child_node(self, problem: hanoi_states.ProblemHanoi, action: hanoi_states.ActionHanoi):
        """
        Genera el nodo hijo a partir de una acción.

        Args:
            problem (hanoi_states.ProblemHanoi): Problema de la Torre de Hanoi.
            action (hanoi_states.ActionHanoi): Acción a aplicar.

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
