from constants import *


class Synchronizer:
    def __init__(self, sequence: list):
        """
        Initializes the Synchronizer object.

        Parameters:
        - sequence (list): A list containing the sequence of actions.

        Attributes:
        - queue (list): A list that stores the sequence of actions.
        - state (str): Represents the current state of the synchronizer. Possible values are 'initiation', 'sequence',
                       and 'end'.
        """
        # The syncronizer consume the sequence, so it has only one use
        self.queue = list(reversed(sequence))
        self.state = "initiation"

    def update(self) -> dict:
        """
        Updates the synchronizer state and returns the next sequence action.

        Returns:
        - dict: A dictionary representing the next sequence action.
        """
        if self.state == "initiation":
            # If in the initiation state, return the initiation sequence
            self.state = "sequence"
            seq = {
                "type": "initiation",
                "total_frames": FRAMES_INITIAL_STATE
            }
        elif self.state == "sequence":
            # If in the sequence state, pop the next action from the queue
            seq = self.queue.pop()
            seq["total_frames"] = FRAMES_ANIMATION

            # If the queue is empty, transition to the end state
            if len(self.queue) == 0:
                self.state = "end"
        else:
            # If in the end state, return the end sequence
            seq = {
                "type": "end"
            }

        return seq
