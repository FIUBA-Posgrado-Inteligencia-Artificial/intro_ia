import logic
from constants import *


class Animator:
    """
    Class responsible for managing animations of disk movement in the Hanoi Tower simulation.

    Attributes:
    - hanoi_logic (logic.HanoiBaseLogic): The logic module for Hanoi Tower simulation.
    - disk_height (int): Height of the disk sprite.
    - ask_new_seq (bool): Flag indicating if a new sequence needs to be executed.
    - flag_animate (bool): Flag indicating if animation is currently active.
    - frame_counter (int): Counter for animation frames.
    - complete_movement (dict): Information about the complete movement to be executed.
    """

    def __init__(self, hanoi_logic: logic.HanoiBaseLogic, disk_height: int):
        """
        Initializes the Animator.

        Parameters:
        - hanoi_logic (logic.HanoiBaseLogic): The logic module for Hanoi Tower simulation.
        - disk_height (int): Height of the disk sprite.
        """

        # Flags and counters initialization
        self.ask_new_seq = True
        self.flag_animate = False
        self.frame_counter = 0

        # Logic and disk height initialization
        self.hanoi_logic = hanoi_logic
        self.disk_height = disk_height

        # Complete movement information
        self.complete_movement = {}

    def get_sequence(self, seq):
        """
        Processes the sequence information and sets up for animation.

        Parameters:
        - seq (dict): The sequence information to be processed.
        """

        def delta_mov_per_frames(cord_in: int, cord_out: int, total_frames: int):
            """
            Calculates delta movement per frame for animation.

            Parameters:
            - cord_in (int): Starting coordinate.
            - cord_out (int): Ending coordinate.
            - total_frames (int): Total frames for the movement.

            Returns:
            - float: Delta movement per frame.
            """
            return (cord_out-cord_in) / total_frames

        # Reset animation flags and counters
        self.ask_new_seq = False
        self.frame_counter = 0
        self.flag_animate = False

        if seq["type"] == "movement":
            # Set animation flag
            self.flag_animate = True

            # Calculate starting and ending coordinates for movement
            starting_coordinates = self.hanoi_logic.remove_disk_from_peg(seq["peg_start"], self.disk_height)
            ending_cordinates = self.hanoi_logic.get_next_disk_position(seq["peg_end"], self.disk_height)
            self.hanoi_logic.add_disk_to_peg(seq["peg_end"], self.disk_height)

            # Split animation into three parts
            frames_per_part = seq["total_frames"] // 3

            # Calculate delta movement per frame for each part of animation
            delta_frames_per_part = [delta_mov_per_frames(starting_coordinates[1], ANIM_Y_HIGHEST_POS,
                                                          frames_per_part),
                                     delta_mov_per_frames(starting_coordinates[0], ending_cordinates[0],
                                                          frames_per_part),
                                     delta_mov_per_frames(ANIM_Y_HIGHEST_POS, ending_cordinates[1],
                                                          frames_per_part)
                                     ]

            # Store complete movement information
            self.complete_movement = {
                "type":  seq["type"],
                "disk_id": seq["disk"],
                "start_coord": starting_coordinates,
                "end_coord": ending_cordinates,
                "delta_frames_per_part": delta_frames_per_part,
                "phase": 1,
            }
        # Set complete movement information for end sequence
        elif seq["type"] == "end":
            self.complete_movement = {
                "type": seq["type"]
            }
        # Set complete movement information for other sequence types
        else:
            self.complete_movement = {
                "type": seq["type"],
                "total_frames": seq["total_frames"]
            }

    def animate(self, disk_dict: dict):
        """
        Animates the movement of disk sprites.

        Parameters:
        - disk_dict (dict): Dictionary containing disk sprites.
        """

        type_seq = self.complete_movement["type"]

        if type_seq == "movement":
            if self.flag_animate:

                disk_id = self.complete_movement["disk_id"]
                delta_x = 0
                delta_y = 0

                # Execute the appropriate movement
                if self.complete_movement["phase"] == 1:
                    # For the first phase, move the disk vertically towards the highest point
                    delta_y = self.complete_movement["delta_frames_per_part"][0]
                    # Modify dynamically the velocity of movement
                    delta_y, advance_phase = modify_velocity(delta_y, disk_dict[disk_id].center[1], ANIM_Y_HIGHEST_POS)
                    self.complete_movement["delta_frames_per_part"][0] = delta_y

                elif self.complete_movement["phase"] == 2:
                    # For the second phase, move the disk horizontally towards the target peg
                    delta_x = self.complete_movement["delta_frames_per_part"][1]
                    delta_x, advance_phase = modify_velocity(delta_x, disk_dict[disk_id].center[0],
                                                             self.complete_movement["end_coord"][0])
                    self.complete_movement["delta_frames_per_part"][1] = delta_x

                else:
                    # For the third phase, move the disk vertically towards the target peg
                    delta_y = self.complete_movement["delta_frames_per_part"][2]
                    delta_y, advance_phase = modify_velocity(delta_y, disk_dict[disk_id].center[1],
                                                             self.complete_movement["end_coord"][1])
                    self.complete_movement["delta_frames_per_part"][2] = delta_y

                # Move the disk sprite
                disk_dict[disk_id].move_sprite(delta_x=delta_x, delta_y=delta_y)

                # Check if phase should advance
                if advance_phase:
                    self.complete_movement["phase"] += 1

                # If all phases are completed
                if self.complete_movement["phase"] == 4:
                    # Clean imperfections
                    disk_dict[disk_id].force_pos_spite(x=self.complete_movement["end_coord"][0],
                                                       y=self.complete_movement["end_coord"][1])
                    # Reset flags and counters
                    self.ask_new_seq = True
                    self.flag_animate = False
                    self.frame_counter = 0

        else:
            # If it's not a movement sequence
            self.frame_counter += 1
            if type_seq == "end":
                self.frame_counter = 0
            elif self.frame_counter > self.complete_movement["total_frames"]:
                # Reset flags and counters
                self.ask_new_seq = True
                self.flag_animate = False


def modify_velocity(delta: int, cord_start: int, cord_end: int) -> tuple:
    """
    Modifies velocity of movement.

    Parameters:
    - delta (int): Delta movement.
    - cord_start (int): Starting coordinate.
    - cord_end (int): Ending coordinate.

    Returns:
    - int: Modified delta movement.
    - bool: Flag indicating if phase should advance.
    """
    distance_to_objective = cord_end - cord_start

    # If distance is very small, set delta to 0 and advance phase
    if abs(distance_to_objective) < 1:
        return 0, True

    # If delta is smaller than remaining distance, keep delta as is
    if abs(delta) < abs(distance_to_objective):
        return delta, False

    # Otherwise, reduce delta to half of the remaining distance
    new_delta = int(distance_to_objective / 2)

    # Ensure new delta is not too small
    if abs(new_delta) < 1:
        new_delta = 1
        # Ensure new delta has the same sign as the distance to objective
        if distance_to_objective < 0:
            new_delta *= -1

    return new_delta, False
