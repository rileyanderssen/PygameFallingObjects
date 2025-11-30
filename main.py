import pygame
import sys
from player import Player
from objects.falling_rectangle import FallingRetangle
from objects.falling_object import FallingObject

pygame.init()

WIDTH, HEIGHT = 900, 750
SKY_BLUE = (135, 206, 235)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PLAYER_Y = 680

font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 72)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Objects")
game_over = False

player = Player(WIDTH, HEIGHT, PLAYER_Y)

falling_objects: list[FallingObject] = []
spawn_timer = 0
SPAWN_INTERVAL = 300

clock = pygame.time.Clock()

running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_SPACE:
                falling_objects = []
                spawn_timer = 0
                game_over = False

    screen.fill(SKY_BLUE)

    if not game_over:
        spawn_timer += dt
        if spawn_timer >= SPAWN_INTERVAL:
            falling_objects.append(FallingRetangle(WIDTH))
            spawn_timer = 0

        for obj in falling_objects[:]:
            obj.update()
            obj.draw(screen)

            if obj.y > HEIGHT:
                falling_objects.remove(obj)
            
            if obj.check_collision(player):
                game_over = True

        keys = pygame.key.get_pressed()
        player.move(keys)

        pygame.draw.rect(screen, (34, 139, 34), (0, PLAYER_Y, WIDTH, HEIGHT - PLAYER_Y)) 
        pygame.draw.rect(screen, (139, 69, 19), (0, PLAYER_Y + 30, WIDTH, HEIGHT - PLAYER_Y))

        player.draw(screen)

    if game_over:
        game_over_text = large_font.render("GAME OVER!", True, RED)
        restart_text = font.render("Press SPACE to restart", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
        screen.blit(restart_text, (WIDTH // 2 - 180, HEIGHT // 2 + 20))
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()