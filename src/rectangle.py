import math

from pygame.math import Vector2

class Rectangle:
    """
    base class for bouncing objects
    """
    def __init__(self, x, y, color, width, height):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
