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
            print(self.maze[y])
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
        for b in self.blocks:
            block_n = b
            x = block_n.xpos
            y = block_n.ypos
            pygame.draw.rect(self.game_display, pygame.Color("blue"), (x, y, BLOCK_SIZE, BLOCK_SIZE))

    def draw_pellets(self):
        for p in self.pel:
            pel_n = p 
            x = pel_n.pel_x + (BLOCK_SIZE / 2)
            y = pel_n.pel_y + (BLOCK_SIZE / 2)
            pygame.draw.circle(self.game_display, pygame.Color("white"), (x, y), PELL_SIZE)
        
        for p in self.eaten_list:
            pel_n = p
            pel_x = pel_n.pel_x + (BLOCK_SIZE / 2)
            pel_y = pel_n.pel_y + (BLOCK_SIZE / 2)
            pygame.draw.rect(self.game_display, pygame.Color("black"), (pel_x - (BLOCK_SIZE / 2), pel_y - (BLOCK_SIZE / 2), BLOCK_SIZE, BLOCK_SIZE))

    def is_eaten(self, pac_x, pac_y, pac_rad):
        for p in self.pel:
            pel_n = p
            pel_x = pel_n.pel_x + (BLOCK_SIZE / 2)
            pel_y = pel_n.pel_y + (BLOCK_SIZE / 2)
            pac_x = pac_x
            pac_y = pac_y
            pac_rad = pac_rad

            if (pac_x - pac_rad <= pel_x <= pac_x + pac_rad) and (pac_y - pac_rad <= pel_y <= pac_y + pac_rad):
                if not p in self.eaten_list:
                    self.eaten_list.append(p)
                    self.game_state.score += 1
                print(len(self.eaten_list))

    def is_colliding(self, x, y, r, direction):
        list_of_detected_collisions = []
        fudge = 1

        for b in self.blocks:
            block_n = b
            block_x = block_n.xpos
            block_y = block_n.ypos
            pac_x = x
            pac_y = y
            pac_rad = r

            if direction == Direction.left:
              if ((block_x + fudge< pac_x - pac_rad < block_x + BLOCK_SIZE) and ((block_y < pac_y - pac_rad < block_y + BLOCK_SIZE) or (block_y < pac_y + pac_rad < block_y + BLOCK_SIZE))):
                  list_of_detected_collisions.append(" collided with left ")
            elif direction == Direction.right:
              if ((block_x < pac_x + pac_rad < block_x + BLOCK_SIZE) and ((block_y < pac_y - pac_rad < block_y + BLOCK_SIZE) or (block_y < pac_y + pac_rad < block_y + BLOCK_SIZE))):
                  list_of_detected_collisions.append(" collided with right ")
            elif direction == Direction.up:
              if ((block_y < pac_y - pac_rad < block_y + BLOCK_SIZE) and ((block_x < pac_x - pac_rad < block_x + BLOCK_SIZE) or (block_x < pac_x + pac_rad < block_x + BLOCK_SIZE))):
                  list_of_detected_collisions.append(" collided with up ")
            elif direction == Direction.down:
              if ((block_y < pac_y + pac_rad < block_y + BLOCK_SIZE) and ((block_x < pac_x - pac_rad < block_x + BLOCK_SIZE) or (block_x < pac_x + pac_rad < block_x + BLOCK_SIZE))):
                  list_of_detected_collisions.append(" collided with down ")

        for i in list_of_detected_collisions:
            if i == "collided with left" or "collided with right" or "collided with up" or "collided with down":
              return True
        else:
            return False