import itertools
import random
import math
import numpy as np

from sudoku_stuff import cost_function, return_neib_states, obtain_all_cells
from genetic import (obtain_fixed_pos_in_chromosome_sudoku, obtain_chromosome_sudoku, reproduction_sudoku,
                     mutate_chromosome_sudoku_with_temperature, obtain_sibling_from_chromosome_sudoku)


def gradient_descent_sudoku(initial_state: dict, fixed_squares: dict, max_iterations: int = 1000) -> tuple:
    """
    Realiza la optimización del Sudoku utilizando el método de descenso de gradiente.

    Args:
        initial_state (dict): El estado inicial del Sudoku.
        fixed_squares (dict): Diccionario que contiene las casillas fijas del Sudoku,
        max_iterations (int, opcional): El número máximo de iteraciones permitidas.
                                        Por defecto es 100.
    Returns:
        dict: El mejor estado encontrado después de la optimización.
        float: El costo del mejor estado encontrado
    """
    best_state = initial_state
    cost_state = cost_function(best_state)

    # Iteramos hasta max_iterations
    for iteration in range(max_iterations):

        # Calculamos la función de costo para el estado actual
        cost_state = cost_function(best_state)

        # Si el costo es cero, significa que estamos en el minimo. Esto tiene sentido para el caso de Sudoku y la
        # función de costo que implementamos.
        if cost_state == 0:
            break

        # Obtenemos a los vecinos más cercanos
        neib_states = return_neib_states(best_state, fixed_squares)

        # Calculamos el delta del costo entre el estado actual y sus vecinos
        neib_energy_list = [cost_function(neib_state) - cost_state for neib_state in neib_states]

        # Obtenemos el índice de la lista de estados vecinos que tenga el mínimo valor
        index_min_energy = np.argmin(neib_energy_list)

        # Si el delta del costo es positivo o cero, es que no hay vecino que reduzca el gradiente, llegamos a un minimo
        # local.
        if neib_energy_list[index_min_energy] >= 0:
            return best_state, cost_state

        # Si no, seguimos avanzando
        best_state = neib_states[index_min_energy]

    # Si terminamos las iteraciones, retornamos nuestro mejor resultado
    return best_state, cost_state


def gradient_descent_random_sudoku(initial_state: dict, fixed_squares: dict, max_iterations: int = 1000,
                                   move_in_zero: bool = False) -> tuple:
    """
    Realiza la optimización del Sudoku utilizando el método de descenso de gradiente estocástico.

    Args:
        initial_state (dict): El estado inicial del Sudoku.
        fixed_squares (dict): Diccionario que contiene las casillas fijas del Sudoku,
        max_iterations (int, opcional): El número máximo de iteraciones permitidas.
                                        Por defecto es 100.
        move_in_zero (bool, opcional): Nos permite movernos en mesetas, donde la derivada es cero
    Returns:
        dict: El mejor estado encontrado después de la optimización.
        float: El costo del mejor estado encontrado
    """
    best_state = initial_state
    cost_state = cost_function(best_state)

    # Iteramos hasta max_iterations
    for iteration in range(max_iterations):

        # Calculamos la función de costo para el estado actual
        cost_state = cost_function(best_state)

        # Si el costo es cero, significa que estamos en el minimo. Esto tiene sentido para el caso de Sudoku y la
        # función de costo que implementamos.
        if cost_state == 0:
            break

        # Obtenemos a los vecinos más cercanos
        neib_states = return_neib_states(best_state, fixed_squares)

        # Calculamos el delta del costo entre el estado actual y sus vecinos
        neib_energy_list = [cost_function(neib_state) - cost_state for neib_state in neib_states]

        # Obtenemos el índice de la lista de estados vecinos que tengan el mínimo valor y que además sea negativo
        # significando que estamos descendiendo en la función en la dirección de máximo descenso.
        if move_in_zero:
            # Permitimos movernos en mesetas
            index_min_energy = [i for i, x in enumerate(neib_energy_list) if x <= 0]
        else:
            index_min_energy = [i for i, x in enumerate(neib_energy_list) if x < 0]

        # Si no tenemos ningún índice, significa que ya no hay más
        # descenso, retornamos lo mejor que llegó el método
        if not index_min_energy:
            return best_state, cost_state

        # Si no, elegimos una dirección al azar de los máximos cambios
        index_sel = random.choice(index_min_energy)
        best_state = neib_states[index_sel]

    # Si terminamos las iteraciones, retornamos nuestro mejor resultado
    return best_state, cost_state


