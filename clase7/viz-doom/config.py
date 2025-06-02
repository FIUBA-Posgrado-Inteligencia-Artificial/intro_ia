from enum import Enum


class Actions(Enum):
    MOV_LEFT = 0
    MOV_RIGHT = 1
    SHOOT = 2
    STAND = 3

# Constants
NUMBER_OF_EPISODES = 2
MAX_MOVS = 15

PLAYER_INITIAL = 4

LEFT_WALL = 240
RIGHT_WALL = -170
BLOCK = 51.25
LAST_BLOCK = 7
FIRST_BLOCK = 0
POS_BLOCK_RANGE = tuple([BLOCK*i + RIGHT_WALL for i in range(1, 8)])

class AnimationConstants:
    PLAYER_START_UP_FPS = 60
    ANIM_MOV_STOP_FPS = 60
    ANIM_MOV_THINK_FPS = 70
    ANIM_PLAYER_SHOOT = 10
    ANIM_PLAYER_WAIT_AFTER_SHOOT = 50
