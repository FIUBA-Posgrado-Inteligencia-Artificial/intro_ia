"""
Algoritmos de búsqueda local para la gira. Son las mismas implementaciones que se
explican paso a paso en las notebooks, para poder reutilizarlas en las notebooks
siguientes.
"""

import math
import random

import numpy as np

import gira

# Cada cuántas iteraciones de Simulated Annealing se guarda el historial
HISTORY_EVERY = 100

# Parámetros fijos del algoritmo genético: cuántas giras compiten en cada torneo y
# cuántas de las mejores pasan directo a la generación siguiente
TOURNAMENT_SIZE = 3
ELITE_SIZE = 2


def gradient_descent(
    tour: list, distances: np.ndarray, max_iterations: int = 10_000
) -> tuple:
    """
    Busca la mejor gira con gradiente descendente: en cada paso se mueve al mejor
    vecino y se detiene cuando ningún vecino mejora la gira actual.

    Args:
        tour (list): Gira desde donde arranca la búsqueda.
        distances (np.ndarray): Matriz de distancias entre ciudades.
        max_iterations (int, opcional): Cantidad máxima de pasos. Por defecto 10.000.

    Returns:
        tuple: (la gira encontrada, lista con el costo de la gira en cada paso)
    """
    moves = gira.obtain_moves(len(tour))
    history = [gira.cost_function(tour, distances)]

    for _ in range(max_iterations):
        # Cuánto cambia el costo con cada movimiento 2-opt posible
        deltas = [gira.delta_cost(tour, i, j, distances) for i, j in moves]

        # El movimiento que más reduce el costo
        best = int(np.argmin(deltas))

        # Si ningún vecino es mejor que la gira actual, llegamos a un mínimo
        if deltas[best] >= 0:
            break

        tour = gira.two_opt(tour, *moves[best])
        history.append(history[-1] + deltas[best])

    return tour, history


def stochastic_gradient_descent(
    tour: list, distances: np.ndarray, max_iterations: int = 10_000
) -> tuple:
    """
    Busca la mejor gira con gradiente descendente estocástico: en cada paso se mueve
    a un vecino al azar entre los que mejoran la gira actual, y se detiene cuando
    ningún vecino la mejora.

    Args:
        tour (list): Gira desde donde arranca la búsqueda.
        distances (np.ndarray): Matriz de distancias entre ciudades.
        max_iterations (int, opcional): Cantidad máxima de pasos. Por defecto 10.000.

    Returns:
        tuple: (la gira encontrada, lista con el costo de la gira en cada paso)
    """
    moves = gira.obtain_moves(len(tour))
    history = [gira.cost_function(tour, distances)]

    for _ in range(max_iterations):
        # Los movimientos que reducen el costo, junto con cuánto lo reducen
        improvements = []
        for i, j in moves:
            delta = gira.delta_cost(tour, i, j, distances)
            if delta < 0:
                improvements.append((i, j, delta))

        # Si ningún vecino es mejor que la gira actual, llegamos a un mínimo
        if not improvements:
            break

        i, j, delta = random.choice(improvements)
        tour = gira.two_opt(tour, i, j)
        history.append(history[-1] + delta)

    return tour, history


def simulated_annealing(
    tour: list,
    distances: np.ndarray,
    initial_temperature: float = 500,
    final_temperature: float = 1,
    max_iterations: int = 100_000,
) -> tuple:
    """
    Busca la mejor gira con Simulated Annealing. En cada iteración se elige un vecino
    al azar: si mejora la gira, se acepta; si la empeora en delta km, se acepta con
    probabilidad exp(-delta / temperatura). La temperatura baja de forma geométrica
    desde initial_temperature hasta final_temperature.

    Args:
        tour (list): Gira desde donde arranca la búsqueda.
        distances (np.ndarray): Matriz de distancias entre ciudades.
        initial_temperature (float, opcional): Temperatura inicial, en km. Por
                                               defecto 500.
        final_temperature (float, opcional): Temperatura en la última iteración, en
                                             km. Por defecto 1.
        max_iterations (int, opcional): Cantidad de iteraciones. Por defecto 100.000.

    Returns:
        tuple: (la mejor gira encontrada, diccionario con el historial: el costo de
               la gira actual, el de la mejor gira y la temperatura, cada
               HISTORY_EVERY iteraciones)
    """
    # La temperatura se multiplica por cooling_rate en cada iteración, de forma que
    # llegue a final_temperature en la última
    cooling_rate = (final_temperature / initial_temperature) ** (1 / max_iterations)
    temperature = initial_temperature

    cost = gira.cost_function(tour, distances)
    best_tour, best_cost = tour, cost
    history = {"cost": [], "best_cost": [], "temperature": []}

    for iteration in range(max_iterations):
        # Elegimos un vecino al azar y calculamos cuánto cambia el costo
        i, j = gira.random_move(len(tour))
        delta = gira.delta_cost(tour, i, j, distances)

        # Si mejora, lo aceptamos. Si empeora, lo aceptamos con probabilidad
        # exp(-delta / temperature)
        if delta < 0 or random.random() < math.exp(-delta / temperature):
            tour = gira.two_opt(tour, i, j)
            cost += delta
            if cost < best_cost:
                best_tour, best_cost = tour, cost

        if iteration % HISTORY_EVERY == 0:
            history["cost"].append(cost)
            history["best_cost"].append(best_cost)
            history["temperature"].append(temperature)

        temperature *= cooling_rate

    return best_tour, history


