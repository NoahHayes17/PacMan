from enum import IntEnum

# Screen
DISPLAY_W = 800
DISPLAY_H = 800
FPS = 60

# Pacman Layout
X_OFFSET = 50
Y_OFFSET = 80
BLOCK_SIZE = 30
PELL_SIZE = 2.5
GHOST_RADIUS = BLOCK_SIZE - 15.4

# Pacman and ghost move by one step
STEP = 1.5

DATA_FONT_SIZE = 18
DATA_FONT_COLOR =  (140,140,140)

ROCKET_FILENAME = 'pngs/rocket.png'

class Direction(IntEnum):
    right = 0
    down = 1
    up = 2
    left = 3

class GhostName(IntEnum):
    inky0   = 0
    blinky0 = 1
    pinky0  = 2
    clyde0  = 3
    inky1   = 4
    pinky1  = 5
    blinky1 = 6
    clyde1  = 7

class GameState:
    def __init__(self):
        self.lives = 3
        self.score = 0
        self.game_over = False

# Absolute values, not multiplied by dt otherwise the fleet loses sync
INVADER_HORIZONTAL_SPEED = 12
INVADER_VERTICAL_SPEED = 12

ROCKET_SPEED = 0.25
BOMB_SPEED = 0.35
TORPEDO_SPEED = 0.45
