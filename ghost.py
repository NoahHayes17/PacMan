import pygame
from defs import *
import random
from pacman import *

inky0_lookup = [
    [   0, 30, 30, 30 ], # Right 
    [  60, 30, 30, 30 ], # Down
    [ 120, 30, 30, 30 ], # Up
    [ 180, 30, 30, 30 ]  # Left
]

pinky0_lookup = [
    [   0, 60, 30, 30 ], # Right
    [  60, 60, 30, 30 ], # Down
    [ 120, 60, 30, 30 ], # Up
    [ 180, 60, 30, 30 ]  # Left
]

blinky0_lookup = [
    [   0, 90, 30, 30 ], # Right
    [  60, 90, 30, 30 ], # Down
    [ 120, 90, 30, 30 ], # Up
    [ 180, 90, 30, 30 ]  # Left
]

clyde0_lookup = [
    [   0, 120, 30, 30 ], # Right
    [  60, 120, 30, 30 ], # Down
    [ 120, 120, 30, 30 ], # Up
    [ 180, 120, 30, 30 ]  # Left
]

inky1_lookup = [
    [  30, 30, 30, 30 ], # Right 
    [  90, 30, 30, 30 ], # Down
    [ 150, 30, 30, 30 ], # Up
    [ 210, 30, 30, 30 ]  # Left
]

pinky1_lookup = [
    [  30, 60, 30, 30 ], # Right
    [  90, 60, 30, 30 ], # Down
    [ 150, 60, 30, 30 ], # Up
    [ 210, 60, 30, 30 ]  # Left
]

blinky1_lookup = [
    [  30, 90, 30, 30 ], # Right
    [  90, 90, 30, 30 ], # Down
    [ 150, 90, 30, 30 ], # Up
    [ 210, 90, 30, 30 ]  # Left
]

clyde1_lookup = [
    [  30, 120, 30, 30 ], # Right
    [  90, 120, 30, 30 ], # Down
    [ 150, 120, 30, 30 ], # Up
    [ 210, 120, 30, 30 ]  # Left
]

sprite_lookup0 = [ inky0_lookup, pinky0_lookup, blinky0_lookup, clyde0_lookup]
sprite_lookup1 = [ inky1_lookup, pinky1_lookup, blinky1_lookup, clyde1_lookup ]

class Ghost(Pacman):
    def __init__(self, game_display, ghostName_lookup, maze, x, y, s1, s2, s3, s4):
        Pacman.__init__(self, game_display, maze, s1, s2, s3, s4)
        self.name = ghostName_lookup
        self.x = x
        self.y = y
        self.counter = 0

    def draw(self):
        self.counter = self.counter + 1
        print(self.counter)
        if (int(self.counter/5) % 2) == 0:
            self.selection = sprite_lookup0[self.name][self.direction]
        else:
            self.selection = sprite_lookup1[self.name][self.direction]
    
        self.game_display.blit(self.image, (self.x-GHOST_RADIUS, self.y-GHOST_RADIUS), self.selection)
        self.move()

    def move(self):
        possible_directions = Pacman.get_possible_directions(self)
        self.opposite_direction = self.find_opposite_direction()

        i = random.randint(0, len(possible_directions) - 1 )
        if possible_directions[i] != self.opposite_direction:
            self.direction = possible_directions[i] 
        Pacman.move_common(self)

    def find_opposite_direction(self):
        if self.direction == Direction.left:
            self.opposite_direction = Direction.right
        if self.direction == Direction.right:
            self.opposite_direction = Direction.left
        if self.direction == Direction.up:
            self.opposite_direction = Direction.down
        if self.direction == Direction.down:
            self.opposite_direction = Direction.up
        return self.opposite_direction