def local_beam_search(
    initial_tours: list, distances: np.ndarray, max_iterations: int = 10_000
) -> tuple:
    """
    Busca la mejor gira con Local Beam. Mantiene k giras: en cada paso genera todos
    los vecinos de las k giras y se queda con los k mejores. Se detiene cuando el
    mejor vecino no mejora a la mejor gira actual.

    Args:
        initial_tours (list): Las k giras desde donde arranca la búsqueda.
        distances (np.ndarray): Matriz de distancias entre ciudades.
        max_iterations (int, opcional): Cantidad máxima de pasos. Por defecto 10.000.

    Returns:
        tuple: (la mejor gira encontrada, lista con el costo de la mejor gira en cada
               paso)
    """
    k = len(initial_tours)
    moves = gira.obtain_moves(len(initial_tours[0]))

    # Cada elemento del haz es una tupla (costo, gira), ordenada de menor a mayor
    beam = sorted((gira.cost_function(tour, distances), tour) for tour in initial_tours)
    history = [beam[0][0]]

    for _ in range(max_iterations):
        # Los vecinos de todas las giras del haz. No armamos las giras vecinas:
        # guardamos su costo, de qué gira del haz salen y con qué movimiento
        successors = []
        for index, (cost, tour) in enumerate(beam):
            for i, j in moves:
                new_cost = cost + gira.delta_cost(tour, i, j, distances)
                successors.append((new_cost, index, i, j))
        successors.sort()

        # Armamos las k mejores giras vecinas, sin repetir. Dos giras distintas del
        # haz pueden tener a la misma gira como vecina
        new_beam = []
        seen = set()
        for new_cost, index, i, j in successors:
            new_tour = gira.two_opt(beam[index][1], i, j)
            if tuple(new_tour) in seen:
                continue
            seen.add(tuple(new_tour))
            new_beam.append((new_cost, new_tour))
            if len(new_beam) == k:
                break

        # Si el mejor vecino no mejora a la mejor gira del haz, terminamos
        if new_beam[0][0] >= beam[0][0]:
            break

        beam = new_beam
        history.append(beam[0][0])

    return beam[0][1], history


def stochastic_local_beam_search(
    initial_tours: list,
    distances: np.ndarray,
    temperature: float = 50,
    max_iterations: int = 300,
) -> tuple:
    """
    Busca la mejor gira con Local Beam estocástico. Mantiene k giras: en cada paso
    genera todos los vecinos de las k giras y elige k al azar, dándole más
    probabilidad a los mejores. Un vecino que es delta km peor que el mejor vecino
    tiene un peso de exp(-delta / temperatura).

    Args:
        initial_tours (list): Las k giras desde donde arranca la búsqueda.
        distances (np.ndarray): Matriz de distancias entre ciudades.
        temperature (float, opcional): Temperatura, en km. Por defecto 50.
        max_iterations (int, opcional): Cantidad de pasos. Por defecto 300.

    Returns:
        tuple: (la mejor gira encontrada, lista con el costo de la mejor gira
               encontrada hasta cada paso)
    """
    k = len(initial_tours)
    moves = gira.obtain_moves(len(initial_tours[0]))

    beam = [(gira.cost_function(tour, distances), tour) for tour in initial_tours]
    best_cost, best_tour = min(beam)
    history = [best_cost]

    for _ in range(max_iterations):
        # Los vecinos de todas las giras del haz, igual que en Local Beam
        successors = []
        for index, (cost, tour) in enumerate(beam):
            for i, j in moves:
                new_cost = cost + gira.delta_cost(tour, i, j, distances)
                successors.append((new_cost, index, i, j))

        # El peso de cada vecino depende de cuánto peor es que el mejor vecino
        lowest_cost = min(successor[0] for successor in successors)
        weights = [
            math.exp(-(successor[0] - lowest_cost) / temperature)
            for successor in successors
        ]

        # Elegimos k vecinos al azar según sus pesos. Un mismo vecino puede salir
        # elegido más de una vez
        chosen = random.choices(successors, weights=weights, k=k)
        beam = [
            (new_cost, gira.two_opt(beam[index][1], i, j))
            for new_cost, index, i, j in chosen
        ]

        best_cost, best_tour = min([(best_cost, best_tour), *beam])
        history.append(best_cost)

    return best_tour, history


