import math

from pygame.math import Vector2

class Rectangle:
    """
    base class for rectangle objects
    """
    def __init__(self, bounds, position, color):
        self.position = position
        self.bounds = bounds
        self.color = color

    def update(self):
        #TODO: Change state
        pass

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.rect(screen, self.color, self.position)

class Paddle(Rectangle):
    """
    rectangle that player controls
    """

    def update(self):
        super().update()

class Enemy(Rectangle):
    """
    rectangle to is destroyed when a ball hits it
    """

    def update(self): #TODO: Disappear when hit
        super().update()