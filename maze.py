import pygame
from defs import *
from block import Block
from pellet import Pellet

class Maze:
    def __init__(self, game_display, game_state):
        self.game_display = game_display
        self.game_state = game_state
        self.maze = ["BBBBBBBBBBBBBBBBB",
                     "B...............B",
                     "B.BB.BBB.BBB.BB.B",
                     "B...............B",
                     "B.B.BB.B.B.BB.B.B",
                     "B....B.B.B.B....B",
                     "B.BB.B.B.B.B.BB.B",
                     "B.BB.B.....B.BB.B",
                     "B....B.BBB.B....B",
                     "B.BB.B.....B.BB.B",
                     "B.BB.BBB.BBB.BB.B",
                     "B...............B",
                     "B.BBB.BBBBB.BBB.B",
                     "B.BB....B....BB.B",
                     "B.BB.BB.B.BB.BB.B",
                     "B...............B",
                     "BBBBBBBBBBBBBBBBB"]
        self.blocks = []
        self.pel = []
        self.eaten_list = []

        for y in range(0, len(self.maze)):
            for x in range(0, len(self.maze[y])):
                if self.maze[y][x] == "B":
                   block_x = (x * BLOCK_SIZE) + X_OFFSET
                   block_y = (y * BLOCK_SIZE) + Y_OFFSET
                   new_block = Block(block_x, block_y)
                   self.blocks.append(new_block)
                
                if self.maze[y][x] == ".":
                   pel_x = (x * BLOCK_SIZE) + X_OFFSET
                   pel_y = (y * BLOCK_SIZE) + Y_OFFSET
                   new_pel = Pellet(pel_x, pel_y)
                   self.pel.append(new_pel)
  
    def draw_blocks(self):
        for block in self.blocks:
            x = block.x
            y = block.y
            pygame.draw.rect(self.game_display, pygame.Color("blue"), (x, y, BLOCK_SIZE, BLOCK_SIZE))

    def draw_pellets(self):
        for pell in self.pel:
            x = pell.x + (BLOCK_SIZE / 2)
            y = pell.y + (BLOCK_SIZE / 2)
            pygame.draw.circle(self.game_display, pygame.Color("white"), (x, y), PELL_SIZE)
        
        for pell in self.eaten_list:
            x = pell.x + (BLOCK_SIZE / 2)
            y = pell.y + (BLOCK_SIZE / 2)
            pygame.draw.rect(self.game_display, pygame.Color("black"), (x - (BLOCK_SIZE / 2), y - (BLOCK_SIZE / 2), BLOCK_SIZE, BLOCK_SIZE))

    def is_eaten(self, pac_x, pac_y, pac_rad):
        for pell in self.pel:
            x = pell.x + (BLOCK_SIZE / 2)
            y = pell.y + (BLOCK_SIZE / 2)
    
            if (pac_x - pac_rad <= x <= pac_x + pac_rad) and (pac_y - pac_rad <= y <= pac_y + pac_rad):
                if not pell in self.eaten_list:
                    self.eaten_list.append(pell)
                    self.game_state.score += 1
                    
        if len(self.eaten_list) == len(self.pel):
            self.game_state.game_won = True

    def is_colliding(self, x, y, r, direction):
        fudge = 1
        
        for block in self.blocks:
            if direction == Direction.left:
                if block.x + fudge < x - r < block.x + BLOCK_SIZE and \
                   (block.y < y - r < block.y + BLOCK_SIZE or 
                    block.y < y + r < block.y + BLOCK_SIZE):
                    return True
            elif direction == Direction.right:
                if block.x < x + r < block.x + BLOCK_SIZE and \
                   (block.y < y - r < block.y + BLOCK_SIZE or 
                    block.y < y + r < block.y + BLOCK_SIZE):
                    return True
            elif direction == Direction.up:
                if block.y < y - r < block.y + BLOCK_SIZE and \
                   (block.x < x - r < block.x + BLOCK_SIZE or 
                    block.x < x + r < block.x + BLOCK_SIZE):
                    return True
            elif direction == Direction.down:
                if block.y < y + r < block.y + BLOCK_SIZE and \
                   (block.x < x - r < block.x + BLOCK_SIZE or 
                    block.x < x + r < block.x + BLOCK_SIZE):
                    return True
        
        return False