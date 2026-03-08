from constants import *


class HanoiPeg:
    """
    Initializes a HanoiPeg object.

    Parameters:
    - id_peg (int): The ID of the peg.
    - x_peg (int): The x-coordinate of the peg.
    """
    def __init__(self, id_peg: int, x_peg: int):

        self.id_peg = id_peg
        self.peg_height = BASE_TOP
        self.peg_x = x_peg
        self.number_disk_in_peg = 0

    def get_position_of_all_disks(self, disk_height: int) -> list:
        """
        Calculates the position of all disks on the peg.

        Parameters:
        - disk_height (int): The height of the disk.

        Returns:
        - list: A list of tuples representing the position of all disks on the peg.
        """
        x = self.peg_x
        y = self.peg_height + disk_height // 2

        output_list = []
        for i in range(disk_height):
            output_list.append((x, y))
            y += (disk_height + SPACE_DISK_HEIGHT)

        return output_list

    def get_next_disk_position(self, disk_height: int) -> tuple:
        """
        Calculates the position of the next disk to be added to the peg.

        Parameters:
        - disk_height (int): The height of the disk.

        Returns:
        - tuple: A tuple representing the position of the next disk.
        """
        x = self.peg_x
        y = self.peg_height - (disk_height + SPACE_DISK_HEIGHT)
        y += int(disk_height/2)
        return x, y

    def add_disk_to_peg(self, disk_height: int):
        """
        Adds a disk to the peg.

        Parameters:
        - disk_height (int): The height of the disk.
        """
        self.peg_height -= (disk_height + SPACE_DISK_HEIGHT)
        self.number_disk_in_peg += 1

    def remove_disk_from_peg(self, disk_height: int):
        """
        Removes a disk from the peg.

        Parameters:
        - disk_height (int): The height of the disk.

        Returns:
        - tuple: A tuple representing the position of the removed disk.
        """
        self.number_disk_in_peg -= 1

        x = self.peg_x
        y = self.peg_height

        self.peg_height += (disk_height + SPACE_DISK_HEIGHT)

        if self.number_disk_in_peg < 1:
            self.number_disk_in_peg = 0
            self.peg_height = BASE_TOP

        return x, y


class HanoiBaseLogic:
    """
    Initializes a HanoiBaseLogic object.

    Parameters:
    - pegs_centers (tuple): A tuple containing the centers of the pegs.
    """
    def __init__(self, pegs_centers: tuple):

        self.pegs = [HanoiPeg(1, pegs_centers[0]),
                     HanoiPeg(2, pegs_centers[1]),
                     HanoiPeg(3, pegs_centers[2])]

    def get_next_disk_position(self, id_peg: int, disk_height: int):
        """
        Retrieves the position of the next disk to be added to the peg.

        Parameters:
        - id_peg (int): The ID of the peg.
        - disk_height (int): The height of the disk.

        Returns:
        - tuple: A tuple representing the position of the next disk.
        """
        for peg in self.pegs:
            if peg.id_peg == id_peg:
                return peg.get_next_disk_position(disk_height)

    def add_disk_to_peg(self, id_peg: int, disk_height: int):
        """
        Adds a disk to the peg.

        Parameters:
        - id_peg (int): The ID of the peg.
        - disk_height (int): The height of the disk.
        """
        for peg in self.pegs:
            if peg.id_peg == id_peg:
                peg.add_disk_to_peg(disk_height)

    def remove_disk_from_peg(self, id_peg: int,  disk_height: int):
        """
        Removes a disk from the peg.

        Parameters:
        - id_peg (int): The ID of the peg.
        - disk_height (int): The height of the disk.

        Returns:
        - tuple: A tuple representing the position of the removed disk.
        """
        x, y = 0, 0
        for peg in self.pegs:
            if peg.id_peg == id_peg:
                x, y = peg.remove_disk_from_peg(disk_height)

        return x, y


def initialize_logic(initial_state: dict, disk_height: int) -> HanoiBaseLogic:
    """
    Initializes the logic for the Hanoi tower simulation.

    Parameters:
    - initial_state (dict): The initial state of the tower.
    - disk_height (int): The height of the disks.

    Returns:
    - HanoiBaseLogic: An instance of the HanoiBaseLogic class initialized with the provided initial state and disk
    height.
    """

    hanoi_base = HanoiBaseLogic((PEG_LEFT_CENTER, PEG_CENTER_CENTER, PEG_RIGHT_CENTER))

    for peg_name in initial_state:
        peg_number = int(peg_name[-1])
        for _ in initial_state[peg_name]:
            hanoi_base.add_disk_to_peg(peg_number, disk_height)

    return hanoi_base
