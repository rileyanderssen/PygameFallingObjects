import pygame
from player import Player
import math

class PowerUp:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = 30
    
    def draw(self, screen):
        center_x = self.x + self.size // 2
        center_y = self.y + self.size // 2
    
        pygame.draw.circle(screen, self.color, (center_x, center_y), self.size // 2)
        pygame.draw.circle(screen, (255, 255, 255), (center_x, center_y), self.size // 4)
    
    def check_collision(self, player: Player):
        center_x = self.x + self.size // 2
        center_y = self.y + self.size // 2
        
        closest_x = max(player.x, min(center_x, player.x + player.size))
        closest_y = max(player.y, min(center_y, player.y + player.size))
        
        distance = math.sqrt((center_x - closest_x)**2 + (center_y - closest_y)**2)
        
        return distance < self.size // 2
