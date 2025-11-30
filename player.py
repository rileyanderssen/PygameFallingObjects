import pygame

PLAYER_COLOR = (0, 128, 255)

class Player():
    def __init__(self, screen_width: int, screen_height: int, player_y: int):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = screen_width // 2
        self.y = player_y
        self.speed = 15
        self.size = 30
        
    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
    
    def draw(self, screen):
        rect = pygame.Rect(
            self.x,
            self.y,
            self.size,
            self.size
        )

        pygame.draw.rect(screen, PLAYER_COLOR, rect)
