import math

from pygame.math import Vector2

class Rectangle:
    """
    base class for rectangle objects
    """
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.rect(screen, self.color, self.position)
