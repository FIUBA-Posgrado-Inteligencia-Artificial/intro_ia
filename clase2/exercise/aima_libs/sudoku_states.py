import matplotlib.pyplot as plt
from IPython.display import HTML
from matplotlib.animation import FuncAnimation

from aima_libs import aima

DIGITS = "123456789"
ROWS = "ABCDEFGHI"
COLUMNS = DIGITS

# Nombres de las 81 celdas, por filas: ('A1', 'A2', ..., 'I9')
CELLS = tuple(row + column for row in ROWS for column in COLUMNS)

# Las 27 unidades del Sudoku: 9 filas, 9 columnas y 9 cajas de 3 x 3. Cada unidad es
# una lista con los índices (de 0 a 80) de sus celdas
ROW_UNITS = [[9 * r + c for c in range(9)] for r in range(9)]
COLUMN_UNITS = [[9 * r + c for r in range(9)] for c in range(9)]
BOX_UNITS = [
    [9 * (3 * br + r) + 3 * bc + c for r in range(3) for c in range(3)]
    for br in range(3)
    for bc in range(3)
]
ALL_UNITS = ROW_UNITS + COLUMN_UNITS + BOX_UNITS

# Para cada celda, los índices de las celdas que comparten fila, columna o caja con
# ella (sus "pares"). Dos pares no pueden tener el mismo dígito
PEERS = [
    sorted({other for unit in ALL_UNITS if cell in unit for other in unit} - {cell})
    for cell in range(81)
]

# Sudokus predefinidos. Cada string recorre el tablero por filas, de A1 a I9, y un
# punto indica una celda vacía
PUZZLES = {
    # 38 pistas
    "facil": (
        "3.456.9..185..97......78415"
        ".2..1..49.49.5......198.67."
        "49..3...7.18745..6.......8."
    ),
    # 26 pistas. Es el Sudoku de Arto Inkala (2012) con 5 pistas extra tomadas
    # de su solución
    "dificil": (
        "8..........36.2....75.9.2.."
        ".5.2.7.......457.....1.9.3."
        "..1....68..85...1..96...4.."
    ),
    # 21 pistas. El Sudoku de Arto Inkala (2012), conocido como "el más difícil
    # del mundo"
    "inkala": (
        "8..........36......7..9.2.."
        ".5...7.......457.....1...3."
        "..1....68..85...1..9....4.."
    ),
}


class StatesSudoku:
    """
    Representa un estado del tablero de Sudoku, con algunas celdas completas y otras
    vacías.
    """

    def __init__(self, grid: tuple, cost: float = 0.0):
        """
        Inicializa un estado del Sudoku.

        Args:
            grid (tuple): Tupla de 81 enteros que recorre el tablero por filas, de A1
                a I9. Un 0 indica una celda vacía.
            cost (float): Costo asociado al estado.
        """
        if len(grid) != len(CELLS):
            raise ValueError("El tablero debe tener 81 celdas")
        if not all(0 <= value <= 9 for value in grid):  # noqa: PLR2004
            raise ValueError("Los valores de las celdas deben estar entre 0 y 9")

        self.grid = tuple(grid)
        self.accumulated_cost = cost

    def __eq__(self, other):
        """
        Dos estados son iguales si tienen el mismo tablero.

        Args:
            other: Otro estado del Sudoku a comparar.

        Returns:
            bool: True si los estados son iguales, False en caso contrario.
        """
        return isinstance(other, StatesSudoku) and self.grid == other.grid

    def __lt__(self, other):
        """
        Compara dos estados según su costo acumulado.

        Args:
            other: Otro estado del Sudoku a comparar.

        Returns:
            bool: True si este estado tiene menor costo acumulado.
        """
        return self.accumulated_cost < other.accumulated_cost

    def __hash__(self):
        """
        Genera un hash para el estado, a partir del tablero.

        Returns:
            int: Hash generado para el estado.
        """
        return hash(self.grid)

    def __repr__(self):
        """
        Representación en una línea del estado, con un punto en las celdas vacías.

        Returns:
            str: Cadena que representa el estado.
        """
        return "SudokuState: " + "".join(str(v) if v else "." for v in self.grid)

    def __str__(self):
        """
        Representación del tablero en varias líneas, con las cajas separadas.

        Returns:
            str: Cadena que representa el tablero.
        """
        horizontal_line = "+-------+-------+-------+"
        lines = [horizontal_line]
        for r in range(9):
            line = "|"
            for c in range(9):
                value = self.grid[9 * r + c]
                line += f" {value if value else '.'}"
                if c in (2, 5, 8):
                    line += " |"
            lines.append(line)
            if r in (2, 5, 8):
                lines.append(horizontal_line)
        return "\n".join(lines)

    def empty_cells(self) -> list:
        """
        Obtiene las celdas vacías del tablero.

        Returns:
            list: Índices (de 0 a 80) de las celdas vacías, en orden.
        """
        return [index for index, value in enumerate(self.grid) if value == 0]

    def candidates(self, index: int) -> list:
        """
        Obtiene los dígitos que se pueden poner en una celda sin repetir un dígito en
        su fila, su columna o su caja.

        Args:
            index (int): Índice de la celda, de 0 a 80.

        Returns:
            list: Dígitos posibles para la celda, de menor a mayor.
        """
        used = {self.grid[peer] for peer in PEERS[index]}
        return [digit for digit in range(1, 10) if digit not in used]

    def accumulate_cost(self, cost):
        """
        Acumula el costo asociado al estado.

        Args:
            cost: Costo a acumular.
        """
        self.accumulated_cost += cost

    def get_accumulated_cost(self):
        """
        Obtiene el costo acumulado del estado.

        Returns:
            float: Costo acumulado del estado.
        """
        return self.accumulated_cost

    def get_state(self) -> tuple:
        """
        Obtiene el tablero del estado.

        Returns:
            tuple: Tupla de 81 enteros, con 0 en las celdas vacías.
        """
        return self.grid


