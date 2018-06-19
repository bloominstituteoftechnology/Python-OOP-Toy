import math

from pygame.math import Vector2

class Rectangle:
    def __init__(self, SCREEN_SIZE, color, x, y, width, height):
        self.color = color
        self.SCREEN_SIZE = SCREEN_SIZE
        self.x = x
        self.y = y
        self.width = width
        self.height = height  

    def draw(self, Surface, pygame):
        # cast x and y to int for drawing
        pygame.draw.rect(Surface, self.color, (self.x, self.y, self.height, self.width))