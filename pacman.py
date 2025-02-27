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
        self.animation_counter = 0
        self.animation_frames = [
            pygame.Rect(0, 0, 30, 30),    # Mouth fully open
            pygame.Rect(30, 0, 30, 30),   # Mouth partially open
            pygame.Rect(60, 0, 30, 30)    # Mouth closed
        ]
        self.moving = False

    def draw(self):
        if self.moving:
            self.animation_counter = (self.animation_counter + 1) % 25
            if self.animation_counter < 10:
                frame = 0  # Mouth fully open
            elif self.animation_counter < 20:
                frame = 1  # Mouth half open
            else:
                frame = 2  # Mouth closed
        else:
            frame = 0 
        
        # Select the correct animation frame and rotate based on direction
        self.selection = self.animation_frames[frame]
        
        # Create a surface with the Pacman sprite
        pacman_surface = pygame.Surface((30, 30), pygame.SRCALPHA)
        pacman_surface.blit(self.image, (0, 0), self.selection)
        
        # Rotate based on direction
        if self.direction == Direction.right:
            rotated_surface = pacman_surface  # No rotation
        elif self.direction == Direction.left:
            rotated_surface = pygame.transform.rotate(pacman_surface, 180)
        elif self.direction == Direction.up:
            rotated_surface = pygame.transform.rotate(pacman_surface, 90)
        elif self.direction == Direction.down:
            rotated_surface = pygame.transform.rotate(pacman_surface, 270)
            
        self.game_display.blit(rotated_surface, (self.x-self.radius, self.y-self.radius))
        self.move()
        self.maze.is_eaten(self.x, self.y, self.radius)

    def move(self):
        possible_directions = self.get_possible_directions()

        for i in possible_directions:
            if i == self.direction_request:
                self.direction = self.direction_request
                
        old_x, old_y = self.x, self.y
        self.move_common()
        # Check if Pacman actually moved
        self.moving = (old_x != self.x or old_y != self.y)

    def move_common(self):
        new_x = self.x
        new_y = self.y
        if self.direction == Direction.left:
            new_x -= STEP
        if self.direction == Direction.right:
            new_x += STEP
        if self.direction == Direction.up:
            new_y -= STEP
        if self.direction == Direction.down:
            new_y += STEP

        if not self.maze.is_colliding(new_x, new_y, self.radius, self.direction):
            self.x = new_x
            self.y = new_y

    def get_possible_directions(self):
        possible_directions = []
        if not self.maze.is_colliding(self.x - STEP, self.y, self.radius, Direction.left):
            possible_directions.append(Direction.left)
        if not self.maze.is_colliding(self.x + STEP, self.y, self.radius, Direction.right):
            possible_directions.append(Direction.right)
        if not self.maze.is_colliding(self.x, self.y - STEP, self.radius, Direction.up):
            possible_directions.append(Direction.up)
        if not self.maze.is_colliding(self.x, self.y + STEP, self.radius, Direction.down):
            possible_directions.append(Direction.down)
        return possible_directions

    def set_direction_request(self, direction):
        self.direction_request = direction
