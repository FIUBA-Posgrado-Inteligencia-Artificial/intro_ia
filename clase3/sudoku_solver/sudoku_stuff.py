import math
import random

from collections import Counter


DIGITS_CONST = '123456789'
ROWS_CONST = 'ABCDEFGHI'
COLUMNS_CONST = DIGITS_CONST
SUDOKU_SIZE_CONST = 3*3


def cross(A, B) -> tuple:
    """Producto cruzado de strings en A y strings en B"""
    return tuple(a + b for a in A for b in B)


def obtain_all_cells(rows: str = ROWS_CONST, cols: str = COLUMNS_CONST):
    """
    Retorna todas las coordenadas de las celdas

    Args:
        rows (str, opcional): String con el nombre de las filas. Por defecto es 'ABCDEFGHI'
        cols (str, opcional): String con el nombre de las columnas. Por defecto es '123456789'

    Returns:
        Tupla con todas las coordenadas de las celdas del sudoku

    """
    return cross(rows, cols)


def obtain_coordinates_of_units(rows: str = ROWS_CONST, cols: str = COLUMNS_CONST, sudoku_size: int = SUDOKU_SIZE_CONST):
    """Obtenemos las coordenadas de las unidades del sudoku

    Args:
        rows (str, opcional): String con el nombre de las filas. Por defecto es 'ABCDEFGHI'
        cols (str, opcional): String con el nombre de las columnas. Por defecto es '123456789'
        sudoku_size(int, opcional): Tamaño del sudoku. Por defecto es 9.
    Returns:
        dict - Diccionario con tuplas conformadas por las coordenadas de las celdas que pertenecen a cada unidad.
              "boxes": Tuplas con las coordenadas de las celdas que pertenecen a cada caja.
              "rows": Tuplas con las coordenadas de las celdas que pertenecen a cada fila.
              "columns": Tuplas con las coordenadas de las celdas que pertenecen a cada columna.
              "units": Tuplas con las coordenadas de las celdas que pertenecen a cada caja, fila y columna.
    """

    # Obtenemos el largo o el ancho del sudoku en tamaño de cajas
    side_sudoku = int(math.sqrt(sudoku_size))

    # Obtenemos las cajas
    all_boxes = [cross(rs, cs) for rs in map(''.join, zip(*[iter(rows)]*side_sudoku)) for cs in map(''.join, zip(*[iter(cols)]*side_sudoku))]
    # Obtenemos las filas
    all_rows = [cross(rows, c) for c in cols]
    # obtenemos las columnas
    all_columns = [cross(r, cols) for r in rows]
    # unimos a todas las unidades
    all_units = all_rows + all_columns + all_boxes

    output = {
        "boxes": all_boxes,
        "rows": all_rows,
        "columns": all_columns,
        "units": all_units
    }

    return output


def init_state(fixed_squares, rows: str = ROWS_CONST, cols: str = COLUMNS_CONST, max_value: int = SUDOKU_SIZE_CONST) -> dict:
    """
    Inicializa un estado aleatorio para el Sudoku.

    Args:
        fixed_squares (dict): Diccionario que contiene las casillas fijas del Sudoku,
        con claves como coordenadas (e.g., "A1", "B2") y valores como los números
        fijos correspondientes.
        rows (str, opcional): String con el nombre de las filas. Por defecto es 'ABCDEFGHI'
        cols (str, opcional): String con el nombre de las columnas. Por defecto es '123456789'
        max_value (int, optional): Valor máximo que se puede insertar como digito en el
        Sudoku. Por defecto es 9.

    Returns:
        dict: Diccionario que representa el tablero de Sudoku generado aleatoriamente,
        con las casillas fijas y las casillas vacías llenas con valores aleatorios.
    """

    # Inicializamos el tablero del Sudoku
    puzzle = {}

    # Iteramos sobre cada fila del tablero
    for row in rows:
        # Creamos una lista de columnas disponibles para cada fila
        available_columns = [num for num in range(1, max_value + 1)]

        # Eliminamos los números que ya están en la fila
        for col in cols:
            if row + col in fixed_squares:
                available_columns.remove(int(col))

        # Asignamos valores aleatorios a las casillas vacías en la fila
        for col in available_columns:
            square = row + str(col)
            # Elegimos aleatoriamente un número disponible para la casilla
            value = random.choice(range(1, max_value + 1))
            puzzle[square] = value

    puzzle.update(fixed_squares)
    return puzzle


def print_state(state_to_print: dict, rows: str = ROWS_CONST, cols: str = COLUMNS_CONST) -> None:
    """
    Imprime el estado actual del Sudoku.

    Args:
        state_to_print (dict): Diccionario que representa el tablero de Sudoku, 
        con claves como coordenadas (e.g., "A1", "B2") y valores como los números 
        en las casillas correspondientes.
        rows (str, opcional): String con el nombre de las filas. Por defecto es 'ABCDEFGHI'
        cols (str, opcional): String con el nombre de las columnas. Por defecto es '123456789'
    """
    size = int(len(rows) ** 0.5)  # Tamaño de las cajas (e.g., 2 para 2x2, 3 para 3x3)
    horizontal_line = "+".join(["-" * (size * 3)] * size)
    horizontal_line = "*" + horizontal_line + "*"
    print(horizontal_line)

    for index_row, row in enumerate(rows):
        print("|", end="")
        for col_index, col in enumerate(cols):
            print(f" {state_to_print[row + col]} ", end="")
            if (col_index + 1) % size == 0 and col_index < len(cols) - 1:
                print("|", end="")
        print("|")
        if (index_row + 1) % size == 0 and index_row < len(rows) - 1:
            print(horizontal_line)

    print(horizontal_line)


