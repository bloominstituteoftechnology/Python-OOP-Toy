import math

from pygame.math import Vector2


class Rectangle:
    """
    base class for rectangles
    """

    def __init__(self, bounds, position, velocity, color):
        self.bounds = bounds
        self.position = position
        self.velocity = velocity
        self.color = color
        # self.height = height
        # self.width = width

    def update(self):
        pass

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, (200, 150, 100, 50))