def simulated_annealing_sudoku(initial_state: dict, fixed_squares: dict, max_iterations: int = 1000,
                               initial_temperature: float = 0.01, cooling_rate: float = 0.1) -> tuple:
    """
    Realiza la optimización del Sudoku utilizando Simulated Annealing.

    Args:
        initial_state (dict): El estado inicial del Sudoku.
        fixed_squares (dict): Diccionario que contiene las casillas fijas del Sudoku.
        max_iterations (int, optional): El número máximo de iteraciones permitidas.
                                        Por defecto es 100.
        initial_temperature (float, optional): La temperatura inicial para el algoritmo de Simulated Annealing.
        cooling_rate (float, optional): La tasa de enfriamiento para el algoritmo de Simulated Annealing.

    Returns:
        dict: El mejor estado encontrado después de la optimización.
        float: El costo del mejor estado encontrado
    """
    current_state = initial_state
    best_state = initial_state
    temperature = initial_temperature
    best_cost = cost_function(best_state)

    # Iteramos hasta max_iterations
    for iteration in range(max_iterations):

        # Calculamos la función de costo para el estado actual
        current_cost = cost_function(current_state)

        # Obtenemos los vecinos de un estado
        neib_states = return_neib_states(current_state, fixed_squares)
        amount_neib = len(neib_states)

        # Mientras un estado tengas vecinos
        while amount_neib > 0:
            # Obtenemos un estado vecino aleatorio
            neib_state = random.choice(neib_states)
            neib_states.remove(neib_state)
            amount_neib -= 1

            # Calculamos la función de costo para el estado vecino
            neib_cost = cost_function(neib_state)

            # Calculamos el delta de costo entre el estado actual y el vecino
            delta_cost = neib_cost - current_cost

            # Si el vecino es mejor o se acepta según la probabilidad de Boltzmann, actualizamos el estado actual
            if delta_cost < 0:
                current_state = neib_state
                break
            else:
                if temperature > 0:
                    if random.random() < math.exp(-delta_cost / temperature):
                        current_state = neib_state
                        break

        # Si termino el anterior ciclo y se visitaron a todos los vecinos y no se acepto ningún cambio
        # se termina el proceso.
        if amount_neib < 1:
            return best_state, best_cost

        # Si el nuevo estado es mejor que el mejor estado encontrado hasta ahora, actualizamos el mejor estado
        if current_cost < best_cost:
            best_state = current_state
            best_cost = cost_function(best_state)

        # Si el costo es cero, significa que estamos en el mínimo. Esto tiene sentido para el caso de Sudoku y la
        # función de costo que implementamos.
        if best_cost == 0:
            break

        # Enfriamos el problema
        temperature *= cooling_rate

    # Si terminamos las iteraciones, retornamos el mejor resultado encontrado
    return best_state, best_cost


def local_beam_search(initial_generation: list, fixed_squares: dict, max_iterations: int = 100) -> tuple:
    """
    Realiza la optimización del Sudoku utilizando búsqueda por Local Beam.

    Args:
        initial_generation (list): Lista con estados iniciales del Sudoku.
        fixed_squares (dict): Diccionario que contiene las casillas fijas del Sudoku.
        max_iterations (int, optional): El número máximo de iteraciones permitidas.
                                        Por defecto es 100.

    Returns:
        dict: El mejor estado encontrado después de la optimización.
        float: El costo del mejor estado encontrado
        int: Numero indicando en que generación se encontró el mejor resultado
    """
    # Inicializamos para poder arrancar
    best_state = initial_generation[0]
    best_cost = cost_function(best_state)
    best_iteration = 0
    no_changes = 0

    number_population = len(initial_generation)
    current_population = initial_generation.copy()

    # Iteramos hasta max_iterations
    for iteration in range(max_iterations):
        no_changes += 1

        # Para cada uno de la generación, calculamos su función de costo
        actual_cost_list = []
        for index in range(number_population):
            state = current_population[index]
            cost = cost_function(state)
            actual_cost_list.append(cost)
            if cost < best_cost:
                no_changes = 0
                best_state = state
                best_cost = cost
                best_iteration = iteration

        # Si es solución, terminamos.
        # También si pasamos varias iteraciones sin cambios, terminamos
        if best_cost == 0 or no_changes > 5:
            return best_state, best_cost, best_iteration

        # Obtenemos a todos los vecinos posibles y sus costos
        all_neib = []
        all_cost = []
        for index, state in enumerate(current_population):
            actual_neib = return_neib_states(state, fixed_squares)
            all_neib += actual_neib
            all_cost += [cost_function(state_neib) for state_neib in actual_neib]

        # Ordenamos a los vecinos en función del costo
        index_neib_list = sorted(range(len(all_cost)), key=lambda x: all_cost[x])
        all_neib = [all_neib[k] for k in index_neib_list]

        # Nos quedamos con los k de la generación
        current_population = all_neib[:number_population]

    # Si terminamos las iteraciones, retornamos el mejor resultado encontrado
    return best_state, best_cost, best_iteration


