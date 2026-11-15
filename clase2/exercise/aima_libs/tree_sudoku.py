from aima_libs import aima, sudoku_states


class NodeSudoku(aima.Node):
    """
    Clase que define un nodo en el árbol de búsqueda para el Sudoku.
    """

    def __init__(self, state: sudoku_states.StatesSudoku, parent=None, action=None):
        """
        Inicializa un nodo en el espacio de búsqueda.

        Args:
            state (sudoku_states.StatesSudoku): Estado del nodo.
            parent (NodeSudoku | None): Nodo padre.
            action (sudoku_states.ActionSudoku | None): Acción realizada para llegar
                a este nodo.
        """
        super().__init__(state, parent=parent, action=action)
        self.path_cost = state.accumulated_cost

    def child_node(
        self, problem: sudoku_states.ProblemSudoku, action: sudoku_states.ActionSudoku
    ):
        """
        Genera el nodo hijo a partir de una acción.

        Args:
            problem (sudoku_states.ProblemSudoku): Problema del Sudoku.
            action (sudoku_states.ActionSudoku): Acción a aplicar.

        Returns:
            NodeSudoku: Nodo hijo generado.
        """
        next_state = problem.result(self.state, action)
        return NodeSudoku(next_state, parent=self, action=action)
