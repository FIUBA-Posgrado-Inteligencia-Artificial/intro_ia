import multiprocessing

from functools import partial
from typing import Any

from tqdm.notebook import tqdm

from sudoku_stuff import is_solution, init_state


def execute_search(j: int, optim_func: Any, fixed_squares: dict) -> tuple:
    """
    Función que ejecuta la búsqueda de un algoritmo que se pasa como argumento.
    Args:
        j (int): Valor para indicar la iteración que esta corriendo
        optim_func (Any): Función con el método de búsqueda implementado
        fixed_squares (dict): Diccionario que contiene las casillas fijas del Sudoku
    Returns:
        bool: Indica si encontró la solución o no
        dict: Diccionario con el ultimo estado encontrado.
        dict: Diccionario con el primer estado con que se inicio el Sudoku
        int: Retorna el valor de la iteración
    """
    initial_state = init_state(fixed_squares)
    last_state, last_cost = optim_func(initial_state=initial_state, fixed_squares=fixed_squares)

    solution_bool = False
    if is_solution(last_state):
        solution_bool = True
    return solution_bool, last_state, initial_state, j


def execute_search_evolution(j: int, optim_func: Any, fixed_squares: dict, number_generation_initial: int = 20) -> tuple:
    """
    Función que ejecuta la búsqueda de un algoritmo que se pasa como argumento del tipo que maneja multiple
    generaciones.
    Args:
        j (int): Valor para indicar la iteración que esta corriendo
        optim_func (Any): Función con el método de búsqueda implementado
        fixed_squares (dict): Diccionario que contiene las casillas fijas del Sudoku
        number_generation_initial (int, opcional): Numero de estados con el cual va arrancar la búsqueda
    Returns:
        bool: Indica si encontró la solución o no
        dict: Diccionario con el ultimo estado encontrado.
        int: Generación en donde se encontró el mejor estado.
        int: Retorna el valor de la iteración
    """
    initial_generation = []
    for i in range(number_generation_initial):
        initial_generation.append(init_state(fixed_squares))

    last_state, last_cost, best_generation = optim_func(initial_generation=initial_generation, fixed_squares=fixed_squares)

    solution_bool = False
    if is_solution(last_state):
        solution_bool = True
    return solution_bool, last_state, best_generation, j


def parallel_sudoku_search(optim_func: Any, fixed_squares: dict, num_workers: int = multiprocessing.cpu_count(),
                           max_iterations: int = 500, generation_method: bool = False, number_generation_initial: int = 20) -> list:
    """
    Función que hace realiza la ejecución de la resolución de Sudoku de forma paralela en multiproceso.
    Args:
        optim_func (Any): Función con el método de búsqueda implementado
        fixed_squares (dict): Diccionario que contiene las casillas fijas del Sudoku
        num_workers (int, opcional): Numero de trabajadores para realizar el procesamiento. Por defecto se usa todos
                                     los cpus de la maquina.
        max_iterations (int, opcional): Cuantas veces se quiere ejecutar la búsqueda. Por defecto se usa 500
        generation_method (bool, opcional): Si el algoritmo de búsqueda a usar es del tipo que genera multiple estados
                                            por generación (Local Beam o Algoritmo Genético)
        number_generation_initial (int, opcional): Numero de estados con el cual va arrancar la búsqueda. Solo valido si
                                                   generation_method es True. Por defecto se usa 20.
    Returns:
        list - Retorna una lista con todas las búsquedas realizadas
    """
    # Pre-iniciamos a la función de optimización
    if generation_method:
        execute_search_partial = partial(execute_search_evolution, optim_func=optim_func, fixed_squares=fixed_squares,
                                         number_generation_initial=number_generation_initial)
    else:
        execute_search_partial = partial(execute_search, optim_func=optim_func, fixed_squares=fixed_squares)

    pool = multiprocessing.Pool(processes=num_workers)

    result_list_tqdm = []
    for result in tqdm(pool.imap(func=execute_search_partial, iterable=list(range(max_iterations))), total=max_iterations):
        result_list_tqdm.append(result)

    return result_list_tqdm