def genetic_algorithm_sudoku(initial_generation: list, fixed_squares: dict, max_iterations: int = 50,
                             initial_temperature: float = 100.0):
    """
    Realiza la optimización del Sudoku utilizando un algoritmo genético.

    Args:
        initial_generation (list): Lista con estados iniciales del Sudoku.
        fixed_squares (dict): Diccionario que contiene las casillas fijas del Sudoku.
        max_iterations (int, optional): El número máximo de iteraciones permitidas. Por defecto es 100.
        initial_temperature (float, optional): La temperatura inicial para controlar la probabilidad de mutación. Por defecto es 0.1.

    Returns:
        dict: El mejor estado encontrado después de la optimización.
        float: El costo del mejor estado encontrado
        int: Numero indicando en que generación se encontró el mejor resultado
    """
    temperature = initial_temperature
    best_state = initial_generation[0]
    best_cost = cost_function(best_state)
    best_iteration = 0
    no_changes = 0

    number_population = len(initial_generation)
    current_population = initial_generation.copy()

    # Obtenemos las posiciones del sudoku que no pueden mutar
    squares = obtain_all_cells()
    not_valid_positions = obtain_fixed_pos_in_chromosome_sudoku(fixed_squares, squares)

    # Iteramos hasta max_iterations
    for iteration in range(max_iterations):

        no_changes += 1

        # Para cada uno de la generación, calculamos su función de costo
        actual_cost_list = [cost_function(state) for state in current_population]

        for index, cost in enumerate(actual_cost_list):
            if cost < best_cost:
                no_changes = 0
                best_state = current_population[index]
                best_cost = cost
                best_iteration = iteration

        # Si es solución, terminamos.
        # También si pasamos varias iteraciones sin cambios, terminamos
        if best_cost == 0 or no_changes > 9:
            return best_state, best_cost, best_iteration

        # Ordenamos a los estados en función del costo de menor a mayor (función de idoneidad)
        index_list = sorted(range(len(actual_cost_list)), key=lambda x: actual_cost_list[x])
        current_population = [current_population[k] for k in index_list]

        # Nos quedamos con solo un valor de estados igual a la población inicial que pasan a reproducirse
        current_population = current_population[:number_population]

        # Obtenemos los cromosomas de los estados
        all_chromosome = [obtain_chromosome_sudoku(state, squares) for state in current_population]

        # Reproducimos a todos con todos
        sibling_chromosomes_list = []

        # Generamos los hijos
        for chromosome_1, chromosome_2 in itertools.combinations(all_chromosome, 2):
            offspring_1, offspring_2 = reproduction_sudoku(chromosome_1, chromosome_2)
            sibling_chromosomes_list.extend([offspring_1, offspring_2])

        # Vemos si algún hijo muta
        sibling_chromosomes_list = [mutate_chromosome_sudoku_with_temperature(chromosome, not_valid_positions, temperature)
                                    for chromosome in sibling_chromosomes_list]

        # Diezmamos a la población inicial a una décima parte de la original
        current_population = current_population[:number_population // 10]

        # Creamos la nueva generación de estados usando el cromosoma obtenido
        # Y los agregamos a la generación anterior diezmada. Es decir, mantenemos los mejores padres.
        current_population += [obtain_sibling_from_chromosome_sudoku(chromosome, squares) for chromosome in
                               sibling_chromosomes_list]

    # Si terminamos las iteraciones, retornamos el mejor resultado encontrado
    return best_state, best_cost, best_iteration
