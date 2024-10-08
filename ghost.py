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
        possible_directions = self.get_possible_directions()
        self.opposite_direction = self.find_opposite_direction()

        i = random.randint(0, len(possible_directions) - 1 )
        if possible_directions[i] != self.opposite_direction:
            self.direction = possible_directions[i] 

        new_x = self.x
        new_y = self.y
        if self.direction == Direction.left:
            new_x = self.x - STEP
        if self.direction == Direction.right:
            new_x = self.x + STEP
        if self.direction == Direction.up:
            new_y = self.y - STEP
        if self.direction == Direction.down:
            new_y = self.y + STEP

        if (False == self.maze.is_colliding(new_x, new_y, self.radius, self.direction)):
            self.x = new_x
            self.y = new_y
        else:
            self.x = self.x
            self.y = self.y

    def get_possible_directions(self):
        possible_directions = []
        if (False == self.maze.is_colliding(self.x - STEP, self.y, self.radius, Direction.left)):
            possible_directions.append(Direction.left)
        if (False == self.maze.is_colliding(self.x + STEP, self.y, self.radius, Direction.right)):
            possible_directions.append(Direction.right)
        if (False == self.maze.is_colliding(self.x, self.y - STEP, self.radius, Direction.up)):
            possible_directions.append(Direction.up)
        if (False == self.maze.is_colliding(self.x, self.y + STEP, self.radius, Direction.down)):
            possible_directions.append(Direction.down)
        return possible_directions

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