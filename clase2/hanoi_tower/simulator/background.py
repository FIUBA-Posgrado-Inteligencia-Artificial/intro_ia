import pygame
from constants import *


def draw_pegs(display: pygame.display, color=(130, 130, 130)):
    """
    Draws the pegs on the display.

    Parameters:
    - display (pygame.display): The display surface to draw on.
    - color (tuple): RGB color tuple representing the color of the pegs. Default is (130, 130, 130).
    """

    # Calculate left positions of each peg
    peg_1_left = int(PEG_CENTER_CENTER - PEGS_WIDTH/2)
    peg_2_left = int(PEG_LEFT_CENTER - PEGS_WIDTH/2)
    peg_3_left = int(PEG_RIGHT_CENTER - PEGS_WIDTH/2)

    # Draw base and pegs
    pygame.draw.rect(display, color, pygame.Rect(BASE_LEFT, BASE_TOP, SCREEN_WIDTH - 2 * BASE_LEFT, PEGS_WIDTH))
    pygame.draw.rect(display, color, pygame.Rect(peg_1_left, PEGS_TOP, PEGS_WIDTH, PEGS_HEIGHT))
    pygame.draw.rect(display, color, pygame.Rect(peg_2_left, PEGS_TOP, PEGS_WIDTH, PEGS_HEIGHT))
    pygame.draw.rect(display, color, pygame.Rect(peg_3_left, PEGS_TOP, PEGS_WIDTH, PEGS_HEIGHT))


def draw_background(display: pygame.display):
    """
    Draws the background on the display.

    Parameters:
    - display (pygame.display): The display surface to draw on.
    """
    display.fill((0, 0, 0))  # Fill the display with black color
    draw_pegs(display)  # Draw the pegs on the display