def load_puzzle(name: str) -> StatesSudoku:
    """
    Crea el estado inicial de uno de los Sudokus predefinidos.

    Args:
        name (str): Nombre del Sudoku: "facil", "dificil" o "inkala".

    Returns:
        StatesSudoku: Estado con las pistas del Sudoku y el resto de las celdas vacías.
    """
    return StatesSudoku(
        tuple(0 if value == "." else int(value) for value in PUZZLES[name])
    )


class ActionSudoku:
    """
    Representa una acción en el Sudoku: poner un dígito en una celda vacía.
    """

    def __init__(self, index: int, digit: int):
        """
        Inicializa una acción.

        Args:
            index (int): Índice de la celda, de 0 a 80.
            digit (int): Dígito a poner en la celda, de 1 a 9.
        """
        self.index = index
        self.digit = digit
        self.action = f"Put {digit} in {CELLS[index]}"
        self.cost = 1.0

    def __repr__(self):
        """
        Representación formal de una acción.

        Returns:
            str: Cadena que representa la acción.
        """
        return self.action

    def __str__(self):
        """
        Representación en cadena de una acción.

        Returns:
            str: Cadena que representa la acción.
        """
        return self.action

    def execute(self, state_sudoku: StatesSudoku) -> StatesSudoku:
        """
        Ejecuta la acción en un estado del Sudoku.

        Args:
            state_sudoku (StatesSudoku): Estado en el que se ejecuta la acción.

        Returns:
            StatesSudoku: Nuevo estado, con el dígito puesto en la celda.
        """
        grid = list(state_sudoku.grid)
        grid[self.index] = self.digit
        return StatesSudoku(tuple(grid), cost=state_sudoku.accumulated_cost + self.cost)


class ProblemSudoku(aima.Problem):
    """
    Clase que define el problema del Sudoku.

    Attributes:
        initial (StatesSudoku): El estado inicial del problema, con las pistas.
        goal (None): El Sudoku no tiene un estado objetivo conocido de antemano: el
            objetivo es cualquier tablero completo, ver `goal_test()`.
    """

    def __init__(self, initial: StatesSudoku):
        """
        Inicializa el problema del Sudoku.

        Args:
            initial (StatesSudoku): El estado inicial del problema.
        """
        super().__init__(initial=initial, goal=None)

    def actions(self, state: StatesSudoku):
        """
        Devuelve las acciones posibles desde un estado: poner en la **primera celda
        vacía** (recorriendo el tablero por filas) cada uno de los dígitos que no
        se repiten en su fila, su columna o su caja.

        Como todas las celdas vacías se tienen que completar en algún momento, alcanza
        con elegir una sola por paso: el orden en que se completan no cambia la
        solución, pero sí cuántos nodos tiene el árbol de búsqueda.

        Args:
            state (StatesSudoku): Estado actual del Sudoku.

        Returns:
            list: Lista con todas las acciones posibles. Si una celda vacía no tiene
                ningún dígito posible, la lista está vacía: es un callejón sin salida.
        """
        empty = state.empty_cells()
        if not empty:
            return []

        index = empty[0]
        return [ActionSudoku(index, digit) for digit in state.candidates(index)]

    def result(self, state: StatesSudoku, action: ActionSudoku) -> StatesSudoku:
        """
        Calcula el nuevo estado después de aplicar una acción.

        Args:
            state (StatesSudoku): Estado actual del Sudoku.
            action (ActionSudoku): Acción a aplicar.

        Returns:
            StatesSudoku: Nuevo estado después de aplicar la acción.
        """
        return action.execute(state)

    def goal_test(self, state: StatesSudoku) -> bool:
        """
        Comprueba si un estado es una solución: el tablero está completo. Como las
        acciones solo ponen dígitos que no se repiten, un tablero completo siempre
        cumple las reglas del Sudoku.

        Args:
            state (StatesSudoku): Estado a comprobar.

        Returns:
            bool: True si no quedan celdas vacías.
        """
        return 0 not in state.grid

    def path_cost(self, c, state1, action, state2):
        """
        Calcula el costo del camino.

        Args:
            c: Costo acumulado hasta el estado actual (No utilizado, pero necesario por
                la herencia)
            state1 (StatesSudoku): Estado inicial.
            action (ActionSudoku): Acción realizada.
            state2 (StatesSudoku): Estado resultante después de la acción.
                (No utilizado, pero necesario por la herencia)

        Returns:
            float: Costo total del camino.
        """
        return state1.accumulated_cost + action.cost


