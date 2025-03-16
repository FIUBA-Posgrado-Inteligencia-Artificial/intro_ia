import math
import random

from sudoku_stuff import SUDOKU_SIZE_CONST


def obtain_chromosome_sudoku(state: dict, squares: list) -> str:
    """
    Convierte el estado del Sudoku en un cromosoma.

    Args:
        state (dict): El estado actual del Sudoku.
        squares (list): Lista con todas las celdas del Sudoku.

    Returns:
        str: El cromosoma generado a partir del estado del Sudoku.
    """

    chromosome = ""
    for cell in squares:
        chromosome += str(state[cell])
    return chromosome


def obtain_sibling_from_chromosome_sudoku(chromosome: str, squares: list) -> dict:
    """
    Convierte un cromosoma en un estado del Sudoku.

    Args:
        chromosome (str): El cromosoma a ser convertido en estado del Sudoku.
        squares (list): Lista con todas las celdas del Sudoku.

    Returns:
        dict: El estado del Sudoku generado a partir del cromosoma.
    """
    new_state = {}
    for index, cell in enumerate(squares):
        new_state[cell] = int(chromosome[index])
    return new_state


def reproduction_sudoku(chromosome_a: str, chromosome_b: str) -> tuple:
    """
    Realiza el proceso de reproducción entre dos cromosomas del Sudoku.

    Args:
        chromosome_a (str): El primer cromosoma.
        chromosome_b (str): El segundo cromosoma.

    Returns:
        tuple: Una tupla que contiene los dos nuevos cromosomas generados.
    """
    cut_chrom = random.randint(1, len(chromosome_a) - 2)

    sibling_a = chromosome_a[:cut_chrom] + chromosome_b[cut_chrom:]
    sibling_b = chromosome_b[:cut_chrom] + chromosome_a[cut_chrom:]

    return sibling_a, sibling_b


def obtain_fixed_pos_in_chromosome_sudoku(fixed_squares: dict, squares: list) -> list:
    """
    Obtiene las posiciones fijas (que no puede mutar) en el cromosoma del Sudoku.

    Args:
        fixed_squares (dict): Diccionario que contiene las casillas fijas del Sudoku.
        squares (list): Lista con todas las celdas del Sudoku.

    Returns:
        list: Lista de posiciones fijas en el cromosoma.
    """
    not_valid_positions = []
    for index, cell in enumerate(squares):
        if cell in fixed_squares:
            not_valid_positions.append(index)
    return not_valid_positions


def mutate_chromosome_sudoku_with_temperature(chromosome: str, not_valid_positions: list, temperature: float,
                                              max_value: int = SUDOKU_SIZE_CONST) -> str:
    """
    Realiza una mutación en el cromosoma del Sudoku utilizando temperatura.

    Args:
        chromosome (str): El cromosoma a ser mutado.
        not_valid_positions (list): Lista de posiciones fijas en el cromosoma.
        temperature (float): El valor de temperatura para controlar la probabilidad de mutación.
        max_value (int, opcional): El valor máximo permitido en el Sudoku. Por defecto es 9.

    Returns:
        str: El cromosoma mutado.
    """
    pos_to_mutate = not_valid_positions[0]

    while pos_to_mutate in not_valid_positions:
        pos_to_mutate = random.randint(0, len(chromosome) - 1)

    mutation = chromosome[pos_to_mutate]
    while mutation == chromosome[pos_to_mutate]:
        mutation = random.choice(range(max_value + 1))

    # Calcula la probabilidad de aceptar la mutación utilizando la temperatura
    mutation_probability = math.exp(-1 * (1 / temperature))

    # Si la probabilidad de mutación es mayor que un valor aleatorio, realiza la mutación
    if random.random() < mutation_probability:
        # Realiza la mutación en la posición seleccionada
        if pos_to_mutate == 0:
            return str(mutation) + chromosome[1:]
        elif pos_to_mutate == len(chromosome) - 1:
            return chromosome[:-1] + str(mutation)

        return chromosome[:pos_to_mutate] + str(mutation) + chromosome[pos_to_mutate + 1:]

    # Si no se acepta la mutación, devuelve el cromosoma sin cambios
    return chromosome
