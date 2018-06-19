import math

from pygame.math import Vector2


class Rectangle2:
    """
    base class for bouncing objects
    """

    def __init__(self, bounds, position, velocity, color, radius):
        self.position = position
        self.velocity = velocity
        self.bounds = bounds
        self.color = color

    def update(self):
        # bounce at edges.  TODO: Fix sticky edges
        # screen width
        if self.position.x < 0 + (self.position.x / 2) or self.position.x > self.bounds[0] - (self.position.x / 2):
            self.velocity.x *= -1
        # screen height
        if self.position.y < 0 + (self.position.y / 2) or self.position.y > self.bounds[1] - (self.position.y / 2):
            self.velocity.y *= -1
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.rect(screen, self.color, [int(
            self.position.x), int(self.position.y), int(
            self.position.x + 1), int(self.position.y + 1)])
