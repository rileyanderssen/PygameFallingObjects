import pygame
from player import Player
import math

class FallingObject:
    def __init__(self, x, y, width, height, color, shape="rect"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.shape = shape
    
    def draw(self, screen):
        if self.shape == "circle":
            radius = self.width // 2
            center_x = int(self.x + radius)
            center_y = int(self.y + radius)
            pygame.draw.circle(screen, self.color, (center_x, center_y), radius)
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def check_collision(self, player: Player):
        if self.shape == "circle":
            radius = self.width // 2
            circle_center_x = self.x + radius
            circle_center_y = self.y + radius
            
            closest_x = max(player.x, min(circle_center_x, player.x + player.size))
            closest_y = max(player.y, min(circle_center_y, player.y + player.size))
            
            distance = math.sqrt((circle_center_x - closest_x)**2 + (circle_center_y - closest_y)**2)
            
            return distance < radius
        else:
            obj_rect = pygame.Rect(self.x, self.y, self.width, self.height)
            player_rect = pygame.Rect(player.x, player.y, player.size, player.size)
            return obj_rect.colliderect(player_rect)