def return_neib_states(state: dict, fixed_squares: dict, sudoku_size: int = SUDOKU_SIZE_CONST,
                       rows: str = ROWS_CONST, cols: str = COLUMNS_CONST) -> list:
    """
    Retorna todos los estados vecinos del estado actual del Sudoku.

    Args:
        state (dict): Diccionario que representa el tablero de Sudoku actual.
        fixed_squares (dict): Diccionario que contiene las casillas fijas del Sudoku.
        sudoku_size(int, opcional): Tamaño del sudoku. Por defecto es 9.
        rows (str, opcional): String con el nombre de las filas. Por defecto es 'ABCDEFGHI'
        cols (str, opcional): String con el nombre de las columnas. Por defecto es '123456789'

    Returns:
        list: Una lista de diccionarios que representan los estados vecinos.
    """
    all_neib = []

    coordinates_dict = obtain_coordinates_of_units(rows=rows, cols=cols, sudoku_size=sudoku_size)
    all_units = coordinates_dict["units"]
    squares = obtain_all_cells(rows=rows, cols=cols)

    # Intercambiar los valores de dos casillas en la misma unidad
    for unit in all_units:
        for index, cell in enumerate(unit):
            if cell in fixed_squares:
                continue
            for second_cell in unit[index + 1:]:
                if second_cell not in fixed_squares:
                    new_neib = state.copy()
                    new_neib[cell] = state[second_cell]
                    new_neib[second_cell] = state[cell]
                    all_neib.append(new_neib)
    
    # Cambiar el valor de una casilla
    for cell in squares:
        if cell not in fixed_squares:
            for new_value in range(1, sudoku_size+1):
                if new_value == state[cell]:
                    continue
                new_neib = state.copy()
                new_neib[cell] = new_value
                all_neib.append(new_neib)
                
    return all_neib


def is_solution(state: dict, sudoku_size: int = SUDOKU_SIZE_CONST, rows: str = ROWS_CONST, cols: str = COLUMNS_CONST) -> bool:
    """Retorna si un estado es solución del Sudoku. Para ello todas las unidades deben tener todos los números del 1 al
    9 sin repetirse.

    Args:
        state (dict): Diccionario que representa el tablero de Sudoku actual.
        sudoku_size(int, opcional): Tamaño del sudoku. Por defecto es 9.
        rows (str, opcional): String con el nombre de las filas. Por defecto es 'ABCDEFGHI'
        cols (str, opcional): String con el nombre de las columnas. Por defecto es '123456789'

    Returns:
        list: Una lista de diccionarios que representan los estados vecinos.
    """
    # Obtenemos todas las unidades para verificar si es solución
    coordinates_dict = obtain_coordinates_of_units(rows=rows, cols=cols, sudoku_size=sudoku_size)
    all_units = coordinates_dict["units"]

    # Vamos pasando de unidad a unidad
    for unit in all_units:
        # Obtenemos los valores de las celdas de la unidad
        values = [state[cell] for cell in unit]
        # Usamos un set para verificar que todos los números estén exactamente una sola vez.
        if len(set(values)) != sudoku_size or not all(1 <= val <= sudoku_size for val in values):
            return False

    # Si termina el ciclo sin problemas, es solución
    return True


def cost_function(state: dict, sudoku_size: int = SUDOKU_SIZE_CONST, rows: str = ROWS_CONST, cols: str = COLUMNS_CONST,
                  penalty_value: float = 0.05) -> float:
    """
    Calcula la función de costo del estado actual del Sudoku.

    Args:
        state (dict): Diccionario que representa el tablero de Sudoku actual.
        sudoku_size(int, opcional): Tamaño del sudoku. Por defecto es 9.
        rows (str, opcional): String con el nombre de las filas. Por defecto es 'ABCDEFGHI'
        cols (str, opcional): String con el nombre de las columnas. Por defecto es '123456789'
        Sudoku. Por defecto es 9.
        penalty_value (float, opcional): Valor base para penalizar las equivocaciones. Por defecto es 0.05
    Returns:
        float: El valor de la función de costo.
    """
    # Obtenemos todas las unidades para verificar
    coordinates_dict = obtain_coordinates_of_units(rows=rows, cols=cols, sudoku_size=sudoku_size)
    all_units = coordinates_dict["units"]

    # Usado como template, para no hacer un dict comprehension en cada loop
    zeroes = {i: 0 for i in range(1, sudoku_size + 1)}

    penalization = 0
    for unit in all_units:
        values = [state[cell] for cell in unit]

        # Usamos Counter para contar las ocurrencias
        ocurrences = zeroes.copy()
        ocurrences.update(Counter(values))

        # Si el elemento no está o está dos veces, le sumamos una penalización
        # Aguante esa programación funcional :)
        penalization += sum([abs((i - 1) * penalty_value) for i in ocurrences.values()])

    return penalization
