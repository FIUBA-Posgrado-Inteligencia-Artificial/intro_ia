import copy
from typing import Optional


def is_sorted(test_list: list) -> bool:
    """
    Comprueba si una lista está ordenada de forma descendente.

    Args:
        test_list (list): Lista a comprobar.

    Returns:
        bool: True si la lista está ordenada de forma descendente, False en caso contrario.
    """
    if test_list == sorted(test_list, reverse=True):
        return True
    return False


class StatesHanoi:
    """
    Representa un estado posible de ubicación de discos de la Torre de Hanoi.
    """

    def __init__(self, rod1: list, rod2: list, rod3: list, max_disks: int = 5, cost: float = 0.0):
        """
        Inicializa un estado posible de ubicación de discos de la Torre de Hanoi.

        Args:
            rod1 (list): Discos en la primera varilla.
            rod2 (list): Discos en la segunda varilla.
            rod3 (list): Discos en la tercera varilla.
            max_disks (int): Máximo número de discos permitidos.
            cost (float): Costo asociado al estado.
        """
        # Comprobamos si es un estado ilegal
        if (set.intersection(set(rod1), set(rod2)) or
                set.intersection(set(rod2), set(rod3)) or
                set.intersection(set(rod1), set(rod3))):
            raise ValueError('El mismo disco está en varillas diferentes')

        all_values = set.union(set(rod1), set(rod2), set(rod3))
        if not all(0 < i < (max_disks + 1) for i in all_values):
            raise ValueError('Valor de disco incorrecto')

        if not all(i in all_values for i in range(1, max_disks + 1)):
            raise ValueError('No todos los discos están insertados')

        for rod in [rod1, rod2, rod3]:
            if not is_sorted(rod):
                raise ValueError('No es un estado de Hanoi válido')

        self.rods = [rod1, rod2, rod3]
        self.number_of_disks = sum([len(rod) for rod in self.rods])
        self.number_of_pegs = 3
        self.accumulated_cost = cost

        self.string_representation = ""
        self.generate_representation()

    def generate_representation(self):
        """
        Genera una representación en forma de string del estado de Hanoi.
        """
        strings = 'HanoiState: '
        for rod in self.rods:
            strings += ' '.join(str(disk) for disk in rod)
            strings += " | "
        self.string_representation = strings[:-3]

    def __eq__(self, other):
        """
        Compara dos estados de Hanoi para verificar si son iguales.

        Dos estados de Hanoi son iguales si tienen la misma cantidad de discos y la misma ubicación.

        Args:
            other: Otro estado de Hanoi a comparar.

        Returns:
            bool: True si los estados son iguales, False en caso contrario.
        """
        if self.number_of_disks == other.number_of_disks:
            if self.rods == other.rods:
                return True

    def __repr__(self):
        """
        Representación formal de un objeto StatesHanoi.

        Returns:
            str: Cadena que representa el estado de Hanoi.
        """
        self.generate_representation()
        return self.string_representation

    def __str__(self):
        """
        Representación en string de un objeto StatesHanoi.

        Returns:
            str: Cadena que representa el estado de Hanoi.
        """
        self.generate_representation()
        return self.string_representation

    def __hash__(self):
        """
        Genera un hash para el objeto StatesHanoi.

        Returns:
            int: Hash generado para el estado de Hanoi.
        """
        self.generate_representation()
        return hash(self.string_representation)

    def get_last_disk_rod(self, number_rod: int, peek: bool = False) -> Optional[int]:
        """
        Obtiene el último disco de una varilla específica.

        Args:
            number_rod (int): Índice de la varilla.
            peek (bool): Indica si se desea solo obtener el último disco sin eliminarlo de la varilla.

        Returns:
            Optional[int]: El último disco de la varilla si existe, None en caso contrario.
        """
        rod = self.rods[number_rod]
        if len(rod) != 0:
            if peek:
                return rod[-1]
            return rod.pop()
        return None

    def check_valid_disk_in_rod(self, number_rod: int, disk: int) -> bool:
        """
        Comprueba si es válido colocar un disco en una varilla específica.

        Args:
            number_rod (int): Índice de la varilla.
            disk (int): Número del disco a colocar.

        Returns:
            bool: True si es válido colocar el disco en la varilla, False en caso contrario.
        """
        last_disk_in_rod = self.get_last_disk_rod(number_rod, peek=True)
        if last_disk_in_rod:
            if last_disk_in_rod > disk:
                return True
        else:
            return True
        return False

    def put_disk_in_rod(self, number_rod: int, disk: int):
        """
        Coloca un disco en una varilla específica.

        Args:
            number_rod (int): Índice de la varilla.
            disk (int): Número del disco a colocar.
        """
        if self.check_valid_disk_in_rod(number_rod, disk):
            self.rods[number_rod].append(disk)

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

    def get_state(self) -> list:
        """
        Obtiene una representación del estado de Hanoi.

        Returns:
            list: Lista que representa el estado de Hanoi.
        """
        return self.rods

    def get_state_dict(self) -> dict:
        """
        Obtiene una representación del estado de Hanoi como un diccionario.

        Returns:
            dict: Diccionario que representa el estado de Hanoi.
        """
        return_dict = {}
        for index, rod in enumerate(self.rods):
            return_dict[f'peg_{index+1}'] = rod
        return return_dict


class ActionHanoi:
    """
    Representa una acción en el problema de la Torre de Hanoi.
    """

    def __init__(self, disk: int, rod_input: int, rod_out: int):
        """
        Inicializa una acción para mover un disco de la Torre de Hanoi.

        Args:
            disk (int): Número del disco.
            rod_input (int): Índice de la varilla de entrada.
            rod_out (int): Índice de la varilla de salida.
        """
        self.disk = disk
        self.rod_input = rod_input

        if rod_input != rod_out:
            self.action = f"Move disk {disk} from {rod_input + 1} to {rod_out + 1}"
            self.action_dict = {
                "type": "movement",
                "disk": disk,
                "peg_start": rod_input + 1,
                "peg_end": rod_out + 1
            }
            self.cost = 1.0
            self.rod_out = rod_out
        else:
            self.action = f"Maintain disk {disk} in {rod_input + 1}"
            self.action_dict = {
                "type": "maintain",
                "disk": disk,
                "peg": rod_input + 1
            }
            self.cost = 0.0
            self.rod_out = rod_input

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
            str: String que representa la acción.
        """
        return self.action

    def execute(self, state_hanoi: StatesHanoi):
        """
        Ejecuta la acción en un estado de Hanoi dado.

        Args:
            state_hanoi (StatesHanoi): Estado de Hanoi en el que se ejecutará la acción.

        Returns:
            StatesHanoi: Nuevo estado de Hanoi después de ejecutar la acción.
        """
        if "move" in self.action.lower():
            state_out = copy.deepcopy(state_hanoi)

            disk = state_out.get_last_disk_rod(self.rod_input)
            state_out.put_disk_in_rod(self.rod_out, disk)
            state_out.accumulate_cost(self.cost)
            return state_out
        return state_hanoi
