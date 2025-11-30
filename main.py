import pygame
import sys
from player import Player
from objects.falling_rectangle import FallingRetangle
from objects.falling_object import FallingObject
from objects.falling_circle import FallingCircle
from power_up.power_up import PowerUp
from power_up.slow_motion import SlowMotion
from power_up.point import Point

pygame.init()

WIDTH, HEIGHT = 900, 750
SKY_BLUE = (135, 206, 235)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PLAYER_Y = 650

font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 72)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Objects")
game_over = False

player = Player(WIDTH, HEIGHT, PLAYER_Y)

falling_objects: list[FallingObject] = []
power_up: PowerUp = None
point: PowerUp = None

spawn_timer = 0
SPAWN_INTERVAL = 600

circle_spawn_timer = 0
SPAWN_CIRCLE_INTERVAL = 800

power_up_spawn_timer = 0
POWER_UP_SPAWN_INTERVAL = 3000

point_spawn_timer = 0
POINT_SPAWN_INTERVAL = 2500

clock = pygame.time.Clock()

score = 0

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
                circle_spawn_timer = 0
                game_over = False
                score = 0
                point = None
                power_up = None

    screen.fill(SKY_BLUE)

    if not game_over:
        spawn_timer += dt
        circle_spawn_timer += dt
        power_up_spawn_timer += dt
        point_spawn_timer += dt
        if spawn_timer >= SPAWN_INTERVAL:
            falling_objects.append(FallingRetangle(WIDTH))
            spawn_timer = 0

        if power_up_spawn_timer >= POWER_UP_SPAWN_INTERVAL:
            power_up = SlowMotion(WIDTH, PLAYER_Y)
            power_up_spawn_timer = 0
            
        if circle_spawn_timer >= SPAWN_CIRCLE_INTERVAL:
            falling_objects.append(FallingCircle(WIDTH))
            circle_spawn_timer = 0
        
        if point_spawn_timer >= POINT_SPAWN_INTERVAL:
            point = Point(WIDTH, PLAYER_Y)
            point_spawn_timer = 0

        for obj in falling_objects[:]:
            obj.update()
            obj.draw(screen)

            if obj.y > HEIGHT:
                falling_objects.remove(obj)
            
            if obj.check_collision(player):
                game_over = True

        keys = pygame.key.get_pressed()
        player.move(keys)

        pygame.draw.rect(screen, (34, 139, 34), (0, PLAYER_Y + player.size, WIDTH, HEIGHT - PLAYER_Y)) 
        pygame.draw.rect(screen, (139, 69, 19), (0, PLAYER_Y + player.size + 30, WIDTH, HEIGHT - PLAYER_Y))

        player.draw(screen)

        if power_up:
            power_up.draw(screen)

            if power_up.check_collision(player):
                power_up = None

        if point:
            point.draw(screen)

            if point.check_collision(player):
                score += 1
                point = None

    if game_over:
        game_over_text = large_font.render("GAME OVER!", True, RED)
        restart_text = font.render("Press SPACE to restart", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
        screen.blit(restart_text, (WIDTH // 2 - 180, HEIGHT // 2 + 20))

    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    

    pygame.display.flip()

pygame.quit()
sys.exit()