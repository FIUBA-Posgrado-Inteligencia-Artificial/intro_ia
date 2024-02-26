import pygame
import random

import matplotlib.colors as mcolors

import logic
from constants import *


# List of colors for disks
colors = list(mcolors.XKCD_COLORS.values())


class HanoiDiskSprites(pygame.sprite.Sprite):
    """
    Initializes a HanoiDiskSprites object.

    Parameters:
    - id_number (int): The ID number of the disk.
    - width (int): The width of the disk.
    - height (int): The height of the disk.
    - color (tuple): The color of the disk.
    - center_coord (tuple): The center coordinates of the disk.
    """
    def __init__(self, id_number, width, height, color, center_coord):
        super().__init__()
        self.id_number = id_number
        self.width = width
        self.height = height
        self.color = color

        left = int(center_coord[0] - self.width / 2)
        top = int(center_coord[1] - self.height / 2)

        # generate the sprite
        self.image = pygame.Surface([self.width, self.height])
        pygame.draw.rect(self.image,
                         self.color,
                         pygame.Rect(0, 0, self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = left
        self.rect.y = top
        self.center = self.rect.center


    def move_sprite(self, delta_x=0, delta_y=0):
        """
        Moves the sprite by the specified deltas.

        Parameters:
        - delta_x (int): The change in the x-coordinate.
        - delta_y (int): The change in the y-coordinate.
        """
        self.rect.x += delta_x
        self.rect.y += delta_y
        self.center = self.rect.center

    def force_pos_spite(self, x=None, y=None):
        """
        Forces the sprite to a specific position.

        Parameters:
        - x (int): The x-coordinate of the position.
        - y (int): The y-coordinate of the position.
        """
        if x is None:
            x = self.center[0]
        if y is None:
            y = self.center[1]

        self.rect.x = int(x - self.width / 2)
        self.rect.y = int(y - self.height / 2)
        self.center = self.rect.center


def obtain_number_of_disks(initial_state: dict) -> int:
    """
    Obtains the total number of disks in the initial state.

    Parameters:
    - initial_state (dict): The initial state of the tower.

    Returns:
    - int: The total number of disks.
    """
    temp = []
    for peg_name in initial_state:
        temp.append(set(initial_state[peg_name]))
    return len(set.union(*temp))


def obtain_disks_height(number_of_disk: int) -> int:
    """
    Obtains the height of each disk based on the number of disks.

    Parameters:
    - number_of_disk (int): The total number of disks.

    Returns:
    - int: The height of each disk.
    """
    disk_height = int(MAX_TOWER_HEIGHT / number_of_disk - SPACE_DISK_HEIGHT)
    if disk_height > MAX_DISK_HEIGHT:
        disk_height = MAX_DISK_HEIGHT
    if disk_height < MIN_DISK_HEIGHT:
        raise ValueError("Too many disks")

    return disk_height


def obtain_disks_geometries(number_of_disk: int, disk_height: int) -> dict:
    """
    Obtains the geometries of each disk.

    Parameters:
    - number_of_disk (int): The total number of disks.
    - disk_height (int): The height of each disk.

    Returns:
    - dict: A dictionary containing the geometries of each disk.
    """
    delta_width = int((MAX_DISK_WIDTH - MIN_DISK_WIDTH) / number_of_disk)

    disk_width = MAX_DISK_WIDTH
    disks_geometries = {}
    for i in reversed(range(number_of_disk)):
        color_index = random.randint(0, len(colors))
        disks_geometries[i + 1] = {"width": disk_width,
                                   "height": disk_height,
                                   "color": colors[color_index]
                                   }
        disk_width -= delta_width

    return disks_geometries


def create_sprites(number_of_disk: int, disk_height: int, base_logic: logic.HanoiBaseLogic, initial_state: dict):
    """
    Creates disk sprites based on the initial state and tower logic.

    Parameters:
    - number_of_disk (int): The total number of disks.
    - disk_height (int): The height of each disk.
    - base_logic (HanoiBaseLogic): The base logic of the tower.
    - initial_state (dict): The initial state of the tower.

    Returns:
    - dict: A dictionary containing the disk sprites.
    """
    disks_geometries = obtain_disks_geometries(number_of_disk, disk_height)

    sprites_stack = {}
    for peg in base_logic.pegs:
        disk_position = peg.get_position_of_all_disks(disk_height)

        for index, disk_id in enumerate(reversed(initial_state[f"peg_{peg.id_peg}"])):

            disk_geometry = disks_geometries[disk_id]
            disk_sprite = HanoiDiskSprites(id_number=disk_id,
                                           width=disk_geometry["width"],
                                           height=disk_geometry["height"],
                                           color=disk_geometry["color"],
                                           center_coord=disk_position[index],
                                           )
            sprites_stack[disk_id] = disk_sprite

    return sprites_stack
