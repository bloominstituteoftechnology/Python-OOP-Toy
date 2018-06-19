import math

from pygame.math import Vector2

class Rectangle:
    """
    base class for bouncing objects
    """
    def __init__(self, bounds, position, velocity, color, width, height):
        self.position = position
        self.velocity = velocity
        self.bounds = bounds
        self.color = color
        self.width = width
        self.height = height

    def update(self):
        # bounce at edges.  TODO: Fix sticky edges
        if self.position.x < 0 or self.position.x > self.bounds[0] - self.width: # screen width
            self.velocity.x *= -1
        if self.position.y < 0 or self.position.y > self.bounds[1] - self.height: # screen height
            self.velocity.y *= -1
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], self.width, self.height))