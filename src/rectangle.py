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
       

        

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.height, self.width))