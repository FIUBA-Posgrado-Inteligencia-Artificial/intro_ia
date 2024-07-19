import json
import pygame
import sys

# Importing custom modules
import animator
import background
import logic
import sprites
import synchronizer
from constants import *


# ----------------------------------------------
# Sequence Loading
# ----------------------------------------------

# Function to load configuration from JSON file
def load_configuration(file_path):
    with open(file_path, "r") as json_file:
        return json.load(json_file)


# Load initial and sequence states
initial_state = load_configuration("./initial_state.json")
sequence = load_configuration("./sequence.json")

# This two variable are important for the animator and the sequencer
number_of_disks = sprites.obtain_number_of_disks(initial_state)
disk_height = sprites.obtain_disks_height(number_of_disks)


# ----------------------------------------------
# Pygame Initialization
# ----------------------------------------------

# Initialize Pygame and create the display screen
def initialize_pygame():
    pygame.init()
    return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Main game loop
def main():
    # Initialize Pygame
    screen = initialize_pygame()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Hanoi's tower simulation")

    # Initialize the logic (registers how many disks are in each peg and the height of the tower per each peg)
    hanoi_base = logic.initialize_logic(initial_state, disk_height)

    # Initialize the disk sprites
    disks_sprites_groups = pygame.sprite.Group()
    disks_sprites = sprites.create_sprites(number_of_disks, disk_height, hanoi_base, initial_state)
    for disk_id in disks_sprites:
        disks_sprites_groups.add(disks_sprites[disk_id])

    # Initiate the synchronizer
    sync_manager = synchronizer.Synchronizer(sequence)
    # Initiate the animator
    anim_manager = animator.Animator(hanoi_base, disk_height)

    # Flag to execute the next sequence
    flag_execute_next_seq = anim_manager.ask_new_seq

    while True:  # Sequence Loop
        handle_events()  # Handle Pygame events

        # Synchronize
        if flag_execute_next_seq:
            seq = sync_manager.update()  # Get the next sequence from the synchronizer
            anim_manager.get_sequence(seq)  # Pass the sequence to the animator

        # Animation
        anim_manager.animate(disks_sprites)  # Animate the disks
        disks_sprites_groups.update()  # Update the disk sprites
        flag_execute_next_seq = anim_manager.ask_new_seq  # Check if there's a new sequence to execute

        # Draw all elements
        background.draw_background(screen)  # Draw the background
        disks_sprites_groups.draw(screen)  # Draw the disk sprites

        pygame.display.flip()  # Update the display

        # Limit the FPS by sleeping for the remainder of the frame time
        clock.tick(FPS)


# Handle Pygame events
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


# -----------
if __name__ == "__main__":
    main()
