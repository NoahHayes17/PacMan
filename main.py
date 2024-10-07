import pygame
from defs import *
from maze import Maze
from pacman import Pacman
from ghost import Ghost

count = 0

def update_label(data, title, font, x, y, gameDisplay):
    label = font.render('{} {}'.format(title, data), 1, DATA_FONT_COLOR)
    gameDisplay.blit(label, (x, y))
    return y

def update_data_labels(gameDisplay, dt, game_time, font):
    y_pos = 0
    gap = 15
    x_pos = 10
    y_pos = update_label(round(1000/dt,2), 'FPS', font, x_pos, y_pos + gap, gameDisplay)
    y_pos = update_label(round(game_time/1000,2),'Game time', font, x_pos, y_pos + gap, gameDisplay)

def check_collisions(pacman, ghosts):
    for ghost in ghosts:
        distance = ((pacman.x - ghost.x) ** 2 + (pacman.y - ghost.y) ** 2) ** 0.5
        if distance < (pacman.radius + ghost.radius):
            return True
    return False

def show_game_over(game_display, game_state): 
    overlay = pygame.Surface((DISPLAY_W, DISPLAY_H))
    overlay.fill((0, 0, 0))
    overlay.set_alpha(128)
    game_display.blit(overlay, (0, 0))
    
    font = pygame.font.SysFont("monospace", 64)
    game_over_text = font.render("GAME OVER", True, (255, 0, 0))
    text_rect = game_over_text.get_rect(center=(DISPLAY_W/2, DISPLAY_H/2))
    game_display.blit(game_over_text, text_rect)
    
    score_font = pygame.font.SysFont("monospace", 32)
    score_text = score_font.render(f"Final Score: {game_state.score}", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(DISPLAY_W/2, DISPLAY_H/2 + 50))
    game_display.blit(score_text, score_rect)
    
    pygame.display.update()
    
    pygame.time.wait(2000)

def run_game():
    pygame.init()
    game_display = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
    pygame.display.set_caption('Pacman')
    pygame.key.set_repeat(1, 10) 

    running = True
    label_font = pygame.font.SysFont("monospace", DATA_FONT_SIZE)

    game_state = GameState()
    maze = Maze(game_display, game_state)
    
    pacman = Pacman(game_display, maze, 30, 0, 30, 30)
    pacman.x = X_OFFSET + (BLOCK_SIZE * 8) + pacman.radius  # Center horizontally
    pacman.y = Y_OFFSET + (BLOCK_SIZE * 10) + pacman.radius  # Lower half of maze

    inky_x = X_OFFSET + (BLOCK_SIZE * 1) + GHOST_RADIUS  # Top-left
    inky_y = Y_OFFSET + (BLOCK_SIZE * 1) + GHOST_RADIUS

    pinky_x = X_OFFSET + (BLOCK_SIZE * 15) + GHOST_RADIUS  # Top-right
    pinky_y = Y_OFFSET + (BLOCK_SIZE * 1) + GHOST_RADIUS

    blinky_x = X_OFFSET + (BLOCK_SIZE * 1) + GHOST_RADIUS  # Bottom-left
    blinky_y = Y_OFFSET + (BLOCK_SIZE * 15) + GHOST_RADIUS

    clyde_x = X_OFFSET + (BLOCK_SIZE * 15) + GHOST_RADIUS  # Bottom-right
    clyde_y = Y_OFFSET + (BLOCK_SIZE * 15) + GHOST_RADIUS

    ghosts = [
        Ghost(game_display, GhostName.inky0, maze, inky_x, inky_y, 0, 30, 30, 30),
        Ghost(game_display, GhostName.pinky0, maze, pinky_x, pinky_y, 0, 60, 30, 30),
        Ghost(game_display, GhostName.blinky0, maze, blinky_x, blinky_y, 0, 90, 30, 30),
        Ghost(game_display, GhostName.clyde0, maze, clyde_x, clyde_y, 0, 120, 30, 30)
    ]
    
    clock = pygame.time.Clock()
    dt = 0
    game_time = 0

    while running and not game_state.game_over:
        dt = clock.tick(FPS)
        game_time += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            pacman.set_direction_request(Direction.left)
        if keys[pygame.K_d]:
            pacman.set_direction_request(Direction.right)
        if keys[pygame.K_w]:
            pacman.set_direction_request(Direction.up)
        if keys[pygame.K_s]:
            pacman.set_direction_request(Direction.down)

        game_display.fill(pygame.Color("black"))
        update_data_labels(game_display, dt, game_time, label_font)
 
        maze.draw_blocks()
        maze.draw_pellets()        
        pacman.draw()
        
        for ghost in ghosts:
            ghost.draw()
            
        if check_collisions(pacman, ghosts):
            game_state.lives -= 1
            if game_state.lives <= 0:
                game_state.game_over = True
            else:
                pacman.x = X_OFFSET + BLOCK_SIZE + pacman.radius
                pacman.y = Y_OFFSET + BLOCK_SIZE + pacman.radius
                pygame.time.wait(1000)

        for i in range(game_state.lives):
            pygame.draw.circle(game_display, (255, 255, 0),
                             (30 + i * 25, DISPLAY_H - 30), 10)

        pygame.display.update()
        
    if game_state.game_over:
        show_game_over(game_display, game_state)  

if __name__ == "__main__":
    run_game()