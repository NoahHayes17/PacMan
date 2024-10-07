import pygame
from defs import *

class Pacman:
    def __init__(self, game_display, maze, s1, s2, s3, s4):
        self.game_display = game_display
        self.maze = maze
        self.radius = (BLOCK_SIZE - 15.4)
        self.x = X_OFFSET + BLOCK_SIZE + self.radius 
        self.y = Y_OFFSET + BLOCK_SIZE + self.radius
        self.direction = Direction.right
        self.direction_request = Direction.right
        self.image = pygame.image.load("png/PacmanSprites.png")
        self.selection = pygame.Rect(s1, s2, s3, s4)

    def draw(self):
        self.game_display.blit(self.image, (self.x-GHOST_RADIUS, self.y-GHOST_RADIUS), self.selection)
        self.move()
        pac_x = self.x
        pac_y = self.y
        pac_rad = self.radius
        self.maze.is_eaten(pac_x, pac_y, pac_rad)

    def move(self):
        possible_directions = self.get_possible_directions()

        for i in possible_directions:
            if i == self.direction_request:
                self.direction = self.direction_request

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

    def set_direction_request(self, direction):
        self.direction_request = direction
