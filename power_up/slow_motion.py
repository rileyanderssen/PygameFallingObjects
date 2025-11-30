import pygame
import random
from power_up.power_up import PowerUp

class SlowMotion(PowerUp):
    def __init__(self, screen_width, spawn_height):
        x = random.randint(0, screen_width - 40)

        super().__init__(x, spawn_height, (255, 100, 255))