def _draw_board(
    ax, state: StatesSudoku, initial: StatesSudoku | None = None, highlight=None
):
    """
    Dibuja el tablero en unos ejes de matplotlib. Las pistas se muestran en negro, los
    dígitos agregados durante la búsqueda en azul y la celda `highlight`, en rojo.

    Args:
        ax (matplotlib.axes.Axes): Ejes donde dibujar.
        state (StatesSudoku): Estado a dibujar.
        initial (StatesSudoku | None): Estado inicial del problema, con las pistas.
        highlight (int | None): Índice de la celda a destacar.
    """
    ax.clear()

    # Líneas finas punteadas entre celdas y gruesas entre cajas
    for k in range(10):
        width, style, color = (2.5, "-", "black") if k % 3 == 0 else (1, ":", "gray")
        ax.plot([k, k], [0, 9], linestyle=style, linewidth=width, color=color)
        ax.plot([0, 9], [k, k], linestyle=style, linewidth=width, color=color)

    for index, value in enumerate(state.grid):
        if value == 0:
            continue
        if index == highlight:
            color = "red"
        elif initial is None or initial.grid[index] != 0:
            color = "black"
        else:
            color = "dodgerblue"
        ax.text(
            index % 9 + 0.5,
            8.5 - index // 9,
            str(value),
            ha="center",
            va="center",
            fontsize=14,
            fontweight="bold" if index == highlight else "normal",
            color=color,
        )

    ax.set_xlim(0, 9)
    ax.set_ylim(0, 9)
    ax.set_aspect("equal")
    ax.axis("off")


def plot_sudoku(state: StatesSudoku, initial: StatesSudoku | None = None, title=""):
    """
    Dibuja el tablero. Si se pasa el estado inicial, las pistas se muestran en negro
    y los dígitos agregados durante la búsqueda en azul.

    Args:
        state (StatesSudoku): Estado a dibujar.
        initial (StatesSudoku | None): Estado inicial del problema, con las pistas.
        title (str): Título del gráfico.
    """
    _, ax = plt.subplots(figsize=(4, 4))
    _draw_board(ax, state, initial)
    if title:
        ax.set_title(title)
    plt.show()


def animate_solution(solution, interval: int = 300):
    """
    Anima el camino de la solución: el tablero se va completando paso a paso, con el
    dígito que se acaba de poner en rojo. La animación se muestra en la notebook, con
    botones para reproducirla, pausarla y avanzar o retroceder paso a paso.

    Args:
        solution (NodeSudoku): Último nodo de la solución encontrada.
        interval (int): Milisegundos entre un paso y el siguiente.

    Returns:
        IPython.display.HTML: La animación, lista para mostrarse en la notebook.
    """
    nodes = solution.path()
    initial = nodes[0].state

    fig, ax = plt.subplots(figsize=(4, 4.4), dpi=72)

    def draw_step(step):
        node = nodes[step]
        highlight = node.action.index if node.action else None
        _draw_board(ax, node.state, initial, highlight)
        action = f": {node.action}" if node.action else ""
        ax.set_title(f"Paso {step} de {len(nodes) - 1}{action}")

    animation = FuncAnimation(fig, draw_step, frames=len(nodes), interval=interval)
    html = HTML(animation.to_jshtml())
    plt.close(fig)  # Para que no se muestre además una imagen fija del último paso
    return html