def tournament_selection(population: list, costs: list) -> list:
    """
    Elige una gira de la población por torneo: toma TOURNAMENT_SIZE giras al azar y
    devuelve la de menor costo.

    Args:
        population (list): Lista de giras.
        costs (list): Costo de cada gira de la población.

    Returns:
        list: La gira ganadora del torneo.
    """
    competitors = random.sample(range(len(population)), TOURNAMENT_SIZE)
    winner = min(competitors, key=lambda index: costs[index])
    return population[winner]


def order_crossover(parent_a: list, parent_b: list) -> list:
    """
    Reproducción por orden (OX): copia un tramo al azar del padre A, en las mismas
    posiciones, y completa el resto con las ciudades que faltan en el orden en que
    aparecen en el padre B. El primer y el último lugar de la gira no se tocan.

    Args:
        parent_a (list): Gira del padre A.
        parent_b (list): Gira del padre B.

    Returns:
        list: La gira hija.
    """
    i, j = gira.random_move(len(parent_a))
    segment = parent_a[i : j + 1]

    # Las ciudades del padre B que no están en el tramo, en el orden de B
    in_segment = set(segment)
    rest = [city for city in parent_b[1:-1] if city not in in_segment]

    # Las primeras i - 1 ciudades de rest van antes del tramo y las demás, después
    middle = rest[: i - 1] + segment + rest[i - 1 :]
    return [parent_a[0], *middle, parent_a[-1]]


def improve_tour(tour: list, distances: np.ndarray, tries: int) -> list:
    """
    Mejora una gira probando movimientos 2-opt al azar y aplicando solo los que
    reducen el costo.

    Args:
        tour (list): La gira.
        distances (np.ndarray): Matriz de distancias entre ciudades.
        tries (int): Cantidad de movimientos que se prueban.

    Returns:
        list: La gira mejorada.
    """
    for _ in range(tries):
        i, j = gira.random_move(len(tour))
        if gira.delta_cost(tour, i, j, distances) < 0:
            tour = gira.two_opt(tour, i, j)
    return tour


def genetic_algorithm(
    initial_population: list,
    distances: np.ndarray,
    max_generations: int = 1_000,
    mutation_probability: float = 0.5,
    improvement_tries: int = 0,
) -> tuple:
    """
    Busca la mejor gira con un algoritmo genético. En cada generación, las
    ELITE_SIZE mejores giras pasan directo a la siguiente, y el resto de la nueva
    población se forma con hijos de dos padres elegidos por torneo, combinados con
    la reproducción por orden y mutados con un movimiento 2-opt al azar.

    Args:
        initial_population (list): Las giras de la población inicial.
        distances (np.ndarray): Matriz de distancias entre ciudades.
        max_generations (int, opcional): Cantidad de generaciones. Por defecto 1.000.
        mutation_probability (float, opcional): Probabilidad de que un hijo mute.
                                                Por defecto 0,5.
        improvement_tries (int, opcional): Si es mayor que 0, cada gira nueva se
                                           mejora con improve_tour(), probando esa
                                           cantidad de movimientos 2-opt (algoritmo
                                           memético). Por defecto 0.

    Returns:
        tuple: (la mejor gira encontrada, lista con el costo de la mejor gira de
               cada generación)
    """
    population_size = len(initial_population)
    population = [
        improve_tour(tour, distances, improvement_tries) for tour in initial_population
    ]
    costs = [gira.cost_function(tour, distances) for tour in population]
    history = [min(costs)]

    for _ in range(max_generations):
        # Elitismo: las mejores giras pasan directo a la nueva generación
        ranking = sorted(range(population_size), key=lambda index: costs[index])
        new_population = [population[index] for index in ranking[:ELITE_SIZE]]

        while len(new_population) < population_size:
            # Selección: dos padres elegidos por torneo
            parent_a = tournament_selection(population, costs)
            parent_b = tournament_selection(population, costs)

            # Reproducción y mutación
            child = order_crossover(parent_a, parent_b)
            if random.random() < mutation_probability:
                child = gira.random_neib_state(child)

            child = improve_tour(child, distances, improvement_tries)
            new_population.append(child)

        population = new_population
        costs = [gira.cost_function(tour, distances) for tour in population]
        history.append(min(costs))

    best = int(np.argmin(costs))
    return population[best], history
