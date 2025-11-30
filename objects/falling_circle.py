import random
from objects.falling_object import FallingObject

class FallingCircle(FallingObject):
    def __init__(self, screen_width):
        x = random.randint(0, screen_width - 40)
        self.radius = 20
    
        super().__init__(x, -50, self.radius * 2, self.radius * 2, (190, 0, 0), "circle")
        self.fall_speed = 20
    
    def update(self):
        self.y += self.fall_speed
    