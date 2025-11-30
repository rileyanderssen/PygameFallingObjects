import random
from objects.falling_object import FallingObject

class FallingRetangle(FallingObject):
    def __init__(self, screen_width):
        x = random.randint(0, screen_width - 40)

        super().__init__(x, -50, 40, 40, (255, 0, 0))
        self.fall_speed = random.randint(3, 20)
    
    def update(self):
        self.y += self.fall_speed